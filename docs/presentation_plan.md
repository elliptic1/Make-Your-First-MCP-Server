# Presentation Blueprint

## Audience
- Early-career Android engineers and hobbyist mobile developers who are curious about the Model Context Protocol (MCP).
- Developer advocates or developer relations engineers who run workshops and need a reproducible live-coding guide.
- Hackathon participants who have basic Kotlin/Java familiarity and want to connect MCP tooling to Android projects.

## Key Learning Objectives
1. Understand the core ideas behind MCP (servers, tools, prompts, and resources) and how they fit into everyday Android workflows.
2. Learn how to explore and validate a public HTTP API that will power an MCP server.
3. Configure Android Studio with Copilot and HTTP client utilities to accelerate server development.
4. Scaffold a minimal MCP server that proxies a public API, then expose that server to clients via stdio and HTTP.
5. Practice an end-to-end live demo that includes IDE setup, Copilot prompting, API calls, and troubleshooting strategies.

## Presentation Flow
1. **Introduction (5 minutes)**
   - Welcome, agenda, what attendees will build.
   - Brief overview of MCP concepts and tooling ecosystem.
   - Introduce the Cat Facts API as today’s data source and explain why it is a great teaching example.
2. **Live Coding Demo (20 minutes)**
   - Open Android Studio, confirm plugins, and tour the prepared project folder.
   - Use Copilot to bootstrap the MCP server scaffolding.
   - Show how to craft HTTP requests to the Cat Facts API and inspect responses.
   - Implement the server endpoint and run automated tests.
   - Demonstrate launching the MCP server over stdio and discuss client integration paths.
3. **Wrap-Up (5 minutes)**
   - Recap what was built and the learning objectives.
   - Share troubleshooting tips and recommended follow-up exercises.
   - Point attendees to slides, repo, and additional MCP resources.
