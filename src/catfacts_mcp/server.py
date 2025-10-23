"""FastMCP server that proxies the Cat Facts API."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from mcp.server import FastMCP

from .config import CatFactsSettings
from .http_client import CatFactsClient


@asynccontextmanager
async def lifespan(_: FastMCP) -> AsyncIterator[dict[str, CatFactsClient]]:
    """Manage shared resources for the MCP server."""

    client = CatFactsClient(CatFactsSettings())
    try:
        yield {"catfacts": client}
    finally:
        await client.close()


def create_server() -> FastMCP:
    """Instantiate the MCP server with registered tools."""

    app = FastMCP(
        name="Cat Facts Companion",
        instructions="Use the cat-fact tool to retrieve random trivia for demos.",
        lifespan=lifespan,
        dependencies=["httpx"],
    )

    @app.tool()
    async def cat_fact() -> str:
        """Retrieve a random cat fact from catfact.ninja."""

        client: CatFactsClient = app.get_context()["catfacts"]
        data = await client.fetch_random_fact()
        fact = data.get("fact")
        length = data.get("length")
        if fact is None:
            return "Cat fact service returned an unexpected payload."
        if length:
            return f"{fact} (length: {length})"
        return fact

    return app


async def main() -> None:  # pragma: no cover - convenience entrypoint
    """Run the server over stdio when executed as a script."""

    server = create_server()
    await server.run_stdio_async()


if __name__ == "__main__":  # pragma: no cover - convenience entrypoint
    asyncio.run(main())
