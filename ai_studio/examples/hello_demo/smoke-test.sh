#!/usr/bin/env bash
set -euo pipefail

PY=.venv/bin/python
if [ ! -x "$PY" ]; then
  PY=python3
fi

echo "Running ai_studio hello_demo smoke-test..."
"$PY" ai_studio/examples/hello_demo/run_demo.py | grep -q "HELLO DEMO OK"

echo "SMOKE: ai_studio hello_demo OK"
