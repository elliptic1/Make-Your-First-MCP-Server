"""Configuration helpers for the Cat Facts MCP server."""

from __future__ import annotations

from dataclasses import dataclass


DEFAULT_BASE_URL = "https://catfact.ninja"


@dataclass(slots=True)
class CatFactsSettings:
    """Simple settings container for the Cat Facts API."""

    base_url: str = DEFAULT_BASE_URL
    timeout_seconds: float = 10.0


__all__ = ["CatFactsSettings", "DEFAULT_BASE_URL"]
