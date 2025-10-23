# Live Demo Script

## Preflight (before participants join)
- Launch Android Studio with the repository opened.
- Start a terminal tab in the IDE pointing to the project root and activate the virtual environment.
- Ensure Copilot is logged in and suggestions appear (type `fun demo` in a Kotlin file and accept a suggestion to prove it works).
- Open `catfacts.http` scratch file with the GET request prepared.

## Demo Timeline
1. **00:00 – Set the stage (1 min)**
   - Show the slides with agenda and outcomes.
   - Mention the Cat Facts API and explain the plan.
2. **01:00 – Project tour (2 min)**
   - Walk through the repository structure (`docs`, `src`, `tests`).
   - Highlight `pyproject.toml` and explain dependencies.
3. **03:00 – Copilot-assisted scaffolding (6 min)**
   - Create a new file `src/catfacts_mcp/server.py` (or open existing stub).
   - Prompt Copilot: “Create a FastMCP server with one tool that fetches a cat fact using httpx.”
   - Accept/refine suggestions, narrating the MCP concepts.
4. **09:00 – API exploration (4 min)**
   - Switch to `catfacts.http` and run the request.
   - Show the JSON response and map fields to the tool implementation.
5. **13:00 – Implement the HTTP client (4 min)**
   - Open `src/catfacts_mcp/http_client.py` and explain the `CatFactsClient` class.
   - Discuss error handling and the benefits of isolating API logic.
6. **17:00 – Wire up the server entrypoint (3 min)**
   - Review `create_server()` and show how the lifespan manager keeps a shared client.
   - Demonstrate running `python -m catfacts_mcp.server` to start the stdio server (use local machine, not sandbox).
7. **20:00 – Run automated tests (3 min)**
   - Execute `pytest -q` from the IDE terminal.
   - Explain mocked responses and why we avoid live HTTP calls in CI.
8. **23:00 – Showcase MCP integration (4 min)**
   - If time permits, connect a compatible MCP client (e.g., VS Code or Claude Desktop) and call the `cat_fact` tool.
   - Otherwise, describe the integration steps using slides.
9. **27:00 – Q&A and recap (3 min)**
   - Return to slides summarizing what attendees learned and next steps.

## Fallback Strategies
- If the live API is unreachable, run `tests/sample_responses.json` (recorded data) and modify the tool to read from disk.
- Keep screenshots of successful requests in the slides for quick reference.
- Prepare a local mock server (e.g., `python -m http.server`) serving static JSON as a last resort.
