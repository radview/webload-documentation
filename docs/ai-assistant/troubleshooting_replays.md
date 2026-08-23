# Troubleshooting Replays

## Diagnosing a failing replay

When a script does not replay correctly, ask:

- *Why did the replay fail?*
- *Replay the current script and tell me what breaks*
- *Diagnose this replay*

The assistant replays the script, builds diagnostics from the run, compares
the replay traffic with the recorded traffic, and reads the replay logs. It
then explains the first failing step and the most likely cause — for
example, an expired session value that needs correlation, a request the
server now rejects, or a script error — and recommends the fix.

The diagnosis separates confirmed evidence from inference. When the available
logs and traffic do not establish a cause, the assistant says that the result
is inconclusive and recommends the next evidence-gathering step instead of
presenting a guess as fact.

When the cause is correlation, the assistant can continue directly into the
correlation workflow; the fix still arrives as a proposal for your
approval.

## Healing a script that used to work

If a script that previously replayed correctly has stopped working — the
application changed, or an environment moved — say so:

- *This script used to work — fix it*
- *Heal this script*

Framing it this way matters: the goal is to restore known-good behavior. The
assistant diagnoses the current replay and prefers the smallest in-place
repair. If the application flow changed too much for a local repair, it can
guide you through re-recording, but it cannot automatically hold an old and a
new recording together to compare, merge, or transplant their changes.

## Common situations

**The Recorder is not responding.** The assistant tells you when it cannot
reach the WebLOAD Recorder. Start the Recorder (or restart it if it is open
but unresponsive) and retry.

**Sign-in required.** Script analysis and changes require a signed-in
WebLOAD AI session. If the chat reports that the session expired, sign in
again from the chat panel.

**No response content saved.** Some operations — response validations in
particular — need the recorded response bodies. If the assistant reports
that no saved response is available, replay or record the script and ask
again.

**Expected requests are missing.** The assistant can inspect active Recorder
URL and content filters before recommending that you change the filters and
record again.

**Out of tokens.** Metered operations consume your organization's usage
tokens. If the balance is exhausted, the chat reports it; contact your
administrator to add tokens.

## Reporting a problem

When something looks wrong, the most useful report to your administrator or
to RadView support includes:

- the exact prompt you typed,
- the script that was loaded,
- the approximate time, and
- the visible error message.
