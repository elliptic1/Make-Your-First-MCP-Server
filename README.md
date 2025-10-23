# Make Your First MCP Server

This repository contains a 30-minute presentation and code-along that guides Android-focused developers through building their first [Model Context Protocol](https://github.com/modelcontextprotocol) (MCP) server. The workshop uses the free Cat Facts API and a Python-based MCP server to demonstrate how to scaffold tooling, integrate public APIs, and rehearse a live demo with GitHub Copilot.

## Contents
- `docs/presentation_plan.md` – Audience definition, learning objectives, and presentation flow.
- `docs/api_research.md` – Research notes, sample endpoints, and JSON responses for the Cat Facts API.
- `docs/ide_setup.md` – Android Studio/IntelliJ setup checklist including Copilot and HTTP client configuration.
- `docs/demo_script.md` – Minute-by-minute script for the live coding portion of the talk.
- `docs/supporting_materials.md` – Slide outline, troubleshooting tips, and participant takeaways.
- `docs/rehearsal_checklist.md` – Run-through checklist covering timing, prompts, and fallback strategies.
- `src/catfacts_mcp/` – Python MCP server implementation.
- `tests/` – Mocked tests validating the Cat Facts HTTP client.

## Quick Start
1. **Create a virtual environment** and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```
2. **Run the tests** (uses mocked HTTP responses):
   ```bash
   pytest -q
   ```
3. **Start the MCP server** locally (stdio transport):
   ```bash
   python -m catfacts_mcp.server
   ```
4. **Call the `cat_fact` tool** from an MCP-compatible client (e.g., Claude Desktop) to fetch a random fact.

> **Note:** The execution sandbox used for automated tests does not allow outbound HTTP calls. Always verify Cat Facts API access on your presentation machine before going live.

## Live Demo Highlights
- Show how GitHub Copilot can bootstrap a FastMCP server and HTTP client.
- Inspect real API responses using the IDE HTTP client scratch files.
- Demonstrate running the server via stdio and discuss how to integrate with MCP-aware editors.
- Share troubleshooting strategies and next steps for attendees to continue building MCP tools.
