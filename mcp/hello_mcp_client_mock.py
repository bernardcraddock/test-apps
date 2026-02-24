#!/usr/bin/env python3
"""
Simple MCP Client "Hello World" Example
Demonstrates the basic structure of an MCP (Model Context Protocol) client
"""

import json
import sys


class SimpleMCPClient:
    """A basic MCP client that demonstrates the client-server pattern"""
    
    def __init__(self, server_name="HelloMCPServer"):
        """Initialize the MCP client with a server name"""
        self.server_name = server_name
        self.request_id = 1
        
    def create_request(self, method, params=None):
        """
        Create a JSON-RPC 2.0 formatted request
        
        JSON-RPC format:
        {
            "jsonrpc": "2.0",
            "method": "method_name",
            "params": {...},
            "id": 1
        }
        """
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self.request_id
        }
        
        if params:
            request["params"] = params
            
        self.request_id += 1
        return request
    
    def send_request(self, method, params=None):
        """Send a request to the MCP server"""
        request = self.create_request(method, params)
        print(f"\n📤 Sending request to {self.server_name}:")
        print(json.dumps(request, indent=2))
        return request
    
    def mock_server_response(self, request):
        """
        Simulate an MCP server response
        In a real scenario, this would send to an actual server and receive back
        """
        method = request["method"]
        request_id = request["id"]
        
        # Simulate different responses based on method
        if method == "hello":
            result = {
                "message": "Hello from MCP Server!",
                "version": "1.0",
                "timestamp": "2026-01-29T04:45:00Z"
            }
        elif method == "get_info":
            result = {
                "server_name": self.server_name,
                "capabilities": ["hello", "get_info", "echo"],
                "status": "ready"
            }
        elif method == "echo":
            result = {
                "echo": request.get("params", {}).get("message", "No message"),
                "received_at": "2026-01-29T04:45:00Z"
            }
        else:
            result = {"error": f"Unknown method: {method}"}
        
        # JSON-RPC response format
        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": request_id
        }
        
        return response
    
    def receive_response(self, response):
        """Display the response from MCP server"""
        print(f"\n📥 Response from {self.server_name}:")
        print(json.dumps(response, indent=2))
        return response


def main():
    """Main demonstration"""
    print("=" * 60)
    print("🎯 Simple MCP Client - Hello World Example")
    print("=" * 60)
    
    # Create an MCP client
    client = SimpleMCPClient(server_name="HelloMCPServer")
    
    print("\n" + "=" * 60)
    print("Example 1: Sending a 'hello' request")
    print("=" * 60)
    
    # Send a hello request
    request1 = client.send_request("hello")
    response1 = client.mock_server_response(request1)
    client.receive_response(response1)
    
    print("\n" + "=" * 60)
    print("Example 2: Getting server info")
    print("=" * 60)
    
    # Send a get_info request
    request2 = client.send_request("get_info")
    response2 = client.mock_server_response(request2)
    client.receive_response(response2)
    
    print("\n" + "=" * 60)
    print("Example 3: Echo request with parameters")
    print("=" * 60)
    
    # Send an echo request with parameters
    request3 = client.send_request("echo", {"message": "Hello from MCP Client!"})
    response3 = client.mock_server_response(request3)
    client.receive_response(response3)
    
    print("\n" + "=" * 60)
    print("✅ MCP Client Examples Complete!")
    print("=" * 60)
    
    print("\n📚 Key Concepts:")
    print("  1. CLIENT: Your program (this script)")
    print("  2. SERVER: External service (GitHub, local service, etc.)")
    print("  3. PROTOCOL: JSON-RPC 2.0 for structured communication")
    print("  4. REQUEST: Client sends method + params to server")
    print("  5. RESPONSE: Server replies with result or error")


if __name__ == "__main__":
    main()
