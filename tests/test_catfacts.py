from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import httpx
from httpx import Response

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from catfacts_mcp.server import CATFACTS_BASE_URL, CATFACTS_TIMEOUT, fetch_cat_fact


def test_fetch_cat_fact() -> None:
    async def runner() -> None:
        async def handler(request: httpx.Request) -> Response:
            assert request.url.path == "/fact"
            return Response(200, json={"fact": "Cats purr."})

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(
            base_url=CATFACTS_BASE_URL,
            timeout=CATFACTS_TIMEOUT,
            transport=transport,
        ) as client:
            data = await fetch_cat_fact(client)

        assert data["fact"] == "Cats purr."

    asyncio.run(runner())
