# Running WebLOAD from the Command Line

You can run the following WebLOAD components from the command line:

- WebLOAD License – You can register and update your WebLOAD license.
- WebLOAD Console – You can launch a WebLOAD test that invokes the WebLOAD Console and runs a specified test according to the specified parameters.
- WebLOAD Analytics – You can launch WebLOAD Analytics and generate a report for a specified session, then publish or print it.
- WebLOAD Recorder – You can launch a WebLOAD Recorder test that invokes the WebLOAD Recorder and runs a specified test according to the specified parameters.

## Registering and Updating your WebLOAD License through the CLI

You can register or upload a WebLOAD license through a command line interface. You can enter the WebLOAD Update License command into a batch file or into an external script and it will run directly, without user intervention, using the parameters specified.

**To register or update your WebLOAD license through the command line interface:**

Enter the wlUpdateLicenseApplicationCmd command together with the optional parameters (described below) into your external script, to automatically launch a WebLOAD License action.

### Syntax

Use the following syntax to define the parameters for registering or updating a WebLOAD license through a command line interface:

`wlUpdateLicenseApplicationCmd {-help}|{-info}|{-free}|{-file license_file}|{-server server_address}|{-hostid}`

### **Parameters**

|**Parameter**|**Description**|**Comments**|
| :- | :- | :- |
|-help|Display all available command parameters and their syntax.||
|-info|Display the full license details of the installed license.||
|-free|Create and install a license for a free WebLOAD version. This version provides 50 virtual clients, and is available for an unlimited period of time. You can use the free WebLOAD edition immediately after running this command.||
|<p>-file</p><p>*license\_file*</p>|Install the specified license file, which you received from RadView (refer to the *WebLOAD Installation Guide* for further explanations). If license registration is successful, a confirmation appears in the command-line output. You can then begin working with WebLOAD.||
|<p>- server</p><p>*server\_address*</p>|Connect to the WebRM server, whose address is the specified IP address. This option is relevant if you installed a WebRM server. For further explanations, refer to the *WebLOAD Installation Guide*.||
|-hostid|Display the host ID of the computer. This information is needed if you wish to receive a WebLOAD license file from RadView. For further explanations, refer to the *WebLOAD Installation Guide*.||

### Examples

**Example 1:**

`wlUpdateLicenseApplicationCmd -info`

This command provides as output the license information.

**Example 2:**

`wlUpdateLicenseApplicationCmd -file webload.lic`

This command uploads the specified license file, and installs it. Following successful installation, you can begin working with WebLOAD.

## Running a WebLOAD Console Test through the CLI

You can perform load testing through a command line interface. You can enter the WebLOAD Console launch command into a batch file or into an external script and WebLOAD Console will run directly, without user intervention, using the parameters specified.

**To run WebLOAD Console through the command line interface:**

Enter the `WebLOAD.exe` command together with a series of optional parameters (described below) into your external script to automatically launch a WebLOAD test. When your script runs, the executable file will invoke WebLOAD Console and run the specified test according to the specified parameters.

> **Note:** Verify that the script used with the template specified, and any included files, are accessible to the Load Template or Load Session file that will be run.

### Syntax

Use the following syntax to define the parameters for running a WebLOAD test through a command line interface:

`WebLOAD.exe [<file name to open>][<file name to save>]
[<flags>]`

### Parameters

|**Parameter**|**Description**|**Comments**|
| :- | :- | :- |
|File name to open|The name of the `*.tpl` or `*.ls` file (Load Template or Load Session file) to run. |Optional parameter|
|File name to save|The name of the `*.ls` file containing the test data. This file will be saved in the current directory unless otherwise specified.|Optional parameter|
|Flags|<p>- /ar – Automatically run the WebLOAD test without waiting for user input. If this flag is not specified, the Console is called up with the specified Load Template/Load Session but the test is not automatically run. The system waits for user input.</p><p>- /ar *`<*time*>`* – Automatically run the test for the length of time specified in *`<time>`/*</p><p>- /vc <num>– The number of Virtual Client licenses to allocate when using WebRM License Server.</p><p>- /pc `<num>`– The number of Probing Client licenses to allocate when using WebRM License Server.</p><p>- /rc *`<*results\_file\_name*>`* – Place the results in the specified file (an XML file).</p><p>- /ag `<script name>` - The name of an existing script (`*.wlp`) to open.</p>|Optional parameter|

The parameters are all optional. If no parameters are entered, the executable launches the Console and does not run a test. If the autorun flag `</ar>` flag is not set, the

`<file name to save>` and the `<time>` parameters are ignored.

> **Note:** If there is a conflict between the time defined in this command and the time defined in the WebLOAD Scheduler, the load test runs for the shorter of the two periods defined.

### Examples

**Example 1**

`WebLOAD.exe test1.tpl`

This command opens the Console and the `test1.tpl` template. The Console waits for user input.

**Example 2**

`WebLOAD.exe test1.tpl march9.ls /ar 30`

This command opens the Console and automatically runs a test using the `test1.tpl` template file. The test results are saved in the Load Session file `march9.ls`, which includes all of the test data and results. This file is saved in the current directory, unless otherwise specified. The autorun flag is set, meaning that the test runs without user intervention. The test will run for 30 seconds.

**Example 3**

`WebLOAD.exe /ag c:\agendas\MyAgenda.wlp`

This command opens the Console and the WebLOAD Wizard to the script/Mix Selection dialog box. The `MyAgenda.wlp` script is automatically selected and the WebLOAD Wizard waits for user input.

**Example 4**

`WebLOAD.exe test1.tpl march9.ls /ar 30 /rc result1.xml`

This command performs all the actions described in Example 2 above, and in addition the execution return code is saved in `result1.xml`.

**Example 5**

`WebLOAD.exe test1.tpl march9.ls /ar 30 /vc 100 /pc 3`

This command performs all the actions described in Example 2 above, and in addition it allocates 100 virtual clients and 3 probing clients from the WebRM server.

## JSON Based Load test - Console CLI

### Syntax

Use the following syntax to define the parameters for running a WebLOAD test through a command line interface:

| Parameter             | Description                                                | Comments                                               |
|-----------------------|------------------------------------------------------------|--------------------------------------------------------|
| File name to open     | The name of the `*.tpl` or `*.ls` or *`.json` file to run.                   | Optional parameter                                     |
| File name to save     | The name of the `*.ls` file containing the test data.         | Optional parameter                                     |

Example:
`WebLOAD.exe load_test.json test_results.ls /ar /rc result_code.xml`

### Fields

#### Test (required, one)

- `name` (string, required): The name of the test.
- `type` (string, required): The type of the test. The value is "agenda".

#### Agendas (array, required at least one)

- `agendaname` (string, required): The name of the agenda.
- `agendapath` (string, required): The path to the agenda script (js or wlp).
- `percentage` (int, required): The percentage of the agenda.
- `execoptions` (array, optional): The execution options for the agenda. Options are added as wlGlobals settings. See WebLOAD JavaScript Reference Guide for possible values.
  - `Name` (string): The name of the wlGlobals execution option.
  - `Value` (string): The value of the execution option.

#### SleepOptions (dict, optional)

`SleepType` (string) The sleep options for the agenda. (one of the following):

- 1 - Sleep time as recorded
  - `SetMaxSleepTime` (bool): Whether to set the maximum sleep time.
  - `MaxSleepTime` (int): The maximum sleep time.
- 2 - Ignore recorded sleep time
- 3 - Set random sleep time between
  - `SleepRandMax` (int): The maximum random sleep time.
  - `SleepRandMin` (int): The minimum random sleep time.
- 4 - Set sleep time deviation
  - `SleepDeviation` (int): The sleep deviation in percent, so 10 means plus minus 10% of the recorded sleep time.

`TransactionSleepType` (string): The transaction sleep type. (one of the following):

- "0" - Transaction timers include sleep time ('Transaction Time')
- "1" - Transaction timers exclude sleep time ('Transaction Net Time')
- "2" - Transaction timers exclude sleep time but named "Transaction Time"
- "3" - Both timers - including and excluding sleep time

#### Load Machines (one of the following is required)

- ##### LoadGenerator (array)

     A list of objects that represent the load generators to be used in the test.
  - `name` (string, required): The name of the load generator machine. (Each name can only appear once in the list)
  - `type` (string, required): The type of the load generator machine. "PC" for windows or linux load-generator, "Cloud" for cloud based load-generator as defined in the console.

- ##### Locations (array)

    A list of objects that represent the locations used in the test. Locations are defined in the Dashboard and can contain more than one load-generator
  - `distribution` (int, required): The distribution percentage.
  - `name` (string, required): The name of the location.

#### Schedule (dict, required) all times in minutes

- `RampUpTime` (int, optional): The ramp-up time.
- `Duration` (int, optional): The duration of the test.
- `RampDownTime` (int, optional): The ramp-down time.
- `MaxVC` (int, required): The maximum virtual users count.
- `LimitRounds` (bool, optional): Whether to limit the rounds.
- `Rounds` (int): If LimitRounds is set to true, what is the maximum number of rounds to run before stopping the test. The test will still use the proviced schedule of ramp-up, duration and ramp-down but will stop once the total number of rounds reached the target.

#### SlaManager (array, optional)

This list contains one object that specifies the SLA manager settings.

- `name` (string): The name of the SLA rule.
- `message` (string): A message to be shown in case the SLA rules are violated.
- `msg` (string): This is the Action Definition:
  - 0 - Display info message
  - 1 - Display warning
  - 2 - Display error
  - 3 - Display fatal error and stop test execution
- `operator` (string): The operator to be used when evaluating the rule. The value can be "and" or "or".
- `stats` (list of objects): A list of objects that define the statistics for the SLA rule.

Each object in the `stats` list contains the following attributes:

- `id` (string, optional): The ID of the statistic.
- `name` (string, required): The name of the statistic.
- `op` (string, required): The operator to be used when evaluating the statistic. The values can be:
  - ">"
  - "<"
  - ">="
  - "<="
  - "="
- `type` (string, required): The type of the statistic. The values can be "Min", "Max", "Avg", or "Last".
- `value` (number, required): The values to be compared to the statistic.

#### Optional statistics names

- Aborted Rounds
- Attempted Connections
- Connect Time
- Connection Speed (Bits Per Second)
- Content Size
- DNS Lookup Time
- Failed Connections
- Failed Hits
- Failed Hits Per Second
- Failed Rounds
- Failed Rounds Per Second
- Hit Time
- Hits
- Hits Per Second
- Load Size
- Page Time
- Pages
- Pages Per Second
- Packets Sent
- Packets Sent Per Second
- Process Time
- Receive Time
- Response Data Size
- Response Time
- Return status
- Round Time
- Rounds
- Rounds Per Second
- Send Time
- Successful Connections
- Successful Hits
- Successful Hits Per Second
- Successful Rounds
- Successful Rounds Per Second
- Successful Transactions
- Successful Transactions Per Second
- Throughput (Bytes Per Second)
- Time To First Byte
- Transaction Time
- Transactions
- Transactions Per Second

#### SuccessOptions (object, optional)

This object specifies the success options for the test.
combination of the following:

- `FailSevereError` (boolean):  Fail the test if a severe error occurs during the test run.
- `FailOnErrorsCount` (boolean):  Fail the test if the number of errors is higher than.
- `FailOnErrorCountNumber` (number): The number of errors that should occur before the test fails.
- `FailOnWarningsCount` (boolean): Fail the test if the number of warnings is higher than
- `FailOnWarningCountNumber` (number): The number of warnings that should occur before the test fails.
- `FailOnError` (boolean): Stop the test when a failure occours.

#### Sample Json code - simple

```json
{
    "test": {
        "name": "simple script test",        
        "agendas": [
            {
                "agendaname": "myAgenda",
                "agendapath": "C:\\data\\myAgenda.wlp"
            }
        ],
        "loadGenerator": [
            {
                "name": "localhost",
                "type": "PC"
            }
        ],        
        "schedule": {
            "RampUpTime": 20,
            "Duration": 30,
            "RampDownTime": 20,
            "MaxVC": 100
        }        
    }
}
```

#### Sample Json code - advanced

```json
{
    "test": {
        "name": "Detailed script test",
        "type": "agenda",
        "agendas": [
            {
                "agendaname": "myAgenda",
                "agendapath": "C:\\myAgenda.wlp",
                "percentage": 50,
                "execoptions": [
                    {
                        "Name": "UserAgentOption",
                        "Value": "Mozilla/5.0"
                    }
                ],
                "SleepOptions": {
                    "SleepType": "1",
                    "SetMaxSleepTime": true,
                    "MaxSleepTime": 10
                }
            },
            {
                "agendaname": "jsBasedScript",
                "agendapath": "C:\\jsBasedScript.js",
                "percentage": 50
            }
        ],
        "locations": [
            {
                "name": "us_east1",
                "distribution": 50
            },
            {
                "name": "us_west1",
                "distribution": 50
            }

        ],        
        "schedule": {
            "RampUpTime": 60,
            "Duration": 10,
            "RampDownTime": 20,
            "MaxVC": 100,
            "LimitRounds": true,
            "Rounds": 20
        },
        "slaManager": [
            {
                "name": "Check login time and page time",
                "operator": "or",
                "stats": [
                    {
                        "name": "Login Time",
                        "type": "Current Value",
                        "op": ">",
                        "value": 10
                    },
                    {
                        "name": "Page Time",
                        "type": "Current Value",
                        "op": ">",
                        "value": 5
                    }
                ],
                "message": "Login or page time is too high",
                "msg": "2"
            }
        ],
        "successOptions": {
            "FailOnError": true,
            "FailOnErrorsCount": true,
            "FailOnErrorCountNumber": 10,            
            "FailSevereError": true
        }
    }
}
```

## Generating an Analytics Report through the CLI

WebLOAD Analytics can be executed in command line mode. This enables incorporating WebLOAD Analytics in scripts. Two executables are available:

- **WLAnalyticsCMD.exe** – Automatically generates a report for a specified session, and publishes or prints it. WebLOAD Analytics then closes.
- **WLAnalytics.exe** – Launches the WebLOAD Analytics UI, and generates a report for a specified session.

The executables are located in `<Installation dir>\bin`.  For example:

`C:\Program Files\RadView\WebLOAD\bin.`

### Running WLAnalyticsCMD.exe

Use this executable to generate a report for a specified session, and publish or print it.

#### Syntax

**WLAnalyticsCmd.exe –m U**|**P** {**-t** *template\_path*}|{**-p** *portfolio\_path*}

{**-s** *session\_name*}|{**-ls** *session\_path*} [**-f DOC**|**ODT**|**HTML**|**XLS**|**RTF**|**PDF**] [**-l** *report\_location*] [**-n** *output\_report\_name*] [**-h**]

#### Parameters

<table><tr><th colspan="1" valign="top"><b>Parameter</b></th><th colspan="1" valign="top"><b>Description</b></th><th colspan="1" valign="top"><b>Comments</b></th></tr>
<tr><td colspan="1" valign="top"><b>-m</b></td><td colspan="1" valign="top"><p>Indicates the action. Specify one of the following</p><p><b>U</b> – Publish.</p><p><b>P</b> – Print.</p></td><td colspan="1" valign="top">Mandatory parameter.</td></tr>
<tr><td colspan="1" valign="top"><b>-t</b> <i>template_path</i></td><td colspan="1" valign="top"><p>Generates a chart from a specified template.</p><p>You must specify the path to the template directory (either absolute or relative to the gallery).</p></td><td colspan="1" rowspan="2" valign="top"><p></p><p></p><p>You must specify one of the two options:</p><p><b>-t</b> or <b>–p</b>.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-p</b> <i>portfolio_path</i></td><td colspan="1" valign="top"><p>Generates a report from a portfolio.</p><p>You must specify the path to the portfolio directory (either absolute or relative to the Portfolio category).</p></td></tr>
<tr><td colspan="1" valign="top"><b>-s</b> <i>session_name</i></td><td colspan="1" valign="top"><p>Specifies a session already loaded into WebLOAD. You must specify the session name.</p><p><b>Note</b>: You can use this parameter multiple times to specify multiple sessions. This is necessary if you are generating a regression chart.</p></td><td colspan="1" rowspan="2" valign="top"><p></p><p></p><p></p><p></p><p></p><p></p><p>You must specify one of the two options:</p><p><b>-s</b> or <b>–ls</b>.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-ls</b> <i>session_path</i></td><td colspan="1" valign="top"><p>Specifies a load session file to import into WebLOAD.</p><p>You must specify the full path.</p><p><b>Note</b>: You can use this parameter multiple times to load multiple sessions. This is necessary if you are generating a regression chart.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-f</b></td><td colspan="1" valign="top"><p>Specifies the output format for a published report. Select one of the following: <b>DOC</b>, <b>ODT</b>, <b>HTML</b>, <b>XLS</b>, <b>RTF</b>, or <b>PDF</b>.</p><p>If you do not specify an output format, the default format, specified in Analytics Preferences, is used.</p></td><td colspan="1" valign="top">Optional parameter.</td></tr>
<tr><td colspan="1" valign="top"><b>-l</b> <i>report_location</i></td><td colspan="1" valign="top"><p>Specifies the location of the published report.</p><p>If you do not specify a location, the default location, specified in Analytics Preferences, is used.</p></td><td colspan="1" valign="top">Optional parameter.</td></tr>
<tr><td colspan="1" valign="top"><p><b>-n</b></p><p><i>output_report_name</i></p></td><td colspan="1" valign="top">Specifies a name for the newly created report. If you do not specify a name, the application provides a default name.</td><td colspan="1" valign="top">Optional parameter.</td></tr>
<tr><td colspan="1" valign="top"><b>-h</b></td><td colspan="1" valign="top">Displays the help.</td><td colspan="1" valign="top">Optional parameter.</td></tr>
</table>

> **Note:** Note that you must specify:
>
> - Publish or print.
> - A template or portfolio.
> - A session, either previously loaded or to be imported.

#### Examples

**Example 1:**

To load the `mysession.ls` Load Session, generate a ‘General/Load Size Summary’ chart, and publish it in the default file format, in the default location, under the name `test-report`:

`WLAnalyticsCmd.exe -m U -t "General\Load Size Summary" -ls "C:\mysession.ls" –n "test-report"`

**Example 2:**

To use the loaded `first-session` Load Session, generate a ‘Summary Portfolio’ portfolio, and print it:

`WLAnalyticsCmd.exe -m P -p "Summary Portfolio" -s "first- session"`

**Example 3:**

To use the loaded `first-session` and `second-session` Load Sessions, generate a ‘Regression/Load Size Summary’ regression chart, and publish it as a PDF file in C:\myreports, using a default name:

`WLAnalyticsCmd.exe -m U -t "Regression\Load Size Summary" -s`

`"first-session" -s "second-session" –f PDF –l "c:\myreports"`

### Running WLAnalytics.exe

Use this executable to open the WebLOAD Analytics UI, and open a report or generate a report for a specified session.

#### Syntax

`WLAnalytics.exe {-t template_path}|{- p portfolio_path}`

`{-s session_name}|{-ls session_path} [-h] [-noSplash]`

#### Parameters

<table><tr><th colspan="1" valign="top"><b>Parameter</b></th><th colspan="1" valign="top"><b>Description</b></th><th colspan="1" valign="top"><b>Comments</b></th></tr>
<tr><td colspan="1" valign="top"><b>-t</b> <i>template_path</i></td><td colspan="1" valign="top"><p>Generates a chart from a specified template.</p><p>You must specify the path to the template directory (either absolute or relative to the gallery).</p></td><td colspan="1" rowspan="2" valign="top"><p></p><p></p><p>You must specify one of the two options:</p><p><b>-t</b> or <b>–p</b>.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-p</b> <i>portfolio_path</i></td><td colspan="1" valign="top"><p>Generates a report from a portfolio.</p><p>You must specify the path to the portfolio directory (either absolute or relative to the Portfolio category).</p></td></tr>
<tr><td colspan="1" valign="top"><b>-s</b> <i>session_name</i></td><td colspan="1" valign="top"><p>Specifies a session already loaded into WebLOAD. You must specify the session name.</p><p><b>Note</b>: You can use this parameter multiple times to specify multiple sessions. This is necessary if you are generating a regression chart.</p></td><td colspan="1" rowspan="2" valign="top"><p></p><p></p><p></p><p></p><p></p><p></p><p>You must specify one of the two options:</p><p><b>-s</b> or <b>–ls</b>.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-ls</b> <i>session_path</i></td><td colspan="1" valign="top"><p>Specifies a load session file to import into WebLOAD.</p><p>You must specify the full path.</p><p><b>Note</b>: You can use this parameter multiple times to load multiple sessions. This is necessary if you are generating a regression chart.</p></td></tr>
<tr><td colspan="1" valign="top"><b>-h</b></td><td colspan="1" valign="top">Displays the help.</td><td colspan="1" valign="top">Optional parameter.</td></tr>
<tr><td colspan="1" valign="top"><b>-noSplash</b></td><td colspan="1" valign="top">Launches without a Splash screen.</td><td colspan="1" valign="top">Optional parameter.</td></tr>
</table>

> **Note:** Note that you must specify:
>
> - A template, report, or portfolio.
> - A session, either previously loaded or to be imported.
>

#### Examples

**Example 1:**

To open the WebLOAD Analytics UI, load the mysession.ls Load Session, and generate a ‘General/Load Size Summary’ chart:

`WLAnalytics.exe -t "General\Load Size Summary" -ls "C:\mysession.ls"`

**Example 2:**

To open the WebLOAD Analytics UI, use the loaded first-session Load Session, and generate a ‘Summary Portfolio’ portfolio:

`WLAnalytics.exe -p "Summary Portfolio" -s "first-session"`

## Running WebLOAD Recorder Testing through the CLI

You can initiate WebLOAD Recorder testing directly through the CLI. You can enter the WebLOAD Recorder launch command into a batch file or into an external script and WebLOAD Recorder will run directly, without user intervention, using the parameters specified.

**To run WebLOAD Recorder testing through the CLI:**

Enter the WebloadRecorder.exe command together with a series of optional parameters (described below) into your external script to automatically launch a WebLOAD Recorder test. When your script runs, the executable file will invoke WebLOAD Recorder and run the specified test according to the specified parameters.

#### Syntax

Use the following syntax to define the parameters for running a WebLOAD Recorder test **through a Command Line Interface.:**

`webloadide.exe [<flags>][<project or session name to open>]
[<session name to save to>][<Number of rounds to run>]`

To run more than one session, append all relevant parameters at the end of the syntax. See examples 2 and 3 in [*Examples*](#examples).

#### Parameters

When running a test invoked by the executable, you can specify the following parameters:

|**Parameter**|**Description**|**Comments**|
| :- | :- | :- |
|Flags|<p>/a - auto run</p><p>Automatically run the WebLOAD Recorder test without waiting for user input. If this flag is not specified, WebLOAD Recorder is opened with the specified project / session but the test is not automatically run. The system waits for user input.</p><p>/r - auto record</p><p>Start Recorder in recording mode - can be used for recording automation. Can also add  `/time` X to automatically stop recording after X seconds, for example  /time 30. Specify the `.wlp` (or .js) to save to. You can also use special link to control the recording - add transactions and stop recorindg, see [Special Links](#special-link-during-recording) </p>|Optional parameter|
|Project or session name to open|The name of the `.wlp` file or `.wls` file (Project file or Session file) to run.|Optional parameter|
|Session name to save to|The name of the `.wls` file containing the test data. This file will be saved in the current directory unless otherwise specified.|Optional parameter|
|Number of rounds to run|The number of iterations to run during runtime. The default value is 1.|Optional parameter|

The parameters are all optional. If no parameters are entered, the executable launches WebLOAD Recorder and does not run a test. If the autorun flag </a> flag is not set, the `< Session name to save to >`, and the < Number of rounds to run > parameters are ignored.

#### Examples

**Example 1:**

`WebloadRecorder.exe /r test1.wlp /time 60`

Start WebLOAD Recorder in Recording mode, ready to record any traffic that goes to localhost:9884 - for automation, point the traffic to this proxy. Save results to test1 project file and waits for user input. Stop recording after 60 seconds, or when getting stop signal. To stop or add transactions see [special links](#special-link-during-recording).

Tip: To correlate script automatically upon recording, change in WebLOAD Recorder, Tools -> Recording and script generation options -> Correlation Options -> Correlation level to 'Use existing rules' or 'Discover rules' to trigger correlation for recorded scripts.

**Example 2:**

`WebloadRecorder.exe test1.wlp`

This command opens WebLOAD Recorder with the test1 project file and waits for user input.

**Example 3:**

`WebloadRecorder.exe /a test1.wlp test2.wlp 3`

This command:

- Opens WebLOAD Recorder and automatically runs a test using the test1.wlp project file.

- Runs the project for three iterations.

- Saves the test results in the WebLOAD Recorder session file test1.wls, which includes all of the test data and results.

**Example 4:**

`WebloadRecorder.exe /a test1.wlp test1.wls 3 /a test2.wlp test2.wls 2`

This command:

- Opens WebLOAD Recorder and automatically runs a test using the test1.wlp project file.

- Runs the project test1.wlp for three iterations.
- Saves the test results in the WebLOAD Recorder session file test1.wls, which includes all of the test data and results.
- Opens the WebLOAD Recorder project file test2.wlp.
- Runs the project test2.wlp for two iterations.
- Saves the test results in the WebLOAD Recorder session file test2.wls, which includes all of the test data and results.

#### Special Link During Recording

During recording, you can use these special links to trigger special behavior. This can be useful when automating recording that is done through another software, for example when the script is running from Selenium and being recorded by WebLOAD.

- `https://www.radview.com/stop-recording/` - instructs the recording to end
- `https://www.radview.com/begin-transaction/?name=` - Add BeginTransaction with the given name
- `https://www.radview.com/end-transaction/?name=` - Add EndTransaction with the given name
- `https://www.radview.com/code-block/?` - Add JavaScript code block, See [Adding Custom Code During Recording](#adding-custom-code-during-recording)

## Adding Custom Code During Recording

WebLOAD Recorder allows you to inject custom JavaScript code into your test script **while recording**, by making a request to specific special URL. This is useful for Recording automation - you can use any automation platform that is capable of making requests - for example Selenium + Python, or Playright + nodejs, etc.
Make an HTTP request to `https://www.radview.com/code-block/?`

Append query parameters to specify:

- The **JavaScript code** to inject
- The **sections** where the code should be inserted:  
  `InitClient`, `InitAgenda`, `TerminateClient`, `TerminateAgenda`

### Parameters

| Parameter          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `JS`              | Optional. The JavaScript code to insert.            |
| `InitClient`      | Optional. Code will be inserted into the **Init Client** section.            |
| `InitAgenda`      | Optional. Code will be inserted into the **Init Agenda** section.            |
| `TerminateClient` | Optional. Code will be inserted into the **Terminate Client** section.       |
| `TerminateAgenda` | Optional. Code will be inserted into the **Terminate Agenda** section.       |

- At least one of the parameters must be specified.
- All parameters must be URL- encoded.

### Examples

#### Insert code into the main recording agenda

`https://www.radview.com/code-block/?JS=doLogin%28%22user%22%2C%20%22password%22%29`

##### CodeBlock created

``` javascript

/***** WLIDE - ID:2 - CodeBlock *****/
doLogin("user", "password")
// END WLIDE
```

#### Insert code into multiple specific sections

`https://www.radview.com/code-block/?JS=InfoMessage(%22dd%22)&InitClient=message2&InitAgenda=3&TerminateClient=4&TerminateAgenda=9`
