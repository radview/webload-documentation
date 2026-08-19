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

The assistant replays the script, scans the responses for values that
appear in later requests, and proposes correlation rules — for example,
extracting a value from a response body or from a cookie. Review the
proposed rules and approve to apply them. After applying, replay the script
to confirm the result; the assistant reports what improved.

If a specific value is the problem, name it: *correlate the SessionId
value*.

## Parameterization

A recorded script submits the same values on every iteration. Ask:

- *Parameterize the login fields*
- *Find the best values to parameterize in this script*

The assistant identifies hardcoded values worth varying — credentials and
form values that repeat through the script — and proposes replacing them
with parameters, naming the exact form fields as they appear in the script.
Approve to apply.

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

## Approving, rejecting, and undoing

- Every change arrives as a **proposal card** — the script is untouched
  until you click **Approve**.
- **Reject** discards the proposal. For correlation discovery, which runs
  inside the Recorder, rejecting also restores the script to its
  pre-discovery state.
- Type *undo* to reverse the last applied change, *redo* to reapply it.
  Undo history is kept for the current agent session.
