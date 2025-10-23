# Rehearsal Checklist

1. **Timing Dry Run**
   - Run through the full 30-minute flow with a timer.
   - Track segment durations in `docs/demo_script.md` and adjust pacing.
2. **Environment Verification**
   - Confirm Android Studio launches quickly and Copilot suggestions appear.
   - Test the virtual environment activation and `pytest -q` execution.
   - Send a live request to `https://catfact.ninja/fact` and screenshot the response for slides.
3. **Copilot Prompting Practice**
   - Rehearse the exact prompts (“Create a FastMCP server…”) to ensure Copilot returns predictable suggestions.
   - Prepare manual code snippets in case Copilot output differs on stage.
4. **Fallbacks & Recovery**
   - Practice switching to offline fixtures using a `--offline` flag or by injecting sample JSON.
   - Have commands ready to restart the server or re-run tests after failure.
5. **Hardware & Logistics**
   - Check HDMI/USB-C adapters, clicker, and microphone.
   - Store slides locally and in the cloud for redundancy.
   - Bring printed copies of the troubleshooting cheat sheet.
