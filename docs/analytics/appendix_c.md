# Appendix C: Running Analytics in Command Line Mode



WebLOAD Analytics can be executed in command line mode. This enables incorporating WebLOAD Analytics in scripts. 



Two executables are available: 

- WLAnalyticsCMD.exe – Automatically generates a report for a specified session, and publishes or prints it. WebLOAD Analytics then closes. 
- WLAnalytics.exe – Launches the WebLOAD Analytics UI, and generates a report for a specified session.  

The executables are located in *`<Installation dir>`*`\bin`. For example: `C:\Program Files\RadView\WebLOAD\bin`.



## Running WLAnalyticsCMD.exe

Use this executable to generate a report for a specified session, and publish or print it. 

**Syntax** 

`WLAnalyticsCmd.exe –m U|P {-t template_path}|{-p portfolio_path} {-s session_name}|{-ls session_path} [-f DOC|ODT|HTML|XLS|RTF|PDF] [-l report_location] [-n output_report_name] [-h]` 



**Parameters** 

| **Parameter**                | **Description**                                              | **Comments**                                                 |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **-m**                       | Indicates  the action. Specify one of the following<br><br> **U** – Publish. <br>**P** – Print. | Mandatory  parameter.                                        |
| **-t** *`template_path`*       | Generates  a chart from a specified template. You must specify the path to the template  directory (either absolute or relative to the gallery). | You must  specify one of the two options: **-t** or **–p**.  |
| **-p** *`portfolio_path`*      | Generates  a report from a portfolio.  You must  specify the path to the portfolio directory (either absolute or relative to  the Portfolio category). |                                                              |
| **-s** *`session_name`*        | Specifies  a session already loaded into WebLOAD.  You must  specify the session name.<br><br> **Note**: You can use this parameter multiple times to  specify multiple sessions. This is necessary if you are generating a  regression chart. | You must specify one of the two  options: **-s** or **–ls**. |
| **-ls** *`session_path`*       | Specifies  a load session file to import into WebLOAD.  You must  specify the full path.  **Note**: You can use this parameter multiple times to load multiple sessions. This  is necessary if you are generating a regression chart. |                                                              |
| **-f**                       | Specifies  the output format for a published report.  Select  one of the following: **DOC**, **ODT**, **HTML**, **XLS**, **RTF**, or **PDF**.<br>  If you  do not specify an output format, the default format, specified in Analytics  Preferences, is used. | Optional parameter.                                          |
| **-l** *`report_location`*     | Specifies  the location of the published report. If you do not specify a location, the  default location, specified in Analytics Preferences, is used. | Optional parameter.                                          |
| **-n** *`output_report_name`* | Specifies  a name for the newly created report. If you do not specify a name, the  application provides a default name. | Optional parameter.                                          |
| **-h**                       | Displays  the help.                                          | Optional parameter.                                          |



> **Note:** Note that you must specify: 
>
> - Publish or print. 
> - A template or portfolio.  
> - A session, either previously loaded or to be imported. 



**Examples** 

To load the `mysession.ls` Load Session, generate a ‘General/Load Size Summary’ chart, and publish it in the default file format, in the default location, under the name `test-report`: 

`WLAnalyticsCmd.exe -m U -t "General\Load Size Summary" -ls "C:\mysession.ls" –n "test-report"` 

To use the loaded `first-session` Load Session, generate a ‘Summary Portfolio’ portfolio, and print it: 

`WLAnalyticsCmd.exe -m P -p "Summary Portfolio" -s “first-session"` 

To use the loaded `first-session` and `second-session` Load Sessions, generate a ‘Regression/Load Size Summary’ regression chart, and publish it as a PDF file in `C:\myreports`, using a default name: 

`WLAnalyticsCmd.exe -m U -t "Regression\Load Size Summary" -s “first- session" -s "second-session" –f PDF –l “c:\myreports”`



**Running WLAnalytics.exe**  

Use this executable to open the WebLOAD Analytics UI, and open a report or generate a report for a specified session. 

**Syntax** 

`WLAnalytics.exe {-t template_path}|{- p portfolio_path}
{-s session_name}|{-ls session_path} [-h] [-noSplash]` 



**Parameters** 

| **Parameter**                            | **Description**                                              | **Comments**                                                |
| ----------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| **-t** *`template_path`*  | Generates  a chart from a specified template. You must specify the path to the template  directory (either absolute or relative to the gallery). | You must specify one of the two options: **-t** or **–p**.  |
| **-p** *`portfolio_path`* | Generates a report from a portfolio.  You must specify the path to the portfolio directory  (either absolute or relative to the Portfolio category). |                                                             |
| **-s** *`session_name`*   | Specifies  a session already loaded into WebLOAD.  You must specify the session name.  **Note**: You can use this parameter multiple times to  specify multiple sessions. This is necessary if you are generating a  regression chart. | You must specify one of the two options: **-s** or **–ls**. |
| **-ls** *`session_path`*  | Specifies a load session file to  import into WebLOAD.  You must  specify the full path.<br><br>**Note**: You can use this parameter multiple times to load multiple sessions. This  is necessary if you are generating a regression chart. |                                                             |
| **-h**                  | Displays the help.                                           | Optional  parameter.                                        |
| **-noSplash**           | Launches without a Splash  screen.                           | Optional  parameter.                                        |



> **Note:** 
>
> Note that you must specify:
>
> - A template, report, or portfolio.
> - A session, either previously loaded or to be imported.



**Examples** 

To open the WebLOAD Analytics UI, load the `mysession.ls` Load Session, and generate a ‘General/Load Size Summary’ chart: 

`WLAnalytics.exe -t "General\Load Size Summary" -ls "C:\mysession.ls"` 

To open the WebLOAD Analytics UI, use the loaded first-session Load Session, and generate a ‘Summary Portfolio’ portfolio: 

`WLAnalytics.exe -p "Summary Portfolio" -s “first-session"`