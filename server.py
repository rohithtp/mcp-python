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