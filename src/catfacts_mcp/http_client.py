"""HTTP client utilities for interacting with the Cat Facts API."""

from __future__ import annotations

import logging
from typing import Any

import httpx

from .config import CatFactsSettings

LOGGER = logging.getLogger(__name__)


class CatFactsClient:
    """Lightweight wrapper around the Cat Facts API."""

    def __init__(self, settings: CatFactsSettings | None = None) -> None:
        self._settings = settings or CatFactsSettings()
        self._client = httpx.AsyncClient(base_url=self._settings.base_url, timeout=self._settings.timeout_seconds)

    async def close(self) -> None:
        await self._client.aclose()

    async def fetch_random_fact(self) -> dict[str, Any]:
        """Fetch a single random cat fact."""

        endpoint = "/fact"
        LOGGER.debug("Requesting cat fact from %s", endpoint)

        try:
            response = await self._client.get(endpoint)
            response.raise_for_status()
        except httpx.HTTPError as exc:  # pragma: no cover - network dependent
            LOGGER.error("Failed to fetch cat fact: %s", exc)
            raise

        payload: dict[str, Any] = response.json()
        return payload


__all__ = ["CatFactsClient"]
