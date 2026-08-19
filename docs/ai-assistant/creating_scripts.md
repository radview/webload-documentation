# Creating and Opening Scripts

## Recording a new script

Tell the assistant to record — for example:

- *Record a new script*
- *Record http://www.example.com*

If you did not include a URL, the assistant asks for one. It then opens a
capture browser on that URL and recording begins. Perform your business flow
in the browser exactly as a real user would — sign in, search, add to cart,
check out.

While recording, the assistant reports what is being captured. When you are
done, either:

- tell the assistant — *stop recording* — or
- press **Stop** in the Recorder, or simply close the capture browser.

The recorded traffic becomes a WebLOAD script, which appears in the
Recorder and in the chat's script panel. The assistant summarizes what was
captured and suggests next steps.

## Opening an existing script

To work on a script you already have:

- *Open an existing script* — the assistant asks which project to open.
- *Open C:\\Projects\\checkout.wlp* — opens a specific project directly.

Scripts open in the WebLOAD Recorder as usual; the assistant works on the
project the Recorder has open.

## Viewing and understanding the script

Ask at any time:

- *Show me the script*
- *Analyze the current script*
- *What URLs were recorded?*
- *List the transactions and validations*

These are read-only questions — the assistant inspects the script and
answers without changing anything.

## Editing the script

Ask for the change in plain language:

- *Add a 3 second sleep after the login request*
- *Comment out line 12*
- *Rename the transaction "Tx1" to "Login"*

The assistant shows a proposal card with the exact change. The script is
modified only after you approve, and an applied change can be reversed with
*undo*.
