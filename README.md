# mcp-python

This project demonstrates the usage of the FastMCP server with tools and resources.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp-python
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

1. Start the MCP server:
   ```bash
   uvicorn server:mcp --host 0.0.0.0 --port 3000
   ```

   This will start the server on `http://localhost:3000`.

## Running Tests

### Unit Tests
Run the unit tests for the server:
```bash
python -m unittest test_server.py
```

### cURL Tests
Run the cURL-based tests:
```bash
python test_ssh_curl.py
```

Ensure the server is running on `http://localhost:3000` before executing the cURL tests.

## Tools and Resources

- **Tools**:
  - `add`: Adds two numbers. Accessible via `/tools/add`.

- **Resources**:
  - `greeting://{name}`: Returns a personalized greeting. Accessible via `/resources/greeting://{name}`.