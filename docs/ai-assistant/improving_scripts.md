# Improving Your Script

A raw recording usually replays incorrectly: session IDs expire, tokens
change, and every Virtual Client submits the same data. The assistant's
improvement workflows close that gap. Each one follows the same pattern —
the assistant analyzes the script, shows you a proposal, and applies it only
after you approve.

## Correlation

Dynamic values — session IDs, CSRF tokens, view states — are captured with
the values that were valid during recording, and are rejected by the server
at replay. Correlation extracts each value from a live response and reuses
it in the requests that follow.

Ask:

- *Run correlation on the current script*
- *Fix the session handling in this script*

The assistant scans the recorded responses for values that appear in later
requests and proposes correlation rules — for example, extracting a value
from a response body or from a cookie. Review the proposed rules and approve
to apply them. By default, approval also runs a verification replay and
reports whether the rules resolved the failure or whether more work is
needed.

If a specific value is the problem, name it: *correlate the SessionId
value*.

Automatic discovery covers common values found in recorded response bodies and
cookies. When you identify a specific dynamic value, the assistant can also
author supported rules from header or regular-expression evidence, and some
proven encoded-value transformations. Specialized XML, XPath, JSON/JSPath,
application-specific replacement expressions, and client-side JavaScript cases
may need additional diagnosis, manual Recorder correlation, or a new recording.
The assistant reports when the evidence points to an unsupported or missing
source rather than claiming that correlation is complete.

## Parameterization

A recorded script submits the same values on every iteration. Ask:

- *Parameterize the login fields*
- *Find the best values to parameterize in this script*

The assistant identifies hardcoded values worth varying — credentials and
form values that repeat through the script — and proposes replacing them
with parameters, naming the exact form fields as they appear in the script.
Approve to apply.

You can also ask for a specific data source or generation method. Supported
parameter definitions include local CSV data, numeric ranges, random strings,
and date/time values. Values can advance for each round, each use, or each
Virtual Client, depending on the requested update policy.

## Response validations

A replay can "pass" while every page returns an error. Validations make
success measurable. Ask:

- *Add a validation that the account page contains "Welcome"*
- *Verify that the checkout page title is "Order Confirmation"*

Supported validation types:

- **Text** — the response contains, or must not contain, a given text.
- **Page title** — the page title equals an expected value.
- **Content length** — the response size is within an expected range.

Each validation carries a **failure severity** that you choose in the
proposal — for example error versus warning — which determines how a failed
check is reported during a load test.

Validations need recorded response content to work from. If the selected
request has no saved response, the assistant asks you to replay or record
first — without changing the script.

## Transactions

Transactions wrap business steps — *Login*, *Search*, *Checkout* — so the
load test reports timing per step. Ask:

- *Add transactions around each business step*
- *Wrap the login requests in a transaction named "Login"*

The assistant proposes transaction boundaries based on the recorded flow;
review the names and boundaries and approve.

## Project and script settings

The assistant can explain two configuration layers that may contain different
values:

- **Current Project Options** — Recorder settings for the active project.
- **Script (wlGlobals)** — values written into the script; these values take
  precedence at run time.

Ask *show the HTTP options* or *which settings can I change?* to inspect both
layers. Ask for a specific change, such as *set the project HTTP version to
HTTP/2* or *enable wlGlobals SaveSource*, to receive a settings proposal for
review before anything is applied.

## Approving, rejecting, and undoing

- Every change arrives as a **proposal card** — the script is untouched
  until you click **Approve**.
- **Reject** discards the proposal. For correlation discovery, which runs
  inside the Recorder, rejecting also restores the script to its
  pre-discovery state.
- Type *undo* to reverse the last applied change, *redo* to reapply it.
  Undo history is kept for the current agent session.
