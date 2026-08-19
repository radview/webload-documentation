# Introduction

The WebLOAD AI Assistant is a chat-based assistant embedded in the WebLOAD
Recorder. It helps you create, fix, and optimize load test scripts through
guided recording, correlation, parameterization, validation, and
troubleshooting — until you reach a script that is ready for a load test.

The assistant guides you through the process and acts only with your
involvement: every change it proposes to your script is presented for your
review, and you decide whether to apply it.

The WebLOAD AI Assistant is available starting with WebLOAD 14.0.

**The AI Assistant is a paid add-on, purchased separately from WebLOAD.** It
is not included in a WebLOAD license: your organization purchases an AI
Assistant package — a number of named users plus a balance of usage tokens —
and each user signs in with their own WebLOAD AI account. Without a
purchased package and an account, the chat panel is visible in the Recorder
but the assistant cannot be used. Contact RadView or your account manager to
purchase or evaluate the AI Assistant.

## What the assistant can do

- **Create scripts** — record a business flow in a browser and turn it into a
  WebLOAD script, or open and work on an existing project.
- **Correlate dynamic values** — discover session IDs, tokens, and other
  values that change between recording and replay, and propose correlation
  rules that keep the script runnable.
- **Parameterize** — find hardcoded values worth varying between Virtual
  Clients, such as credentials and repeated form values, and replace them
  with parameters.
- **Validate responses** — add checks that a page really loaded correctly,
  with a failure severity you choose.
- **Organize transactions** — wrap business steps in named transactions so
  results are measurable.
- **Assess readiness** — answer "is this script ready for a load test?" with
  a concrete review of what is present and what is missing.
- **Troubleshoot replays** — run the script, read the logs and traffic, and
  explain why a replay fails and what to do about it.
- **Answer questions** — about your script, the Recorder, WebLOAD scripting,
  and the last replay.

## Who it is for

- New users unfamiliar with load testing who need a guided path to a first
  runnable script.
- Performance engineers new to WebLOAD who know what they want and need the
  WebLOAD-specific steps done for them.
- Experienced WebLOAD engineers who want to cut the time spent on scripting
  and correlation maintenance.

## How it works

The assistant has two parts:

- The **WebLOAD AI Recorder Agent**, a service installed on the same machine
  as the WebLOAD Recorder. It connects the chat to your Recorder — recording,
  replaying, and editing happen locally on your machine.
- The **WebLOAD AI cloud service**, which provides the intelligence. The
  agent sends your requests, together with the script and diagnostic context
  needed to answer them, to the cloud service and carries out the resulting
  actions locally.

An internet connection and a WebLOAD AI account are required. Metered
operations such as analysis, correlation, and script updates consume usage
tokens from your organization's purchased balance; heavier operations (such
as correlation and iterative healing) consume more than lighter ones (such
as explaining a script). Your current balance is always visible in the chat
panel's status bar.
