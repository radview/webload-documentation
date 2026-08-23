# FAQ

**Is the AI Assistant included with WebLOAD?**
No. The AI Assistant is a paid add-on, purchased separately from WebLOAD as
a package of named users and usage tokens. The chat panel appears in the
Recorder from WebLOAD 14.0, but using the assistant requires a purchased
package and a WebLOAD AI account. Contact RadView or your account manager
to purchase or evaluate it.

**What are usage tokens?**
Tokens meter the assistant's work. Every AI-assisted operation consumes
tokens from your organization's balance — lighter operations such as
explaining or analyzing a script cost less; heavier ones such as
correlation and repair cycles cost more. Tokens are consumed for both
successful and unsuccessful attempts. The current balance is shown in the
chat panel's status bar, and your administrator can purchase additional
tokens.

**Does the assistant change my script on its own?**
No. Every script change is presented as a proposal card and applied only
after you approve it. Applied changes can be reversed with *undo* during
the current agent session.

**What does the History button do?**
For a saved Recorder project, **History** keeps a local, per-chat revision
record of stable script changes observed by the Recorder Agent. You can inspect
changes or the full file in unified or side-by-side view, rename a displayed
revision label, and restore an earlier revision after confirmation. History is
separate from *undo* and *redo*. Its source and diffs remain on the Recorder
machine and are not sent as AI context or included in the **Save** diagnostic
package. Starting **New Chat** creates a new history scope and requests removal
of the previous chat's local history. See [Using the History button](getting_started.md#using-the-history-button)
for prerequisites, restore safeguards, and screenshots.

**Does my script leave my machine?**
The recording, replaying, and editing all happen locally, through the
WebLOAD AI Recorder Agent installed on your machine. To answer your
requests, the agent sends the relevant context — your prompt, script
content, and diagnostic data such as logs and traffic summaries — to the
WebLOAD AI cloud service for processing. If your environment restricts
outbound data, contact RadView to discuss your deployment options.

**Can I use the assistant offline?**
No. The assistant requires an internet connection to the WebLOAD AI cloud
service. The WebLOAD Recorder itself remains fully usable offline.

**What information is sent to the cloud service?**
The local Recorder Agent sends the prompt and the script or diagnostic context
needed for the requested operation. When redaction is enabled, the agent applies
built-in pattern-based rules to recognized credentials, tokens, cookies, email
addresses, phone numbers, and credit-card-like numbers. Redaction is enabled by
default, but administrators can configure its mode, including disabling it.
Pattern-based redaction cannot guarantee detection of every sensitive value, so
submit only data that your organization authorizes for AI processing. Recording
and replay are performed locally. Local script history is not sent as AI
context.

**Which browsers and sites can it record?**
The assistant records through the same capture technology as the WebLOAD
Recorder, in a dedicated capture browser it opens for the session. It supports
browser-based HTTP/S flows that the Recorder capture technology can record.

**Do I need to know WebLOAD's JavaScript to use it?**
No — that is the point. You describe what you want in plain language, and
the assistant does the WebLOAD-specific work. Experienced users can still
ask for precise, low-level edits (down to a specific line) and inspect
every proposal before it is applied.

**Where do I report problems or give feedback?**
Through your usual RadView support channel. Include the exact prompt, the
loaded script, the approximate time, and the visible error — see
[Troubleshooting Replays](troubleshooting_replays.md).
