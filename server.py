"""A starter MCP server built with the official Python SDK (mcp 2.x, MCPServer).

Run directly:   python server.py
Inspect:        mcp dev server.py
"""

from datetime import datetime, timezone

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("starter-mcp-server")

# In-memory note store (resets when the server restarts).
_notes: dict[str, str] = {}


# ---------- Tools ----------

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def current_time() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


@mcp.tool()
def save_note(title: str, content: str) -> str:
    """Save a note under a title (overwrites an existing note with that title)."""
    _notes[title] = content
    return f"Saved note '{title}'."


@mcp.tool()
def list_notes() -> list[str]:
    """List the titles of all saved notes."""
    return sorted(_notes)


@mcp.tool()
def read_note(title: str) -> str:
    """Read a saved note by title."""
    if title not in _notes:
        raise ValueError(f"No note titled '{title}'.")
    return _notes[title]


# ---------- Resources ----------

@mcp.resource("notes://{title}")
def note_resource(title: str) -> str:
    """Expose each note as a readable resource."""
    return _notes.get(title, f"No note titled '{title}'.")


# ---------- Prompts ----------

@mcp.prompt()
def summarize_notes() -> str:
    """Ask the model to summarize all saved notes."""
    if not _notes:
        return "There are no notes yet. Suggest a few useful notes to create."
    body = "\n\n".join(f"## {t}\n{c}" for t, c in sorted(_notes.items()))
    return f"Summarize these notes in a few bullet points:\n\n{body}"


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
