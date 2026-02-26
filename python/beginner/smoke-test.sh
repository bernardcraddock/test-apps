#!/usr/bin/env bash
set -euo pipefail

# Quick smoke-test for python examples (fast checks)
PY=.venv/bin/python
if [ ! -x "$PY" ]; then
  PY=python
fi

echo "Running python sample smoke-test..."
"$PY" python/sample.py | grep -q "a 10"

echo "SMOKE: python sample OK"
