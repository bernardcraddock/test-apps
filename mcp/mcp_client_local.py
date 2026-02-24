#!/usr/bin/env python3
"""
Local MCP Client - Connects to local MCP server
Demonstrates bidirectional client-server communication
"""

import socket
import json
import time
from typing import Dict, Any, Optional


class LocalMCPClient:
    """
    Client that connects to a local MCP server
    Sends JSON-RPC 2.0 requests and receives responses
    """
    
    def __init__(self, host: str = "localhost", port: int = 5555):
        """
        Initialize the client
        
        Args:
            host: Server host address
            port: Server port
        """
        self.host = host
        self.port = port
        self.socket = None
        self.request_id = 0
        
        print(f"🔌 MCP Client initialized: {host}:{port}")
    
    def connect(self) -> bool:
        """
        Connect to the MCP server
        
        Returns:
            True if connected successfully, False otherwise
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"✅ Connected to server at {self.host}:{self.port}\n")
            return True
        except ConnectionRefusedError:
            print(f"❌ Connection refused. Is the server running?")
            return False
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return False
    
    def create_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a JSON-RPC 2.0 request
        
        Args:
            method: RPC method name
            params: Method parameters
            
        Returns:
            JSON-RPC request object
        """
        self.request_id += 1
        
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self.request_id
        }
        
        if params:
            request["params"] = params
        
        return request
    
    def send_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Send a request to the server and receive response
        
        Args:
            method: RPC method name
            params: Method parameters
            
        Returns:
            Response from server or None if error
        """
        if not self.socket:
            print("❌ Not connected to server")
            return None
        
        # Create and send request
        request = self.create_request(method, params)
        
        print(f"📤 Sending request:")
        print(f"   Method: {method}")
        print(f"   ID: {request['id']}")
        if params:
            print(f"   Params: {params}")
        
        try:
            request_json = json.dumps(request)
            self.socket.sendall(request_json.encode('utf-8'))
            
            # Receive response
            response_data = self.socket.recv(1024).decode('utf-8')
            response = json.loads(response_data)
            
            print(f"\n📥 Response received:")
            print(f"   Status: {'✅ Success' if 'result' in response else '❌ Error'}")
            print(f"   ID: {response.get('id')}")
            
            if 'result' in response:
                print(f"   Result: {json.dumps(response['result'], indent=2)}")
            else:
                error = response.get('error', {})
                print(f"   Error: {error.get('message')}")
            
            print()
            return response
        
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}")
            return None
        except Exception as e:
            print(f"❌ Request error: {e}")
            return None
    
    def disconnect(self):
        """Disconnect from server"""
        if self.socket:
            self.socket.close()
            print("👋 Disconnected from server")


def main():
    """Main entry point - demonstrate client-server communication"""
    
    print("="*70)
    print("🌐 Local MCP Client - Connecting to Server")
    print("="*70 + "\n")
    
    # Create client
    client = LocalMCPClient(host="localhost", port=5555)
    
    # Connect to server
    if not client.connect():
        print("\n❌ Failed to connect. Make sure server is running:")
        print("   python mcp_server.py")
        return
    
    print("="*70)
    print("📋 Running Demonstrations")
    print("="*70 + "\n")
    
    # Example 1: Ping - Health check
    print("#" * 70)
    print("# Example 1: Ping (Health Check)")
    print("#" * 70 + "\n")
    client.send_request("ping")
    
    # Example 2: Echo - Send message to server
    print("#" * 70)
    print("# Example 2: Echo (Send Message)")
    print("#" * 70 + "\n")
    client.send_request("echo", {"message": "Hello from MCP Client!"})
    
    # Example 3: Calculate - Arithmetic operations
    print("#" * 70)
    print("# Example 3: Calculate (Arithmetic)")
    print("#" * 70 + "\n")
    
    operations = [
        ("add", {"operation": "add", "a": 10, "b": 5}),
        ("subtract", {"operation": "subtract", "a": 10, "b": 5}),
        ("multiply", {"operation": "multiply", "a": 10, "b": 5}),
        ("divide", {"operation": "divide", "a": 10, "b": 5}),
    ]
    
    for op_name, params in operations:
        print(f"⚡ Operation: {op_name}")
        client.send_request("calculate", params)
        time.sleep(0.5)  # Small delay for readability
    
    # Example 4: Get Time
    print("#" * 70)
    print("# Example 4: Get Server Time")
    print("#" * 70 + "\n")
    client.send_request("get_time")
    
    # Clean up
    print("="*70)
    print("✅ All examples completed!")
    print("="*70 + "\n")
    
    print("📚 Key Learning Points:")
    print("  1. CLIENT: This Python script (creates connections)")
    print("  2. SERVER: mcp_server.py (listens and responds)")
    print("  3. PROTOCOL: JSON-RPC 2.0 over TCP sockets")
    print("  4. COMMUNICATION: Bidirectional (request → response)")
    print("  5. THREADING: Server handles multiple clients simultaneously")
    print()
    
    client.disconnect()


if __name__ == "__main__":
    main()
