# Checking Script Readiness

Before a script goes into a load test, it should replay cleanly, handle
dynamic values, vary its data, validate its responses, and report per-step
timings. The readiness check reviews all of that in one question.

Ask:

- *Is the script ready for a load test?*
- *What is missing in this script?*
- *Review this script*
- *What should be improved before I use this script?*

The assistant inspects the script and the last replay and reports:

- what the script already covers — recorded flow, transactions,
  validations, parameters, correlation;
- what is missing or weak — for example, no validations, hardcoded
  credentials, or an uncorrelated session value;
- the recommended next steps, in order.

The readiness check is an assessment — it does not change the script. When
it recommends an improvement, ask for it explicitly (for example, *run
correlation* or *parameterize the login fields*) and the assistant starts
the matching workflow with a proposal for your approval.

## Read-only questions

The same workflow answers any inspection question, at any time:

- *Which script is open?*
- *List the transactions, validations, and parameters*
- *What URLs were recorded?*
- *Show the recorder options*
- *Did the last replay pass?*

Read-only questions never record, replay, or modify anything.
