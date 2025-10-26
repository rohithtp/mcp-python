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

    def test_list_tools_introspection(self):
        # Test the list_tools introspection tool
        async def run_test():
            result = await mcp.call_tool("list_tools", {})
            return result
        
        result = asyncio.run(run_test())
        # Check that the result contains tool information
        self.assertIn("tools", result[0].text)
        self.assertIn("add", result[0].text)

    def test_list_resources_introspection(self):
        # Test the list_resources introspection tool
        async def run_test():
            result = await mcp.call_tool("list_resources", {})
            return result
        
        result = asyncio.run(run_test())
        # Check that the result contains resource information
        self.assertIn("resources", result[0].text)
        self.assertIn("greeting://", result[0].text)

    def test_get_server_info_introspection(self):
        # Test the get_server_info introspection tool
        async def run_test():
            result = await mcp.call_tool("get_server_info", {})
            return result
        
        result = asyncio.run(run_test())
        # Check that the result contains server information
        self.assertIn("server_name", result[0].text)
        self.assertIn("Demo", result[0].text)
        self.assertIn("capabilities", result[0].text)

if __name__ == "__main__":
    unittest.main()
