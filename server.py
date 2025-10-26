# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add introspection tools
@mcp.tool()
def list_tools() -> dict:
    """List all available tools and their schemas"""
    tools_info = {
        "tools": [
            {
                "name": "add",
                "description": "Add two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "integer", "description": "First number"},
                        "b": {"type": "integer", "description": "Second number"}
                    },
                    "required": ["a", "b"]
                }
            },
            {
                "name": "list_tools",
                "description": "List all available tools and their schemas",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "list_resources",
                "description": "List all available resources and their schemas",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }
    return tools_info


@mcp.tool()
def list_resources() -> dict:
    """List all available resources and their schemas"""
    resources_info = {
        "resources": [
            {
                "uri": "greeting://{name}",
                "description": "Get a personalized greeting",
                "parameters": {
                    "name": {"type": "string", "description": "Name to greet"}
                }
            }
        ]
    }
    return resources_info


@mcp.tool()
def get_server_info() -> dict:
    """Get comprehensive server information and capabilities"""
    return {
        "server_name": "Demo",
        "version": "1.0.0",
        "capabilities": {
            "tools": ["add", "list_tools", "list_resources", "get_server_info"],
            "resources": ["greeting://{name}"],
            "introspection": True
        },
        "description": "A demo MCP server with basic arithmetic and greeting capabilities"
    }


# Run the server
if __name__ == "__main__":
    import asyncio
    import sys
    
    # Print startup information
    print("🚀 Starting MCP Server...", flush=True)
    print("📡 Server: Demo", flush=True)
    print("🔌 Communication: stdio (standard input/output)", flush=True)
    print("⏳ Waiting for MCP client connections...", flush=True)
    print("🛑 Press Ctrl+C to stop the server", flush=True)
    print("-" * 50, flush=True)
    
    try:
        asyncio.run(mcp.run_stdio_async())
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user", flush=True)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Server error: {e}", flush=True)
        sys.exit(1)