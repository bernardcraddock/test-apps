# Mock MCP Client - Educational Demo

## Overview

This is an **educational mock implementation** that demonstrates the **JSON-RPC 2.0 protocol** used by the Model Context Protocol (MCP). It simulates a client-server communication pattern **without making real network calls**.

**What it teaches:**
- How MCP protocol structures requests and responses
- Client-server communication flow
- JSON-RPC message format
- How to build a simple protocol handler

## What It Does

The script simulates a client sending structured requests to a mock server:

```
┌─────────────────────┐
│   Mock MCP Client   │
│                     │
│ 1. create_request() │──→ Creates JSON-RPC request
│ 2. send_request()   │──→ Sends to mock server
│ 3. Receives mock    │←── Mock server responds
│    response         │
└─────────────────────┘
```

## How to Install and Run

### Prerequisites
- Python 3.14.2 (or later)
- Located in: `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/`

### Step 1: Activate Virtual Environment
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
```

### Step 2: Run the Script
```bash
cd mcp
python hello_mcp_client_mock.py
```

### Expected Output
```
Starting Mock MCP Client...

Creating request #1
📤 Request sent to mock server:
   ID: 1
   Method: initialize

Receiving response from mock server...
📥 Response received:
   ID: 1
   Protocol Version: 2.0
   ...
```

## Technology & Libraries

| Technology | Purpose | Why Used |
|-----------|---------|----------|
| **Python 3.14.2** | Runtime environment | Modern, readable syntax for learning |
| **json** | Request/Response formatting | Built-in, standard for data interchange |
| **sys** | System utilities | Built-in, for command-line output |

**No external dependencies!** This script uses only Python built-in modules, making it lightweight and focused on protocol concepts.

## Code Structure

```python
class SimpleMCPClient:
    ├── create_request()      # Build JSON-RPC request structure
    ├── send_request()        # Simulate sending to server
    ├── mock_server_response()# Simulate server responses
    └── receive_response()    # Parse and display responses

main():
    ├── Initialize client
    ├── Send multiple requests
    ├── Display protocol flow
    └── Show request/response patterns
```

## Key Concepts Explained

### JSON-RPC 2.0 Message Format
Every request has this structure:
```json
{
  "jsonrpc": "2.0",
  "method": "method_name",
  "params": {...},
  "id": 1
}
```

### Protocol Flow
```
Client                    Mock Server
  │                           │
  ├─ Create request ──────────┤
  │                           │
  ├─ Send to server ─────────→│
  │                           │
  │         ← Receive response│
  │                           │
  └─ Parse response           │
```

## Learning Outcomes

After running this script, you'll understand:
- ✅ How MCP protocol structures communication
- ✅ What JSON-RPC 2.0 message format looks like
- ✅ Client-server request/response patterns
- ✅ How to build simple protocol handlers

## Next Steps

Once you understand this mock implementation, explore:
1. **REST Countries Client** - See real HTTP API communication
2. **Real MCP Server** - Connect to actual MCP services
3. Build your own MCP protocol handler

## Files

- `hello_mcp_client_mock.py` - Main script (~4.3KB)

## Notes

- This is **not a real MCP client** - it doesn't connect to actual MCP servers
- No network calls are made (all responses are mocked)
- Use this to understand protocol concepts before building real clients
