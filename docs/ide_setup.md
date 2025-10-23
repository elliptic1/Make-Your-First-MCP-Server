# Android Studio / IntelliJ Setup Checklist

1. **Install Android Studio or IntelliJ IDEA Ultimate.**
   - Ensure the IDE version is 2023.3 or newer for best MCP plugin compatibility.
2. **Verify Kotlin and Java Support.**
   - Android Studio ships with Kotlin by default; in IntelliJ install the *Kotlin* plugin from `Settings > Plugins` if needed.
3. **Enable GitHub Copilot.**
   - Install the *GitHub Copilot* plugin, sign in with workshop credentials, and run the quickstart to confirm suggestions appear in an editor buffer.
4. **Install HTTP Client Tools.**
   - Android Studio: enable the built-in *HTTP Client* (works from `.http` scratch files).
   - IntelliJ: optionally add the *REST Client* plugin for a more guided UI.
5. **Clone the Workshop Repository.**
   - `git clone https://github.com/.../Make-Your-First-MCP-Server.git`
   - Open the folder as a Gradle-less project (we will run Python tooling, not Android builds).
6. **Create a Python SDK.**
   - Point the IDE to a Python 3.12 interpreter with the workshop virtual environment.
   - Install dependencies with `pip install -e .[dev]`.
7. **Validate API Connectivity.**
   - Create a `catfacts.http` scratch file and paste:
     ```http
     ### Get a random fact
     GET https://catfact.ninja/fact
     ```
   - Click *Run* to send the request. You should receive JSON similar to the samples in `docs/api_research.md`.
   - If behind a proxy, configure `HTTP Proxy` in `Appearance & Behavior > System Settings > HTTP Proxy` and retry.

> **Environment note:** The automated tests in this repository rely on mocked responses because the execution sandbox cannot reach external HTTP services. Run at least one live request locally before the presentation day to confirm connectivity.
