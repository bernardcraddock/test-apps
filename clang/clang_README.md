clang / C++ / Objective-C experiments

Purpose
- Native-language experiments (C++, Objective-C, mixed Objective-C++). Small, self-contained examples — not production code.

Quick start — examples in this folder
- Compile and run the C++ example:
  - `clang++ -std=c++17 -O2 -o cppmain/cppmain cppmain/cppmain.cpp && ./cppmain/cppmain`
- Objective-C++ example:
  - `clang++ -ObjC++ -o objcmain/objcmain objcmain/objcmain.mm && ./objcmain/objcmain`
- Combined examples and additional notes are in `compile.README`.

Notable files
- `cppmain.cpp` — simple C++ example
- `main.mm`, `objcmain.mm` — Objective-C / Objective-C++ examples
- `combined-main` / `combined-main.mm` — mixed-language experiments
- `compile.README` — build notes and tips

Conventions
- Provide one-line build + run commands. Prefer reproducible flags and note the target platform (macOS vs Linux).
- Never commit large binaries; list build artifacts in `.gitignore`.

Smoke-test (fast)
- Quick local smoke-tests (compile & run):
  - `bash clang/tests/smoke-clang-cppmain.sh`  # prints `SMOKE: clang cppmain OK` on success
  - `bash clang/tests/smoke-clang-objc.sh`     # Objective-C / ObjC++ examples; prints `SMOKE: clang objc OK`

Quick contributor checklist ✅
- Add minimal input/expected-output and the exact compiler command used to verify the example.
- Add a short note about required SDKs/toolchain versions.

See: `../.github/copilot-instructions.md` for repository conventions.
