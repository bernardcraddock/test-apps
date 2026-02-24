java — Java examples and quick experiments

Purpose
- Small Java/Maven/Gradle examples used for learning and demos. Keep examples self-contained and easy to build.

Quick start — local examples
- Single-file example (quick run):
  - `javac java/getUser.java && java -cp java getUser`
- Maven example (rxeg):
  - `cd java/rxeg && mvn -DskipTests package`
  - Run the example jar or the class in `target/` (see `rxeg/pom.xml` for the main class).

Notable files
- `getUser.java` — single-file demo
- `rxeg/pom.xml` + `rxeg/RxJavaExample.java` — Maven RxJava demo (artifacts in `rxeg/target`)

Dependencies
- JDK 11+ (project may target JDK 17 in some examples). Use `sdkman`/`jenv` to switch if needed.

Examples & verification
- Add expected console output for each example so reviewers can quickly validate behavior.

Smoke-test (fast)
- Quick local smoke-test (verifies JDK and example presence):
  - `bash java/tests/smoke-java.sh`  # prints `SMOKE: java OK` on success

Quick contributor checklist ✅
- State the JDK version and provide exact build + run commands.
- Add `*_README.md` in subfolders with example-specific instructions.
- Avoid committing build artifacts (put them in `.gitignore`).

See: `../.github/copilot-instructions.md` for repository-wide conventions.
