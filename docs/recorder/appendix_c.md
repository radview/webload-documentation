# Appendix C: Launching WebLOAD Recorder Testing through the Command Line Interface

This section provides instructions and examples for using Command Line Interface (CLI) to launch WebLOAD Recorder testing.



## Running WebLOAD Recorder Testing through the CLI

You can also initiate WebLOAD Recorder testing directly through the CLI. You can enter the WebLOAD Recorder launch command into a batch file or into an external script and WebLOAD Recorder will run directly, without user intervention, using the parameters specified.

**To run WebLOAD Recorder testing through the CLI:**

Enter the webloadIDE.exe command together with a series of optional parameters (described below) into your external script to automatically launch a WebLOAD Recorder test. When your script runs, the executable file will invoke WebLOAD Recorder and run the specified test according to the specified parameters.

### Syntax

Use the following syntax to define the parameters for running a WebLOAD Recorder test through a Command Line Interface:

webloadide.exe [<flags>][<project or session name to open>] [<session name to save to>][<Number of rounds to run>]

To run more than one session, append all relevant parameters at the end of the syntax. See examples 2 and 3 in [*Examples* ](#_bookmark354).




### Parameters
When running a test invoked by the executable, you can specify the following parameters:



|**Parameter**|**Description**|
| :- | :- |
|Flags|<p>/a - auto run</p><p>Automatically run the WebLOAD Recorder test without waiting for user input. If this flag is not specified, WebLOAD Recorder is opened with the specified project / session but the test is not automatically run. The system waits for user input.</p>|
|Project or session name to open|The name of the .wlp file or .wls file (Project file or Session file) to run.|
|Session name to save to|The name of the .wls file containing the test data. This file will be saved in the current directory unless otherwise specified.|
|Number of rounds to run|The number of iterations to run during runtime. The default value is 1.|


Parameters are all optional. If no parameters are entered, the executable launches WebLOAD Recorder and does not run a test. If the autorun flag </a> flag is not set, the

< Session name to save to >, and the < Number of rounds to run > parameters are ignored.

### Examples

**Example 1:**

`webloadide.exe test1.wlp`

This command opens WebLOAD Recorder with the test1 project file and waits for user input.

**Example 2:**

`webloadide.exe /a test1.wlp test2.wlp 3`

This command:

- Opens WebLOAD Recorder and automatically runs a test using the test1.wlp

  project file.

- Runs the project for three iterations.
- Saves the test results in the WebLOAD Recorder session file test1.wls, which includes all of the test data and results.

**Example 3:**

`webloadide.exe /a test1.wlp test1.wls 3 /a test2.wlp test2.wls 2`

This command:

- Opens WebLOAD Recorder and automatically runs a test using the test1.wlp

  project file.

- Runs the project test1.wlp for three iterations.
- Saves the test results in the WebLOAD Recorder session file test1.wls, which includes all of the test data and results.
- Opens the WebLOAD Recorder project file test2.wlp.
- Runs the project test2.wlp for two iterations.
- Saves the test results in the WebLOAD Recorder session file test2.wls, which includes all of the test data and results.



