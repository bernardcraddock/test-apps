bash — shell utilities and helpers

Purpose
- Portable, small shell utilities and platform-specific helpers. Scripts should be safe to inspect and provide `--dry-run` where destructive.

Quick start — common commands (3 examples)
1) Inspect safely
   - file bash/docker_cleanup.sh && head -n 60 bash/docker_cleanup.sh
2) Lint a script
   - shellcheck bash/docker_cleanup.sh
3) Dry-run then execute (if provided)
   - bash bash/docker_cleanup.sh --dry-run
   - bash bash/docker_cleanup.sh --confirm

Notable files
- `docker_cleanup.sh` — cleanup helper (read header for flags)

Runnable examples (copy-paste)
- Show the first 30 lines and check for destructive ops:
  - file bash/docker_cleanup.sh && sed -n '1,30p' bash/docker_cleanup.sh
- Run a non-destructive smoke-test (prints planned actions):
  - bash bash/docker_cleanup.sh --dry-run | tee /tmp/docker_cleanup-dryrun.log

Example smoke-test (POSIX)
- `tests/smoke-docker-cleanup.sh` (suggested):
  - #!/usr/bin/env bash
  - set -euo pipefail
  - bash bash/docker_cleanup.sh --dry-run | grep -q "would remove" && echo "SMOKE: docker_cleanup dry-run OK"

Safety patterns to follow (examples)
- Use `set -euo pipefail` at the top of scripts
- Provide `--dry-run`, `--yes` and `--log` flags
- Use `mktemp` for temp files and `trap` to cleanup

Testing & verification
- Add `smoke-test.sh` that executes the script in a safe mode and asserts output lines:
  - `./smoke-test.sh` should exit 0 and print a short verification line.
- Example test (POSIX shell):
  - `bash -n script.sh` (syntax check)
  - `shellcheck script.sh` (static lint)

Contributor checklist ✅
- [ ] Purpose and minimal run examples
- [ ] `--dry-run` and `--help` implemented
- [ ] Platform matrix and required binaries listed
- [ ] A smoke-test that validates intended behavior

See: `../.github/copilot-instructions.md` for global rules (inspect with `file` before running).
