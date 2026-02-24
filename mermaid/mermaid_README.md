mermaid — diagrams and flowcharts

Purpose
- Canonical location for architecture and workflow diagrams (`.mmd`) used across the repository.

Quick start
- Render a single diagram:
  - `npm run mermaid:render -- mermaid/flowchart.mmd`
- Render all diagrams:
  - `npm run mermaid:render:all`

Notable diagrams in this folder
- `AIDevWorkFlow.mmd` — AI development workflow
- `flowchart.mmd` — process flow examples
- `pumped-model-deps.mmd` — model dependency diagrams
- Rendered SVGs are committed alongside sources when useful for reviewers.

Conventions
- Keep diagrams focused (one idea per file). Include a one-line purpose at top of the `.mmd` file.
- Prefer source `.mmd` in this folder; add generated `.svg` to `diagrams/` or commit small, review-friendly exports.

Quick contributor checklist ✅
- Add a one-line description to new `.mmd` files and include an example render command.
- If diagram is shared across projects, place in this folder and reference it from the consumer's README.

See: top-level `package.json` for rendering scripts and `../.github/copilot-instructions.md` for documentation rules.
