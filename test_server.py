import unittest
import asyncio
from server import mcp

class TestServer(unittest.TestCase):
    def test_add_tool(self):
        # Test the add tool by calling it directly
        async def run_test():
            result = await mcp.call_tool("add", {"a": 2, "b": 3})
            return result
        
        result = asyncio.run(run_test())
        # Extract the text content from the MCP response
        self.assertEqual(result[0].text, "5")

    def test_get_greeting_resource(self):
        # Test the greeting resource by reading it directly
        async def run_test():
            result = await mcp.read_resource("greeting://Alice")
            return result
        
        result = asyncio.run(run_test())
        # Extract the content from the MCP response
        self.assertEqual(result[0].content, "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
