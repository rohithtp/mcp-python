# mcp-python

This project demonstrates the usage of the FastMCP server with tools and resources.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp-python
   ```

2. Install dependencies using one of the following methods:

   **Option A: Using uv (Recommended)**
   ```bash
   uv sync
   ```
   This will create a virtual environment and install all dependencies automatically.

   **Option B: Using pip**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running the Server

The MCP server is designed to work with stdio communication, not HTTP endpoints. To run the server:

**Option A: Using uv (Recommended)**
```bash
uv run python server.py
```

**Option B: Using pip**
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
python server.py
```

The server will run as a stdio server, communicating via standard input/output. This is the standard way MCP servers work.

## Installing New Dependencies

To add new dependencies to the project:

**Option A: Using uv (Recommended)**
```bash
uv add <package-name>
```
This will automatically update `pyproject.toml` and install the package.

**Option B: Using pip**
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install <package-name>
pip freeze > requirements.txt  # Update requirements.txt
```

## Running Tests

### Unit Tests
Run the unit tests for the server:
```bash
uv run python -m unittest test_server.py
```
or with pip:
```bash
source venv/bin/activate
python -m unittest test_server.py
```

### Client Tests
Run the client-server integration tests:
```bash
uv run python client_server.py
```
or with pip:
```bash
source venv/bin/activate
python client_server.py
```

**Note**: The `test_ssh_curl.py` file contains tests for HTTP endpoints that don't exist in this MCP server implementation. MCP servers communicate via stdio, not HTTP.

## Tools and Resources

- **Tools**:
  - `add`: Adds two numbers. Can be called via MCP client using `session.call_tool("add", arguments={"a": 2, "b": 3})`.

- **Resources**:
  - `greeting://{name}`: Returns a personalized greeting. Can be accessed via MCP client using `session.read_resource("greeting://Alice")`.