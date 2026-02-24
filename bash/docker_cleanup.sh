#!/usr/bin/env bash
set -euo pipefail

# docker_cleanup.sh
# Interactive Docker Desktop cleanup for macOS (Intel/Sequoia)
# Prompts before every command by default. Use --auto to run without prompts (DANGEROUS).

LOGFILE="$HOME/docker_cleanup.log"
: > "$LOGFILE"

ask_and_run() {
  local cmd="$1"
  local prompt_message
  prompt_message="About to run: $cmd\nDo you want to run this command? [y/N] "

  # If --auto is enabled, run without prompting (but still log). This must be passed explicitly.
  if [[ ${AUTO:-false} == true ]]; then
    echo "[AUTO] Running: $cmd" | tee -a "$LOGFILE"
    eval "$cmd"
    return
  fi

  printf "%b" "$prompt_message"
  read -r reply
  case "$reply" in
    [Yy]|[Yy][Ee][Ss])
      echo "Running: $cmd" | tee -a "$LOGFILE"
      eval "$cmd"
      ;;
    *)
      echo "Skipped: $cmd" | tee -a "$LOGFILE"
      ;;
  esac
}

confirm_continue() {
  echo
  printf "%b" "WARNING: This script will remove Docker Desktop files, containers, images, volumes and helper tools (destructive). Continue? [y/N] "
  read -r ok
  if [[ ! $ok =~ ^([yY]|[yY][eE][sS])$ ]]; then
    echo "Aborting as requested." | tee -a "$LOGFILE"
    exit 1
  fi
}

usage() {
  cat <<EOF
Usage: $0 [--auto] [--preview]
  --auto    : Run without per-command prompts (DANGEROUS; still logs). Not recommended.
  --preview : Show what would run and exit (no commands executed).
  --help    : Show this help text.

By default the script prompts for each and every command. It logs actions to $LOGFILE.
EOF
}

# Parse args
PREVIEW=false
AUTO=false
for arg in "$@"; do
  case "$arg" in
    --preview) PREVIEW=true ;;
    --auto) AUTO=true ;;
    --help) usage; exit 0 ;;
    *) echo "Unknown arg: $arg"; usage; exit 1 ;;
  esac
done

if [[ "$PREVIEW" == true ]]; then
  echo "Preview mode: Commands will not be executed. Use no flags to run interactively." | tee -a "$LOGFILE"
fi

# Very explicit header
cat <<-EOF | tee -a "$LOGFILE"

=== Docker Desktop Cleanup Script ===
Date: $(date -u)
Host: $(hostname)
macOS Version: $(sw_vers -productVersion 2>/dev/null || echo "unknown")
Architecture: $(uname -m)
Logfile: $LOGFILE
=====================================

EOF

# Confirm before proceeding with destructive operations
confirm_continue

# Helper to either preview or run
run_or_preview() {
  if [[ "$PREVIEW" == true ]]; then
    echo "[PREVIEW] $1" | tee -a "$LOGFILE"
  else
    ask_and_run "$1"
  fi
}

# 1) Stop Docker Desktop and related processes
run_or_preview "osascript -e 'tell application \"Docker\" to quit' || true"
run_or_preview "pkill -f Docker || true"
run_or_preview "killall \"Docker Desktop\" 2>/dev/null || true"
run_or_preview "launchctl list | grep -i docker || true"

# 2) Optional: Remove containers, images, volumes (if docker CLI available)
if command -v docker >/dev/null 2>&1; then
  echo "\nDocker CLI detected: $(command -v docker)" | tee -a "$LOGFILE"
  run_or_preview "docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Status}}' || true"
  run_or_preview "docker stop \\$(docker ps -aq) || true"
  run_or_preview "docker rm -vf \\$(docker ps -aq) || true"
  run_or_preview "docker rmi -f \\$(docker images -aq) || true"
  run_or_preview "docker volume rm \\$(docker volume ls -q) || true"
  run_or_preview "docker system prune -a --volumes --force || true"
else
  echo "\nDocker CLI not found; skipping container/image cleanup steps." | tee -a "$LOGFILE"
fi

# 3) Remove Docker Desktop app + user files
run_or_preview "sudo rm -rf /Applications/Docker.app"
run_or_preview "rm -rf ~/Library/Containers/com.docker.docker"
run_or_preview "rm -rf ~/Library/Application\\ Support/Docker\\ Desktop"
run_or_preview "rm -rf ~/Library/Group\\ Containers/group.com.docker"
run_or_preview "rm -rf ~/Library/Group\\ Containers/group.com.docker.settings"
run_or_preview "rm -rf ~/Library/Preferences/com.docker.docker.plist"
run_or_preview "rm -rf ~/Library/Logs/Docker\\ Desktop"
run_or_preview "rm -rf ~/.docker"
# Remove VM images (if present)
run_or_preview "rm -rf ~/Library/Containers/com.docker.docker/Data/vms || true"
run_or_preview "rm -f ~/Library/Containers/com.docker.docker/Data/docker.raw || true"

# 4) Remove privileged helpers / launch daemons
run_or_preview "sudo rm -f /Library/PrivilegedHelperTools/com.docker.vmnetd || true"
run_or_preview "sudo rm -f /Library/LaunchDaemons/com.docker.vmnetd.plist || true"
run_or_preview "sudo launchctl remove com.docker.vmnetd 2>/dev/null || true"

# 5) Remove Docker CLI/binaries (detect and list before removal)
BINARIES=(docker docker-compose docker-credential-osxkeychain com.docker.cli)
for b in "${BINARIES[@]}"; do
  found=( $(which -a "$b" 2>/dev/null || true) )
  if [[ ${#found[@]} -gt 0 ]]; then
    echo "Found $b at: ${found[*]}" | tee -a "$LOGFILE"
    for f in "${found[@]}"; do
      run_or_preview "sudo rm -f $f || true"
    done
  fi
done

# If brew managed
if command -v brew >/dev/null 2>&1; then
  echo "\nHomebrew detected: $(command -v brew)" | tee -a "$LOGFILE"
  run_or_preview "brew uninstall --cask docker || true"
  run_or_preview "brew uninstall docker docker-compose docker-credential-helper || true"
fi

# 6) Clean up networking bits (if present)
if /sbin/ifconfig docker0 >/dev/null 2>&1; then
  run_or_preview "sudo ifconfig docker0 down || true"
  run_or_preview "sudo ifconfig docker0 destroy || true"
else
  echo "No docker0 interface detected; skipping network cleanup." | tee -a "$LOGFILE"
fi

# 7) Final suggestions: reboot
run_or_preview "echo \"To complete cleanup, a reboot is recommended. Run: sudo shutdown -r now\""

# Summarize
cat <<-EOF | tee -a "$LOGFILE"

Cleanup complete (or preview finished).
Log file: $LOGFILE
If you removed everything and want to reinstall Docker Desktop (Intel):
  - brew install --cask docker
  - or download from https://www.docker.com/get-started

EOF

exit 0
