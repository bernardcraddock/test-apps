ai_studio — overview

Purpose
- Short experiments, reference architecture notes and visualisations for AI-related projects and demos. The folder is documentation-first: code belongs in a subfolder when runnable examples are needed.

What this README provides
- Quick commands to preview diagrams, run small demos, and add new experiments that are easy to reproduce.

Quick start — local checks (3 examples)
1) Preview architecture diagram (fast)
   - Open in VS Code (Mermaid preview) or render an SVG/PDF:
     - `npm run mermaid:render -- ai_studio/ai_studio_arch.mmd`
     - open ai_studio/ai_studio_arch.svg
2) Run a minimal Python demo (example placeholder)
   - Create an example file `examples/hello_demo/run_demo.py` with a single function and run:
     - `.venv/bin/python ai_studio/examples/hello_demo/run_demo.py`
   - Smoke-test (one-liner):
     - `.venv/bin/python -c "from pathlib import Path; print(Path('ai_studio').exists())"`
3) Export diagram to PDF (CI-friendly)
   - `npm run mermaid:render -- ai_studio/ai_studio_arch.mmd && ls -lh ai_studio/ai_studio_arch.pdf`

Notable files
- `ai_studio_arch.md` — narrative and rationale
- `ai_studio_arch.mmd` — mermaid source
- `ai_studio_arch.svg` / `ai_studio_arch.pdf` — rendered exports

Rendered artifacts
- Commit rendered SVG/PDF only when they improve reviewability (small files). Prefer storing large exports in `diagrams/` or attach to PRs.

How to add a runnable example (recommended layout)
- Create a subfolder `examples/<name>/` with:
  - `<name>_README.md` (purpose + run steps)
  - `requirements.txt` or `package.json` when dependencies are required
  - `smoke-test.sh` (executable script that prints expected output)

Verification & smoke-tests (what reviewers expect)
- Minimal smoke-test must run in <10s and print deterministic output. Example:
  - `.venv/bin/python ai_studio/examples/hello_demo/run_demo.py --smoke-test`
  - `./ai_studio/examples/hello_demo/smoke-test.sh`

Contributor checklist ✅
- [ ] Short one-paragraph purpose
- [ ] Exact run command(s) and required versions
- [ ] Expected output (1–3 lines) and a smoke-test
- [ ] Link to related architecture diagrams (if relevant)

Tips and conventions
- Prefer small, single-purpose examples. Keep code and heavy data out of the folder.
- Follow the repository rule: name README as `ai_studio_README.md` and include per-example `*_README.md`.

See also: `../.github/copilot-instructions.md` (naming, safety, venv usage).
