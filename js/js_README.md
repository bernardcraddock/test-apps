js — JavaScript / Node experiments

Purpose
- Small Node/browser demos, investigative scripts (memory leaks), and tiny web prototypes.

Quick start — runnable examples (3)
1) Memory-leak repro
   - Run the vulnerable script: `node js/mem-leak/mem-leak.js`
   - Observe RSS growth (macOS): `ps -o rss= -p $(pgrep -n node)`
   - Compare with the fixed variant: `node js/mem-leak/mem-leak-fix.js`
2) Tiny web demo (my-js-app)
   - `node js/my-js-app/server.js` — open the URL printed by the server (commonly `http://localhost:3000`).
3) Static preview
   - `npx http-server js/my-js-app` and open `index.html`

Notable files
- `js/mem-leak/mem-leak.js`, `mem-leak-fix.js` — investigative examples
- `js/my-js-app/server.js`, `index.html` — tiny demo

Verification & smoke-tests
- `tests/smoke-js-my-js-app.sh` (suggested): start server, curl health endpoint, assert HTTP 200.
- Memory repro smoke: run `node mem-leak.js & sleep 3; ps -o rss= -p $!` and compare with fixed variant.

Dependencies & environment
- Node.js (use `nvm` or specify `engines` in `package.json`). Use `npm ci` in CI for reproducible installs.

Quick contributor checklist ✅
- Provide a one-line run command and Node.js version.
- Include reproduction steps for bugs and an automated smoke-test.

Debugging tips
- Use `node --inspect` and collect heap snapshots for memory analysis.

See: `../.github/copilot-instructions.md` for repository conventions.
