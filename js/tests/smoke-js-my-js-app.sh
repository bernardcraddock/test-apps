#!/usr/bin/env bash
set -euo pipefail

SRV=js/my-js-app/server.js
if [ ! -f "$SRV" ]; then
  echo "SKIP: $SRV not found" >&2
  exit 0
fi

node $SRV &
PID=$!
trap 'kill -9 $PID 2>/dev/null || true' EXIT

# wait up to 3s for server
for i in 1 2 3; do
  if curl -sS http://127.0.0.1:3000/ | grep -q "Hello, World!"; then
    echo "SMOKE: js my-js-app OK"
    exit 0
  fi
  sleep 1
done

echo "FAIL: server did not respond in time" >&2
exit 2
