#!/usr/bin/env python3
"""
Local MCP Server - Educational Implementation
Demonstrates bidirectional MCP communication using JSON-RPC 2.0
"""

import socket
import json
import threading
import time
from typing import Dict, Any, Optional


class SimpleMCPServer:
    """
    A simple MCP server that listens for client connections
    and processes JSON-RPC 2.0 requests.
    
    This is educational - demonstrates how MCP servers work:
    1. Listen on a port
    2. Accept client connections
    3. Receive JSON-RPC requests
    4. Process requests
    5. Send JSON-RPC responses back
    """
    
    def __init__(self, host: str = "localhost", port: int = 5555):
        """
        Initialize the MCP server
        
        Args:
            host: Host address to bind to
            port: Port to listen on
        """
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.client_count = 0
        
        print(f"🚀 MCP Server initialized: {host}:{port}")
    
    def start(self):
        """Start the server and listen for connections"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            print(f"✅ Server listening on {self.host}:{self.port}")
            print("⏳ Waiting for client connections...\n")
            
            # Accept connections in a loop
            while self.running:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    self.client_count += 1
                    
                    print(f"\n🤝 Client #{self.client_count} connected from {client_address}")
                    
                    # Handle client in a separate thread
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, client_address, self.client_count)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except KeyboardInterrupt:
                    print("\n\n⛔ Server interrupted by user")
                    self.stop()
                    break
                except Exception as e:
                    if self.running:
                        print(f"❌ Error accepting connection: {e}")
        
        except Exception as e:
            print(f"❌ Server error: {e}")
        finally:
            self.stop()
    
    def handle_client(self, client_socket: socket.socket, address: tuple, client_id: int):
        """
        Handle a single client connection
        
        Args:
            client_socket: Socket connected to client
            address: Client address
            client_id: Client identifier
        """
        try:
            client_socket.settimeout(30)  # 30 second timeout
            
            while True:
                # Receive data from client
                data = client_socket.recv(1024).decode('utf-8')
                
                if not data:
                    print(f"👋 Client #{client_id} disconnected")
                    break
                
                # Parse JSON-RPC request
                try:
                    request = json.loads(data)
                    print(f"\n📥 Client #{client_id} request:")
                    print(f"   Method: {request.get('method')}")
                    print(f"   ID: {request.get('id')}")
                    
                    # Process the request
                    response = self.process_request(request)
                    
                    # Send JSON-RPC response
                    response_json = json.dumps(response)
                    client_socket.sendall(response_json.encode('utf-8'))
                    
                    print(f"📤 Response sent to client #{client_id}")
                    
                except json.JSONDecodeError as e:
                    error_response = {
                        "jsonrpc": "2.0",
                        "error": {"code": -32700, "message": "Parse error"},
                        "id": None
                    }
                    client_socket.sendall(json.dumps(error_response).encode('utf-8'))
                    print(f"❌ JSON Parse error: {e}")
        
        except socket.timeout:
            print(f"⏱️  Client #{client_id} timeout")
        except Exception as e:
            print(f"❌ Error handling client #{client_id}: {e}")
        finally:
            client_socket.close()
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a JSON-RPC 2.0 request and return response
        
        Args:
            request: JSON-RPC request object
            
        Returns:
            JSON-RPC response object
        """
        request_id = request.get('id')
        method = request.get('method')
        params = request.get('params', {})
        
        # Route to appropriate handler
        if method == "ping":
            result = self.method_ping()
        elif method == "echo":
            result = self.method_echo(params)
        elif method == "calculate":
            result = self.method_calculate(params)
        elif method == "get_time":
            result = self.method_get_time()
        else:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": f"Method not found: {method}"},
                "id": request_id
            }
        
        return {
            "jsonrpc": "2.0",
            "result": result,
            "id": request_id
        }
    
    def method_ping(self) -> Dict[str, str]:
        """Ping method - simple health check"""
        print("   → Processing: ping")
        return {"status": "pong", "message": "Server is alive!"}
    
    def method_echo(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Echo method - return what client sends"""
        message = params.get("message", "")
        print(f"   → Processing: echo('{message}')")
        return {"echoed": message, "length": len(message)}
    
    def method_calculate(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate method - simple arithmetic"""
        operation = params.get("operation")
        a = params.get("a", 0)
        b = params.get("b", 0)
        
        print(f"   → Processing: calculate({a} {operation} {b})")
        
        try:
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return {"error": "Division by zero"}
                result = a / b
            else:
                return {"error": f"Unknown operation: {operation}"}
            
            return {
                "operation": operation,
                "operands": {"a": a, "b": b},
                "result": result
            }
        except Exception as e:
            return {"error": str(e)}
    
    def method_get_time(self) -> Dict[str, Any]:
        """Get time method - return current timestamp"""
        print("   → Processing: get_time")
        return {
            "timestamp": time.time(),
            "readable": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def stop(self):
        """Stop the server"""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("\n🛑 Server stopped")


def main():
    """Main entry point"""
    print("="*70)
    print("🌐 Local MCP Server - Educational Implementation")
    print("="*70)
    print("\nSupported methods:")
    print("  • ping - Health check")
    print("  • echo - Echo back a message")
    print("  • calculate - Simple arithmetic (add, subtract, multiply, divide)")
    print("  • get_time - Get current server time")
    print("\nProtocol: JSON-RPC 2.0 over TCP")
    print("Start a client to connect (mcp_client_local.py)")
    print("\n" + "="*70 + "\n")
    
    # Create and start server
    server = SimpleMCPServer(host="localhost", port=5555)
    server.start()


if __name__ == "__main__":
    main()
