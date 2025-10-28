"""FastMCP server that proxies the Cat Facts API with minimal boilerplate."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

import httpx
from mcp.server import FastMCP

CATFACTS_BASE_URL = "https://catfact.ninja"
CATFACTS_TIMEOUT = 10.0


async def fetch_cat_fact(client: httpx.AsyncClient) -> dict[str, Any]:
    """Fetch a single random cat fact from the public API."""

    response = await client.get("/fact")
    response.raise_for_status()
    payload: dict[str, Any] = response.json()
    return payload


@asynccontextmanager
async def lifespan(_: FastMCP) -> AsyncIterator[dict[str, httpx.AsyncClient]]:
    """Provide a shared HTTP client for all tool executions."""

    async with httpx.AsyncClient(base_url=CATFACTS_BASE_URL, timeout=CATFACTS_TIMEOUT) as client:
        yield {"catfacts": client}


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

        client: httpx.AsyncClient = app.get_context()["catfacts"]
        data = await fetch_cat_fact(client)
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
