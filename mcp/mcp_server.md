# Local MCP Server & Client - Educational Implementation

## Overview

This is a **complete, working MCP server and client** that demonstrates real bidirectional communication over the Model Context Protocol. It shows how MCP works **in both directions** - not just client-to-server, but proper request/response patterns.

**What it teaches:**
- How MCP servers listen for connections
- Handling multiple concurrent clients with threading
- Proper JSON-RPC 2.0 request/response flow
- Server-side request processing
- Error handling in real communication

## Architecture

```
┌──────────────────────────────────────────────────────┐
│          LOCAL MCP SERVER-CLIENT DEMO               │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Terminal 1              Network (TCP)  Terminal 2  │
│  ┌─────────────────┐     Socket 5555    ┌─────────┐ │
│  │ mcp_server.py   │ ←─────────────→ │ mcp_      │ │
│  │                 │   JSON-RPC 2.0  │ client_   │ │
│  │ • Listens on    │                 │ local.py  │ │
│  │   port 5555     │   Bidirectional │ • Connects│ │
│  │ • Handles       │   Requests &    │ • Sends   │ │
│  │   requests      │   Responses     │   requests│ │
│  │ • Uses threads  │                 │ • Receives│ │
│  │   for clients   │                 │   responses│ │
│  └─────────────────┘                 └─────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## What They Do

### MCP Server (`mcp_server.py`)
- **Listens** on port 5555 for incoming client connections
- **Accepts** multiple clients simultaneously using threading
- **Receives** JSON-RPC 2.0 requests from clients
- **Processes** requests (ping, echo, calculate, get_time)
- **Sends** JSON-RPC responses back to clients
- **Logs** all communication for learning

### MCP Client (`mcp_client_local.py`)
- **Connects** to the server on localhost:5555
- **Creates** properly formatted JSON-RPC 2.0 requests
- **Sends** requests to server
- **Receives** responses and displays them
- **Demonstrates** 4 different RPC methods

## How to Install and Run

### Prerequisites
- Python 3.14.2
- Located in: `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/mcp/`
- Shared virtual environment at: `../../.venv/`

---

## Running Options

### ✅ Option 1: Manual (Two Terminal Windows/Tabs)

**Terminal 1 - Start Server:**
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
cd mcp
python mcp_server.py
```

**Terminal 2 - Run Client** (after server is ready):
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
cd mcp
python mcp_client_local.py
```

**Server stays running** - you control when to stop (Ctrl+C)

**When to use:** Learning, debugging, interactive testing

---

### ✅ Option 2: VS Code Split Terminal

**1. Open VS Code folder:** `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/`

**2. Open integrated terminal:** `Ctrl+Backtick` (or View → Terminal)

**3. Split terminal:** Click the split icon (or `Cmd+\`)

**4. In left terminal:**
```bash
source .venv/bin/activate && cd mcp && python mcp_server.py
```

**5. In right terminal:**
```bash
source .venv/bin/activate && cd mcp && python mcp_client_local.py
```

**Advantages:**
- Both visible at once
- Same VS Code window
- Easy to see server logs and client output side-by-side

**When to use:** Active development, debugging, learning

---

### ✅ Option 3: Single Command (Testing/Automation)

Run both in sequence with automatic cleanup:

```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps && \
source .venv/bin/activate && \
python mcp/mcp_server.py & \
sleep 2 && \
python mcp/mcp_client_local.py && \
kill %1
```

**What happens:**
1. Start server in background
2. Wait 2 seconds for server to initialize
3. Run client (it connects, runs, exits)
4. Kill server process
5. Done

**Output:**
- See server startup
- See all client requests/responses
- Clean shutdown

**When to use:** Quick testing, CI/CD, batch runs, demonstration

---

### ✅ Option 4: VS Code Tasks (Advanced)

Create `.vscode/tasks.json` to run server and client with one click:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "MCP: Start Server",
      "type": "shell",
      "command": "cd ${workspaceFolder}/mcp && python mcp_server.py",
      "isBackground": true,
      "problemMatcher": []
    },
    {
      "label": "MCP: Run Client",
      "type": "shell",
      "command": "cd ${workspaceFolder}/mcp && python mcp_client_local.py",
      "dependsOn": ["MCP: Start Server"]
    }
  ]
}
```

**Use:** Press `Cmd+Shift+B` → Select "MCP: Run Client"

**When to use:** Frequent testing, development workflow integration

---

## Expected Output

### Server Output
```
======================================================================
🌐 Local MCP Server - Educational Implementation
======================================================================

Supported methods:
  • ping - Health check
  • echo - Echo back a message
  • calculate - Simple arithmetic
  • get_time - Get current server time

Protocol: JSON-RPC 2.0 over TCP
======================================================================

✅ Server listening on localhost:5555
⏳ Waiting for client connections...

🤝 Client #1 connected from ('127.0.0.1', 54321)

📥 Client #1 request:
   Method: ping
   ID: 1

   → Processing: ping
📤 Response sent to client #1
```

### Client Output
```
======================================================================
🌐 Local MCP Client - Connecting to Server
======================================================================

🔌 MCP Client initialized: localhost:5555
✅ Connected to server at localhost:5555

======================================================================
📋 Running Demonstrations
======================================================================

######################################################################
# Example 1: Ping (Health Check)
######################################################################

📤 Sending request:
   Method: ping
   ID: 1
   
📥 Response received:
   Status: ✅ Success
   ID: 1
   Result: {
     "status": "pong",
     "message": "Server is alive!"
   }
```

---

## Quick Start Recommendations

**First Time / Learning:**
→ Use **Option 2** (VS Code Split Terminal) - see both sides

**Regular Testing:**
→ Use **Option 1** (Two Terminals) - full control

**Quick Verification:**
→ Use **Option 3** (Single Command) - fast, clean

**Production/Automation:**
→ Use **Option 4** (VS Code Tasks) - integrated workflow

## Technology & Libraries

| Library | Purpose | Why Used |
|---------|---------|----------|
| **socket** | TCP network communication | Built-in, direct control over connections |
| **json** | Request/response formatting | Built-in, standard for JSON-RPC 2.0 |
| **threading** | Handle multiple clients | Built-in, essential for concurrent server |
| **time** | Timestamps | Built-in, used by get_time method |

**No external dependencies!** Everything uses Python built-in libraries.

## Code Structure

### Server (`mcp_server.py`)

```python
class SimpleMCPServer:
    ├── start()                    # Listen for connections
    ├── handle_client()            # Process individual client
    ├── process_request()          # Route to methods
    │
    ├── method_ping()              # Health check
    ├── method_echo()              # Echo message
    ├── method_calculate()         # Arithmetic
    └── method_get_time()          # Server time

main():
    ├── Create server
    └── Start listening
```

### Client (`mcp_client_local.py`)

```python
class LocalMCPClient:
    ├── connect()                  # Connect to server
    ├── create_request()           # Build JSON-RPC request
    ├── send_request()             # Send & receive
    └── disconnect()               # Close connection

main():
    ├── Create client
    ├── Connect to server
    ├── Run 4 demonstrations
    └── Disconnect
```

## Communication Flow

### Request/Response Cycle

```
1. Client Creates Request
   ├─ method: "ping"
   ├─ id: 1
   └─ jsonrpc: "2.0"
   
   ↓ (TCP Socket)
   
2. Server Receives Request
   ├─ Parse JSON-RPC format
   ├─ Extract method
   └─ Route to handler
   
   ↓ (Processing)
   
3. Server Processes
   ├─ Execute method_ping()
   ├─ Generate result
   └─ Create response
   
   ↓ (TCP Socket)
   
4. Client Receives Response
   ├─ result: "pong"
   ├─ id: 1 (matches request)
   └─ jsonrpc: "2.0"
```

## Supported RPC Methods

### 1. `ping`
**Purpose:** Health check / connection verification
**Request:**
```json
{"jsonrpc": "2.0", "method": "ping", "id": 1}
```
**Response:**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "pong",
    "message": "Server is alive!"
  },
  "id": 1
}
```

### 2. `echo`
**Purpose:** Echo back a message
**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "echo",
  "params": {"message": "Hello!"},
  "id": 2
}
```
**Response:**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "echoed": "Hello!",
    "length": 6
  },
  "id": 2
}
```

### 3. `calculate`
**Purpose:** Perform arithmetic operations
**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "calculate",
  "params": {"operation": "add", "a": 10, "b": 5},
  "id": 3
}
```
**Response:**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "operation": "add",
    "operands": {"a": 10, "b": 5},
    "result": 15
  },
  "id": 3
}
```

### 4. `get_time`
**Purpose:** Get current server time
**Request:**
```json
{"jsonrpc": "2.0", "method": "get_time", "id": 4}
```
**Response:**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "timestamp": 1706612345.678,
    "readable": "2026-01-30 11:45:45"
  },
  "id": 4
}
```

## Key Features

✅ **Bidirectional Communication** - True client-server conversation
✅ **Concurrent Clients** - Server uses threading to handle multiple clients
✅ **JSON-RPC 2.0 Compliant** - Proper protocol implementation
✅ **Error Handling** - Parse errors, method not found, etc.
✅ **Formatted Logging** - Easy to follow communication flow
✅ **Educational** - Every step is logged and explained

## Threading Deep Dive

The server uses **threading** to handle multiple clients simultaneously:

```python
# Main thread: Accept connections
while self.running:
    client_socket, address = server_socket.accept()
    
    # Spawn new thread for this client
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )
    client_thread.daemon = True
    client_thread.start()
    
    # Main thread immediately goes back to accept()
    # Ready for next connection!
```

**Result:** Server can handle multiple clients without blocking! ✅

## How to Run Multiple Clients

While server is running, run the client script multiple times:

**Terminal 1 (Server):**
```bash
python mcp_server.py
```

**Terminal 2 (Client #1):**
```bash
python mcp_client_local.py
```

**Terminal 3 (Client #2):**
```bash
python mcp_client_local.py
```

Watch the server handle both clients! Each gets a thread.

## Learning Outcomes

After running these scripts, you'll understand:
- ✅ How MCP servers listen and accept connections
- ✅ How JSON-RPC 2.0 works in real communication
- ✅ Request/response patterns (real, not mocked)
- ✅ How servers process multiple clients with threading
- ✅ Error handling in network communication
- ✅ Bidirectional client-server architecture

## Comparison: Mock vs Local vs Real

| Feature | Mock | Local | Real |
|---------|------|-------|------|
| Network | ❌ None | ✅ TCP | ✅ HTTP/TCP |
| Server | 📝 Simulated | ✅ Real | ✅ External |
| Concurrency | ❌ No | ✅ Threads | ✅ Processes |
| Error handling | 📋 Simple | 🛡️ Complete | 🛡️ Complete |
| Use case | 🎓 Learn protocol | 🎓 Learn server | 🚀 Production |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Connection refused" | Make sure server is running in another terminal |
| Port already in use | Change port in both scripts (line 12 server, line 32 client) |
| No output from server | Check if it's actually listening (should show "Waiting for connections") |
| Client hangs | Server might be blocked, restart both |
| Timeout errors | Network issues or server crashed - restart |

## Extending This Project

### 1. Add More Methods
```python
def method_weather(self, params):
    city = params.get("city")
    # Fetch real weather data
    return {"city": city, "temp": 72}
```

### 2. Add Authentication
```python
def authenticate(self, token):
    return token == "secret123"
```

### 3. Connect to External APIs
```python
def method_fetch_data(self, params):
    import requests
    response = requests.get("https://api.example.com/...")
    return response.json()
```

### 4. Build a Real MCP Server
Use `mcp-python-sdk` package for production-ready MCP

### 5. Add Persistence
Store data in a database between requests

## Next Steps

After mastering this local server:
1. **Add more complex methods** - Connect to real APIs
2. **Build error recovery** - Handle crashes gracefully
3. **Add logging** - Log all requests to a file
4. **Create a web UI** - Build a frontend to interact with server
5. **Connect real MCP** - Use `mcp-python-sdk` for production

## Files

- `mcp_server.py` - Server implementation (~280 lines)
- `mcp_client_local.py` - Client implementation (~220 lines)
- `mcp_server.md` - This comprehensive README

## References

- **JSON-RPC 2.0 Spec**: https://www.jsonrpc.org/specification
- **Python socket module**: https://docs.python.org/3/library/socket.html
- **Python threading**: https://docs.python.org/3/library/threading.html
- **MCP Protocol**: https://modelcontextprotocol.io/

## Notes

- Both scripts use **only built-in Python libraries** (no external dependencies)
- The server is **thread-safe** and handles concurrent clients
- All communication is **logged** for educational purposes
- Requests/responses are **human-readable JSON** for learning
- This is a **simplified educational version** - production servers have more features

## Key Takeaway

You now understand **how MCP works**:
1. Servers listen for connections
2. Clients connect and send requests
3. Servers process and send responses
4. This happens bidirectionally over the network

This is the foundation for working with real MCP servers! 🚀
