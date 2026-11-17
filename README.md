# Starter MCP Server

A minimal [Model Context Protocol](https://modelcontextprotocol.io) server in Python, built with the official SDK (mcp 2.x, `MCPServer`). Use it as a starting point for your own tools.

## What it includes

| Type     | Name              | Description                          |
|----------|-------------------|--------------------------------------|
| Tool     | `add`             | Add two numbers                      |
| Tool     | `current_time`    | Current UTC time                     |
| Tool     | `save_note`       | Save a note (in memory)              |
| Tool     | `list_notes`      | List note titles                     |
| Tool     | `read_note`       | Read a note by title                 |
| Resource | `notes://{title}` | Each note as a resource              |
| Prompt   | `summarize_notes` | Ask the model to summarize all notes |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python server.py        # stdio server
mcp dev server.py       # open the MCP Inspector (needs Node.js)
```

## Use with Claude Code

```bash
claude mcp add starter -- /ABSOLUTE/PATH/mcp-server/.venv/bin/python /ABSOLUTE/PATH/mcp-server/server.py
```

## Use with Claude Desktop

Add this to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "starter": {
      "command": "/ABSOLUTE/PATH/mcp-server/.venv/bin/python",
      "args": ["/ABSOLUTE/PATH/mcp-server/server.py"]
    }
  }
}
```

## Add your own tool

```python
@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

The type hints and docstring become the tool's schema and description automatically.
