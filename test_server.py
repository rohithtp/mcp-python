import unittest
from server import mcp

class TestServer(unittest.TestCase):
    def test_add_tool(self):
        # Debugging: Check if "add" exists in tools
        self.assertIn("add", mcp.tools, "The 'add' tool is missing in mcp.tools")
        # Test the add tool
        result = mcp.tools["add"](2, 3)
        self.assertEqual(result, 5)

    def test_get_greeting_resource(self):
        # Debugging: Check if "greeting://{name}" exists in resources
        self.assertIn("greeting://{name}", mcp.resources, "The 'greeting://{name}' resource is missing in mcp.resources")
        # Test the greeting resource
        result = mcp.resources["greeting://{name}"]("Alice")
        self.assertEqual(result, "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
