#!/usr/bin/env bash
set -euo pipefail

# Run docker_cleanup.sh in preview mode and accept the confirmation prompt non-interactively
printf 'y\n' | bash bash/docker_cleanup.sh --preview | tee /tmp/docker_cleanup-smoke.log

grep -q "Preview mode" /tmp/docker_cleanup-smoke.log && echo "SMOKE: bash docker_cleanup preview OK"
