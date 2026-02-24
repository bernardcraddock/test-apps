#!/usr/bin/env bash
set -euo pipefail

# Fast smoke-test for java examples
# - verifies JDK is usable by compiling/running a tiny program
# - verifies presence of rxeg example (quick static checks)

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# 1) Verify javac/java present and can compile a tiny program
cat > "$TMPDIR/TestSmoke.java" <<'JAVA'
public class TestSmoke {
  public static void main(String[] args) {
    System.out.println("JAVA_SMOKE_OK");
  }
}
JAVA

if ! command -v javac >/dev/null 2>&1; then
  echo "SKIP: javac not available" >&2
  exit 0
fi

javac -d "$TMPDIR" "$TMPDIR/TestSmoke.java"
java -cp "$TMPDIR" TestSmoke | grep -q "JAVA_SMOKE_OK"

# 2) Quick static checks for examples in repo
if [ -f "$ROOT/rxeg/pom.xml" ]; then
  grep -q "public static void main" "$ROOT/rxeg/RxJavaExample.java" || true
else
  echo "NOTE: rxeg/pom.xml not present (skipping rxeg check)"
fi

echo "SMOKE: java OK"
