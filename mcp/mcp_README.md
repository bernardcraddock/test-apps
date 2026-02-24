mcp — Model Context Protocol experiments

Purpose
- Prototypes and reference implementations for MCP servers and clients (Python-based). Includes mock clients and examples that demonstrate messaging and terminal progress.

Quick start (recommended)
1. Activate workspace venv: `source .venv/bin/activate`
2. Start the example server (background):
   - `.venv/bin/python mcp/mcp_server.py`
3. Run the mock client/demo in another shell:
   - `.venv/bin/python mcp/hello_mcp_client_mock.py`

Docs & notable files
- `mcp_server.md` — server design and usage
- `hello_mcp_client_mock.md` — how the mock client works
- `mcp_server.py`, `mcp_client_local.py`, `hello_mcp_client_mock.py` — runnable examples
- `rest_countries_client.py` + `rest_countries_client.md` — example of an HTTP-backed client

Examples & verification
- `rest_countries_client.py` is a self-contained example you can run to see request/response flows.

Developer tips
- Keep protocol contracts in the same folder and add example request/response JSON for tests.
- Prefer small integration smoke scripts that can be executed by CI (if added).

Quick contributor checklist ✅
- Document the protocol, provide an example request/response, and include a short smoke-test command.
- Avoid committing credentials; provide `.env.example` where needed.

See: `../.github/copilot-instructions.md` for security and documentation rules.
