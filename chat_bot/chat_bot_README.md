chat_bot — experimental chat/assistant demos

Purpose
- Prototypes and integration experiments for chat/assistant interfaces: mock clients, simple UIs and backend connectors.

Quick start — runnable examples (3)
1) Mock client (MCP-backed, Python)
   - Copy `.env.example` -> `.env` and populate required values.
   - .venv/bin/python mcp/hello_mcp_client_mock.py --demo
   - Smoke-test (curl):
     - `curl -sS -X POST -H "Content-Type: application/json" -d '{"msg":"hello"}' http://localhost:PORT/api/demo | jq .`
2) Minimal local UI (if present)
   - Start the dev server per-example and open the UI in a browser.
3) Automated integration check
   - `./verify_demo.sh` should start server, send a test message, and assert the expected response.

Security & secrets
- Never commit secrets. Provide `.env.example` and a short note about required vars.
- Add a `logs/README.md` describing how to scrub or rotate logs before sharing.

Developer tips
- Provide example request/response JSON files in `examples/<name>/payloads/`.
- Add a `verify_demo.sh` that performs an end-to-end smoke-test and exits non-zero on failure.

Quick contributor checklist ✅
- [ ] `*_README.md` for each example
- [ ] `.env.example` with required variables (no secrets)
- [ ] One reproducible smoke-test command
- [ ] Privacy note describing data handling

See: `../.github/copilot-instructions.md` for documentation & security rules.
