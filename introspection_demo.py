#!/usr/bin/env python3
"""
MCP Introspection Demo

This script demonstrates how to use MCP introspection tools to discover
server capabilities and interact with them dynamically.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def demonstrate_introspection():
    """Demonstrate MCP introspection capabilities"""
    
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env=None,
    )
    
    print("🔍 MCP Introspection Demo")
    print("=" * 50)
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("\n1️⃣ Getting Server Information")
            print("-" * 30)
            try:
                server_info = await session.call_tool("get_server_info", {})
                print("Server Info:")
                print(json.dumps(server_info.content[0].text, indent=2))
            except Exception as e:
                print(f"Error getting server info: {e}")
            
            print("\n2️⃣ Listing Available Tools")
            print("-" * 30)
            try:
                tools_response = await session.call_tool("list_tools", {})
                tools_data = json.loads(tools_response.content[0].text)
                print("Available Tools:")
                for tool in tools_data["tools"]:
                    print(f"  • {tool['name']}: {tool['description']}")
                    print(f"    Parameters: {json.dumps(tool['parameters'], indent=4)}")
                    print()
            except Exception as e:
                print(f"Error listing tools: {e}")
            
            print("\n3️⃣ Listing Available Resources")
            print("-" * 30)
            try:
                resources_response = await session.call_tool("list_resources", {})
                resources_data = json.loads(resources_response.content[0].text)
                print("Available Resources:")
                for resource in resources_data["resources"]:
                    print(f"  • {resource['uri']}: {resource['description']}")
                    print(f"    Parameters: {json.dumps(resource['parameters'], indent=4)}")
                    print()
            except Exception as e:
                print(f"Error listing resources: {e}")
            
            print("\n4️⃣ Using Discovered Tools")
            print("-" * 30)
            try:
                # Use the add tool that we discovered
                add_result = await session.call_tool("add", {"a": 15, "b": 27})
                print(f"Using 'add' tool: 15 + 27 = {add_result.content[0].text}")
            except Exception as e:
                print(f"Error using add tool: {e}")
            
            print("\n5️⃣ Using Discovered Resources")
            print("-" * 30)
            try:
                # Use the greeting resource that we discovered
                greeting_result = await session.read_resource("greeting://World")
                print(f"Using greeting resource: {greeting_result.contents[0].text}")
            except Exception as e:
                print(f"Error using greeting resource: {e}")
            
            print("\n✅ Introspection Demo Complete!")


if __name__ == "__main__":
    asyncio.run(demonstrate_introspection())
