import subprocess
import json

# Define the base URL for the MCP server
BASE_URL = "http://localhost:3000"  # Updated to port 3000

def test_add_tool():
    """Test the 'add' tool using cURL"""
    payload = json.dumps({"a": 2, "b": 3})
    result = subprocess.run(
        [
            "curl",
            "-X", "POST",
            f"{BASE_URL}/tools/add",
            "-H", "Content-Type: application/json",
            "-d", payload
        ],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"cURL failed: {result.stderr}"
    response = json.loads(result.stdout)
    assert response == 5, f"Unexpected response: {response}"

def test_greeting_resource():
    """Test the 'greeting' resource using cURL"""
    name = "Alice"
    result = subprocess.run(
        [
            "curl",
            "-X", "GET",
            f"{BASE_URL}/resources/greeting://{name}"
        ],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"cURL failed: {result.stderr}"
    response = result.stdout.strip()
    assert response == "Hello, Alice!", f"Unexpected response: {response}"

if __name__ == "__main__":
    print("Testing 'add' tool...")
    test_add_tool()
    print("Testing 'greeting' resource...")
    test_greeting_resource()
    print("All tests passed!")
