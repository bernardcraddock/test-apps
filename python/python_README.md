python — learning scripts and utilities

Purpose
- Educational examples, small data-processing scripts, notebooks, and cookbook-style snippets intended for reproducible experimentation.

Quick start — runnable examples & commands
1) Run the import detector
   - `.venv/bin/python python/detect_imports.py python`
   - Smoke-test: `.venv/bin/python python/detect_imports.py python | head -n 20`
2) Run the sample script
   - `.venv/bin/python python/sample.py`
   - Expected behavior: prints a short summary (see inline comments in `sample.py`).
3) Open the notebook (interactive)
   - `source .venv/bin/activate && jupyter lab python/myfirstnotebook.ipynb`
4) Beginner exercises (quick check)
   - `.venv/bin/python python/beginner/a.py`

Notable files & folders
- `detect_imports.py` — import-analysis utility
- `myfirstnotebook.ipynb` — interactive exploration example
- `copilot_architecture_layers/` — architecture notes and JSON metadata
- `beginner/` — small exercises and beginner examples

Environment & system deps
- Use the workspace `.venv` (Python 3.14). Install with:
  - `.venv/bin/python -m pip install -r requirements.txt`
- System packages: `poppler` for PDF processing (macOS: `brew install poppler`).

Testing, smoke-tests & CI-friendly checks
- Add a fast smoke-test script `python/smoke-test.sh` that runs a small subset of examples and prints `SMOKE: OK`.
- Example pytest invocation for quick checks:
  - `.venv/bin/python -m pytest -q python -k quick`

Examples & verification (what to include)
- Example input, expected output, and a one-line verification command for each script.
- For notebooks, include a short `notebook_README.md` describing learning objectives and expected cells to run.

Contributor checklist ✅
- [ ] Purpose and one-line reproducible run command
- [ ] Example input & expected output
- [ ] `requirements.txt` and system dependency notes
- [ ] Fast smoke-test that validates the example

Best practices
- Keep notebooks small and add a short README describing the objective.
- Place large datasets outside the repo; provide a tiny synthetic sample for tests.

See: `../.github/copilot-instructions.md` for venv and documentation standards.
