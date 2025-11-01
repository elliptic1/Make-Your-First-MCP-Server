# Supporting Materials

## Slide Outline
1. **Title:** “Build Your First MCP Server (Android Edition)”
2. **Agenda:** Intro → API exploration → Live coding → Testing → Wrap-up.
3. **What is MCP?**
   - Diagram of client ↔ server ↔ tool.
   - Bullet list of capabilities (prompts, tools, resources).
4. **API Spotlight: Cat Facts**
   - Highlight base URL and example JSON (reuse from `docs/api_research.md`).
5. **IDE Setup Checklist**
   - Summarize key plugins and configuration steps.
6. **Live Coding Milestones**
   - Show how `FastMCP`'s lifespan spins up a shared `httpx.AsyncClient` that feeds the `cat_fact` tool.
7. **Testing & Troubleshooting**
   - Explain mocked tests, proxy configuration, and fallback strategies.
8. **Next Steps**
   - Challenge prompts: add pagination, expose `/breeds`, integrate with Android app.
   - Links to MCP specs, Cat Facts docs, workshop repo, and GitHub's MCP Registry blog post for broader ecosystem context ([How to find, install, and manage MCP servers with the GitHub MCP Registry](https://github.blog/ai-and-ml/generative-ai/how-to-find-install-and-manage-mcp-servers-with-the-github-mcp-registry/)).

## Speaker Notes & Tips
- Emphasize how MCP allows Android developers to reuse tooling in IDEs and AI assistants.
- Remind participants to authenticate Copilot before the session to avoid delays.
- Have a second laptop logged into the IDE in case of hardware issues.
- Record sample API responses and place them in `tests/sample_responses.json` for offline demos.

## Troubleshooting Cheat Sheet
| Issue | Symptom | Quick Fix |
| --- | --- | --- |
| Proxy blocking API | HTTP 403/407 errors | Configure IDE proxy settings or use VPN. |
| Copilot silent | No suggestions appear | Re-authenticate Copilot plugin, check status bar. |
| Python dependency errors | `ModuleNotFoundError` during run | Run `pip install -e .[dev]` and reload virtualenv. |
| API downtime | Requests fail repeatedly | Switch to offline JSON fixtures or local mock server. |

## Next Steps for Participants
- Extend the MCP server with additional tools (e.g., list breeds, search facts by keyword).
- Build a simple Android client that calls the MCP server via HTTP.
- Experiment with hosting the MCP server on Render/Fly.io and securing it with API tokens.
