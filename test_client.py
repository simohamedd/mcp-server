"""Smoke test: start server.py over stdio, list tools, and call a couple."""

import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    params = StdioServerParameters(command=sys.executable, args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            result = await session.call_tool("add", {"a": 2, "b": 3})
            print("add(2, 3) ->", result.content[0].text)

            await session.call_tool("save_note", {"title": "hello", "content": "world"})
            result = await session.call_tool("read_note", {"title": "hello"})
            print("read_note('hello') ->", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
