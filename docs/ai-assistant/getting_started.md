# Getting Started

## Prerequisites

Before you begin, make sure that:

- WebLOAD 14.0 or later is installed, including the WebLOAD Recorder.
- The **WebLOAD AI Recorder Agent** is installed on the same machine. The
  agent is delivered as its own installer (`WebLOAD-AI-Setup-<version>.exe`)
  and runs as a Windows service in the background. Run the installer as an
  administrator.
- Your organization has purchased a WebLOAD AI Assistant package. The AI
  Assistant is a paid add-on, licensed separately from WebLOAD — see
  [Introduction](introduction.md).
- You have a WebLOAD AI account — an email and password provided by your
  administrator from your organization's purchased seats — and the machine
  has internet access.

## Opening the chat

Open the WebLOAD Recorder. The assistant lives in the **AI Assistant**
docking pane inside the Recorder window. If the pane is not visible, enable
it from the Recorder's **View** menu.

## Signing in

Click **Sign in** in the chat panel and enter your WebLOAD AI credentials.
Sign-in is per user: use your own account rather than a shared one, so that
sessions and usage are attributed correctly.

Once signed in, the status chips at the top of the panel show your session,
the Recorder connection, the cloud connection, and your organization's token
balance.

## Your first conversation

Type what you want in plain language. Good first prompts:

- *Record a new script* — the assistant asks for the URL and starts a
  recording session in a capture browser. Walk through your business flow,
  then tell the assistant to stop recording (or press Stop in the Recorder).
- *Open an existing script* — open a `.wlp` project and work on it.
- *Analyze the current script* — get a summary of what the script does.
- *Is the script ready for a load test?* — get a readiness assessment with
  concrete next steps.

The assistant also offers quick-start buttons that match your current state —
for example **Record a new script** when no script is open, or **Replay and
diagnose** when one is.

## How changes are applied

When you ask for a change — correlation, parameterization, validations,
transactions, or a script edit — the assistant first shows a **proposal
card** describing exactly what it wants to change. Nothing is written to
your script until you click **Approve**. Click **Reject** to discard the
proposal.

You can undo an applied change by typing *undo* (and restore it with
*redo*). Undo history is kept for the current agent session.

## The script panel

When a script is loaded, the script panel on the right side of the chat
shows its current content. From the panel you can copy the script to the
Recorder or download it as JavaScript or as a `.wlp` project.
