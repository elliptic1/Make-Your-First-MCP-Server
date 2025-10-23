from __future__ import annotations

import asyncio

import respx
from httpx import Response

from catfacts_mcp.config import CatFactsSettings
from catfacts_mcp.http_client import CatFactsClient


def test_fetch_random_fact() -> None:
    async def runner() -> None:
        settings = CatFactsSettings(base_url="https://catfact.ninja")
        client = CatFactsClient(settings)

        with respx.mock(base_url=settings.base_url) as router:
            router.get("/fact").mock(return_value=Response(200, json={"fact": "Cats purr."}))
            data = await client.fetch_random_fact()

        assert data["fact"] == "Cats purr."
        await client.close()

    asyncio.run(runner())
