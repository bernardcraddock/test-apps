#!/usr/bin/env bash
set -euo pipefail

# Fast smoke-test: compile and run cppmain.cpp
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/cppmain.cpp"
if [ ! -f "$SRC" ]; then
  echo "SKIP: $SRC not found" >&2
  exit 0
fi

CC=${CXX:-clang++}
if ! command -v "$CC" >/dev/null 2>&1; then
  echo "SKIP: $CC not installed" >&2
  exit 0
fi

BIN=$(mktemp -u)
$CC -std=c++17 -O2 -o "$BIN" "$SRC"
# Use fixed-string match to avoid BRE/ERE differences across platforms
"$BIN" | grep -F -q "Hello from C++!"
rm -f "$BIN"

echo "SMOKE: clang cppmain OK"
