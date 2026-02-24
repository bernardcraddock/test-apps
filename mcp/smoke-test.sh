#!/usr/bin/env bash
set -euo pipefail

PY=.venv/bin/python
if [ ! -x "$PY" ]; then
  PY=python3
fi

echo "Running MCP smoke-test..."
"$PY" mcp/hello_mcp_client_mock.py | grep -q "MCP Client" && echo "SMOKE: mcp hello client OK"
