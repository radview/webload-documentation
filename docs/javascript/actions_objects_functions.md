# WebLOAD Actions, Objects, and Functions

This chapter includes syntax specifications for the objects, properties, methods, and functions most useful for users who wish to program the code within their JavaScript scripts. To simplify and clarify the information presented, this chapter begins with a brief introduction to the concept of the basic Document Object Model, or DOM, upon which most website implementations are based. After this basic introduction, the rest of the chapter consists of reference entries for each item, arranged in alphabetical order.

## AcceptEncodingGzip (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Sets the wlGlobals.AcceptEncodingGzip flag, which enables Gzip support. For each request, WebLOAD sends the header “Accept-Encoding: gzip, deflate”. This tells the server that the client can accept zipped content. As most servers will work correctly even if the client does not send the “Accept-Encoding: gzip, deflate” header, it is recommended not to set the wlGlobals.AcceptEncodingGzip flag because it is performance heavy. However, some servers will fail if it is not sent. The default value of AcceptEncodingGzip is **false**.

You may want to test your application in GZIP mode in the following cases:

* The server only works in GZIP mode and rejects any requests that do not enable GZIP mode.
* GZIP is enabled and the server supports non-GZIP requests. A non-GZIP request means that the web server does less work, but places more stress on the network for large responses. This is acceptable if you are testing a back end server.

However, if you realistically want to test an end-to-end system, enable GZIP support.

**GUI mode**

In WebLOAD Recorder, select or deselect the **GZip Support** checkbox in the Browser Parameters tab of the **Default** or **Current Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Console, select or deselect the **GZip Support** checkbox in the Browser Parameters tab of the **Default** or **Current Options** dialog box or the **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Example** a.AcceptEncodingGZip = true

**See also**

* [*HTTP Components*](./using_javascript_ref.md#http-components)

## AcceptLanguage (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Sets the wlGlobals.AcceptLanguage flag, which defines a global value for the AcceptLanguage header. Some applications/servers will behave differently depending on this setting. The AcceptLanguage flag is a simple string and WebLOAD does not enforce any checks on the values assigned to it.

**Example**

wlGlobals.AcceptLanguage = “En-us”

**GUI mode**

In WebLOAD Recorder, select or deselect the **Accept Language** checkbox in the HTTP Parameters tab of the **Default** or **Current Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Console, select or deselect the **Accept Language** checkbox in the HTTP Parameters tab of the **Default** or **Current Options** dialog box or the **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

Some Asian sites check the AcceptLanguage property, and, if they think the client is working in English, the flow might not be exactly as recorded.

## action (property)

**Property of Object**

* form (see [*form (object)* ](##form-object))

**Description**

Specifies the URL to which the form contents are to be sent for processing (read-only string).

**Example**

`Document.forms[0].action`

## Add() (method)

**Method of Objects**

* wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450))
* wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491))

**Description**

Adds the specified number value to the specified shared integer variable.

**Syntax**

`Add(“SharedIntVarName”, number, ScopeFlag)`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SharedIntVarName         | The name of a shared integer variable to be  incremented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| number                   | An integer with the amount to add to the  specified variable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ScopeFlag                | One of two flags, WLCurrentAgenda or WLAllAgendas, signifying the scope of  the shared variable.  When used as a method of the wlGeneratorGlobal object:`<br>`The WLCurrentAgenda scope flag signifies variable values that you wish  to share between all threads of a single script, part of a single process,  running on a single Load Generator.  `<br>`The WLAllAgendas scope  flag signifies variable values that you wish to share between all threads of  one or more scripts, common to a single spawned process, running on a single  Load Generator.  When used as a method of the wlSystemGlobal object:  `<br>`The WLCurrentAgenda scope flag signifies  variable values that you wish to share between all threads of a single  script, potentially shared by multiple processes, running on multiple Load Generators, system wide.  `<br>`The WLAllAgendas scope flag signifies  variable values that you wish to share between all threads of all scripts,  run by all processes, on all Load  Generators, system-wide. |

**Example**

`wlGeneratorGlobal.Add(“MySharedCounter”, 5, WLCurrentAgenda)`

`wlSystemGlobal.Add(“MyGlobalCounter”, 5, WLCurrentAgenda)`

**See also**

* Get() (see [*Get() (addition method)* ](#_bookmark134))
* Set() (see [*Set() (addition method)* ](#set-addition-method))

## AuthType (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Specifies the authentication method to be used by the server: Kerberos or NTLM. The default value is **NTLM**.

> **Note:** The AuthType property is only relevant for playback.

**Example**

`wlGlobals.AuthType = “Kerberos”`

**GUI mode**

To set the authentication method to be used by the server:

* In WebLOAD Console, select the authentication method in the Authentication tab of the **Default, Current Session, or Script Options** dialog box, accessed from the **Tools** tab of the ribbon.
* In WebLOAD Recorder, select the authentication method in the Authentication tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

If the AuthType property was set to “Kerberos” and the server does not support Kerberos, WebLOAD will automatically change the authentication method to “NTLM”.

**See also**

* KDCServer() (see [*KDCServer (property)* ](#_bookmark226))

## Async (property)

**Property of Object**

* [wlHttp](#wlhttp-object)
* [wlGlobals](#wlglobals-object)

**Description**

Causes the HTTP request to be asynchronous.

The possible values of wlHttp.Async are:

* **false** – the following HTTP command is synchronous (default).
* **true** – the following HTTP command is asynchronous.

When using asynchronous requests, the script does not wait for the request to complete before moving on to the next statement. In order to work with the response, you need to specify one of the asynchronous callback functions – [*onDocumentComplete (property)* ](#_bookmark259)and/or [*onDataReceived (property)*.](#_bookmark258)

**Example**

```javascript
wlHttp.Async = true;

wlHttp.onDocumentComplete = function(document) {

InfoMessage(“Response “ + document.wlSource);

}

wlHttp.Get(“http://something”);
```

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http-components)
* [*onDocumentComplete (property)* ](#_bookmark259)
* [*onDataReceived (property)* ](#_bookmark258)
* The *Using Asynchronous Requests* chapter in the *WebLOAD Scripting Guide*

## BeginTransaction() (function)

**Description**

Use the BeginTransaction() and EndTransaction() functions to define the start and finish of a logical block of code that you wish to redefine as a single logical transaction unit. This enables setting timers, verification tests, and other measurements for this single logical unit.

Optionally, you can specify a period of time, which is the minimum amount of time for the transaction. If the total time of the transaction is less than the time period specified, the machine sleeps for the remainder of the time in order to simulate the intermittent activity of real users.

The behavior of the sleep time is affected by the Sleep Time Control settings that are set in the Current Project Options of the WebLOAD Recorder and Console. These settings can be one of the following:

* **Sleep time as recorded** – Runs the script with the delays corresponding to the natural pauses that occurred when recording the script.
* **Ignore recorded sleep time (default)** – Eliminates any pauses when running the script and runs a worst-case stress test.
* **Set random sleep time** – Sets the ranges of delays to represent a range of users.
* **Set sleep time deviation** – Sets the percentage of deviation from the recorded value to represent a range of users.

For more information on setting the Sleep Time Control settings, see *Configuring Sleep Time Control Options* in the *WebLoad Recorder User’s Guide*.

**Note:** If the transaction fails, it still sleeps for the specified time interval. This is true even if an error not directly connected to the transaction is received, for example, HTTP 500 for a GET within the transaction.

**Syntax**

```javascript
BeginTransaction(TransName, [SleepTime])

…

`<any valid JavaScript code>`

…

EndTransaction(TransName,Verification,[SaveFlag])
```

**Parameters**

| **Parameter Name** | **Description**                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| TransName                | The name assigned to this transaction, a  user-supplied string.                                                            |
| SleepTime                | An integer value  specifying the interval of time (in milliseconds) for the minimum amount of  time for the transaction. . |

> **Note:** BeginTransaction() and EndTransaction() functions are usually accessed and inserted into script files directly through the WebLOAD Recorder. For example, the following figure illustrates a section in the Script Tree bracketed by BeginTransaction and EndTransaction nodes. The EndTransaction node is highlighted in the Script Tree.

To mark the beginning of a transaction, drag the **Begin Transaction** icon from the Load toolbox into the Script Tree, directly above the first action you want to include in the transaction. The Begin Transaction dialog box opens. For additional information about the BeginTransaction() function, refer to *Begin and End Transaction* in the *WebLOAD Recorder User’s Guide*.

**See also**

* EndTransaction() (see [*EndTransaction() (function)* ](#_bookmark110))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark307))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark414))
* [*Transaction Verification Components* ](#_bookmark39)
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark419))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark435)[ *(function)* ](#_bookmark435))

## cell (object)

**Property of Objects**

cell objects are grouped into collections of cells. The cells collection is a property of the following objects:

* row (see [*row (object)* ](#_bookmark316))
* wlTables (see [*w*](#_bookmark492)[*lTables (object)* ](#_bookmark492))

**Description**

A cell object contains all the data found in a single table cell. If the cells collection is a property of a wlTables object, then the collection refers to all the cells in a particular table. If the cells collection is a property of a row object, then the collection refers to all the cells in a particular row. Individual cell objects may be addressed by index number, similar to any object within a collection.

**Syntax**

Individual cell objects may be addressed by index number, similar to any object within a collection. For example, to access a property of the 16th cell in myTable, counting across rows and with the first cell indexed at 0, you could write:

`document.wlTables.myTable.cells[15].<*cell-property*>`

If you are working directly with the cells in a wlTables object, as opposed to the cells within a single row object, you may also specify a range of cells from anywhere within the table using the standard spreadsheet format. Specify a group of cells using a string with the following format:

* Use *letters* to indicate columns, starting with the letter **A** to represent the first column.
* Use *numbers* to indicate rows, starting with the number **1** to represent the first column.

> **Note:** This is not typical-the standard JavaScript index begins at **0** to represent the first element in a set.

**Example**

**For cells within a wlTables object:**

`document.wlTables.myTable.cells[“A1:C3”]`

In this example, the string “A1:C3” includes all cells from the first column of the first row up to the third column in the third row, *reading across rows*. This means that the first cell read is in the first column of the first row, the second cell read is in the *second column* of the *first row*, the third cell read is in the third column of the first row, and so on until the end of the first row. If the table includes eight columns, then the ninth cell read will be in the first column of the second row, and so on.

**For cells within a row object:**

To access a property of the 4th cell in the 3rd row in myTable, counting across rows and with the first cell indexed at 0, you could write:

`document.wlTables.myTable.rows[2].cells[3].<*cell-property*>`

> **Note:** Individual table cells often are merged and span multiple rows. In such a case, the cell will only appear in the collection for the *first* of the set of rows that the cell spans.

**Properties**

Each cell object contains information about the data found in one cell of a table. The cell object includes the following properties:

* cellIndex (see [*cellIndex (property)* ](#_bookmark50))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* tagName (see [*tagName (property)* ](#_bookmark407))

**Comment**

cell is often accessed through the wlTables family of table, row, and cell objects.

**See also**

* cellIndex
*[*Collections* ](using_javascript_ref.md#collections)

* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## cellIndex (property)

**Property of Object**

* cell (see [*cell (object)* ](#_bookmark49))

**Description**

An integer containing the ordinal index number of this cell object within the parent table or row. Cells are indexed starting from zero, so the cellIndex of the first cell in a table or row is 0.

**Comment**

cellIndex is a member of the wlTables family of table, row, and cell objects.

**See also**

* cell
* [*Collections* ](#using_javascript_ref.md#collections)
* cols (see [*cols (property)* ] (wltables-property)
* InnerHTML (see [*InnerHTML (property)* ](#)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## CharEncoding (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Contains the value corresponding to the character set being used. The default value is **Default** (0), the regional settings of the computer. For a complete list of the supported character sets, see [*WebLOAD–supported Character Sets* ](#_bookmark599)on page [479.](#_bookmark599)

**Example**

If you want to specify that you are using Japanese (EUC), set the value of CharEncoding as follows:

`wlGlobals.CharEncoding = 51932`

**GUI Mode**

In WebLOAD Console, select a character set in Character Encoding list box in the Browser Parameters tab of the **Default Options** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, select a character set in the Character Encoding list box in the Browser Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* EnforceCharEncoding (see [*EnforceCharEncoding (property)* ](#_bookmark111))

## checked (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))

**Description**

For an `<INPUT type="checkbox">` or `<INPUT type="radio">` element, the checked property indicates whether the element has the HTML checked attribute, that is, whether the element is selected. The property has a value of true if the element has the checked attribute, or false otherwise (read-only).

## ClearAll() (method)

**Method of Object**

* wlCookie (see [*wlCookie (object)* ](#wlcookie-object)))

**Description**

Delete all cookies set by wlCookie in the current thread.

**Syntax**

wlCookie.ClearAll()

## ClearCookiesAtEndOfRound (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Indicates whether to clear the cookies at the end of each round. The default value of ClearCookiesAtEndOfRound is **true**. By setting this flag to false, the cookies list will not be cleared at the end of each round.

**Example**

`wlGlobals.ClearCookiesAtEndOfRound = false`

## ClearDNSCache() (method)

**Method of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Clear the IP address cache.

**Syntax**

`wlHttp.ClearDNSCache()`

**GUI mode**

In WebLOAD Console, disable caching for the Load Generator or for the Probing

Client during a test session by clearing the appropriate box in the Browser Parameters tab of the **Default**, **Current Session Options** or **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, disable caching during execution by clearing the appropriate box in the Browser Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

To enable or disable DNS caching, set the DNSUseCache (see [*DNSUseCache (property)*](#dnsusecache-property)) property.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_-omponents)
* ClearSSLCache() (see [*ClearSSLCache() (method)* ](#_bookmark59))
* DNSUseCache (see [*DNSUseCache (property)* ](#dnsusecache-property))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))

## ClearSSLCache() (method)

**Method of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Clear the SSL decoding-key cache.

**Syntax**
wlHttp.ClearSSLCache()

**GUI mode**

In WebLOAD Console, disable the SSL cache for the Load Generator or for the Probing

Client during a test session by clearing the appropriate box in the Browser Parameters tab of the **Default**, **Current Session Options** or **Script Options** dialog box, accessed from the **Tools** tab of the ribbon..

In WebLOAD Recorder, disable the SSL cache during execution by clearing the appropriate box in the Browser Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon..

**Comment**

To enable or disable SSL caching, set the SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property)) property.

**See also**

* [*HTTP Components* ](#./using_javascript_ref.md#http_components)
* ClearDNSCache() (see [*ClearDNSCache() (method)* ](#cleardnscache-method))
* DNSUseCache (see [*DNSUseCache (property)* ](#dnsusecache-property))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))

## ClientNum (property)

**Description**

ClientNum is set to the serial number of the client in the WebLOAD test configuration. ClientNum is a read-only local property. Each client in a Load Generator has a unique ClientNum. However, two clients in two different Load Generators may have the same ClientNum.

> **Note:** While ClientNum is unique within a single Load Generator, it is not unique system wide. Use VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432)) to obtain an ID number which is unique system-wide.

If there are N clients in a Load Generator, the clients are numbered 0, 1, 2, ..., N-1. You can access ClientNum anywhere in the local context of the Script (InitClient(), main script, TerminateClient(), etc.). ClientNum does not exist in the global context (InitAgenda(), TerminateAgenda(), etc.).

If you mix Scripts within a single Load Generator, instances of two or more Scripts may run simultaneously on each client. Instances on the same client have the same ClientNum value.

ClientNum reports only the main client number. It does not report any extra threads spawned by a client to download nested images and frames (see [*LoadGeneratorThreads*](#_bookmark241) [*(property)* ](#_bookmark241)).

**Comment**

Earlier versions of WebLOAD referred to this value as ThreadNum. The variable name `ThreadNum` will still be recognized for backward compatibility.

**GUI mode**

WebLOAD recommends accessing global system variables, including the ClientNum identification property, through the WebLOAD Recorder. The variables that appear in this list are available for use at any point in a script file. In the WebLOAD Recorder main window, click **Variable Windows** in the **Debug** tab of the ribbon..

For example, it is convenient to add ClientNum to a Message Node to clarify which client sent the messages that appear in the WebLOAD Console Log window.

**See also**

* GeneratorName() (see [*GeneratorName() (function)* ](#generatorname-function))
* GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](#_bookmark176))
* [*Identification Variables and Functions* ](#_bookmark28)
* RoundNum (see [*RoundNum (variable)* ](#_bookmark314))
* ThreadNum (see [*ThreadNum() (property)* ](#_bookmark412))
* VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432))

## Close() (function)

**Method of Object**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

Closes an open file. When called as a method of the wlOutputFile object, closes the open output file being managed by that object.

**Syntax**

**Function call:**

`Close(filename)`

**wlOutputFile method:**

`wlOutputFile.Close()`

**Parameters**

| **Parameter  Name**       | **Description**                                                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Function  call:**       |                                                                                                                                                |
| Filename                        | A string with the name of the ASCII output file to  be closed.                                                                                 |
| **wlOutputFile  method:** | No parameter is necessary  when this function is called as a method of the wlOutputFile object, since  the file to be closed is already known. |

**Example**

**Function call:**

`Close(MyFavoriteFile)`

**wlOutputFile method:**

`MyFileObj = new wlOutputFile(*filename*)`

`…`

`MyFileObj.Close()`

**Comment**

When you use the Close() function to close a file, data will be flashed to the disk.

**See also**

* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))
* wlOutputFile() (see [*wlOutputFile (object)* ](#_bookmark475))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## CloseConnection() (method)

**Method of Object**

* [wlHttp](#wlhttp-object)

**Description**

Closes all open connections. If CloseConnection() is not called, all connections that were opened with the KeepAlive option (see [*KeepAlive (property)* ](#_bookmark228)) remain open until the end of the round. HTTP connections are automatically closed at the end of each round.

**Syntax**

wlHttp.CloseConnection()

**GUI mode**

WebLOAD recommends maintaining or closing connections through the WebLOAD

Console. Enable maintaining connections for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon..

In WebLOAD Console, enable maintaining connections for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default Options** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon..

In WebLOAD Recorder, enable maintaining connections during execution by checking the appropriate box in the Browser Parameters tab of the **Tools**  **Default** or **Current Project Options** dialog box.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* KeepAlive (see [*KeepAlive (property)* ](#_bookmark228))

## cols (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))
* wlTables (see [*wlTables (object)* ](#_bookmark493))

**Description**

When working with wlTables objects, an integer containing the number of columns in this table. The column number is taken from the COLS attribute in the `<TABLE>` tag. This property is optional. If the table does not have a COLS attribute then the value is undefined. When working with element objects of type TextArea, an integer containing the number of columns in this TextArea.

**Comment**

cols is often accessed through the wlTables family of table, row, and cell objects.

**See also**

* cell
* cellIndex
* [*Collections* ](#using_javascript_ref.md#collections)
*


* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)

## ConnectTimeout (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

ConnectTimeout is used to set the amount of time the system will wait for an HTTP connection to be established before timing out. The ConnectTimeout property is defined in milliseconds. Use the ConnectTimeout property to fine tune the Load Generator performance.

**Example**

 wlGlobals.ConnectTimeout = 7

 **See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## ConnectionSpeed (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)

**Description**

WebLOAD allows users to simulate various system and connection configurations, including setting a ‘virtual limit’ on the connection speed available during a test session. Obviously, the speed of the connection to a website is an important factor in the response time seen by users. Setting a limit on the connection speed during a test session allows testers working with higher-speed connections within their own labs to test systems for clients that may be limited in their own workplace connection speeds.

By default, WebLOAD will work with the fastest available connection speed. Testers may set the connection speed to any slower value, measured in bits per second (bps). For example, users may set values of 14,400 bps, 28,800 bps, etc.

> **Note:** The typical single ISDN line can carry 64 Kb, a double line carries 128 Kb, and a T1 line can handle 1.5 Mb.

**Syntax**

You may assign a connection speed using the wlGlobals.ConnectionSpeed property. For example:

```javascript
InitAgenda()

{

wlGlobals.ConnectionSpeed=28800

}

// main Script body

 [wlHttp.Get(“http://abcdef](http://abcdef/)”) 

Sleep(1000)
```

**GUI mode**

WebLOAD recommends setting the connection speed through the WebLOAD Console. You may set different connection speed limits for both the Load Generator and the Probing Client through the checkboxes on the Connection tab of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## content (property)

**Property of Object**

* wlMetas (see [*w*](#_bookmark471)[*lMetas (object)* ](#_bookmark471))

**Description**

Retrieves the value of the CONTENT attribute of the META tag (read-only string).

**Syntax**

` wlMetas[`

 **Example**

`document.wlMetas[0].content`

**See also**

* httpEquiv (see [*httpEquiv (property)* ](#_bookmark204))
* Name (see [*Name (property)* ](#_bookmark253))
* Url (see [*Url (property)* ](#_bookmark422))

## ContentLength (function)

**Description**

Verifies the content length of the service response.

**Syntax**

wlVerification.ContentLength(operator, length, severity)

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| operator                  | One  of the following mathematical operators:`<br>`< - less than.  `<br>`> - greater than.  * = - equal to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| length                    | The  expected length of the content in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| severity                  | Possible values of this parameter are:`<br>`WLSuccess. The transaction  terminated successfully.  `<br>`WLMinorError. This specific  transaction failed, but the test session may continue as usual. The Script  displays a warning message in the Log window and continues execution from the next statement.  `<br>`WLError. This specific  transaction failed and the current test  round was aborted. The Script displays an error message in the Log window and  begins a new round.  `<br>`WLSevereError. This specific  transaction failed and the test  session must be stopped completely. The Script displays an error message in  the Log window and the Load Generator on  which the  error occurred is stopped. |

**Example**

The following code verifies that the page content length is equal to 120 bytes. In case of failure, WebLOAD displays a fatal error and stops the execution.

`wlVerification.ContentLength("=" , 120, WLSevereError);`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## ContentType (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Specifies the content type of the HTTP request.

**Example**

`wlGlobals.ContentType = “text/html”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## ConvertHiddenFields(method)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Converts hidden fields to dynamic values. This is done by correlate the Script so it uses the dynamic value of the field, not the value recorded in the Script.

The ConvertHiddenFields method takes the URL to be submitted via a Get or Post action and searches for it in the current DOM. This is done by looping over the document.form[] collection until it finds a form whose action matches the URL. It then loops over its elements[] collection. Each element whose type is “hidden” is then inserted into the wlHttp.FormData collection, overriding any existing value. The recorded values are replaced by the dynamic values during playback.

> **Note:** ConvertHiddenFields cannot be accessed directly by the user. See the example in the Comment section below.

**Syntax**

Use

SaveCurrentHiddenFields(url) after the page with the fields and specify the URL of the page.

**Comment**

Because the WebLOAD Recorder does not filter internal frames of a page, there are cases when the data required for the correlation will not be found in the DOM of the previous request.

**For example:**

The page you are working with is called frame1.html and is an internal frame of a page called page.html, which has four internal frames (frame1 - frame 4). You recorded a navigation to page.html and then submitted the form on frame1.html. Thus, your Script would appear as follows:

```
Get page.html 

Get frame1.html 

Get frame2.html 

Get frame3.html

 Get frame4.html

Post the form from frame1.html
```

In order to correlate the data for the final Post, you need the document from frame1. The intervening Get’s, however, will not enable you to get this document. Manually insert the SaveCurrentHiddenFields() method after frame1.html in this example. This method saves the hidden fields so that the automatic correlation can use it when needed.

## CookieDomain (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

When set to true, the client checks if the cookie domain matches the request domain during GET/POST. Use this property if you need to emulate the setting of client side cookies or modify server cookies on the client side.

> **Note:** This property can only be inserted manually.

**Example** wlGlobals.CookieDomain = false **See also**

* CookieExpiration (see [*CookieExpiration (property)* ](#cookieexpiration-proprty))
* CookiePath (see [*CookiePath (property)* ](#cookiepath-property))

## CookieExpiration (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

When set to true, the client checks if the cookie expiration matches the system time during GET/POST. Use this property if you need to emulate the setting of client side cookies or modify server cookies on the client side.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.CookieExpiration = false

**See also**

* CookieDomain (see [*CookieDomain (property)* ](#cookiedomain-property))
* CookiePath (see [*CookiePath (property)* ](#cookiepath-property))

## CookiePath (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

When set to true, the client checks if the cookie path matches the request path during GET/POST. Use this property if you need to emulate the setting of client side cookies or modify server cookies on the client side.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.CookiePath = false

**See also**

* CookieDomain (see [CookieDomain (property) ](#cookiedomain-property))
* CookieExpiration (see [*CookieExpiration (property)* ](#cookieexpiration-property))

## CopyFile() (function)

**Description**

Copies files from a source file on the console to a destination file on the Load Generator. The destination file is either explicitly or automatically named. CopyFile can copy both text and binary data files.

**Syntax**

CopyFile(SrcFileName [, DestFileName])

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SrcFileName              | A literal string or  variable containing the full literal name of the file to be copied. WebLOAD  assumes that the source file is located in the default directory specified in  the File Locations tab (User Copy Files entry) in the**Tools** ****  **Global Options** dialog box in the WebLOAD  Console or in the **Tools** **** **Settings** dialog box in the WebLOAD Recorder. For additional information about  the file’s location, refer to *Determining  the Included File Location* in the *WebLOAD  Scripting Guide*. |
| DestFileName             | An optional literal string  or variable containing the full literal name of the file into which the  source file will be copied. If the target parameter is omitted, WebLOAD will  copy the source file to the current directory and return the file name as the  return value of the CopyFile function.                                                                                                                                                                                                                                                                        |

**Return Value**

Optionally, a string with the target file name, returned if the DestFileName

parameter is not specified.

**Example**

To copy the auxiliary file src.txt, located on the WebLOAD Console, to the destination file dest.txt on the current Load Generator, use the following command:

```
function InitAgenda() {…CopyFile(“src.txt”, “dest.txt”)…}
```

You may then access the file as usual in the main body of the Script. For example:

`DataArr = GetLine(“dest.txt”)`

It is convenient to specify only the SrcFileName. To copy the auxiliary file file.dat, located on the WebLOAD Console, to the current Load Generator, using a single file name:

```
function InitAgenda() {…filename = CopyFile(“file.dat”)…}…GetLine(filename)…
```

**GUI mode**

> **Note:** CopyFile() and IncludeFile() functions can be added directly to the code in a script through the IntelliSense Editor, described in [*Using the IntelliSense JavaScript*](#_bookmark18) [*Editor* ](#_bookmark18).

**Comment**

WebLOAD does not create new directories, so any directories specified as target directories *must already exist*.

The CopyFile command must be inserted in the InitAgenda() section of your JavaScript program.

The load engine first looks for the file to be copied in the default User Copy Files directory. If the file is not there, the file request is handed over to WebLOAD, which searches for the file using the following search path order:

1. If a full path name has been hardcoded into the CopyFile command, the system searches the specified location. If the file is not found in an explicitly coded directory, the system returns an error code of File Not Found and will not search in any other locations.

**Note:** It is not recommended to hardcode a full path name, since the Script will then not be portable between different systems. This is especially important for networks that use both UNIX and Windows systems.

2. Assuming no hardcoded full path name in the Script code, the system looks for the file in the current working directory, the directory from which WebLOAD was originally executed.
3. Finally, if the file is still not found, the system searches for the file sequentially through all the directories listed in the File Locations tab.

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))
* wlOutputFile() (see [*wlOutputFile (object)* ](#_bookmark475))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## CreateDOM() (function)

**Description**

CreateDOM functions return a complete Document Object Model (DOM) tree. You may compare this expected DOM to the actual DOM generated automatically as your JavaScript Script runs

> **Note:** WebLOAD uses an extended version of the standard DOM. For more information, see *Understanding the WebLOAD DOM structure* in the *WebLOAD Scripting Guide*.

**Syntax**

`DOM = CreateDOM(HTMLFileName)`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| HTMLFileName             | A literal string or  variable containing the full literal name of the HTML file in which the  information about the expected DOM is  found. |

**Return Value**

Returns a complete Document Object Model (DOM) tree.

**Example**

`DOM = CreateDOM(“HTMLsource”)`

**Comment**

One of the most common practices in functional testing is to compare a known set of correct results previously generated by an application (expected data) to the results produced by an actual current execution of the application (actual data). These sets of results are stored in various Document Object Models (DOMs).

The actual DOM is created automatically each time an HTTP request is accessed through the document object. The expected DOM is assigned by the user to a specific HTTP command. To make the verification functions more easily readable, WebLOAD uses the alias ACTUAL to access the actual document and the alias EXPECTED to access the expected document.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)

## CreateTable() (function)

**Description**

WebLOAD provides a CreateTable function to automatically convert the tables found on an HTML page to parallel wlTables objects. This simplifies access to the exact table entry in which the user is interested. The CreateTable() function returns a window object that includes a wlTables collection. This is a collection of wlTables objects, each of which corresponds to one of the tables found on the HTML page used as the function parameter. The table data may be accessed as any standard wlTables data.

    **Parameter Name**                  **Description**                            HTMLFileName                  A literal string or      variable containing the full literal name of the HTML file in which the      tables to be converted are found.

**Syntax** CreateTable(HTMLFileName) **Parameters**

**Return Value**

Returns a window object that includes a wlTables collection.

**Example**

```
NewTableSet = CreateTable(“HTMLTablePage”) NumTables = NewTableSet.wlTables.length FirstTableName = NewTableSet.wlTables[0].id
```

**Comment**

CreateTable() is a member of the wlTables family of table, row, and cell objects.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## Data (property)

**Property of Object**

* [wlHttp](#wlhttp-object)

**Description**

Holds a string to be submitted in an HTTP Post command.

The Data property has two subfields:

* Data.Type – The MIME type for the submission
* Data.Value – The string to submit You can use Data in two ways:
  * As an alternative to FormData if you know the syntax of the form submission.
  * To submit a string that is not a standard HTML form and cannot be represented by FormData.

Data is for posting data that is not meant to be HTTP encoded, for example Web service calls.

**Example**

Thus the following three code samples are equivalent:

//Sample 1

wlHttp.Data.Type = “application/x-www-form-urlencoded” wlHttp.Data.Value = “SearchFor=icebergs&SearchType=ExactTerm” wlHttp.Post(“http://www.ABCDEF.com/query.exe”)

//Sample 2

wlHttp.FormData.SearchFor = “icebergs” wlHttp.FormData.SearchType = “ExactTerm” wlHttp.Post(“http://www.ABCDEF.com/query.exe”)

//Sample 3 wlHttp.Post(“http://www.ABCDEF.com/query.exe” +

“?SearchFor=icebergs&SearchType=ExactTerm”)

**Methods**

* wlClear() (see [*wlClear() (method)* ](#_bookmark440))

**Properties**

* type (see [*type (property)* ](#type-property))
* value (see [*value (property)* ](#value-property))

**Comment**

Data and DataFile are both collections that hold sets of data. Data collections are stored within the Script itself, and are useful when you prefer to see the data directly. DataFile collections store the data in local text files, and are useful when you are working with large amounts of data, which would be too cumbersome to store within the Script code itself. When working with DataFile collections, only the name of the text file is stored in the Script itself.

Your Script should work with either Data or DataFile collections. Do not use both properties within the same Script.

**See also**

* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#get-transaction-method))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#post-method))

## DataFile (property)

**Property of Object**

* [wlHttp](#wlhttp-object)

**Description**

A file to be submitted in an HTTP Post command.

WebLOAD sends the file using a MIME protocol. DataFile has two subfields:

* DataFile.Type-the MIME type
* DataFile.FileName-the name of the file, for example,

`“c:`

WebLOAD sends the file when you call the wlHttp.Post() method.

**Methods**

* wlClear() (see [*wlClear() (method)* ](#_bookmark440))

**Properties**

* FileName (see [*FileName (property)* ](#filename-property))

**Comment**

DataFile is used for sending files and parallels the posting of mulipart data in HTML. Data and DataFile are both collections that hold sets of data. Data collections are stored within the Script itself, and are useful when you prefer to see the data directly. DataFile collections store the data in local text files, and are useful when you are working with large amounts of data which would be too cumbersome to store within the Script code itself, or binary data. When working with DataFile collections, only the name of the text file is stored in the Script itself.

**See also**

* Data (see [*Data (property)* ](#data-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark290))
* value (see [*value (property)* ](#value-property))

## DebugMessage() (function)

**Description**

Displays a debug message in the Log View of WebLOAD Recorder.

    **Parameter Name**                  **Description**                            msg                  A string with an      informative message to be sent to WebLOAD Recorder, to be displayed in      the Log View.

**Syntax** DebugMessage(msg) **Parameters**

**Comment**

If you call DebugMessage() in the main script, WebLOAD sends a debug message to the Log View of WebLOAD Recorder. The message is not written to the Console’s Log

View during script execution and has no impact on the continued execution of the Script.

**GUI mode**

WebLOAD recommends adding message functions to your Script files directly through the WebLOAD Recorder. Drag the **Message** icon from the General toolbox into the Script Tree at the desired location.

**See also**

* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark216))

## DecodeBinaryEnd (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The DecodeBinaryEnd property is used in conjunction with SaveSource and document.wlSource to enable the user to parse binary data returned from the server. SaveSource and document.wlSource are used to store the server response in wlSource. Since the JavaScript engine does not know how to represent NULLs (binary 0), the engine will convert all binary nulls in the response body to the value of the DecodeBinaryNullAs string. The DecodeBinaryEnd and DecodeBinaryStart properties are used to limit this action to a specific range in the response buffer. If they are not set, the engine will search for binary nulls in the entire buffer. DecodeBinaryEnd and DecodeBinaryStart are used as performance safeguards in case the buffer is very large and you want to parse a section at the start of the buffer.

The value of DecodeBinaryEnd starts from 0 and designates an offset from the beginning of the buffer. The default value of DecodeBinaryEnd is **-1**. This indicates that starting from the DecodeBinaryStart location until the end of the buffer will be converted to binary nulls.

**Note:** This property can only be inserted manually.

**Example** wlGlobals.DecodeBinaryEnd=4 **See also**

* DecodeBinaryNullAs (see [*DecodeBinaryNullAs (property)* ](#decodebinarynullas-property)))
* DecodeBinaryStart (see [*DecodeBinaryStart (property)* ](#decodebinarystart-property))

## DecodeBinaryNullAs (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Supports the decoding of binary data. Decoding is not performed by default. In order to decode binary data, the user must call DecodeBinaryNullAs and provide a string value to replace the NULL character.

> **Note:** This property can only be inserted manually.

**Syntax**

wlGlobals.DecodeBinaryNullAs = “TextString”

**Example**

WLGlobals.DecodeBinaryNullAs = “Classified”

**See also**

* DecodeBinaryEnd (see [*DecodeBinaryEnd (property)* ](#decodebinaryend-property))
* DecodeBinaryStart (see [*DecodeBinaryStart (property)* ](#decodebinarystart-property))

## DecodeBinaryStart (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The DecodeBinaryStart property is used in conjunction with SaveSource and document.wlSource to enable the user to parse binary data returned from the server. SaveSource and document.wlSource are used to store the server response in wlSource. Since the JavaScript engine does not know how to represent NULLs (binary 0), the engine will convert all binary nulls in the response body to the value of the DecodeBinaryNullAs string. The DecodeBinaryEnd and DecodeBinaryStart properties

are used to limit this action to a specific range in the response buffer. If they are not set, the engine will search for binary nulls in the entire buffer. DecodeBinaryEnd and DecodeBinaryStart are used as performance safeguards in case the buffer is very large and you want to parse a section at the start of the buffer.

The value of DecodeBinaryEnd starts from 0 and designates an offset from the beginning of the buffer. The default value of DecodeBinaryStart is **-1**. This indicates that starting from the beginning of the buffer until the DecodeBinaryEnd location will be converted to binary nulls.

> **Note:** This property can only be inserted manually.

**Example** wlGlobals.DecodeBinaryStart=1 **See also**

* DecodeBinaryEnd (see [*DecodeBinaryEnd (property)* ](#decodebinaryend-property))
* DecodeBinaryNullAs (see [*DecodeBinaryNullAs (property)* ](#decodebinarynullas-property))

## defaultchecked (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))

**Description**

For an `<INPUT type=“checkbox”>` or `<INPUT type=“radio”>` element, the default checked value of the form element (read-only string).

**See also**

* checked (see [*checked (property)* ](#_bookmark54))
* cols (see [*cols (property)* ](#wltables-object))
* defaultvalue (see [*defaultvalue (property)* ](#defaultvalue-property))
* id (see [*id (property)* ](#_bookmark208))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* MaxLength (see [*MaxLength (property)* ](#_bookmark246))
* Name (see [*Name (property)* ](#_bookmark253))
* option (see [*option (object)* ](#_bookmark264))
* row (see [*row (object)* ](#_bookmark315))
* selectedindex (see [*selectedindex (property)* ](#_bookmark337))
* Size (see [*Size (property)* ](#_bookmark361))
* title (see [*title (property)* ](#_bookmark415))
* type (see [*type (property)* ](#type-property))
* Url (see [*Url (property)* ](#_bookmark422))
* value (see [*value (property)* ](#value-property))

## defaultselected (property)

**Property of Object**

* option (see [*option (object)* ](#_bookmark264))

**Description**

Returns a Boolean value specifying whether this option was the one originally “selected” before any user acted upon this “select” control.

**See also**

* defaultchecked (see [*defaultchecked (property)* ](#defaultchecked-property))
* selected (see [*selected (property)* ](#_bookmark337))
* value (see [*value (property)* ](#value-property))

## defaultvalue (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))

**Description**

The default value of the form element (read-only string).

## DefineConcurrent() (function)

**Description**

Use the DefineConcurrent()function to define the beginning point, after which all Post and Get HTTP requests are collected, but not executed, until an ExecuteConcurrent() function is run. At this point, the collected HTTP requests are executed concurrently, by two or more threads. The number of threads is defined

in WebLOAD Console in the multithreading number in the Browser Parameters tab of the Script Options dialog box.

To simultaneously execute Post and Get HTTP requests, you must define where in the script to begin collecting the requests and where to stop collecting and begin executing them. The HTTP requests are collected until the engine encounters an ExecuteConcurrent() function in the script. For more information about the ExecuteConcurrent() function, see [*ExecuteConcurrent() (function)* ](#_bookmark120).

All requests performed from the beginning of the DefineConcurrent() function to the ExecuteConcurrent() function are stored in an array of documents. You can access every document by index number or document name as follows:

* By index: wlConcurrentDocuments[i]
* By DocName: wlConcurrentDocuments["documentname"]

The DocName is an optional name you set for a document for quick access from wlConcurrentDocuments. The format for setting the name is: wlHttp.DocName = “documentname”

where DocName is written with a capital D and N.

The default document name is: all_Concurrent_`<index>`.

**Example**

DefineConcurrent()

…

`<any valid JavaScript code, including Post and Get requests>` wlHttp.DocName = "document"

…

ExecuteConcurrent()

for (i=0;i<wlConcurrentDocuments.length;i++) InfoMessage("index "+i+" : "+wlConcurrentDocuments[i].URL)

InfoMessage("by DocName: "+wlConcurrentDocuments["document"].URL)

InfoMessage("default name: "

+wlConcurrentDocuments["all_Concurrent_2"].URL)

**GUI mode**

> **Note:** The DefineConcurrent()function is usually inserted into script files directly through the WebLOAD Recorder. Drag the **Define Concurrent** icon from the Load toolbox into the Script Tree at the desired location.

For additional information about the DefineConcurrent() function, refer to *Define Concurrent* in the *WebLOAD Recorder User’s Guide*.

**See also**

* ExecuteConcurrent() (see [*Exec*](#_bookmark48)[*uteConcurrent() (function)* ](#_bookmark48))

## Delete() (method)

### Delete() (HTTP method)

**Method of Objects**

This function is implemented as a method of the following object:

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Delete command.

    **Parameter Name**                  **Description**                            [URL]                  An optional parameter identifying the      document URL.      You may optionally      specify the URL as a parameter of the method. Delete() connects to the first URL that has been      specified from the following list, in the order specified:      *      A Url parameter specified in the method call.      *      The Url property of the wlHttp object.      *      The local default wlLocals.Url.      `<br>`The global default wlGlobals.Url.

**Syntax** Delete([URL] **Parameters**

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Head() (see [*Head() (method)* ](#_bookmark194))
* Header (see [*Header (property)* ](#header-property))
* Options() (see [*Options() (method)* ](#_bookmark266))
* Post() (see [*Post() (method)* ](#_bookmark289))
* Put() (see [*Put() (method)* ](#_bookmark298))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

### Delete() (cookie method)

**Method of Objects**

* wlCookie (see [*wlCookie (object)* ](#_bookmark443))

**Description**

This method deletes all cookies set by wlCookie in the current thread.

**Syntax**

wlCookie.Delete(name, domain, path)

**Parameters**

| **Parameter  Name** | **Description**                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| name                      | A descriptive name used for the cookie to  be deleted, for example, “CUSTOMER”.                               |
| domain                    | The top-level domain name  for the cookie being deleted, for example,[“www.ABCDEF.com](http://www.ABCDEF.com/)”. |
| path                      | The top-level directory  path, within the specified domain, for the cookie being deleted, for example,  “/”.  |

**Example**

wlCookie.Delete(“CUSTOMER”, [“www.ABCDEF.com](http://www.ABCDEF.com/)”, “/”)

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## DeleteEmptyCookies (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Indicates whether to delete existing cookies if the server sends a “set-cookie” header with empty values for the existing cookies. If DeleteEmptyCookies is false, the existing cookies are set to their empty value (null). The default value of DeleteEmptyCookies is **false**.

**Example**

`wlGlobals.DeleteEmptyCookies = false `

**Comments**

Some servers tell the client to delete existing cookies by sending the client empty cookies.

## DisableSleep (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Setting this property defines how the engine should handle the Sleep command in the script. This boolean flag indicates whether the recorded sleep pauses will be included in the test session (false) or ignored (true).

**Example**

`wlGlobals.DisableSleep = true`

**Comment**

Sleep periods during test sessions are by default kept to the length of the sleep period recorded by the user during the original recording session. If you wish to include sleep intervals but change the time period, set DisableSleep to false and assign values to the other sleep properties as follows:

* SleepRandomMin – Assign random sleep interval lengths, with the minimum time period equal to this property value.
* SleepRandomMax – Assign random sleep interval lengths, with the maximum time period equal to this property value.
* SleepDeviation – Assign random sleep interval lengths, with the time period ranging between this percentage value more or less than the original recorded time period.

**GUI mode**

WebLOAD recommends setting the sleep mode through the WebLOAD Console. Select a setting from the Sleep Time Control tab of the **Default**, **Current** or **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* Sleep() (see [*Sleep() (function)* ](#sleep-function)))
* SleepDeviation (see [*SleepDeviation (property)* ](#sleepdeviation-property))
* SleepRandomMax (see [*SleepRandomMax (property)* ](#sleeprandommax-property))
* SleepRandomMin (see [*SleepRandomMin (property)* ](#sleeprandommin-property))

## DNSUseCache (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enable caching of IP addresses that WebLOAD receives from a domain name server. The value of DNSUseCache may be:

* **false** – Disable IP address caching.
* **true** – Enable IP address caching (default).

Assign a true value to reduce the time for domain name resolution. Assign a false value if you want to include the time for name resolution in the WebLOAD performance statistics.

**GUI mode**

WebLOAD recommends enabling or disabling the DNS cache through the WebLOAD Console. Enable caching for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

To clear the DNS cache, set the ClearDNSCache() (see [*ClearDNSCache() (method)* ](#cleardnscache-method)) property.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* ClearDNSCache() (see [*ClearDNSCache() (method)* ](#cleardnscache-method))
* ClearSSLCache() (see [*ClearSSLCache() (method)* ](#clearsslcache-method)))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))

## document (object)

**Description**

Represents the HTML document in a given browser window. The document object is one of the main entry points into the DOM, used to retrieve parsed HTML data. document objects store the complete parse results for downloaded HTML pages. Use the document properties to retrieve links, forms, nested frames, and other information about the document.

document objects are local to a single thread. WebLOAD creates an independent document object for each thread of a script. You cannot create new document objects using the JavaScript new operator, but you can access HTML documents through the properties and methods of the standard DOM objects. document properties are read- only.

**Syntax**

Access all elements of the Browser DOM through the document object, using the standard syntax. For example, to access links, use the following expression:

document.links[0]

**Methods**

* wlGetAllForms() (see [*wlGetAllForms() (method)* ](#wlgetallforms-method))
* wlGetAllFrames() (see [*wlGetAllFrames() (method)* ](#wlgetallframes-method))
* wlGetAllLinks() (see [*wlGetAllLinks() (method)* ](#wlgetalllinks-method))

**Properties**

* form (see [*form (object)* ](#form-object))
* frames (see [*frames (object)* ](#frames-object))
* Image (see [*Image (object)* ](#image-object))
* link (see [*link (object)* ](#link-object))
* location (see [*location (object)* ](#location-object))
* script (see [*script (object)* ](#script-object))
* title (see [*title (property)* ](#title-property))
* wlHeaders (see [*wlHeaders (object)* ](#wlheaders-object))
* wlMetas (see [*wlMetas (object)* ](#wlmetas-object))
* wlSource (see [*wlSource (property)* ](#wlsource-property))
* wlStatusLine (see [*wlStatusLine (property)* ](#wlstatusline-property))
* wlStatusNumber (see [*wlStatusNumber (property)* ](#wlstatusnumber-property))
* wlTables (see [*wlTables (object)* ](#wltables-object))
* wlVersion (see [*wlVersion (property)* ](#wlversion-property))
* wlXmls (see [*wlXmls (object)* ](#wlxmls-object))

## ElapsedRoundTime (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

The minimum amount of time (in milliseconds) for the round to be played back. If the total time it takes for the round to be played back is less than the time period specified, the machine sleeps for the remainder of the time. This property must be set in InitAgenda(). If it is set anywhere else, it is ignored.

The behavior of the sleep time is affected by the Sleep Time Control settings that are set in the Current Project Options of the WebLOAD Recorder and Console. These settings can be one of the following:

* **Sleep time as recorded (default for the Console)** – Runs the script with the delays corresponding to the natural pauses that occurred when recording the script.
* **Ignore recorded sleep time (default for the WebLOAD Recorder)** – Eliminates any pauses when running the script and runs a worst-case stress test.
* **Set random sleep time** – Sets the ranges of delays to represent a range of users.
* **Set sleep time deviation** – Sets the percentage of deviation from the recorded value to represent a range of users.

For more information on setting the Sleep Time Control settings, see *Configuring Sleep Time Control Options* in the *WebLOAD Recorder User’s Guide*.

**Example**

```
function InitAgenda(){wlGlobals.ElapsedRoundTime = 1056}
```

## element (object)

**Property of Object**

element objects are grouped into collections of elements. The elements collection is also a property of the following objects:

* form (see [*form (object)* ](##form-object))

**Description**

Each element object stores the parsed data for a single HTML form element such as

`<INPUT>`, `<BUTTON>`, `<TEXTAREA>`, or `<SELECT>`. The full elements collection stores all the controls found in a given form except for objects of input type=image. (Compare to the form (see [*form (object)* ](##form-object)) object, which stores the parsed data for an entire HTML form.)

element objects are local to a single thread. You cannot create new element objects using the JavaScript new operator, but you can access HTML elements through the properties and methods of the standard DOM objects. element properties are read- only.

**Syntax**

element objects are organized into collections of elements. elements[0] refers to the first child element, elements[1] refers to the second child element, etc. To access an individual element’s properties, check the length property of the elements collection and use an index number to access the individual elements. For example, to

find out how many element objects are contained within forms[1], check the value of:

document.forms[1].elements.length

You can access a member of the elements collection either by its index number or by its HTML name attribute. For example, suppose that the first element of a form is coded by the HTML tag.

`<INPUT type=“text” name=“yourname”>`

You can access this element by writing either of the following expressions:

document.forms[0].elements[0] document.forms[0].elements[“yourname”] document.forms[0].elements.yourname document.forms[0].yourname

**Example**

Access each element’s properties directly using either of the following lines:

document.forms[0].elements[0].type

-Or-

document.forms[0].yourname.type

**Properties**

* checked (see [*checked (property)* ](#_bookmark54))
* cols (see [*cols (property)* ](#wltables-object))
* defaultchecked (see [*defaultchecked (property)* ](#defaultchecked-property))
* defaultvalue (see [*defaultvalue (property)* ](#defaultvalue-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* Name (see [*Name (property)* ](#_bookmark253))
* id (see [*id (property)* ](#_bookmark208))
* InnerImage (see [*InnerImage (property)* ](#innerimage-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* MaxLength (see [*MaxLength (property)* ](#_bookmark246))
* option (see [*option (object)* ](#_bookmark264))
* OuterLink (see [*OuterLink (property)* ](#outerlink-property))
* row (see [*row (object)* ](#_bookmark315))
* selectedindex (see [*selectedindex (property)* ](#_bookmark337))
* Size (see [*Size (property)* ](#_bookmark361))
* title (see [*title (property)* ](#_bookmark415))
* type (see [*type (property)* ](#type-property))
* Url (see [*Url (property)* ](#_bookmark422))
* value (see [*value (property)* ](#value-property))

**Comment**

The most frequently accessed input elements are of type Button, CheckBox, File, Image, Password, Radio, Reset, Select, Submit, Text, and TextArea.

**See also**

* [*Collections* ](#using_javascript_ref.md#collections)
* Image (see [*Image (object)* ](#_bookmark210))
* [*Select* ](#_bookmark329)

## EncodeBinary (property)

The EncodeBinary property is identical to the EncodeRequestBinaryData property. For additional information, see [*EncodeRequestBinaryData (property)* ](#_bookmark107)on page [83.](#_bookmark107)

## imEncodeFormdata (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Sets the wlGlobals.EncodeFormdata flag.

Generally, when an HTTP client (Microsoft Internet Explorer/Firefox or WebLOAD) sends a post request to the server, the data must be HTTP encoded. Special characters such as blanks, “>“ signs, and so on, are replaced by “%xx”. For example, a space is encoded as “%20”.

Turn off the encoding when the script sends large requests that have no data that needs to be encoded. This improves performance as it bypasses the scanning and reformatting of the request buffer.

**GUI mode**

In WebLOAD Console, select or deselect the **Encode Form Data** checkbox in the HTTP Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, select or deselect the **Encode Form Data** checkbox in the HTTP Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Example**

`wlGlobals.EncodeFormData = true`

**See also**

* [*HTTP Components* ](./using_javascript_refmd#http-components)
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## EncodeRequestBinaryData (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

Used to specify if the binary data in requests should be encoded. The default value of EncodeRequestBinaryData is **false**.

For example, if a mobile operator wants to simulate the sending of binary data from the browser (phone) to the server. Part of the binary data is a value (for example, phone number) that needs parameterization. When the EncodeRequestBinaryData flag is set to true, the binary form data "x0Ax0BAMIRx00" appears as "%0A%0BAMIR%00" in the script.

**Example**

wlGlobals.EncodeRequestBinaryData = true

**GUI mode**

In WebLOAD Recorder, check **Encode Binary Data** in the Script Generation tab of the

**Recording and Script Generation Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* EncodeResponseBinaryData (see [*EncodeResponseBinaryData (property)* ](#_bookmark108))
* EncodeBinary (see [*EncodeBinary (property)* ](#encodebinary-property))
* SaveSource (see [*SaveSource (property)* ](#savesource-property))

## EncodeResponseBinaryData (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

Indicates whether binary data sent in responses should be encoded. EncodeResponseBinaryData can be used with web pages that have binary data sent in responses and on which you would want to perform correlation on that binary data.

The default value of EncodeResponseBinaryData is **false**. When set to true, the response will be encoded when the user accesses document.wlSource. The encoding is performed on the original data, when it is accessed. Readable characters that are not letters are not encoded. That is, "!@#$%^&*()" remains "!@#$%^&*()" and carriage return and tab are translated to \r\t. The response is saved in document.wlSource only if the SaveSource flag is set to true.

**Example**

wlGlobals.EncodeResponseBinaryData = true

**See also**

* EncodeRequestBinaryData (see [*EncodeRequestBinaryData (property)* ](#_bookmark107))

## encoding (property)

**Property of Object**

* form (see [*form (object)* ](##form-object))

**Description**

A read-only string that specifies the MIME encoding for the form.

**See also**

* form (see [*form (object)* ](##form-object))

## EndTransaction() (function)

**Description**

Use the BeginTransaction() and EndTransaction() functions to define the start and finish of a logical block of code that you wish to redefine as a single logical transaction unit. This enables setting timers, verification tests, and other measurements for this single logical unit.

**Syntax**

```javascript
BeginTransaction(TransName)

…

`<any valid JavaScript code>`

…

[SetFailureReason(ReasonName)] EndTransaction(TransName,Verification,[SaveFlag],[FailureReason])
```

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TransName                 | The name assigned to this transaction, a  user-supplied string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verification              | A call to any verification  function that returns one of the following values: WLSuccess, WLMinorError, WLError, or WLSevereError. If the verification  function does not explicitly return a value, the default value is always WLSuccess.  Verification may also be  an expression, constant, or variable that evaluates to one of the preceding  return values. See VerificationFunction() (user-defined) (see[*VerificationFunction()*](#_bookmark434) [*(user-defined) (function)* ](#_bookmark434)), for more information. |
| [SaveFlag]                | An optional Boolean flag  specifying whether WebLOAD should save the results of*all transaction instances*, successes and failures, (true), for later analysis with  Data Drilling, or should save only results of *failed transaction instances* that triggered some sort of error  flag, (false, default).                                                                                                                                                                                                                                        |
| [FailureReason]           | An optional user-supplied string that  provides a reason for the failure.GUI mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**Note:** BeginTransaction() and EndTransaction() functions are usually accessed and inserted into script files directly through the WebLOAD Recorder. For example, the following figure illustrates a section in the Script Tree bracketed by BeginTransaction and EndTransaction nodes. The EndTransaction node is highlighted in the Script Tree.

To mark the end of a transaction, drag the **End Transaction** icon from the Load toolbox into the Script Tree, directly after the last action you want included in the script.

For additional information about the EndTransaction() function, refer to *Begin and End Transaction* in the *WebLOAD Recorder User’s Guide*.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## EnforceCharEncoding (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Indicates whether the parser should use the character set it parses in the HTML pages or override it using the CharEncoding property. The default value is **false** (use the encoding from the HTML pages).

The EnforceCharEncoding property can be set to one of the following values:

* **true** – Use the CharEncoding property.
* **false** (default) – Get the encoding from the HTML pages.

**Example** wlGlobals.EnforceCharEncoding = false **GUI mode**

In WebLOAD Console, check **Enforce Character Encoding** in the Browser Parameters

tab of the **Default Options** or **Current Session Options** dialog box, accessed from the

**Tools** tab of the ribbon.

In WebLOAD Recorder, check **Enforce Character Encoding** in the Browser Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* CharEncoding (see [*CharEncoding (property)* ](#_bookmark52))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## Erase (property)

**Property of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Indicates whether or not to clear the WebLOAD properties of a wlHttp object after each Get(), Post(), or Head() call. wlHttp.Erase is a read/write property. The default value is **true**. This section briefly discusses the implications of each setting.

wlHttp.Erase=true (default)

When Erase is set to true, WebLOAD automatically erases all wlHttp property values after each HTTP access. You must reassign any properties you need before the next HTTP access. For this reason, assign the properties of wlHttp only in the *main script*, not in InitClient(), so they will be reassigned in every round.

Thus if Erase is set to true the following script is incorrect. In this script, the wlHttp properties are assigned values in InitClient(). The script would connect to the Url and submit the FormData only in the first round. After the first Post() call, the Url and FormData property values are erased, so WebLOAD cannot use them in subsequent rounds.

```javascript
function InitClient() {  //Wrong!

wlHttp.Url = [“http://www.ABCDEF.com/products.exe](http://www.ABCDEF.com/products.exe)” wlHttp.FormData[“Name”] = “John Smith” wlHttp.FormData[“Product Interest”] = “Modems”

}

//Main script wlHttp.Post()

To solve the problem, assign the wlHttp property values in the **main script**, so that the

assignments are executed before each Get(), Post(), or Head() call:

//Main script     //OK

wlHttp.Url = [“http://www.ABCDEF.com/products.exe](http://www.ABCDEF.com/products.exe)” wlHttp.FormData[“Name”] = “John Smith” wlHttp.FormData[“Product Interest”] = “Modems” wlHttp.Post()

Alternatively, you could assign values to **wlLocals properties**, which are not erased:

function InitClient() {     //OK

wlLocals.Url = [“http://www.ABCDEF.com/products.exe](http://www.ABCDEF.com/products.exe)” wlLocals.FormData[“Name”] = “John Smith” wlLocals.FormData[“Product Interest”] = “Modems”

}

//Main script wlHttp.Post() **wlHttp.Erase=false
```

You may set Erase to false to prevent erasure. For example, if for some reason you absolutely had to assign values to the wlHttp properties in the InitClient() function of the script, change the value of the Erase property to false. If Erase is false, the properties retain their values through subsequent rounds.

Thus another way to correct the preceding example is to write:

```javascript
function InitClient() 

{            //OK 



wlHttp.Erase = false 

wlHttp.Url =[“http://www.ABCDEF.com/products.exe](http://www.ABCDEF.com/products.exe)” 

wlHttp.FormData[“Name”] = “John Smith” 

wlHttp.FormData[“Product Interest”] = “Modems”

}

//Main script wlHttp.Post()
```

User-defined properties are not linked to the wlHttp.Erase property and will not be

erased automatically by WebLOAD. The only way to reset or erase user-defined properties is for the user to set the new values explicitly.

**See also**

* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* DataCollection.type (see [*type (property)* ](#type-property))
* DataCollection.value (see [*value (property)* ](#value-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark290))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))

## ErrorMessage() (function)

**Description**

Use this function to display an error message in the Log Window and abort the current round.

    **Parameter Name**                  **Description**                            msg                  A string with an error      message to be sent to the WebLOAD Console.

**Syntax** ErrorMessage(msg) **Parameters**

**Comment**

If you call ErrorMessage() in the main script, WebLOAD stops the current round of execution. Execution continues with the next round, at the beginning of the main script.

You may also use the wlException object with the built-in try()/catch()

commands to catch errors within your script.

**GUI mode**

WebLOAD recommends adding message functions to your script files directly through the WebLOAD Recorder. Message function commands can be added to the script in Visual Editing mode using the Toolbox message item and the Insert menu command.

Message function command lines may also be added directly to the code in a JavaScript Object within a script through the IntelliSense Editor, described in [*Using the*](#_bookmark18) [*IntelliSense JavaScript Editor* ](#_bookmark18).

**See also**

* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException (see [*wlException (object)* ](#_bookmark446))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

## ErrorMessage (property)

**Property of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

ErrorMessage is used to define a global error message that appears in the Log window when a verification fail error occurs. When defined, ErrorMessage affects all the verifications in which an error message is not defined. If you define an error message for a specific verification, it overrides the global error message defined in the ErrorMessage property.

**Example**

To set the global error message displayed in the Log window in the event of any verification fail errors to my personalized error message, write:

wlVerification.ErrorMessage = “my personalized error message”

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* PageTime (see [*PageTime (property)* ](#_bookmark271))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* Title (see [*Title (function)* ](#_bookmark417))

## EvaluateScript() (function)

**Description**

Enables testers to include scripts and specify the point during script execution at which the script should be executed.

**Syntax**

EvaluateScript(“Script”, RunModeConstant)

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Script                   | A valid JavaScript syntax, including  function calls.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RunModeConstant          | One of the following list  of constants that acts as a flag when passed as a parameter to EvaluateScript(). Defines the point during  script execution at which WebLOAD should execute the script being included  here. Possible choices include:`<br>`WLAfterInitAgenda  `<br>`WLBeforeInitClient  `<br>`WLBeforeThreadActivation  `<br>`WLOnThreadActivation  `<br>`WLBeforeRound  `<br>`WLAfterRound  `<br>`WLAfterTerminateClient  `<br>`WLAfterTerminateAgenda |

**Comment**

If the script to be executed is in an external file, use the following:

IncludeFile(filename.js) EvaluateScript(“MyFunction()”,WLAfterRound) Where MyFunction() is defined in filename.js.

## event (property)

**Property of Objects**

* link (see [*link (object)* ](#_bookmark235))
* script (see [*script (object)* ](#_bookmark323))

**Description**

Represents the event that occurred to the parent object or the event for which the script is written.

## ExecuteConcurrent() (function)

**Description**

Use the ExecuteConcurrent()function to define the point after which all Post and Get HTTP requests, which have been collected since the DefineConcurrent() function was run, are executed. At this point, the collected HTTP requests are executed concurrently, by two or more threads. The number of threads is defined in the

WebLOAD Console in the multithreading number in the Browser Parameters tab of the Script Options dialog box.

**Note:** This function can only be inserted in your script *after* a DefineConcurrent() function. For more information about the DefineConcurrent() function, see [*DefineConcurrent() (function)* ](#defineconcurrent-function).

When the engine encounters the ExecuteConcurrent() function, it stops collecting the HTTP requests in the script and starts their execution.

**Example**

`DefineConcurrent()`

`…`

`<any valid JavaScript code, including Post and Get requests>`

`…`

`ExecuteConcurrent()`

**GUI mode**

**Note:** The ExecuteConcurrent()function is usually inserted into script files directly through the WebLOAD Recorder. Drag the **Execute Concurrent** icon, from the Load toolbox, into the Script Tree at the desired location.

For additional information about the ExecuteConcurrent() function, refer to

*Execute Concurrent* in the *WebLOAD Recorder User’s Guide*.

**See also**

* DefineConcurrent() (see [*D*](#_bookmark48)[*efineConcurrent() (function)* ](#_bookmark48))

## extractValue()(function)

**Description**

Use this function to extract a specific string contained within another string.

**Syntax**

retVarName = extractValue(prefix, suffix, str, instance)

**Parameters**

| **Parameter Name** | **Description**                                             |
| ------------------------ | ----------------------------------------------------------------- |
| retVarName               | A variable name that will be generated to  the agenda             |
| prefix                   | A string indicating the beginning of the  string to be extracted. |
| suffix                   | A string indicating the end of the string  to be extracted.       |

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| str                       | The string to be extracted is contained  within this string.                                                                                                                                                                                                                                                                                                |
| instance                  | When there is more than  one appearance of the prefix string following by the suffix string, this  optional parameter can be used to indicate the correct string to be returned.  The default value is 1.  For example, when instance  is 3, the third appearance of the  prefix string followed by the suffix string indicates the string to be  returned. |

**Return Value**

The extractValue function returns the extracted string.

**Example**

The following function extracts ‘x’ out of ‘axb’:

retStr = extractValue(“a”, “b”, “axb”)

Since no instance parameter is specified, WebLOAD automatically adds the default value of the instance parameter:

retStr = extractValue(“a”, “b”, “axb”,1)

The following function extracts ‘tttatt’ out of ‘zzzatttattbaxbzzzbzz’:

retStr = extractValue(“a”, “b”,“zzzatttattbaxbzzzbzz”,1)

The following function extracts ‘x’ out of ‘zzzatttattbaxbzzzbzz’:

retStr = extractValue(“a”, “b”,“zzzatttattbaxbzzzbzz”,2)

## FileName (property)

**Property of Object**

* wlHttp.DataFile (see [*DataFile (property)* ](#datafile-property))

**Description**

This property is a string that holds the name of the file being submitted through an HTTP Post command.

**Syntax**

wlHttp.DataFile.FileName = “DataFileName”

**See also**

* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark290))
* type (see [*type (property)* ](#type-property))
* value (see [*value (property)* ](#))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

## FilterURL (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The value of the FilterURL property is a list of filters separated by semi-colons. When retrieving a resource, the engine checks whether the value of any of these filters appear in the URL. If the value of any of the filters appears in the URL, the URL is not executed. Filtering is only performed during playback.

**Example**

For example, if FilterURL = “ynet;cnn.com”, the engine will filter URLs from ynet.com and ynet.co.il, as well as URLS from cnn.com.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## form (object)

**Property of Object**

form objects are grouped into collections of forms. The forms collection is a property of the following object:

* document (see [*document (object)* ](#document-object))

**Description**

Specifies that the contained controls are all elements of a form. Each form object stores the parsed data for a complete HTML form (`<FORM>` tag). A form object contains the complete set of elements and input controls (text, radio buttons, checkboxes, etc.) that are all components of a single form. (Compare to the element (see [*element (object)* ](#_bookmark102)) object, which stores the parsed data for a single HTML form element.)

form objects are local to a single thread. You cannot create new form objects using the JavaScript new operator, but you can access HTML forms through the properties and methods of the standard DOM objects. form properties are read-only.

form objects are grouped together within collections of forms, as described in Collections (see [*Collections* ](#using_javascript_ref.md#collections)). A forms collection contains all form links (HTML `<FORM>` elements) within the document.

**Syntax**

The forms collection includes a length property that reports the number of form objects within a document (read-only). To find out how many form objects are contained within a document, check the value of:

document.forms.length

Use an index number to access an individual form’s properties. Access each form’s properties directly using the following syntax:

`document.forms[*index*#].<*form-property*>`

You can also access a member of the forms collection by its HTML name attribute. For example, suppose that the first form on an HTML page is introduced by the tag:

`<FORM name=“SignUp”`

action=[“http://www.ABCDEF.com/FormProcessor.exe](http://www.ABCDEF.com/FormProcessor.exe)” method=“post”>

You can access this form by writing any of the following expressions:

`document.forms[0]`

`document.forms[“SignUp”]`

`document.forms.SignUp`

`document.SignUp`

**Properties**

* element (see [*element (object)* ](#_bookmark102))
* encoding (see [*encoding (property)* ](#_bookmark106))
* id (see [*id (property)* ](#_bookmark208))
* method (see [*method (property)* ](#_bookmark248))
* Name (see [*Name (property)* ](#_bookmark253))
* target (see [*target (property)* ](#_bookmark409))
* Url (see [*Url (property)* ](#_bookmark422))

**See also**

* [*Collections* ](#using_javascript_ref.md#collections)
* document (see [*document (object)* ](#_bookmark100))
* element (see [*element (object)* ](#_bookmark102))
* Image (see [*Image (object)* ](#_bookmark210))
* [*Select* ](#_bookmark329)

## FormData (property)

**Property of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

A collection containing form field values. WebLOAD submits the field values to the HTTP server when you call the Get(), Post(), or Head() method of the wlHttp object. FormData goes through HTTP encoding before being sent to the server in the same manner as content-type=application/x-www-form-urlencoded.

The collection indices are the field names (HTML name attributes). Before you call wlHttp.Post(), set the value of each element to the data that you want to submit in the HTML field. The fields can be any HTML controls, such as buttons, text areas, or hidden controls.

**Method**

Use the wlClear() (see [*wlClear() (method)* ](#_bookmark440)) method to delete specific FormData fields or clear all the FormData fields at once.

JavaScript supports two equivalent notations for named collection elements: FormData.FirstName or FormData[“FirstName”]. The latter notation also supports spaces in the name, for example, FormData[“First Name”].

##### Getting FormData using Get()

You can get form data using a Get() call. For example:

`wlHttp.FormData[“FirstName”] = “Bill”`

`wlHttp.FormData[“LastName”] = “Smith”`

`wlHttp.FormData[“EmailAddress”] = [“bsmith@ABCDEF.com](mailto:bsmith@ABCDEF.com)”`

`wlHttp.Get(“http://www.ABCDEF.com/submit.cgi”)`

WebLOAD appends the form data to the URL as a query statement, using the following syntax:

`http://www.ABCDEF.com/submit.cgi`

`?FirstName=Bill&LastName=Smith [&amp;Ema](mailto:&EmailAddress=bsmith@ABCDEF.com)[ilAddress=bsmith@ABCDEF.com](mailto:ilAddress=bsmith@ABCDEF.com)`

##### Submitting FormData using Post()

Suppose you are testing an HTML form that requires name and email address data. You need to submit the form to the submit.cgi program, which processes the data. You can code this in the following way:

```
wlHttp.FormData[“FirstName”] = “Bill” 

wlHttp.FormData[“LastName”] = “Smith”

 wlHttp.FormData[“EmailAddress”] = [“bsmith@ABCDEF.com](mailto:bsmith@ABCDEF.com)” 

wlHttp.Post(“http://www.ABCDEF.com/submit.cgi”)
```

The Post() call connects to submit.cgi and sends the FormData fields. In the above example, WebLOAD would post the following fields:

`FirstName=Bil`

 `LastName=Smith`

`[EmailAddress=bsmith@ABCDEF.com`](mailto:EmailAddress=bsmith@ABCDEF.com)

You may also submit FormData with missing fields or with data files.

**See also**

* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark290))
* type (see [*type (property)* ](#type-property))
* value (see [*value (property)* ](#value-property))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))

## frames (object)

**Property of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

The frames object retrieves a collection of all window objects defined by the given document or defined by the document associated with the given window. Each window object contains one of the child windows found in a browser window frameset. The frames collection stores the complete parse results for downloaded HTML frames, including nested child windows. Use the frames properties to retrieve information about any child windows to which the current window or document are linked.

frames collections are local to a single thread. WebLOAD creates an independent frames collection for each thread of a script. You cannot create new frames collections using the JavaScript new operator, but you can access HTML frames through the properties and methods of the standard DOM objects. frames properties are read-only.

**Syntax**

The frames collection includes a length property that reports the number of frame objects within a document (read-only). To find out how many window objects are contained within a document, check the value of:

`document.frames.length`

Use an index number to access an individual frame’s properties. Access each window’s properties directly using the following syntax:

`document.frames[#].<*child-property*>`

You can also access a member of the frames collection by its HTML name attribute. For example:

`document.frames[“namestring”]`

-Or-

document.frames.namestring

If the GetFrames property is false, the frames collection is empty.

**Example**

Access each window’s properties directly through an index number:

`document.frames[1].location`

Access the first child window using the following expression:

``frames[0]``

Access the first child window’s link objects directly using the following syntax:

`frames[0]`.`frames[0]`.links[#].`<*property*>`

For example:

``document.`frames[0]``.links[0].protocol`

**Properties**

* Index (see [*Index (property)* ](#index-property))
* Name (see [*Name (property)* ](#_bookmark253))
* title (see [*title (property)* ](#_bookmark415))
* Url (see [*Url (property)* ](#_bookmark422))

**See also**

* [*Collections* ](#using_javascript_ref.md#collections)
* GetFrames (see [*GetFrames (property)* ](#_bookmark153))

## Function (property)

**Property of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

Function is used to define a global JavaScript function called when a verification fail error occurs. When defined, Function affects all the verifications in which a JavaScript function is not defined. If you define a JavaScript function for a specific verification, it overrides the global JavaScript function defined in the Function property.

**Example**

To set the global JavaScript function called in the event of any verification fail errors to

`GetOperatingSystem(), write:`

`wlVerification.Function = GetOperatingSystem()`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* PageTime (see [*PageTime (property)* ](#_bookmark271))
* Severity (see [*Severity (property)* ](#_bookmark360))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## GeneratorName() (function)

**Description**

GeneratorName() provides a unique identification for the current Load Generator instance, even with multiple spawned processes running simultaneously. The identification string is composed of a combination of the current Load Generator name, computer name, and other internal markers.

**Syntax**

GeneratorName()

**Return Value**

Returns a unique identification string for the current Load Generator.

**GUI mode**

WebLOAD recommends accessing global system variables, including the GeneratorName() identification function through the WebLOAD Recorder. All the variables that appear in this list are available for use at all times in a script file. In the WebLOAD Recorder main window, click **Variables Windows** in the **Debug** tab of the ribbon**.**

For example, it is convenient to add GeneratorName() to a Message Node to clarify which Load Generator sent the messages that appear in the WebLOAD Console Log window.

**See also**

* GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](#_bookmark176))
* [*Identification Variables and Functions* ](#_bookmark28)
* RoundNum (see [*RoundNum (variable)* ](#_bookmark314))
* VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432))

## Get() (method)

### Get() (addition method)

**Method of Objects**

* wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450))
* wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491))

**Description**

Returns the current value of the specified shared variable.

**Syntax**

`Get(“SharedVarName”, ScopeFlag)`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SharedVarName            | The name of a shared variable whose value should  be returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ScopeFlag                | One of two flags, WLCurrentAgenda or WLAllAgendas, signifying the scope of  the shared variable.  When used as a method of the wlGeneratorGlobal object:`<br>`The WLCurrentAgenda scope flag signifies variable values that you wish  to share between all threads of a single script, part of a single process,  running on a single Load Generator.  `<br>`The WLAllAgendas scope flag signifies variable values that you wish to share between  all threads of one or more scripts, common to a single spawned process,  running on a single Load Generator.  When used as a method of the wlSystemGlobal object:  `<br>`The WLCurrentAgenda scope flag signifies  variable values that you wish to share between all threads of a single  script, potentially shared by multiple processes, running on multiple Load Generators, system wide.  `<br>`The WLAllAgendas scope flag signifies  variable values that you wish to share between all threads of all scripts,  run by all processes, on all Load  Generators, system-wide. |

**Return Value**

Returns the current value of the specified shared variable.

**Example**

CurrentCount = wlGeneratorGlobal.Get(“MySharedCounter”, WLCurrentAgenda)

CurrentCount = wlSystemGlobal.Get(“MyGlobalCounter”, WLCurrentAgenda)

**See also**

* Add() (see [*Add() (method)* ](#add-method))
* Set() (see [*Set() (addition method)* ](#set-addition-method))

### Get() (cookie method)

**Method of Objects**

* location (see [*location (object)* ](#_bookmark243))
* wlCookie (see [*wlCookie (object)* ](#wlcookie-object))

**Description**

Searches for the value of a specific cookie and returns it. If there is more than one cookie with the same name, the method returns the first occurrence.

**Syntax**

`wlCookie.Get(name[, domain][, path])`

**Parameters**

| **Parameter Name** | **Description**                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| name                     | A  descriptive name identifying the cookie, for example,  “CUSTOMER”.                         |
| domain                   | The top-level domain name of the cookie, for example,[“www.ABCDEF.com](http://www.ABCDEF.com/)”. |
| path                     | The top-level directory  path, within the specified domain, of the cookie, for example, “/”.  |

**Return Value**

Returns the value of the cookie found.

**Example**

`retValue = wlCookie.Get(“CUSTOMER”, “[www.ABCDEF.com](http://www.abcdef.com/)”, “/” )`

### Get() (transaction method)

**Method of Objects**

This function is implemented as a method of the following object:

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Get command. The method gets the FormData, Data, or DataFile properties in the Get command. In this way, you can get any type of data from an HTTP server.

**Syntax**

`Get([URL] [, TransName])`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [URL]                    | An optional parameter identifying the document  URL.  You may optionally specify  the URL as a parameter of the method. Get() connects to the first URL that has been specified  from the following list, in the order specified:`<br>`A Url parameter  specified in the method call.  `<br>`The Url property of  the wlHttp object.  `<br>`The local default wlLocals.Url.  `<br>`The global default wlGlobals.Url.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [TransName]              | An optional user-supplied  string with the transaction name as it will appear in the Statistics Report.  Use*named transactions* to identify specific HTTP transactions by  name. This simplifies assigning counters when you want WebLOAD to  automatically calculate a specific transaction’s occurrence, success, and  failure rates.  The run-time statistics  for transactions to which you have assigned a name appear in the Statistics  Report. For your convenience, WebLOAD offers an Automatic Transaction option.  In the WebLOAD Console, select Automatic Transaction from the General Tab of  the Global Options dialog box. Automatic Transaction is set to true by default. With Automatic Transaction,  WebLOAD automatically assigns a name to every Get and Post HTTP transaction.  This makes statistical analysis simpler, since all HTTP transaction activity  is measured, recorded, and reported for you automatically. You do not have to  remember to add naming instructions to each Get and Post command in your script. The name assigned by  WebLOAD is simply the URL used by that Get or Post transaction. If your  script includes multiple transactions to the same URL, the information will  be collected cumulatively for those transactions. |

**Example**

```javascript
function InitAgenda() {

//Set the default URL

wlGlobals.Url = [“http://www.ABCDEF.com](http://www.ABCDEF.com/)”

}

//Main script

//Connect to the default URL: wlHttp.Get()

//Connect to a different, explicitly set URL: [wlHttp.Get(“http://www.ABCDEF.com/product_info.html](http://www.ABCDEF.com/product_info.html)”)

//Assign a name to the following HTTP transaction: url= [http://www.ABCDEF.com/product_info.html](http://www.abcdef.com/product_info.html) wlHttp.Get(url,

“UpdateBankAccount”)

Use named transactions as a shortcut in place of the BeginTransaction()...EndTransaction() module. For example, this is one way to identify a logical transaction unit:

BeginTransaction(“UpdateBankAccount”) wlHttp.Get(url)

// the body of the transaction

// any valid JavaScript statements wlHttp.Post(url);

EndTransaction(“UpdateBankAccount”)

// and so on

Using the named transaction syntax, you could write:

wlHttp.Get(url,”UpdateBankAccount”)

// the body of the transaction

// any valid JavaScript statements wlHttp.Post(url,”UpdateBankAccount”)

// and so on

For the HTTPS protocol, include “https://” in the URL and set the required properties of the wlGlobals object:

[wlHttp.Get(“https://www.ABCDEF.com](http://www.ABCDEF.com/)”)
```

**Comment**

You may not use the TransName parameter by itself. Get() expects to receive either *no* parameters, in which case it uses the script’s default URL, or *one* parameter, which must be an alternate URL value, or *two* parameters, including both a URL value and the transaction name to be assigned to this transaction.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Delete() (see [*Delete() (HTTP method)*](#_bookmark94)) 
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Head() (see [*Head() (method)* ](#_bookmark194))
* Header (see [*Header (property)* ](#header-property))
* Options() (see [*Options() (method)* ](#_bookmark266))
* Post() (see [*Post() (method)* ](#_bookmark289))
* Put() (see [*Put() (method)* ](#_bookmark298)onpage [213](#_bookmark298))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## GetApplets (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of Java Applets in an HTML page. The default value of GetApplets is **true**.

**Note:** This property can only be inserted manually.

**Example**

`wlGlobals.GetApplets = true`

 **See also**

* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetCss (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of cascading style sheets in an HTML page. The default value of GetCss is **true**.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.GetCss = true

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137)*on* page [107](#_bookmark137))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145)*on* page [113](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153)*on* page [117](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetElementById() (function)

**Description**

Used to retrieve the element with the specified identification value by querying the DOM of the HTML from the last response.

**Syntax**

`GetElementById(“id”)`

| **Parameter Name** | **Description**                                                              |
| ------------------------ | ---------------------------------------------------------------------------------- |
| id                       | The identification value  of the element to retrieve, enclosed in quotation marks. |

**Return Value**

The first element with the requested identification value or Null if no element was found.

**See also**

* GetElementByName() (see [*GetElementByName() (function)* ](#_bookmark141))
* GetElementsById() (see [*GetElementsById() (function)* ](#_bookmark140))

## GetElementsById() (function)

**Description**

Used to retrieve an array of all elements with the specified identification value by querying the DOM of the HTML from the last response.

> **Note:** An element can be from the `document.forms[].elements[], document.links[] or document.images[]` collections.

**Syntax**

GetElementsById(“id”)

**Return Value**

A list of the requested elements.

**Example**

```javascript
wlHttp.Get("www.abc.com](http://www.abc.com/)")

var elementArr = GetElementsById("id4"); for (var i in elementArr ) {

var elm = elementArr[i];

InfoMessage( "ID:" + elm.id + ", Name:" + elm.name + ", Type:" + elm.type + ", Value:" + elm.value );

}
```

The expected output is:

4.11    ID:id4, Name:event, Type:hidden, Value:search

4.23    ID:id4, Name:process, Type:hidden, Value:login

**See also**

* GetElementsByName() (see [*GetElementsByName() (function)* ](#_bookmark142))
* GetElementById() (see [*GetElementById() (function)* ](#_bookmark139))

## GetElementByName() (function)

**Description**

Used to retrieve the element with the specified name by querying the DOM of the HTML from the last response.

> **Note:** An element can be from the document.forms[].elements[], document.links[] or document.images[] collections.

**Syntax**

`GetElementByName(“name”)`

**Return Value**

The first element with the requested name or Null if no element was found.

**See also**

* GetElementsByName() (see [*GetElementsByName() (function)* ](#_bookmark142))
* GetElementById() (see [*GetElementById() (function)* ](#_bookmark139))

## GetElementsByName() (function)

**Description**

Used to retrieve an array of all elements with the specified name by querying the DOM of the HTML from the last response.

> **Note:** An element can be from the document.forms[].elements[], document.links[] or document.images[] collections.

**Syntax**

`GetElementsByName(“name”)`

| **Parameter Name** | **Description**                                               |
| ------------------------ | ------------------------------------------------------------------- |
| name                     | The name of the elements to retrieve, enclosed in  quotation marks. |

**Return Value**

A list of the requested elements.

**Example**

```javascript
[wlHttp.Get("http://www.webloadmpstore.com/login.php")](http://www.webloadmpstore.com/login.php) var elementArr = GetElementsByName("event");

for (var i in elementArr ) { var elm = elementArr[i];

InfoMessage( "Name:" + elm.name + ", ID:" + elm.id + ", Type:" + elm.type + ", Value:" + elm.value );

}
```

The expected output is:

4.11    Name:event, ID:, Type:hidden, Value:search

4.23    Name:event, ID:, Type:hidden, Value:login

**See also**

* GetElementByName() (see [*GetElementByName() (function)* ](#_bookmark141))
* GetElementsById() (see [*GetElementsById() (function)* ](#_bookmark140))

## GetElementValueById() (function)

**Description**

Used to retrieve the value of the element with the specified identification value by querying the DOM of the HTML from the last response.

> **Note:** An element can be from the document.forms[].elements[], document.links[] or document.images[] collections.

**Syntax**

`GetElementValueById(“id”)`

**Return Value**

The value of the first element with the requested identification value or Null if no element was found.

**Example** GetElementValueById(“sessionid”) **See also**

* GetElementValueByName() (see [*GetElementValueByName() (function)* ](#_bookmark144))

## GetElementValueByName() (function)

**Description**

Used to retrieve the value of the element with the specified name by querying the DOM of the HTML from the last response.

> **Note:** An element can be from the document.forms[].elements[], document.links[] or document.images[] collections.

**Syntax**

`GetElementValueByName(“name”)`

**Return Value**

The value of the first element with the requested name or Null if no element was found.

**Example**

```javascript
wlHttp.Get("http://www.webloadmpstore.com/login.php")](http://www.webloadmpstore.com/login.php) var elementArr = GetElementValueByName("event");

for (var i in elementArr ) { var elm = elementArr[i];

InfoMessage( "Name:" + elm.name + ", ID:" + elm.id + ", Type:" + elm.type + ", Value:" + elm.value );

}
```

**See also**

* GetElementValueById() (see [*GetElementValueById() (function)* ](#_bookmark143))

## GetEmbeds (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of embedded objects in an HTML page. The default value of GetEmbeds is **true**.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.GetEmbeds = true

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetFieldValue() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the HTML value attribute (initial value) of a form field, given its name attribute.

**Syntax**

GetFieldValue(FieldName [, frame])

**Parameters**

| **Parameter Name** | **Description**                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| FieldName                | The name of the field whose value is to be  retrieved.                                       |
| [frame]                  | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested value of the specified field.

**Example**

`ClientFirstName = wlHtml.GetFieldValue(“FirstName”)`

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method only searches within the specified frame and all its nested frames.

## GetFieldValueInForm() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the HTML value attribute (initial value) of a form field, given its name attribute. This method is similar to GetFieldValue(), but the search is limited to a specific form within a specific frame.

**Syntax**

`GetFieldValueInForm(FormIndex, FieldName [, frame])`

**Parameters**

| **Parameter  Name** | **Description**                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| FormIndex                 | Index number that  identifies the specific form to which the search is to be limited.        |
| FieldName                 | The name of the field whose value is to be  retrieved.                                       |
| [frame]                   | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested HTML value attribute of the form field.

**Example**

If an HTML page includes two frames with a form in the second frame.

`wlHtml.GetFieldValueInForm(0, “FirstName”, Frame1)`

searches the first form in Frame1 and returns “Bill”.

**Comment**

The method does not search within nested frames. Omit the optional frame parameter if the HTML page does not contain frames.

## GetFormAction() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve a form object, representing a `<FORM>` element. The action attribute specifies the URL where the form data is to be submitted.

**Syntax**

`GetFormAction(FormIndex [, frame])`

**Parameters**

| **Parameter Name** | **Description**                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| FormIndex                | Index number that  identifies the specific form to which the search is to be limited.        |
| [frame]                  | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested form object.

**Example**

If an HTML page includes two frames with a form in the second frame

`wlHtml.GetFormAction(0, Frame1)`

returns a form object for the form.

**Comment**

The method does not search within nested frames. Omit the optional frame parameter if the HTML page does not contain frames.

## GetFrameByUrl() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve a frame object given its URL.

**Syntax**

`GetFrameByUrl(UrlPattern [, frame])`

**Parameters**

| **Parameter  Name** | **Description**                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| UrlPattern                | The URL for the frame requested.                                                             |
| [frame]                   | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested frame.

**Example**

```javascript
//Retrieve Frame0

Frame0 = wlHtml.GetFrame[ByUrl(“http://MyCompany/Frame0.html](http://MyCompany/Frame0.html)”)

//Retrieve Frame0.1

Frame0_1 = wlHtml.GetFrameByUrl([“http://MyCompany/Frame0B.html](http://MyCompany/Frame0B.html)”)

You may use * as a wildcard character in the URL. The method returns the first frame matching the search pattern. For example:

// To match URL [(http://MyCompany/Frame0B.html)](http://MyCompany/Frame0B.html)) Frame0_1 = wlHtml.GetFrameByUrl(“*B.htm*”)

You may narrow the search to frames nested within a specific parent frame by

specifying the optional frame parameter. For example:

//Search within Frame0 and retrieve Frame0.0

Frame0_0 = wlHtml.GetFrameByUrl(“*/MyCompany/*”,Frame0)
```

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

Comment out `GetFrames=false` when you use the GetFrameByUrl method.

## GetFrames (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of Frames and IFrames in an HTML page. The default value of GetFrames is **true**.

**Note:** This property can only be inserted manually.   Although the default value for GetFrames is true, during recording, the following is automatically inserted in the script: wlGlobals.`GetFrames=false`;

**Example**

wlGlobals.GetFrames = true

**Comments**

When GetMetas is true, GetFrames should also be true as the redirection is retrieved as a frame (see [*GetMetas (property)* ](#_bookmark174)).

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetFrameUrl() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve a location object representing the URL of an HTML page. Optionally, specify a nested frame.

**Syntax**

`GetFrameUrl([frame])`

**Comment**

Comment out `GetFrames=false` when you use the GetFrameByUrl method.

**Return Value**

The requested location object.

**Comment**

This method is equivalent to the location property of a frame object (see [*frames (object)](#frames-object)

).

## GetHeaderValue() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the value of an HTTP header field.

**Syntax**

GetHeaderValue(HeaderName [, frame])

**Parameters**

| **Parameter  Name** | **Description**                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| HeaderName                | The name of the header whose value is to be  retrieved.                                      |
| [frame]                   | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested HTTP header field value.

`wlHtml.GetHeaderValue(“Host”) returns “Server2.MyCompany.com”.`

-Or-

`document.wlHeaders[“host”] document.frame[0].wlHeaders[“host”]`

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetHost() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the host of a URL, including the port number.

**Syntax**

GetHost([frame])

**Parameters**

| **Parameter Name** | **Description**                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| [frame]                  | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested host information.

**Example**

For the following HTTP Header example:

`HTTP/1.1 200 OK`

`Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT`

`Content-type: text/html Connection: close`

`Host: Server2.MyCompany.com:80 wlHtml.GetHost()`

`returns “Server2.MyCompany.com:80”.`

-Or-

`document.wlHeaders[“hostname”] document.frame[0].wlHeaders[“hostname”]`

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetHostName() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the host name of a URL, not including the port number.

**Syntax**

`GetHostName([frame])`

**Return Value**

The requested host name.

`wlHtml.GetHostName()`

`returns “Server2.MyCompany.com”.`

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetImages (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of images in an HTML page. The default value of GetImages is true.

When GetImages is false, the load engine does not retrieve the images from an HTML page.

> **Note:** This property can only be inserted manually.

**Example**

`wlGlobals.GetImages = true`

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetImagesInThinClient (property)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

When set to true, the “Thin” client will retrieve images. The default value of GetImagesInThinClient is **false**.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.GetImagesInThinClient = true

**See also**

* SetClientType (see [*SetClientType (function)* ](#_bookmark352))
* [*Collections* ](#using_javascript_ref.md#collections)
* document (see [*document (object)* ](#_bookmark100))
* Header (see [*Header (property)* ](#header-property))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))

## GetIPAddress() (method)

**Method of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Returns the identity of the *current* IP address.

**Syntax**

`GetIPAddress()`

**Return Value**

Returns a string with the IP address for the current Virtual Client.

**Example**

...

`wlHttp.MultiIPSupport = true CurrentIPAddress = wlHttp.GetIPAddress() wlHttp.Get()`

...

**Comment**

Requesting the identity of the *current* IP address is only meaningful if your script is handling more than one IP address. GetIPAddress() therefore can only return a value if MultiIPSupport=true. If MultiIPSupport is turned off this method will return “Undefined”.

The scope of MultiIPSupport depends, of course, on whether it was set through wlGlobals, wlLocals, or wlHttp. For example, if your script sets wlGlobals.MultiIPSupport, then GetIPAddress() returns a value at any point in the script. If you set only wlHttp.MultiIPSupport, then GetIPAddress()returns a value only if called before the next immediate HTTP transaction.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## GetLine() (function)

**Description**

The GetLine() function reads and parses data from an ASCII file. The function reads the file one line at a time in the following way:

* If you opened the file using the default sequential mode (see [*Open() (function)* ](#_bookmark262)), then:
* The first GetLine() call in any thread of a Load Generator reads the first line of the file.
* Each successive call in any thread of any process of the Load Generator (across the master and slave processes of a single Load Generator/script combination) reads the next line of the file.
* When the last line of the file has been read, the next access loops back to the first line of the file.
* If you opened the file for random access (see [*Open() (function)* ](#_bookmark262)), each successive call in any thread of any process of the Load Generator (across the master and slave processes of a single Load Generator/script combination) reads some randomly selected line of the file. To read the input file lines in random order, you must include Open(filename, WLRandom) in the script’s InitAgenda() function.

In this way, a relatively small file can supply an unending stream of test data, and different clients are supplied with different sequences of data.

> **Note:** The last line of the file should not include a carriage return.

**Syntax**

GetLine(filename[, delimiter])

**Parameters**

| **Parameter  Name** | **Description**                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| filename                  | A string with the name of  the file being read. May optionally include the full directory path.              |
| [delimiter]               | Optional character separating fields in one  line of the input file. Default delimiter character is a comma. |

**Return Value**

The GetLine function returns an array containing both the full lines and the individual tokens. The array (called LineArray in this example) includes the following elements:

* LineArray[0]-the complete line. For example: “John,Smith, [jsmith@ABC.com](mailto:jsmith@ABC.com)”
* LineArray[1]-the first token. In this example:“John”
* LineArray[2]-the second token. In this example:“Smith”
* LineArray[3]-the third token. In this example:[“jsmith@ABC.com](mailto:jsmith@ABC.com)”
* LineArray.RoundNum-number of rounds through the file (including the current round). For example: 4
* LineArray.LineNum-the number of the line that was just read. For example: 1

**Example**

To read and parse the next line of the mydata.txt ASCII input file, in this case including a directory path:

`LineArray = GetLine(“c:\\temp\\mydata.txt”)`

To specify a different delimiter:

`LineArray = GetLine(“c:\\temp\\mydata.txt”, “:”)`

**Comment**

JavaScript requires that you double the backslash in strings. If your directory path includes the backslash character, remember to double the backslashes, as in the preceding example.

If the line found in the file contains no separator characters, then the entire line is considered to be a single token. In that case, the function returns a two-element array (LineArray[0] and LineArray[1]), each containing the entire line.

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile (see [*wlOutputFile() (constructor)* ](#_bookmark477))
* wlOutputFile() (see [*wlOutputFile (object)* ](#_bookmark474))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## GetLine() (method)

**Method of Object**

* wlInputFile (see [*wlInputFile (object)* ](#_bookmark467))

**Description**

The GetLine() function reads and parses data from an ASCII file. The function reads the file one line at a time in the following way:

* If you opened the file using the default WLFileSequential access method (see [*Open() (method)* ](#open-method)), then:
* The first GetLine() call in any thread of a Load Generator reads the first line of the file.
* Each successive call in any thread of any process of any Load Generator reads the next line of the file.
* When the last line of the file has been read, the next access loops back to the first line of the file.
* If you opened the file using the WLFileSequentialUnique access method (see[ *Open() (method)* ](#open-method)), then the procedure is basically as when using the WLFileSequential access mode, except that the if the value/row is being used by another VC, it is not retrieved, but skipped.
* If you opened the file using the WLFileRandom access method (see [*Open() (method)*](#open-method) ), GetLine() reads a random value/row from the file, where there might be multiple access to the same line by different Load Generator machines.
* If you opened the file using the WLFileRandomUnique access method (see [*Open()*](#open-method)[ *(method)* ](#open-method)), GetLine() reads a unique, unused value/row randomly from the file.

> **Note:** The last line of the file should not include a carriage return.

**Syntax**

`strInputFileLine = myFileObj.getLine(*delimiter*)`

**Parameters**

| **Parameter  Name** | **Description**                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| delimiter                 | Optional character separating fields in one  line of the input file. Default delimiter character is a comma. |

**Return Value**

The GetLine function returns an array containing both the full lines and the individual tokens. The array (called strInputFileLine in this example) includes the following elements:

* strInputFileLine [0]-the complete line. For example:“John,Smith, [jsmith@ABC.com](mailto:jsmith@ABC.com)”
* strInputFileLine [1]-the first token. In this example:“John”
* strInputFileLine [2]-the second token. In this example:“Smith”
* strInputFileLine [3]-the third token. In this example:[“jsmith@ABC.com](mailto:jsmith@ABC.com)”
* strInputFileLine.LineNum-the number of the line that was just read. For example: 1

**Example**

To read and parse the next line of the ASCII input file specified in myFileObj:

`strInputFileLine = GetLine(“,”)`

**Comment**

If the line found in the file contains no separator characters, then the entire line is considered to be a single token. In that case, the function returns a two-element array (strInputFileLine[0] and strInputFileLine[1]), each containing the entire line.

**See also**

* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlInputFile (see [*wlInputFile() (constructor)* ](#wlinputfile-constructor))

## GetLinkByName() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve a location object representing a link, given the hypertext display.

**Syntax**

`GetLinkByName(Hypertext [, frame])`

**Parameters**

| **Parameter  Name** | **Description**                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| Hypertext                 | The hypertext displayed in the desired  link.                                                |
| [frame]                   | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested location object.

**Example**

Suppose the HTML on a page contains:

`<A [href=“http://MyCompany/link1.html](http://MyCompany/link1.html)”>Product information </A>`

In this example,

`wlHtml.GetLinkByName(“Product information”)`

returns a location object for [http://MyCompany/link1.html.](http://MyCompany/link1.html)

The search is case sensitive. You may use the * wildcard character in the Hypertext string. For example, wlHtml.GetLinkByName(“*roduct info*”) also returns an object for [http://MyCompany/link1.html.](http://MyCompany/link1.html)

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetLinkByUrl() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve a location object representing a link, given part of the URL string.

**Syntax**

`GetLinkByUrl(UrlPattern [, frame])`

**Parameters**

| **Parameter  Name** | **Description**                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| UrlPattern                | The URL of the desired link. Use the *  wildcard character to represent the missing parts.   |
| [frame]                   | An optional frame  specification, used to limit the scope of the search to a specific frame. |

**Return Value**

The requested location object.

**Example**

Suppose the HTML on a page contains:

`<A [href=“http://MyCompany/link1.html](http://MyCompany/link1.html)”>`Product information `</A>`

In this example,

`wlHtml.GetLinkByUrl(“*link1.htm*”)`

returns a location object for [http://MyCompany/link1.html.](http://MyCompany/link1.html)

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetMessage() (method)

**Method of Object**

* wlException (see [*wlException (object)* ](#wlexception-object))

**Description**

Returns the message string text stored in this object.

**Syntax**

`*wlExceptionObject*.GetMessage()`

**Return Value**

Text string of the error message for this object.

**Example**

`MeaningfulErrorMessage = myExceptionObject.GetMessage()`

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException (see [*wlException (object)* ](#_bookmark446))

## GetMetas (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

The GetMetas property, when set to true, enables the support of redirection for non-recorded scripts, for websites using the HTML META tag (for example, www.ynet.co.il).

> **Note:** Since scripts that were recorded automatically include the redirected URL, the GetMetas property should be used only in scripts that were written manually and that contain a URL with meta direction.

**Example**

`wlGlobals.GetMetas = false`

**Comments**

* Because the redirection is retrieved as a frame, the GetFrames property must be set to true (see [*GetFrames (property)* ](#_bookmark153)).
* The additional wlHttp.GET will not be part of the script (it will be like frame 0).
* The desired page will be requested only on playback.
* The page will not be visible in WebLOAD Recorder’s Browser View. This is because redirection will not be performed (the document will not be replaced). WebLOAD implements the redirected URL by adding a frame to the parent HTML. That is, the first page will be added with an extra frame containing the redirection URL (fully parsed and all the objects in it will be get).

## GetOperatingSystem() (function)

**Description**

Returns a string identifying the operating system running on the current Load Generator.

**Syntax**

GetOperatingSystem()

**Return Value**

Returns the name of the operating system running on the current Load Generator in

the format of the operating system name followed by some version identification.

For example, if the Load Generator is working with a Solaris platform, this function would return the string ‘Solaris’ followed by the version name and release number, such as SunOS2.

If the Load Generator is working with a Linux platform, this function would return the string ‘Linux’ followed by the version name and release number, such as RedHat1.

If the Load Generator is working with a Windows platform, possible return values include:

* Windows 95
* Windows 98
* Windows NT/2000 (*ServicePack#*)
* Windows XP
* Windows (for any other Windows version)

**See also**

* GeneratorName() (see [*GeneratorName() (function)* ](#generatorname-function))
* [*Identification Variables and Functions* ](#_bookmark28)
* RoundNum (see [*RoundNum (variable)* ](#_bookmark314))
* VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432))

## GetOthers (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of objects not covered by the other Get methods in an HTML page. The default value of GetOthers is **true**.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.GetOthers = true

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetPortNum() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the port number of the current URL.

**Syntax**

GetPortNum([frame]) ****

**Return Value**

The requested number.

**Example**

For the following HTTP Header example:

`HTTP/1.1 200 OK`

`Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT`

`Content-type: text/html Connection: close`

`Host: Server2.MyCompany.com:80`

wlHtml.GetPortNum() would return a value such as 80.

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetQSFieldValue() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the value of a search attribute in a URL. The search attributes are the fields following the ? symbol, appended to the end of a URL.

**Syntax**

`GetQSFieldValue(Url, FieldName)`

**Parameters**

| **Parameter  Name** | **Description**                                  |
| ------------------------- | ------------------------------------------------------ |
| Url                       | The complete URL string to be parsed and  searched.    |
| FieldName                 | The name of the field whose value is to be  retrieved. |

**Return Value**

The requested value.

**Example**

The following search string:

`wlHtml.GetQSFieldValue([“http://www.ABCDEF.com/query.exe](http://www.ABCDEF.com/query.exe)” + “?SearchFor=icebergs&SearchType=ExactTerm”,”SearchFor”)`

returns “icebergs”.

## GetScripts (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of external JavaScript scripts in an HTML page. The default value of GetScripts is **true**.

> **Note:** This property can only be inserted manually.

**Example**

`wlGlobals.GetScripts = true`

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetXml() (see [*GetXml() (property)* ](#_bookmark191))

## GetSeverity() (method)

**Method of Object**

* wlException (see [*wlException (object)* ](#_bookmark446))

**Description**

Returns the severity level value stored in this object.

**Syntax**

*wlExceptionObject*.GetSeverity()

**Return Value**

Integer, representing one of the following error level values:

* WLError-this specific transaction failed and the current test round was aborted. The script displays an error message in the Log window and begins a new round.
* WLSevereError-this specific transaction failed and the test session must be stopped completely. The script displays an error message in the Log window and the Load Generator on which the error occurred is stopped.

**Example**

`SeverityLevel = myExceptionObject.GetSeverity()`

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

## GetStatusLine() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the status string from the HTTP header.

**Syntax**

`GetStatusLine([frame])`

| **Parameter  Name** | **Description**                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| [frame]                   | An optional frame  specification, used to retrieve the status string of a specific frame. |

**Return Value**

The requested status string.

**Example**

For the following HTTP Header example:

`HTTP/1.1 200 OK`

`Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT`

`Content-type: text/html Connection: close`

`Host: Server2.MyCompany.com:80`

wlHtml.GetStatusLine() would return “OK”.

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetStatusNumber() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the status code from the HTTP header.

**Syntax**

`GetStatusNumber([frame])`

**Parameters**

| **Parameter Name** | **Description**                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------- |
| [frame]                  | An optional frame  specification, used to retrieve the status code of a specific frame. |

**Return Value**

The requested status number.

**Example**

For the following HTTP Header example:

`HTTP/1.1 200 OK`

`Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT`

`Content-type: text/html Connection: close`

`Host: Server2.MyCompany.com:80`

wlHtml.GetStatusNumber() would return 200.

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetUri() (method)

**Method of Object**

* wlHtml (see [*wlHtml (object)* ](#_bookmark464))

**Description**

Retrieve the URI part of a URL. The URI is the portion of the address following the host name.

**Syntax**

`GetUri([frame])`

| **Parameter Name** | **Description**                                                           |
| ------------------------ | ------------------------------------------------------------------------------- |
| [frame]                  | An optional frame specification, used to retrieve  the URI of a specific frame. |

**Return Value**

The requested URI string.

**Example**

For the following HTTP Header example:

`HTTP/1.1 200 OK`

`Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT`

`Content-type: text/html Connection: close`

`Host: Server2.MyCompany.com:80`

wlHtml.GetUri() would return “WebPage.html”.

**Comment**

By default, the method searches in all frames of the parse tree and returns the first match. You may narrow the search by specifying an optional frame parameter. In that case, the method searches within the specified frame and all its nested frames.

If you are specifying a frame, comment out `GetFrames=false`.

## GetXML (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables the retrieval of external XML in an HTML page. The default value of GetXML is **true**.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.GetXML = true

**See also**

* GetApplets() (see [*GetApplets (property)* ](#_bookmark137))
* GetCss() (see [*GetCss (property)* ](#_bookmark138))
* GetEmbeds() (see [*GetEmbeds (property)* ](#_bookmark145))
* GetFrames() (see [*GetFrames (property)* ](#_bookmark153))
* GetImages() (see [*GetImages (property)* ](#_bookmark162))
* GetOthers() (see [*GetOthers (property)* ](#_bookmark177))
* GetScripts() (see [*GetScripts (property)* ](#getscripts-property))

## hash (property)

**Property of Object**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The HTML anchor portion of the URL, not including the # initial symbol (read-only string).

**Example**

Given the following HTML fragment:

`<A href="https://www.ABCDEF.com:80/products/order.html#modems">`

`[&lt;A ](“https://www.ABCDEF.com:80/products/order.html#modems”)[href=“http://www.ABCDEF.com/search.exe?](http://www.ABCDEF.com/search.exe)`

`SearchFor=modems&SearchType=ExactTerm”>`

links[0].hash is “modems”.

## Head() (method)

**Method of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Head command.

**Syntax**

Head()

**Comment**

This method operates in the same way as Get(), but it retrieves only the HTTP or

HTTPS header from the server. It does not download the body of the URL, such as a Web page.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Post() (see [*Post() (method)* ](#_bookmark289))
* [wlGlobals](#wlglobals-object)
* [wlLocals](#wllocals-object)

## Header (property)

**Property of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

A collection of HTTP header fields that you want to send in a Get(), Post(), or Head() call.

**Example**

By default, WebLOAD sends the following header in any HTTP command:

`host: <host>`

`user-agent: Radview/HttpLoader 1.0 accept: */`*

Here, `<host>` is the host name to which you are connecting, for example:

`www.ABCDEF.com:81.`

You may reset these properties, for example, as follows:

`wlHttp.UserAgent = “Mozilla/4.03 [en] (WinNT; I)”`

Alternatively, you can use the Header property to override one of the default header fields. For example, you can redefine the following header field:

`wlHttp.Header[“user-agent”] = “Mozilla/4.03 [en] (WinNT; I)”`

**GUI mode**

WebLOAD offers a simple way to reset configuration properties using the various tabs of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon. Resetting configuration properties as you run and rerun various testing scenarios enables you to fine tune your tests to match your exact needs at that moment. For example, you can reset the user-agent value through the Browser Parameters tab.

**Comment**

Use the wlClear() (see [*wlClear() (method)* ](#_bookmark440)) method to delete specific Header fields or clear all the Header fields at once.

You cannot override the host header or set a cookie header using the Header property. To set a cookie, see wlCookie (see [*wlCookie (object)* ](#wlcookie-object))

Use the wlHttp.Header property to change or reset specific individual values immediately before executing the next wlHttp GET/POST request.

Any information set using the wlHttp.Header property *takes priority* over any defaults set through the GUI (recommended) or using the wlGlobals, wlLocals, or wlHttp properties. If there is any discrepancy between the document header information and the HTTP values, WebLOAD will work with the information found in the wlHttp.Header property while also issuing a warning to the user.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Post() (see [*Post() (method)* ](#_bookmark290))
* type (see [*type (property)* ](#type-property))
* UserAgent (see [*UserAgent (property)* ](#useragent-property))
* value (see [*value (property)* ](#value-property))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))
* [wlGlobals](#wlglobals-object)
* [wlLocals](#wllocals-object)

## host (property)

**Property of Object**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The host portion of the URL, including both the host name and the port (read-only string).

**Example**

Given the following HTML fragment:

`<A href="https://www.ABCDEF.com:80/products/order.html#modems">`

`[&lt;A ](“https://www.ABCDEF.com:80/products/order.html#modems”)[href=“http://www.ABCDEF.com/search.exe?](http://www.ABCDEF.com/search.exe)`

`SearchFor=modems&SearchType=ExactTerm”>`

links[0].host is “www.ABCDEF.com:80”

## hostname (property)

**Property of Object**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The host name portion of the URL (read-only string).

**Example**

Given the following HTML fragment:

`<A href="https://www.ABCDEF.com:80/products/order.html#modems">`

`[&lt;A ](“https://www.ABCDEF.com:80/products/order.html#modems”)[href=“http://www.ABCDEF.com/search.exe?](http://www.ABCDEF.com/search.exe)`

`SearchFor=modems&SearchType=ExactTerm”>`

links[0].hostname is [“www.ABCDEF.com](http://www.ABCDEF.com/)”

## href (property)

**Property of Object**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The complete URL of the link (read-only string).

**Example**

Given the following HTML fragment:

`<A href="https://www.ABCDEF.com:80/products/order.html#modems">`

`[&lt;A ](“https://www.ABCDEF.com:80/products/order.html#modems”)[href=“http://www.ABCDEF.com/search.exe?](http://www.ABCDEF.com/search.exe)`

`SearchFor=modems&SearchType=ExactTerm”>`

links[0].href is

[“https://www.ABCDEF.com/products/order.html#modems](http://www.ABCDEF.com/products/order.html#modems)”

**Comment**

The href property contains the entire URL. The other link properties contain portions of the URL. links[#].href is the default property for the link object. For example, if

`[links[0\]=‘http://microsoft.com](http://microsoft.com/)’`

then the following two URL specifications are equivalent:

`mylink=links[0].href`

and

mylink=links[0]

## HttpCacheScope (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Defines when the Http cache will be cleared. Possible values are:

* **None** – Defines that all Virtual Clients simulate a browser with no available cache.
* **SingleCommand** – Defines that cache be cleared after each request.
* **SingleCommandIfModified** – Defines that WebLOAD will check for a newer version of the cached item with every request. Whenever the engine has a request for a cached resource, the engine sends the request with an “if-modified-since” header. If the server responds with a 200 status, the engine will refresh the cache.
* **SingleRound** – Defines that cache be cleared after each script execution round. This is the default value for the HttpCacheScope property.
* **WholeRun** – Defines that the cache will never be cleared. Each client maintains its own cache.
* **WholeRunIfModified** – Defines that WebLOAD will check for a newer version of the cached item after each round. Whenever the engine has a request for a cached resource, the engine sends the request with an “if-modified-since” header. If the server responds with a 200 status, the engine will refresh the cache.

**Example**

`wlGlobals.HttpCacheScope = “SingleCommand”`

**GUI mode**

In the WebLOAD Recorder, select one of the cache scope options in the Browser Cache tab of the **Default/Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

>     **Note:** The default value for the cache scope is **SingleRound**.

**See also**

* HttpCacheCachedTypes (see [*HttpCacheCachedTypes (property)* ](#_bookmark203))

## HttpCacheCachedTypes (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Specifies the type of content to include in the HTTP cache: None, HTML, JS, CSS, XML, Applet, Image, Dynamic (a URL with a query string). The default value is **JS**, **CSS**, **XML**, **Applet**, **Image**.

**Example**

`wlGlobals.HttpCacheCachedTypes = “Image,CSS”`

**GUI mode**

For wlGlobals.HttpCacheCachedTypes, you can also set the Cache Content Filter from WebLOAD Recorder or Console.

In WebLOAD Recorder, in the **Browser Cache** tab of the **Default** or **Current Options** dialog box, select either the **Default** or **User Filter** in the Cache Content Filter area. If you select **User Filter**, check the relevant filters.

In WebLOAD Console, in the **Browser Cache** tab of the **Default** or **Current Options** dialog box or the **Script Options** dialog box, select either the **Default** or **User Filter** in the Cache Content Filter area. If you select **User Filter**, check the relevant filters.

**See also**

* HttpCacheScope (see [*HttpCacheScope (property)* ](#httpcachescope-property))

## httpEquiv (property)

**Property of Object

* wlMetas (see [*w*](#_bookmark471)[*lMetas (object)* ](#_bookmark471))

**Description**

Retrieves the value of the HTTP-EQUIV attribute of the META tag (read-only string).

**Syntax** wlMetas[*index#*].httpEquiv **Example** document.wlMetas[0].httpEquiv **See also**

* content (see [*content (property)* ](#_bookmark68))
* Name (see [*Name (property)* ](#_bookmark253))
* Url (see [*Url (property)* ](#_bookmark422))

## HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Identifies the proxy server that the script uses for HTTP SSL access when UseSameProxyforSSL is set to false. The user name and password are for SSL proxy servers that require user authorization. These properties are used when you are working with a separate SSL proxy.

>     **Note:** This property can only be inserted manually.

**Syntax**

`wlGlobals.*httpsProxyProperty* = “TextString”`

**Example**

> wlGlobals.httpsProxy = “proxy.ABCDEF.com:8080”
>
> wlGlobals.httpsProxyUserName = “Bill”
>
> wlGlobals.httpsProxyPassWord = “Classified”

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*
* Proxy, ProxyUserName, ProxyPassWord (see [*Proxy, ProxyUserName,*](#proxyntusername-proxyntpassword-properties)
* ProxyNTUserName, ProxyNTPassWord (see [*ProxyNTUserName, ProxyNTPassWord*](#proxyntusername-proxyntpassword-properties)
* HttpsProxyNTUserName, HttpsProxyNTPassWord (see [*HttpsProxyNTUserName, HttpsProxyNTPassWord (properties)*](#proxyntusername-proxyntpassword-properties))
* UseSameProxyForSSL (see [*UseSameProxyForSSL (property)* ](#_bookmark427))

## HttpsProxyNTUserName, HttpsProxyNTPassWord (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Provides user authorization to the proxy server that the script uses for HTTP SSL access on Windows servers when UseSameProxyforSSL is set to false.

**Syntax**

`wlGlobals.*httpsProxyNTProperty* = “TextString”`

**Example**

`wlGlobals.httpsProxyNTUserName = “Bill”`

`wlGlobals.httpsProxyNTPassWord = “Classified”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*
* HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord (see [*HttpsProxy,*](#httpsproxy-httpsproxyusername-httpsproxypassword-properties))
* Proxy, ProxyUserName, ProxyPassWord (see [*Proxy, ProxyUserName,*](#proxy-proxyusername-proxypassword-properties))
* ProxyNTUserName, ProxyNTPassWord (see [*ProxyNTUserName, ProxyNTPassWord*](#proxyntusername-proxyntpassword-properties))
* UseSameProxyForSSL (see [*UseSameProxyForSSL (property)* ](#_bookmark427))

## id (property)

**Property of Objects**

* element (see [*element (object)* ](#_bookmark102))
* form (see [*form (object)* ](##form-object))
* frames (see [*frames (object)* ](#frames-object))
* Image (see [*Image (object)* ](#_bookmark210))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* script (see [*script (object)* ](#_bookmark323))
* [*Select* ](#_bookmark329)
* wlTables (see [*wlTables (object)* ](#_bookmark493))
* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

Retrieves the string identifying the parent object. The ID value is taken from the ID attribute within the tag. This property is optional. If this object does not have an ID attribute then the value is undefined.

When working with element, forms, frames, image, or map objects, returns a string containing an alternative identification means for the complete image, map, forms or frame or for elements of type Button, CheckBox, File, Image, Password, Radio, Reset, Select, Submit, Text, and TextArea.

**Example**

##### wlTables example:

If the first table on a page is assigned the ID tag myTable, access the table using any of the following:

`document.wlTables[0]`

-Or-

`document.wlTables.myTable`

-Or-

document.wlTables[myTable]

If duplicate identifiers are found, the id property will refer to the first wlTables object found with that identifier.

##### wlXmls example:

If the first XML object on a page is assigned the ID tag myXmlDoc, access the object using any of the following:

`MyBookstore = document.wlXmls[0]`

-Or-

MyBookstore = document.wlXmls.myXmlDoc

-Or-

`MyBookstore = document.wlXmls[“myXmlDoc”]`

If duplicate identifiers are found, the id property will refer to the first XML object found with that identifier.

**See also**

* cell
* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#cols-property)
*
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* load() (see [*load() (method)* ](#load-method))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* src (see [*src (property)* ](#src-property))
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* *Working with HTTP Protocol* in the *WebLOAD Scripting Guide*
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property)))

## Image (object)

**Property of Objects**

Image objects on a Web page are accessed through the document.all collection of the standard DOM structure.

**Description**

Each Image object represents one of the images or video clips embedded in a document (HTML `<IMG>` element). Image objects are accessed through Images [*Collections* ](#using_javascript_ref.md#collections). (Compare to the element (see [*element (object)* ](#element-object)) object, which stores the parsed data for a single HTML form element, where the element may be any one of a variety of types, and the form (see [*form (object)* ](#form-object)) object, which stores the parsed data for an entire HTML form.)

image objects are grouped together within collections of images, accessed directly through the document object (document.images[#]).

**Syntax**

To find out how many image objects are contained within a document, check the value of:

document.images.length

Access each image’s properties directly using the following syntax:

`document.images[*index*#].<*image-property*>`

**Example**

`document.images[1].src`

**Properties**

* id (see [*id (property)* ](#id-property))
* InnerLink (see [*InnerLink (property)* ](#innerlink-property))
* Name (see [*Name (property)* ](#name-property))
* OuterLink (see [*OuterLink (property)* ](#outerlink-property))
* protocol (see [*protocol (property)* ](#protocol-property))
* src (see [*src (property)* ](#src-property))
* Url (see [*Url (property)* ](#url-property))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* form (see [*form (object)* ](##form-object))
* [*Select* ](#_bookmark329)

## IncludeFile() (function)

**Description**

Instructs WebLOAD to include the specified file, and optionally execute scripts that are stored within that file, as part of the initialization process before beginning the main script execution rounds. Encourages modular programming by enabling easy access to sets of library function files.

**Syntax**

`IncludeFile(filename[, WLExecuteScript])`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename                 | A string or variable  containing the full literal name of the file to be included. WebLOAD assumes  that the file is located in the default directory specified in the File  Locations tab (User Include Files entry) in the**Tools** ****  **Global Options** dialog box in the WebLOAD  Console or in the **Tools** **** **Settings** dialog box in the WebLOAD Recorder. For additional information about  the included file’s location, refer to *Determining  the Included File Location* in the *WebLOAD  Scripting Guide*. Once the file is found, any functions or variables  defined within that file are compiled and included within the calling script  when the script is compiled. |
| WLExecuteScript          | WLExecuteScript  is a global  constant that acts as a flag when passed as a parameter to IncludeFile(). WLExecuteScript is an optional parameter. When included, WebLOAD  will not only compile the definitions found in the specified file. WebLOAD  will also execute any additional commands or functions found within that file  outside the included function definitions. With WLExecuteScript  , WebLOAD  enables work with self- initializing include files that can define, set, and  execute the commands necessary to initialize a work environment at compile  time.                                                                                                                                                              |

**Example**

To include the external file MyFunction.js, located on the WebLOAD Console during WebLOAD testing, use the following command:

```javascript
function InitAgenda() 

{ 

IncludeFile(“MyFunction.js”)

}
```

**Comment**

The IncludeFile command must be inserted in the InitAgenda() section of your JavaScript program.

The load engine first looks for the file to be included in the default User Include Files directory. If the file is not there, the file request is handed over to WebLOAD, which searches for the file using the following search path order:

1. If a full path name has been hardcoded into the IncludeFile command, the system searches the specified location. If the file is not found in an explicitly coded directory, the system returns an error code of File Not Found and will not search in any other locations.

> **Note:** It is not recommended to hardcode a full path name, since the script will then not be portable between different systems. This is especially important for networks that use both UNIX and Windows systems.

2. Assuming no hardcoded full path name in the script code, the system looks for the file in the current working directory, the directory from which WebLOAD was originally executed.
3. Finally, if the file is still not found, the system searches for the file sequentially through all the directories listed in the File Locations tab.

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))
* wlOutputFile() (see [*wlOutputFile (object)* ](#_bookmark475))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## Index (property)

**Property of Objects**

* frames (see [*frames (object)* ](#frames-object))

**Description**

Sets or retrieves the index number of the parent object. For example, the ordinal position of an option in a list box.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)

## InfoMessage() (function)

**Description**

Displays a generally informative (but not necessarily problematic) message in the Log Window.

**Syntax**

InfoMessage(msg)

**Parameters**

**Comment**

If you call InfoMessage() in the main script, WebLOAD sends an informative message to the Log window and continues with script execution as usual. The message has no impact on the continued execution of the WebLOAD test.

**GUI mode**

WebLOAD recommends adding message functions to your script files directly through the WebLOAD Recorder. Message function command lines may also be added directly to the code in a JavaScript Object within a script through the IntelliSense Editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18).

**See also**

* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException (see [*wlException (object)* ](#_bookmark446))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

## InnerHTML (property)

**Property of Objects**

* cell (see [*cell (object)* ](#_bookmark49))
* script (see [*script (object)* ](#_bookmark323))
* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

Sets or retrieves the HTML found between the start and end tags of the object.

**Syntax**

When working with cell objects, use the uppercase form:

`…cells[2].InnerHTML`

When working with script or wlXmls objects, use the lowercase form:

…scripts[2].innerHTML

**Comment**

The InnerHTML property for cell objects is written in uppercase.

**See also**

* cell
* cellIndex (see [*cellIndex (property)* ](#_bookmark50)) (cell  property)
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)
*


* 

* InnerImage (see [*InnerImage (property)* ](#innerimage-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* src (see [*src (property)* ](#src-property))
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

## InnerImage (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

Sets or retrieves the image found between the `<Start>` and `<End>` tags of the object. When working with a button object, the image that appears on the button. When working with a link or location object, the image that appears over the link. When working with a TableCell object, the image that appears over a table cell.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))

## InnerLink (property)

**Property of Objects**

* Image (see [*Image (object)* ](#_bookmark210))

**Description**

Represents the inner link field for the parent image object.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* form (see [*form (object)* ](##form-object))
* [*Select* ](#_bookmark329)

## InnerText (property)

**Property of Object**

* cell (see [*cell (object)* ](#_bookmark49))
* element (see [*element (object)* ](#_bookmark102))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

Sets or retrieves *only the text* found between the `<Start>` and `<End>` tags of the object. When working with a Button element object, the text that appears on the button.

When working with a link or location object, the text that appears over the link. When working with a TableCell object, the text that appears over a table cell.

**See also**

* cell
* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)
*


* 
* element (see [*element (object)* ](#_bookmark102))
* id (see [*id (property)* ](#_bookmark208)) (wlTables and wlXmls property)
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell and wlXmls property)
* InnerImage (see [*InnerImage (property)* ](#innerimage-property))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## JVMType (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The JVMType property indicates the JVM to be used in the Load Generator. The value of this property is defined using the WebLOAD Console or WebLOAD Recorder and overrides the JVM definition in webload.ini.

The value (string) of this property is the key for WLJVMs.xml. This file (located on every WebLOAD Machine in the `<WebLOAD Installation Directory>`\extensions\JVMs directory) contains the following parameters for each JVM:

* Type (the value from the flag)
* Path (should be machine-agnostic)
* Options

When Type is "Default", the RadView default (installed) JVM will be used. The default JVM’s path is defined in webload.ini, as it depends on the WebLOAD installation path.

> **Note:** The classpath definitions are defined in webload.ini.

**GUI mode**

In WebLOAD Console, select a JVM from the **Select run-time JVM to be used** drop- down list in the Java Options tab of the **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, select a JVM from the **Select run-time JVM to be used** drop- down list in the Java Options tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

## KDCServer (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)

**Description**

Specifies the address of the Key Distribution Center (KDC) server if you are using the Kerberos authentication method.

>     **Note:** The KDCServer property is only relevant for playback.

**Syntax**

`KDCServer(ServerName)`

**Parameters**

| **Parameter Name** | **Description**                                                            |
| ------------------------ | -------------------------------------------------------------------------------- |
| ServerName               | The name of the KDC server if you are using the  Kerberos authentication method. |

**Example**

wlGlobals.KDCServer = “qa4”

**GUI mode**

To specify the name of the KDC server if you are using the Kerberos authentication method:

* In WebLOAD Console, select the Kerberos radio button and enter the address of the KDC server in the Kerberos Server field in the Authentication tab of the **Default**, **Current Session**, or **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.
* In WebLOAD Recorder, select the Kerberos radio button and enter the address of the KDC server in the Kerberos Server field in the Authentication tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

Only the server name should be specified in KDCServer. For example, specify “qa4” rather than “qa4.radview.co.il”.

**See also**

* AuthType (see [*AuthType (property)* ](#_bookmark46))

## KeepAlive (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enable WebLOAD to keep an HTTP connection alive between successive accesses in the same round of the main script. The possible values are:

* **false** – Do not keep an HTTP connection alive.
* **true** – Keep the connection alive if the server permits. (default)

Keeping a connection alive saves time between accesses. WebLOAD attempts to keep the connection alive unless you switch to a different server. However, some HTTP servers may refuse to keep a connection alive.

Use the wlHttp.CloseConnection() method to explicitly close a connection that you have kept alive. Otherwise, the connection is automatically closed at the end of each round.

**Comment**

You should not keep a connection alive if establishing the connection is part of the performance test.

**GUI mode**

WebLOAD recommends maintaining or closing connections through the WebLOAD Console. Enable maintaining connections for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* CloseConnection() (see [*CloseConnection() (method)* ](#closeconnection-method))
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*
* *Working with HTTP Protocol* in the *WebLOAD Scripting Guide*

## KeepRedirectionHeaders (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

Used to indicate whether to get the location headers of all redirections. The default value of KeepRedirectionHeaders is false.

**Example**

wlGlobals.KeepRedirectionHeaders = true

**Comment**

This property is useful for the following scenario, which occurs in correlation. During a

redirection, in the middle of one of the URLs, there is a parameter in the Location header that is needed for the next Get. Since only the headers of the last Get in a series of redirections are stored in document.wlHeaders, the KeepRedirectionHeaders property, when set to true, enables all the headers in a series of redirections to be saved. The value can be extracted from document.wlHeaders after the navigation is complete.

**See also**

* SaveHeaders (see [*SaveHeaders (property)* ](#_bookmark319))

## key (property)

**Property of Objects**

* Header (see [*Header (property)* ](#header-property))
* wlHeaders (see [*wlHeaders (object)* ](#_bookmark462))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))

**Description**

The search key name (read-only).

**Syntax**

##### For wlHeaders:

document.wlHeaders[*index#*].key = “TextString”

##### For wlSearchPairs:

document.links[1].wlSearchPairs[*index#*].key = “TextString”

##### For wlHttp.Header:

wlHttp.Header[“key”] = “TextString”

**Example**

##### For wlHeaders:

document.wlHeaders[0].key = “Server”

##### For wlSearchPairs:

document.links[1].wlSearchPairs[0].key = “Server”

##### For wlHttp.Header:

wlHttp.Header[“key”] = “Server”

**See also**

* value (see [*value (property)* ](#value-property))

## language (property)

**Property of Object**

* script (see [*script (object)* ](#_bookmark323))

**Description**

Retrieves the language in which the current script is written.

**Example**

“javascript” specifies that the script is written in JavaScript. “vbscript” specifies that the script is written in Visual Basic Script.

## link (object)

**Property of Objects**

Links on a Web page are accessed through link objects that are grouped into collections of links. The links collection is a property of the document object.

**Description**

A link object contains information on an external document to which the current document is linked. Each link object points to one of the URL links (HTML `<A>` elements) within the document. Each link object stores the parsed data for the HTML link (`<A>` element).

link objects are local to a single thread. You cannot create new link objects using the JavaScript new operator, but you can access HTML links through the properties and methods of the standard DOM objects. link properties are read-only.

link objects are organized into Collections (see [*Collections* ](using_javascript_ref.md#collections)) of links or anchors. To access an individual link’s properties, check the length property of the links collection and use an index number to access the individual links.

**Syntax**

To find out how many link objects are contained within a document, check the value of:

document.links.length

Access each link’s properties directly using the following syntax:

document.links[#].`<*link-property*>`

**Example**

`document.links[1].protocol`

**Properties**

* hash (see [*hash (property)* ](#_bookmark192))
* host (see [*host (property)* ](#_bookmark197))
* hostname (see [*hostname (property)* ](#_bookmark197))
* href see [*href (property)* ](#href-property)
* id (see [*id (property)* ](#_bookmark208))
* InnerImage (see [*InnerImage (property)* ](#innerimage-property))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* Name (see [*Name (property)* ](#_bookmark253))
* pathname (see [*pathname (property)* ](#_bookmark286))
* port (see [*port (property)* ](#_bookmark286))
* protocol (see [*protocol (property)* ](#_bookmark294))
* search (see [*search (property)* ](#_bookmark326))
* target (see [*target (property)* ](#_bookmark409))
* title (see [*title (property)* ](#_bookmark415))
* Url (see [*Url (property)* ](#_bookmark422))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* document (see [*document (object)* ](#_bookmark100))

## load() (method)

**Method of Objects**

XML DOM objects on a Web page are accessed through collections of wlXmls objects. The load() function is a method of the following object:

* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

Call load(URL) to download XML documents from a website and automatically load these documents into XML DOM objects.

Do not include any external references when using load().

load() relies on the MSXML parser to performs any HTTP transactions needed to download the XML document. The MSXML module accesses external servers and completes all necessary transactions without any control or even knowledge on the part of the WebLOAD system tester. From WebLOAD’s perspective, these transactions are never performed in the context of the test session. For this reason, any settings that the user enters through the WebLOAD script or Console will not be relayed to the MSXML module and will have no effect on the document ‘load’. For the same reason, the results of any transactions completed this way will not be included in the WebLOAD statistics reports.

**Syntax**

`load(URLString)`

**Parameters**

| **Parameter Name** | **Description**                                                           |
| ------------------------ | ------------------------------------------------------------------------------- |
| URLString                | String parameter with the URL or filename where  the XML document may be found. |

**Example**

`myXMLDoc = document.wlXmls[0] myXMLdoc.load([“http://server/xmls/file.xml](http://server/xmls/file.xml)”)`

**Comment**

You may use load() repeatedly to load and reload XML data into XML DOM objects. Remember that each new ‘load’ into an XML DOM object will overwrite any earlier data stored in that object.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

## load() and loadXML() Method Comparison

**Description**

WebLOAD supports both the load() and the loadXML() methods to provide the user with maximum flexibility. The following table summarizes the advantages and disadvantages of each method:

|                     | **Advantages**                                                                                               | **Disadvantages**                                                                                                                                                                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **loadXML()** | Parameters that the user has defined through  WebLOAD for the testing session will be applied to this transaction. | The method fails if the  DTD section of the XML document string includes any external references.                                                                                                                                                                                                                        |
| **load()**    | The user may load XML files that include  external references in the DTD section.                                  | Parameters that the user  has defined through WebLOAD for the testing session will not be applied to  this transaction.  WebLOAD does not record the HTTP Get operation.  The transaction results  are not included in the session statistics report.  Using this method may  adversely affect the test session results. |

**Comment**

If you wish to measure the time it took to load the XML document using the load() method, create a timer whose results will appear in the WebLOAD statistics. For example:

`myXMLDoc = document.wlXmls[0]`

`SetTimer(“GetXMLTime”)`

`myXMLdoc.load([“http://server/xmls/file.xml](http://server/xmls/file.xml)”)`

`SendTimer(“GetXMLTime”)`

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* wlXmls (see [*wlXmls (object)* ](#_bookmark502))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

## LoadGeneratorThreads (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Optionally, WebLOAD can allocate extra threads to download nested images and frames.

For clients that you define in a Load Generator, this option is controlled by the LoadGeneratorThreads property. The default value of this property is **Single**, which means that Virtual Clients will not use extra threads to download data from the Server.

For the Probing Client, the option is controlled by the ProbingClientThreads property. The default is **Multiple**, which means that the client can use three extra threads for nested downloads. This simulates the behavior of Web browsers, which often use extra threads to download nested images and frames.

The possible values of these properties are:

* **Single** – Do not use extra threads to download nested images and frames. (default for LoadGeneratorThreads)
* **Multiple** – Allocate three extra threads per client (for a total of four threads per client) to download nested images and frames (default for ProbingClientThreads).
* Any specific number of threads between 1 and 8, such as “5” – Allocate that exact number of extra threads per client to download nested images and frames.

**Example**

You can assign any of these properties independently within a single script. In that case, if you configure a Probing Client to run the script, WebLOAD uses the value of ProbingClientThreads and ignores LoadGeneratorThreads (vice versa if you configure a Load Generator to run the script). For example, you might write:

```javascript
function InitAgenda() {

//Do not use extra threads if a

// Probing Client runs the script

wlGlobals.ProbingClientThreads = “Single”

//Use extra threads if a

// Load Generator runs the script wlGlobals.LoadGeneratorThreads = “Multiple”

}
```

**Comment**

The extra threads have no effect on the ClientNum value of the client. The ClientNum variable reports only the main thread number of each client, not the extra threads.

**GUI mode**

WebLOAD recommends enabling or disabling multi-threaded virtual clients through the WebLOAD Console. Enable multi-threading for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default** or **Current Session Options** dialog box and setting the number of threads you prefer.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* ProbingClientThreads (see [*ProbingClientThreads (property)* ](#_bookmark291))
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*

## loadXML() (method)

**Method of Object**

XML DOM objects on a Web page are accessed through collections of wlXmls objects. The loadXML() function is a method of the following objects:

* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

Call loadXML(XMLDocString) to load XML documents into XML DOM objects. This allows users to work with XML documents and data that did not originate in HTML Data Islands, such as with Native Browsing. In a typical scenario, a user downloads an XML document. WebLOAD saves the document contents in string form. The string is then used as the parameter for loadXML(). The information is loaded automatically into an XML object.

> **Note:** Creating a new, blank XML DOM object with WLXmlDocument() and then loading it with a parsed XML string using loadXML() is essentially equivalent to creating a new XML DOM object and loading it immediately using WLXmlDocument(xmlStr). As with the WLXmlDocument(xmlStr) constructor, only standalone, self-contained DTD strings may be used for the loadXML() parameter. External references in the DTD section are not allowed.

**Syntax** loadXML(XMLDocStr) **Parameters**

**Example**

`//create a new XML document object NewXMLObj = new WLXmlDocument() wlHttp.SaveSource = true`

`[wlHttp.Get(“http://www.server.com/xmls/doc.xml](http://www.server.com/xmls/doc.xml)”) XMLDocStr = document.wlSource`

`//load the new object with XML data`

`//from the saved source. We are assuming`

`//no external references, as explained above NewXMLObj.loadXML(XMLDocStr)`

**Comment**

You may use loadXML() repeatedly to load and reload XML data into XML DOM objects. Remember that each new ‘load’ into an XML DOM object will overwrite any earlier data stored in that object.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

## location (object)

**Property of Objects**

* document (see [*document (object)* ](#_bookmark100))

**Description**

A location object stores the parsed URL and location data of the frame or root window. For an overview of parsing, see *Parsing Web pages* in the *WebLOAD Scripting Guide*.

location objects are local to a single thread. You cannot create new location objects using the JavaScript new operator, but you can access HTML locations through the properties and methods of the standard DOM objects. The properties of location are read-only.

**Syntax**

Access the location’s properties directly using the following syntax:

document.location.`<*location-property*>`

 **Properties**

> **Note:** The properties of location are identical to those of link. The only exception is that location has no target property. Also, the location object is not part of any collection. The location properties are listed below for reference.

* hash (see [*hash (property)* ](#_bookmark192))
* host (see [*host (property)* ](#_bookmark197))
* hostname (see [*hostname (property)* ](#_bookmark197))
* href (see [*href (property)* ](#href-property)
* id (see [*id (property)* ](#_bookmark208))
* InnerText (see [*InnerText (property)* ](#_bookmark223))
* Name (see [*Name (property)* ](#_bookmark253))
* pathname (see [*pathname (property)* ](#_bookmark286))
* port (see [*port (property)* ](#_bookmark286))
* protocol (see [*protocol (property)* ](#_bookmark294))
* search (see [*search (property)* ](#_bookmark326))
* title (see [*title (property)* ](#_bookmark415))
* Url (see [*Url (property)* ](#_bookmark422))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))

**Comment**

The href property contains the entire URL. The other location properties contain portions of the URL. location.href is the default property for the location object.

For example, if

`[location=‘http://microsoft.com](http://microsoft.com/)’`

then the following two URL specifications are equivalent:

mylocation=location.href

-Or-

`mylocation=location`

**See also**

* link (see [*link (object)* ](#_bookmark235))

## MaxLength (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))

**Description**

The maximum number of characters the user can enter into a Text or Password element.

## MaxPageTime (function)

**Description**

Verifies the PageTime of the service response. If the PageTime (time to download the page) exceeds the specified maximum value, the verification fails.

**Syntax**

wlVerification.MaxPageTime(timeLimit, severity)

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timeLimit                | The maximum amount of time to download the  page in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| severity                 | Possible values of this parameter are:`<br>`WLSuccess. The transaction  terminated successfully.  `<br>`WLMinorError. This specific  transaction failed, but the test session may continue as usual. The script  displays a warning message in the Log window and continues execution from the  next statement.  `<br>`WLError. This specific  transaction failed and the current test  round was aborted. The script displays an error message in the Log window and  begins a new round.  `<br>`WLSevereError. This specific  transaction failed and the test  session must be stopped completely. The script displays an error message in  the Log window and the Load Generator on  which the  error occurred is stopped. |

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## method (property)

**Property of Object**

* form (see [*form (object)* ](##form-object))

**Description**

Specifies the method that the browser should use to send the form data to the server (read-only string). A value of “Get” will append the arguments to the action URL and open it as if it were an anchor. A value of “Post” will send the data through an HTTP Post transaction. The default is “Post”.

## MultiIPSupport (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

WebLOAD enables use of all available IP addresses. This allows testers to simulate clients with different IP addresses using only one Load Generator. You must first generate additional IP addresses on your machine to use when testing and then set the MultiIPSupport property to true to enable multiple IP support. For more information about generating additional IP addresses, see *Generating IP Addresses in the script* in the *WebLOAD Scripting Guide*.

> **Note:** Setting the MultiIPSupport property to true without generating additional IP addresses on your machine will not enable multiple IP support.

The possible values of wlGlobals.MultiIPSupport are:

* **false** – Use only one IP address. (default)
* **true** – Use all available IP addresses.

When connecting Load Generators through a modem, MultiIPSupport should be set to false.

Probing Clients use only one IP address. Load Generators are set by default to use only one IP address, but may be set to use multiple IP addresses through the MultiIPSupport property.

**GUI mode**

In WebLOAD Console, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

When the Load Generator has more than one IP address (one or more addresses on a network interface card or one or more network interface cards) WebLOAD uses ALL of the available IP addresses. Before setting MultiIPSupport to true, make sure that all of the Applications Being Tested to which the script refers are accessible through all the network interface cards.

Use the GetIPAddress() (see [*GetIPAddress() (method)* ](#_bookmark163)) method to check the identity of the current IP address.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* GetIPAddress() (see [*GetIPAddress() (method)* ](#_bookmark163))
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*
* MultiIPSupportType() (see [*MultiIPSupportType (property)* ](#_bookmark251))

## MultiIPSupportType (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The MultiIPSupportType property works with the wlGlobals.MultiIPSupport

property, and supports the following values:

* **PerClient** (default) – Preserves the current behavior. This means that there are different IPs per client but the same IP is used for all rounds.
* **PerRound** – Supports the use of a different IP from the pool per client, per round, until the pool is exhausted, after which it returns to the beginning.

This property is only referenced when wlGlobals.MultiIPSupport is true.

> **Note:** To support multiple IP addresses, you must generate additional IP addresses on your machine and then set the MultiIPSupport property to true. For more information about generating additional IP addresses, see *Generating IP Addresses in the script* in the *WebLOAD Scripting Guide*.

**GUI mode**

In WebLOAD Console, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

When the Load Generator has more than one IP address (one or more addresses on a network interface card or one or more network interface cards), WebLOAD uses ALL of the available IP addresses. Before setting MultiIPSupport to true, make sure that all of the Systems under Test (SUT) to which the script refers are accessible through all the network interface cards.

Use GetIPAddress() (see [*GetIPAddress() (method)* ](#_bookmark163)) to check the identity of the current IP address.

**See also**

* [*H*TTP Components* ](./using_javascript_ref.md#http_components)
* GetIPAddress() see [*GetIPAddress() (method)* ](#_bookmark163)
* MultiIPSupport() see [*MultiIPSupport (property)* ](#multiipsupport-property)
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*

## MultiIPSupportProtocol (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The MultiIPSupportProtocol property works with the wlGlobals.MultiIPSupport

property, and supports the following values:

* **All** (default) – Support both the IPv4 and IPv6 protocols.
* **IPv4Only** – Support only the IPv4 IP protocol.
* **IPv6Only** – Support only the IPv6 IP protocol.

This property is only referenced when wlGlobals.MultiIPSupport is true.

**GUI mode**

In WebLOAD Console, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Recorder, check or uncheck **Multi IP Support** in the HTTP Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* GetIPAddress() (see [*GetIPAddress() (method)* ](#_bookmark163))
* MultiIPSupport() (see [*MultiIPSupport (property)* ](#multiipsupport-property))
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*

## Name (property)

**Property of Objects**

* element (see [*element (object)* ](#_bookmark102))
* form (see [*form (object)* ](##form-object))
* frames (see [*frames (object)* ](#frames-object))
* Image (see [*Image (object)* ](#_bookmark210))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* [*Select* ](#_bookmark329)
* wlMetas (see [*w*](#_bookmark471)[*lMetas (object)* ](#_bookmark471))

**Description**

Sets or retrieves the identification string of the parent object.

> **Note:** You can access a collection member either by its index number or by its HTML name attribute.

When working with a wlMetas collection, the Name property holds the value of the NAME attribute of the META tag.

When working with an elements collection, the Name property holds the HTML name attribute of the form element (read-only string). The is the identification string for elements of type Button, CheckBox, File, Image, Password, Radio, Reset, Select, Submit, Text, and TextArea. The name attribute is required. If a form element does not have a name, WebLOAD does not include it in the elements collection.

**Syntax**

Collection members may be accessed either through an index number or through a member name, if it exists. For example:

Access the first child window on a Web page using the following expression:

``frames[0]``

Access the first child window’s link objects directly using the following syntax:

``frames[0]`.`frames[0]`.links[#].<*property*>`

Alternatively, you may access a member of the frames collection by its HTML name attribute. For example:

`document.frames[“namestring”]`

-Or-

document.frames.namestring

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* content (see [*content (property)* ](#_bookmark68))
* httpEquiv (see [*httpEquiv (property)* ](#_bookmark204))
* Url (see [*Url (property)* ](#_bookmark422))

## NTUserName, NTPassWord (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The user name and password that the script uses for Windows NT Challenge response authentication (NT Challenge Response).

**Comments**

A user is only authenticated once during a round with a set of credentials. Each subsequent request will use these credentials regardless of what is contained in the script. If the value of these credentials are changed after authentication, they will only be used during the next round, not during the current round.

For example, if you are trying to send a request to a URL with a group of users (user1, user2, and user3), but user1 has already been authenticated, the login is always performed for user1 until the round is complete.

**GUI mode**

By default, WebLOAD senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console. Enter user authentication information through the Authentication tab of the **Default** or **Current Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also set NT user values using the wlGlobals properties. For example:

`wlGlobals.NTUserName = “Bill”`

`wlGlobals.NTPassWord = “Classified”`

**Comment**

WebLOAD automatically sends the user name and password when a wlHttp object connects to an HTTP site. If an HTTP server requests NT Challenge Response authentication and you have not assigned values to NTUserName and NTPassWord, WebLOAD submits the Windows NT user name and password under which the script is running.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Rules of Scope for Local and Global Variables* in the *WebLOAD Scripting Guide*
* *Working with HTTP Protocol* in the *WebLOAD Scripting Guide*

## Num() (method)

**Method of Object**

* wlRand (see [*wlRand (object)* ](#wlrand-object) 

**Description**

Return a random integer.

**Syntax**

wlRand.Num([seed])

**Return Value**

A random integer.

**Example**

wlRand.Num(12345)

**See also**

* Range() (see [*Range() (method)* ](#_bookmark300))
* Seed() (see [*Seed() (method)* ](#_bookmark326))
* Select() (see [*Select() (method)* ](#_bookmark329))

## onDataReceived (property)

**Property of Object**

* [wlHttp](#wlhttp-object)

**Description**

Define a callback function to be called every time more data is received for the request. This is useful for working with asynchronous requests (when wlHttp.Async=true) that need to be inspected before they are completed, for example in an HTTP streaming push scenario.

Use the callback function to handle the asynchronous request, for example – validate the response and make a further request.

The callback function argument is a *limited* ‘document’ object. The document object contains only the following properties:

* wlSource (see [*wlSource (property)* ](#_bookmark485))
* wlStatusNumber (see [*wlStatusNumber (property)* ](#_bookmark488))
* wlStatusLine (see [*wlStatusLine (property)* ](#_bookmark486))

> **Note:** The callback is expected to run in a timely manner, because it blocks the execution of other callback functions. Specifically, try to:

Avoid making synchronous HTTP requests – use asynchronous ones instead.

 Avoid using Sleep() inside a callback function – instead, use [*setTimeout() (function)* ](#_bookmark356)to execute code after a certain period of time.

> **Note:** The onDataRecived callback is called many times – each time more data is received. If you only need to inspect the complete response, use the [*onDocumentComplete (property)* ](#_bookmark259)callback instead.

**Example**

```javascript
wlHttp.Async = true;

wlHttp.onDataReceived = function(document) {

{

if (document.wlStatusNumber==200)

{

InfoMessage( “Got response so far: “ + document.wlSource );

}

}

wlHttp.Get(“http:///.... ”)
```

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* The *Using Asynchronous Requests* chapter in the *WebLOAD Scripting Guide*
* [*wlSource (property)* ](#_bookmark485)
* [*wlStatusNumber (property)* ](#_bookmark488)
* [*wlStatusLine (property)* ](#_bookmark486)
* [*Async (property)* ](#_bookmark47)
* [*onDocumentComplete (property)* ](#_bookmark259)

## onDocumentComplete (property)

**Property of Object**

* [wlHttp](#wlhttp-object)

**Description**

Define a callback function to be called after the request has been completed. Useful in asynchronous requests (when wlHttp.Async=true)

Use the callback function to handle the asynchronous request, for example – validate the response and make a further request.

The callback function argument is the ‘document’ object, containing the response data, headers, status, etc.

 **Note:** The callback is expected to run in a timely manner, because it blocks the execution of other callback functions. Specifically, try to:

Avoid making synchronous HTTP requests – use asynchronous ones instead.

 Avoid using Sleep() inside a callback function – instead, use [*setTimeout() (function)* ](#_bookmark356)to execute code after a certain period of time.

**Note:** The onDocumentComplete callback is called only once – when the request is fully completed. To handle partial responses, use the [*onDataReceived (property)* ](#_bookmark258)callback.

**Example**

```javascript
wlHttp.Async = true;

wlHttp.onDocumentComplete = function(document) {

InfoMessage(“Response “ + document.wlSource);

}

[wlHttp.Get(“http://get](http://get-asynch-data/)-asynch-data”);

//the script will continue to here immediately, not waiting for the request to complete. It will run the onDocumentComplete function when the request is finished.
```

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* The *Using Asynchronous Requests* chapter in the *WebLOAD Scripting Guide*
* [*document (object)* ](#_bookmark100)
* [*Async (property)* ](#_bookmark47)
* [*onDataReceived (property)* ](#_bookmark258)

## Open() (method)

**Method of Object**

* wlInputFile (see [*wlInputFile (object)* ](#_bookmark467))

**Description**

Opens the input file specified in the wlInputFile object. This should be done in the

InitClient section of your script.

**Syntax**

```javascript
function InitAgenda()

{

…

fileID = CopyFile(`<full path>`)

…

}

function InitClient()

{

…

MyFileObj = new wlInputFile(*fileID*)

MyFileObj.Open([AccessMethod], [ShareMethod], [UsageMethod],

[EndOfFileBehavior], [HeaderLines], [‘Delimiter’])

…

}
```

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AccessMethod             | An optional parameter that  defines the method for reading the next value/row from the file. All values  are enumerated numeric values. Possible values are:`<br>`WLFileSequential. Every client gets the  next value/row from the file, where there might be multiple access to the same line by different Load Generator  machines. This is the default value.  `<br>`WLFileSequentialUnique. Gets the next unique  value/row from the file. Preferably, the unique value is the next available  value in sequential order. If another VC is using this value/row, the VC is  not able to access this value/row and will get the next available value/row.  It is recommended to have more values/rows in the file than the number of  clients to avoid delays.  `<br>`WLFileRandom. Gets a random value/row  from the file. There might be multiple access to the same line by different  Load Generator machines.  `<br>`WLFileRandomUnique. Gets a unique, unused value/row randomly from the file. It is  recommended to have more values/rows in the file than the number of clients  to avoid  delays.                                                                                                         |
| ShareMethod              | An optional parameter indicating how the  file is shared among scripts. All values are enumerated numeric values.  Possible values are:`<br>`**WLFileNotShared**. The file can be read only by the current script, and each Load  Generator machine manages a copy of  the file for its VCs independently. If there are multiple Load Generator  processes on a single machine, then the processes share the file. This is the  default value.  `<br>`**WLFileLGShared**. The file can be read only by the  current script, and all Load Generators on any Load Generator machine  share the same copy of the file, which is synchronized between them.  `<br>`**WLFileAgendaShared**. The file can be shared by more than one script.  The unique identifier of the file is its path. The file can be shared by  different scripts, but a copy of the file is managed separately for each Load  Generator machine. If you are using the script–Shared share method, all the  scripts sharing the file should use the WLFileSequentialUnique access method.  `<br>`**WLFileAgendaLGShared**. A single file is shared among Load Generators and among scripts.                                 |
| UsageMethod              | An optional parameter that  defines when to release the value/row back to the ‘pool’ so that it can be  read again from the file. This parameter is only relevant for the  WLFileSequentialUnique and WLFileRandomUnique access methods. All values are  enumerated numeric values. Possible values are:`<br>`**WLFilePerRound**. The script reads a new  value/row from the file once every  round. The value/row is released at the end of the round. This is the default value.  `<br>`**WLFileOncePerClient**. The script reads a new value/row from the file  once at the beginning of the test (in InitClient). The value/row is released  at TerminateClient.  `<br>`**WLFileOncePerSession**. The  script reads a new value/row from the file once, at the beginning of the  session (in InitClient). The value/row is released at the end of the session  (in TerminateAgenda).  `<br>`**WLFileAnytime**. The script can read a new  value/row from the file at any time during a round. It can read a new  value/row more than once during a round. The values are released at the end  of the round. This enables more than one  value/row  to be used concurrently and uniquely. |
| EndOfFileBehavior        | An optional parameter that  defines how WebLOAD behaves when it reaches the end of the file. All values  are enumerated numeric values.**Note:** If you have defined the AccessMethod as WLFileSequential or  WLFileSequentialUnique, the EndOfFileBehavior parameter is mandatory.  Possible values are:  `<br>`**WLFileStartOver**. Start from the beginning  of the file. This is the default value.  `<br>`**WLFileKeepLast**. Keep the last value.  `<br>`**WLFileAbortVC**. Abort the specific VC that  tried to read past the end of the  file. An error message is written to the log  file.  `<br>`**WLFileAbortTest**. Abort the entire test when a VC tries to  read past the end of the  file. An error message is written to the log file.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HeaderLines              | An optional parameter that defines the  number of header lines the file contains. All values are enumerated numeric  values. Possible values are:`<br>`0. The file does not  contain any header lines. This is the default  value.  `<br><X>`. Where `<X>`  is any number above zero. The file contains  `<X>` header lines at  its beginning. The values contained in these header lines are not used as  parameters but as variable  names in  the JavaScript code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Delimiter                | (Optional) The delimiter  being used in the file. The default value is a comma.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**Example**

```javascript
function InitAgenda()

{

InFile1 = CopyFile(“C:\\temp\input.txt”)

}

Function InitClient()

{

myFileObj = new wlInputFile(InFile1) myFileObj.open(WLFileSequentialUnique, WLFileAgendaShared)

}

/*** WLIDE …. ***/

strLine = myFileObj.getLine(“,”)
```

**See also**

* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* [*File Management Functions* ](#_bookmark25)
* GetLine() (see [*GetLine() (function)* ](#getline-function)))
* wlInputFile() (see [*wlInputFile() (constructor)* ](#wlinputfile-constructor)))

## Open() (function)

**Method of Object**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

Opens the output file, specified in the wlOutputFile object. By default, the file is opened for sequential access, enabling the parameters in the file to be read sequentially. This is unique across the master and slave processes of a single Load Generator/script combination. The master assigns the next line of the file that will be

read sequentially for each slave. When all the information in the file is read (see[*GetLine() (function)* ](#getline-function)), it is returned to the beginning of the file.

Alternatively, to open the input file and read its contents in random order, you must include Open(filename, wlRandom) in the script’s InitAgenda() function.

> **Note:** The last line of the file should not include a carriage return.

**Syntax**

For sequential access:

`MyFileObj = new wlOutputFile(*filename*)`

`…`

`MyFileObj.Open()`

For random access:

`Open(*filename*, wlRandom)`

**Parameters**

| **Parameter  Name** | **Description**                                                    |
| ------------------------- | ------------------------------------------------------------------------ |
| filename                  | The name of the file to be opened.                                       |
| wlRandom                  | A flag indicating that the file should be  opened in random access mode. |

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* *Using the Form Data Wizard* in the *WebLOAD Scripting Guide*
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile() (see [*wlOutputFile() (constructor)* ](#_bookmark476))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## option (object)

**Property of Object**

Option objects are grouped into collections of options that are themselves properties of the following:

* element (see [*element (object)* ](#_bookmark102))
* *Select* 

**Description**

A collection of the nested `<OPTION>` objects only found within elements of type SELECT, that is, forms[n].elements[n].type = “SELECT”. Each option object denotes one choice in a select element, containing information about a selected form element.

option objects are local to a single thread. You cannot create new option objects using the JavaScript new operator, but you can access HTML options through the properties and methods of the standard DOM objects. option properties are read- only.

option objects are grouped together within collections of options. To access an individual option’s properties, check the length property of the options collection and use an index number to access the individual options.

**Syntax**

To find out how many option objects are contained within a form element, check the value of:

`document.forms[#].elements[#].options.length`

Access each option’s properties directly using the following syntax:

`document.forms[#].elements[#].options[#].<*option-property*>`

For example:

`document.forms[1].elements[2].options[0].selected`

**Comment**

Options only exist if the type of the parent element is `<SELECT>`, that is, forms[n].elements[n].type = “SELECT”. For example, to check whether a form element is of type `<SELECT>` and includes an options collection, you could use the following script:

```javascript
function InitAgenda()

{

wlGlobals.Proxy = “webproxy.xyz.com:8080”

// Through proxy wlGlobals.SaveSource = true wlGlobals.ParseForms = true wlGlobals.ParseTables = true

}

function CheckElementType(WebTestSite)

{

wlHttp.Get(WebTestSite)

if (document.forms.length > 0)

if (document.forms[0].elements.length > 0)

{

InfoMessage(“We have a candidate. “ +

“Element type is “ + document.forms[0].elements[0].type)

InfoMessage (“document.forms[0].elements[0].options.length is “

\+ document.forms[0].elements[0].options.length)

}

}
```

CheckElementType([“http://www.TestSite1.com/domain/pulldown.htm](http://www.TestSite1.com/domain/pulldown.htm)”) CheckElementType(“http://www.TestSite2.com/”) ErrorMessage(“Done!”)

**Properties**

* defaultselected (see [*defaultselected (property)* ](#defaultvalue-property))
* selected (see [*selected (property)* ](#_bookmark337))
* value (see [*value (property)* ](#value-property))

## Options() (method)

**Method of Objects**

This function is implemented as a method of the following object:

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Options command.

**Syntax**

`Options([URL])`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [URL]                    | An optional parameter identifying the document URL.  You may optionally specify  the URL as a parameter of the method. Options() connects to the first URL that has been specified  from the following list, in the order specified:`<br>`A Url parameter  specified in the method call.  `<br>`The Url property of  the wlHttp object.  `<br>`The local default wlLocals.Url.  `<br>`The global default wlGlobals.Url. |

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Delete() (see [*Delete() (HTTP method)*](#delete-http-method)) 
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Head() (see [*Head() (method)* ](#_bookmark194))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark289))
* Put() (see [*Put() (method)* ](#_bookmark298)onpage [213](#_bookmark298))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## OuterLink (property)

**Property of Objects**

* Image (see [*Image (object)* ](#_bookmark210))

**Description**

Represents the outer link field for the parent image object.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* form (see [*form (object)* ](#form-object))
* [*Select* ](#_bookmark329)

## Outfile (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

The name of a file to which WebLOAD writes response data from the HTTP server.

The Outfile will contain the data from the *next* HTTP transaction, so the Outfile

command must *precede* the next transaction.

The default is ““, which means do not write the response data.

If there is more than one transaction after the Outfile property, only the response data from the *first* transaction will be written. To write the response data from each transaction an Outfile statement must be placed PRIOR to *each* transaction.

The Outfile property is independent of the SaveSource property. Outfile saves in a file. SaveSource stores the downloaded data in document.wlSource, in memory.

The Outfile property is used to implement the Log Report.

**Example**

To write the response data from

`[“http://note/radview/radview.html](http://note/radview/radview.html)” in “c:\temp.html”`

you might write:

`wlHttp.Outfile = “c:\\temp.html”`

`[wlHttp.Get(“http://note/radview/radview.html](http://note/radview/radview.html)”)`

**Comment**

The Outfile property saves *server response data*. To save *script output* m*essages*, use the wlOutputFile. (see [*wlOutputFile (object)* ](#_bookmark475))

**See also**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

## PageContentLength (property)

**Property of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

PageContentLength is used to retrieve the size in bytes of the content object in the GET/POST request. The content object may only be HTML, ASP, or JPG.

**Syntax**

`wlVerification.PageContentLength`

**Example**

[`wlHttp.Get(&#34;http://www.google.com/&#34;)](http://www.google.com/)`

`InfoMessage("page size" + wlVerification.PageContentLength)`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageTime (see [*PageTime (property)* ](#_bookmark271))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## PageTime (property)

**Property of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

PageTime is used to retrieve the page time of the last GET. That is, the total time taken to retrieve the page.

**Syntax**

wlVerification.PageTime

**Example**

[`wlHttp.Get(&#34;http://www.google.com/&#34;)](http://www.google.com/)`

`InfoMessage("page time" + wlVerification.PageTime)`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## Parse (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing on an HTML page.

The Parse property can be set to one of the following values:

* **always** (default) – Each page is parsed and the DOM is created every time the page is visited.
* **OnceOnly** – The page is parsed and the DOM is created only the first time the page is visited. The same data is then reused on future visits.
* **no** – The DOM is not created and no object can be retrieved.

> **Note:** If you want the page to be parsed and the DOM created the first time the page is visited and then reuse this data, set the ParseOnce property to true. For information about the ParseOnce property.This property can only be inserted manually.

**Syntax**

`wlGlobals.Parse = “Always”`

**See also**

* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseApplets (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables/disables parsing of Java applets on an HTML page. The ParseApplets property can be set to one of the following values:

* **true** (default) – Enables parsing of Java applets.
* **false** – Disables parsing of Java applets.

> **Note:** This property can only be inserted manually.   If GetApplets is true, ParseApplets will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseApplets = false

**See also**

* Parse (see [*Parse (property)*](#parse-property)*)* )
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseCss (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of cascading style sheets on an HTML page. The ParseApplets property can be set to one of the following values:

* **true** (default) – Enables parsing of cascading style sheets.
* **false** – Disables parsing of cascading style sheets.

> **Note:** This property can only be inserted manually.   If GetCss is true, ParseCss will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseCss = true

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseEmbeds (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of embedded objects on an HTML page. The ParseEmbeds property can be set to one of the following values:

* **true** (default) – Enables parsing of embedded objects.
* **false** – Disables parsing of embedded objects.

> **Note:** This property can only be inserted manually.

> **Note:** If GetEmbeds is true, ParseEmbeds will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseEmbeds = true

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseForms (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of forms on an HTML page. The ParseForms property can be set to one of the following values:

* **true** (default) – Enables parsing of forms.
* **false** – Disables parsing of forms.

> **Note:** This property can only be inserted manually.   If GetForms is true, ParseForms will automatically be assumed to be true, even if it is set to false.

**Example**

`wlGlobals.ParseForms = true`

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseImages (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of images on an HTML page. The ParseImages property can be set to one of the following values:

* **true** (default) – Enables parsing of images.
* **false** – Disables parsing of images.

> **Note:** This property can only be inserted manually.   If GetImages is true, ParseImages will automatically be assumed to be true, even if it is set to false.

**Example**

`wlGlobals.ParseImages = true`

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseLinks (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of links and areas on an HTML page. The ParseLinks property can be set to one of the following values:

* **true** (default) – Enables parsing of links.
* **false** – Disables parsing of links.

> **Note:** This property can only be inserted manually.   If GetLinks is true, ParseLinks will automatically be assumed to be true, even if it is set to false.

**Example**

`wlGlobals.ParseLinks = true`

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseMetas (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of metas on an HTML page. The ParseMetas property can be set to one of the following values:

* **true** (default) – Enables parsing of metas.
* **false** – Disables parsing of metas.

> **Note:** This property can only be inserted manually. If GetMetas is true, ParseMetas will automatically be assumed to be true, even if it is set to false.

**Example**

`wlGlobals.ParseMetas = true`

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseOnce (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

When set to true, the webpage is parsed and the DOM is created only the first time the page is visited. The same data is reused on future visits. The ParseOnce property is set when you call SetClientType(“Thin”). By default, the ParseOnce property is set to true.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.ParseOnce = true

**See also**

* Parse (see [*Parse (property)*](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))
* SetClientType (see [*SetClientType (function)* ](#_bookmark352))

## ParseOthers (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing on an HTML page for all objects not covered by specific parsing properties. The ParseOthers property can be set to one of the following values:

* **true** (default) – Enables parsing of other objects.
* **false** – Disables parsing of other objects.

> **Note:** This property can only be inserted manually.

**Example**

wlGlobals.ParseOthers = true

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseScripts (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of JavaScript scripts on an HTML page. The ParseScripts property can be set to one of the following values:

* **true** (default) – Enables parsing of JavaScript scripts.
* **false** – Disables parsing of JavaScript scripts.

> **Note:** This property can only be inserted manually. If GetScripts is true, ParseScripts will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseScripts = true

**See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseTables (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of tables on an HTML page. The ParseTables property can be set to one of the following values:

* **true** (default) – Enables parsing of tables.
* **false** – Disables parsing of tables.

> **Note:** This property can only be inserted manually.   If GetTables is true, ParseTables will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseTables = true

 **See also**

* Parse (see [*Parse (property)* ](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseXML (see [*ParseXML (property)* ](#_bookmark284))

## ParseXML (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enables parsing of XML on an HTML page. The ParseXML property can be set to one of the following values:

* **true** (default) – Enables parsing of XML.
* **false** – Disables parsing of XML.

> **Note:** This property can only be inserted manually.  If GetXML is true, ParseXML will automatically be assumed to be true, even if it is set to false.

**Example**

wlGlobals.ParseXML = true

**See also**

* Parse (see [*Parse (property)*](#parse-property))
* ParseApplets (see [*ParseApplets (property)* ](#_bookmark273))
* ParseCss (see [*ParseCss (property)* ](#_bookmark274))
* ParseEmbeds (see [*ParseEmbeds (property)* ](#_bookmark275))
* ParseForms (see [*ParseForms (property)* ](#_bookmark276))
* ParseImages (see [*ParseImages (property)* ](#_bookmark277))
* ParseLinks (see [*ParseLinks (property)* ](#_bookmark278))
* ParseMetas (see [*ParseMetas (property)* ](#_bookmark279))
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark460))
* ParseOthers (see [*ParseOthers (property)* ](#_bookmark281))
* ParseScripts (see [*ParseScripts (property)* ](#_bookmark282))
* ParseTables (see [*ParseTables (property)* ](#_bookmark460))

## PassWord (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The password that the script uses to log onto a restricted HTTP site. WebLOAD automatically uses the appropriate access protocol. For example, if a site expects clients to use the NT Authentication protocol, the appropriate user name and password will be stored and sent accordingly.

**Comments**

A user is only authenticated once during a round with a set of credentials. Each subsequent request will use these credentials regardless of what is contained in the script. If the value of these credentials are changed after authentication, they will only be used during the next round, not during the current round.

For example, if you are trying to send a request to a URL with a group of users (user1, user2, and user3), but user1 has already been authenticated, the login is always performed for user1 until the round is complete.

**GUI mode**

WebLOAD by default senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console by entering user authentication information through the Authentication tab of the **Default** or **Current Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also set user values using the wlGlobals properties. WebLOAD automatically sends the user name and password when a wlHttp object connects to an HTTP site. For example:

`wlGlobals.UserName = “Bill”`

`wlGlobals.PassWord = “TopSecret”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Working with the HTTP Protocol* in the *WebLOAD Scripting Guide*

## pathname (property)

**Property of Objects**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The URI portion of the URL, including the directory path and filename (read-only string).

**Example**

`“/products/order.html” “/search.exe”`

## port (property)

**Property of Objects**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The port of the URL (read-only integer).

**Example**

80

## Post() (method)

**Method of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Post command. The method sends the FormData, Data, or DataFile properties in the Post command. In this way, you can submit any type of data to an HTTP server.

**Syntax**

`Post([URL] [, TransName])`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [URL]                    | An optional parameter identifying the document  URL.  You may optionally specify  the URL as a parameter of the method. Post() connects to first URL that has  been specified from the following list:`<br>`A Url parameter  specified in the method call.  `<br>`The Url property of  the wlHttp object.  `<br>`The local default wlLocals.Url.  `<br>`The global default wlGlobals.Url.  The URL must be a server that accepts the posted  data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [TransName]              | An optional user-supplied  string with the transaction name as it will appear in the Statistics Report,  described in the*Data Drilling- WebLOAD  transaction reports* section of the *WebLOAD  Scripting Guide*.  Use *named transactions* to identify specific HTTP transactions by  name. This simplifies assigning counters when you want WebLOAD to  automatically calculate a specific transaction’s occurrence, success, and  failure rates.  The run-time statistics  for transactions to which you have assigned a name appear in the Statistics  Report. For your convenience, WebLOAD offers an Automatic Transaction option.  In the WebLOAD Console, select Automatic Transaction from the General Tab of  the Global Options dialog box. Automatic Transaction is set to true by default. With Automatic Transaction,  WebLOAD automatically assigns a name to every Get and Post HTTP transaction.  This makes statistical analysis simpler, since all HTTP transaction activity  is measured, recorded, and reported for you automatically. You do not have to  remember to add naming instructions to each Get and Post command in your script. The name assigned by  WebLOAD is simply the URL used by that Get or Post transaction. If your  script includes multiple transactions to the same URL, the information will  be collected cumulatively for those transactions. |

**Example**

```javascript
function InitAgenda() {

//Set the default URL

wlGlobals.Url = [“http://www.ABCDEF.com](http://www.ABCDEF.com/)”

}

//Main script

//Connect to the default URL: wlHttp.Post()

//Connect to a different, explicitly set URL: wlHttp.Post(“http://www.ABCDEF.com/product_info.html”)

//Assign a name to the following HTTP transact: [wlHttp.Get(“http://www.ABCDEF.com/product_info.html](http://www.ABCDEF.com/product_info.html)”,

“UpdateBankAccount”)

//Submit to a CGI program

wlHttp.Url = [“http://www.ABCDEF.com/search.cgi](http://www.ABCDEF.com/search.cgi)” wlHttp.FormData[“SeachTerm”] = “ocean+currents” wlHttp.Post()

//Submit to an HTTP server of any type wlHttp.FormData[“FirstName”] = “Bill” wlHttp.FormData[“LastName”] = “Smith” wlHttp.Post(“http://www.ABCDEF.com/formprocessor.exe”)

Use named transactions as a shortcut in place of the BeginTransaction()...EndTransaction() module. For example, this is one way to identify a logical transaction unit:

BeginTransaction(“UpdateBankAccount”) wlHttp.Get(url)

// the body of the transaction

// any valid JavaScript statements wlHttp.Post(url);

EndTransaction(“UpdateBankAccount”)

// and so on

Using the named transaction syntax, you could write:

wlHttp.Get(url,”UpdateBankAccount”)

// the body of the transaction

// any valid JavaScript statements wlHttp.Post(url,”UpdateBankAccount”)

// and so on
```

For the HTTPS protocol, include “https://” in the URL and set the required properties of the wlGlobals object:

`wlHttp.Post("https://www.ABCDEF.com")`

The URL can contain a string of attribute data.

wlHttp.Post(“http://www.ABCDEF.com/query.exe”+ “?SearchFor=icebergs&SearchType=ExactTerm”)

Alternatively, you can specify the attributes in the FormData or Data property. The method automatically appends these in the correct syntax to the URL. Thus the following two code fragments are each equivalent to the preceding Post command.

`wlHttp.Data.Type = “application/x-www-form-urlencoded”`

`wlHttp.Data.Value = “SearchFor=icebergs&SearchType=ExactTerm”`

`wlHttp.Post(“http://www.ABCDEF.com/query.exe”)`

-Or-

`wlHttp.FormData.SearchFor = “icebergs”`

`wlHttp.FormData.SearchType = “ExactTerm”`

`wlHttp.Post(“http://www.ABCDEF.com/query.exe”)`

**Comment**

You may not use the TransName parameter by itself. Post() expects to receive either *no* parameters, in which case it uses the script’s default URL, or *one* parameter, which must be an alternate URL value, or *two* parameters, including both a URL value and the transaction name to be assigned to this transaction.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Delete() (see [*Delete() (HTTP method)*](#_bookmark94)) 
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Head() (see [*Head() (method)* ](#_bookmark194))
* Options() (see [*Options() (method)* ](#_bookmark266))
* Put() (see [*Put() (method)* ](#_bookmark298)onpage [213](#_bookmark298))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## ProbingClientThreads (property)

**Properties of Objects**

* wlGlobals (see [*wlGlobals (object)* ](./actions_objects_functions.md#wlglobals-object))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))
* wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))

**Description**

Optionally, WebLOAD can allocate extra threads to download nested images and frames.

For clients that you define in a Load Generator, this option is controlled by the LoadGeneratorThreads property. The default value of this property is **Single**, which means that Virtual Clients will not use extra threads to download data from the server.

For the Probing Client, the option is controlled by the ProbingClientThreads property. The default is **Multiple**, which means that the client can use three extra threads for nested downloads. This simulates the behavior of Web browsers, which often use extra threads to download nested images and frames.

The possible values of these properties are:

* **Single** – Do not use extra threads to download nested images and frames. (default for LoadGeneratorThreads)
* **Multiple** – Allocate three extra threads per client (for a total of four threads per client) to download nested images and frames. (default for ProbingClientThreads)
* Any specific number of threads between 1 and 8, such as “5” – Allocate that exact number of extra threads per client to download nested images and frames.

**Example**

You can assign any of these properties independently within a single script. In that case, if you configure a Probing Client to run the script, WebLOAD uses the value of ProbingClientThreads and ignores LoadGeneratorThreads (vice versa if you configure a Load Generator to run the script). For example, you might write:

```javascript
function InitAgenda() {

//Do not use extra threads if a

// Probing Client runs the script

wlGlobals.ProbingClientThreads = “Single”

//Use extra threads if a

// Load Generator runs the script

wlGlobals.LoadGeneratorThreads = “Multiple”

}
```

**Comment**

The extra threads have no effect on the ClientNum value of the client. The ClientNum variable reports only the main thread number of each client, not the extra threads.

**GUI mode**

WebLOAD recommends enabling or disabling multi-threaded virtual clients through the WebLOAD Console. Enable multi-threading for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default** or **Current Session Options** dialog box and setting the number of threads you prefer

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* LoadGeneratorThreads (see [*LoadGeneratorThreads (property)* ](#loadgeneratorthreads-property))

## protocol (property)

**Property of Objects**

* Image (see [*Image (object)* ](#_bookmark210))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The HTTP protocol portion of the URL for the parent object (read-only string).

**Example**

`“https://”`

## Proxy, ProxyUserName, ProxyPassWord (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Identifies the proxy server that the script uses for HTTP access. The user name and password are for proxy servers that require user authorization.

**GUI mode**

WebLOAD by default senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console in one of the following ways:

* Enter user authentication information through the Authentication tab of the

**Default** or **Current Options** dialog box, accessed from the **Tools** tab of the ribbon.

* You may also set proxy user values using the wlGlobals properties. WebLOAD automatically connects via the proxy when a wlHttp object connects to an HTTP site.

**Syntax**

`wlGlobals.*ProxyProperty* = “TextString”`

**Example**

`wlGlobals.Proxy = “proxy.ABCDEF.com:8080”`

`wlGlobals.ProxyUserName = “Bill”`

`wlGlobals.ProxyPassWord = “Classified”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*
* HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord (see [*HttpsProxy,*](#httpsproxy-httpsproxyusername-httpsproxypassword-properties))
* HttpsProxyNTUserName, HttpsProxyNTPassWord (see [*HttpsProxyNTUserName, HttpsProxyNTPassWord (properties)*](#proxyntusername-proxyntpassword-properties))
* ProxyNTUserName, ProxyNTPassWord (see [*ProxyNTUserName, ProxyNTPassWord*](#proxyntusername-proxyntpassword-properties))

## ProxyExceptions (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

The ProxyExceptions property accepts a string based on what the user entered in the Proxy Options tab of the Recording and Script Generation Options dialog box. This string indicates the URLs whose support does not go through the proxy. The format of this string is based on the Internet Explorer format. For more information, see [http://www.microsoft.com/technet/prodtechnol/ie/ieak/techinfo/deploy/60/en/corppro](http://www.microsoft.com/technet/prodtechnol/ie/ieak/techinfo/deploy/60/en/corpprox.mspx?mfr=true) [x.mspx?mfr=true.](http://www.microsoft.com/technet/prodtechnol/ie/ieak/techinfo/deploy/60/en/corpprox.mspx?mfr=true)

**Example**

`wlGlobals.ProxyExceptions = “*.example.com”`

**GUI mode**

WebLOAD takes the current settings of the browser and displays them in the Proxy Options tab of the Recording and Script Generation Options dialog box in WebLOAD Recorder.

In WebLOAD Recorder, click **Recording and Script Generation Options** in the **Tools** tab of the ribbon, and click the Proxy Options tab. Modify the fields, as necessary.

## ProxyNTUserName, ProxyNTPassWord (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Provides user authorization to the proxy server that the script uses for HTTP access on Windows servers.

**GUI mode**

WebLOAD by default senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console in one of the following ways:

* Use the Authentication tab of the **Default** or **Current Options** dialog box to enter user authentication information.
* You may also set proxyNT user values using the wlGlobals properties. WebLOAD automatically connects via the proxy when a wlHttp object connects to an HTTP site.

**Syntax**

`wlGlobals.*ProxyNTProperty* = “TextString”`

**Example**

`wlGlobals.ProxyNTUserName = “Bill”`

`wlGlobals.ProxyNTPassWord = “Classified”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*
* HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord (see [*HttpsProxy,*](#httpsproxy-httpsproxyusername-httpsproxypassword-properties))
* HttpsProxyNTUserName, HttpsProxyNTPassWord see [*HttpsProxyNTUserName, HttpsProxyNTPassWord (properties)*](#proxy-proxyusername-proxypassword-properties)
* Proxy, ProxyUserName, ProxyPassWord (see [*Proxy, ProxyUserName,*](#proxy-proxyusername-proxypassword-properties))

## Put() (method)

**Method of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

Perform an HTTP or HTTPS Put command. The method sends the FormData, Data, or DataFile properties in the Put command. In this way, you can submit any type of data to an HTTP server.

**Syntax**

`Put([URL] [, TransName])`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [URL]                    | An optional parameter identifying the document  URL.  You may optionally specify the URL as a parameter  of the method. Put() connects to first URL that has been specified from the  following list:`<br>`A Url parameter specified in the method call.  `<br>`The Url property of the wlHttp object.  `<br>`The local default wlLocals.Url.  `<br>`The global default wlGlobals.Url.  The URL must be a server that accepts the  submitted data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [TransName]              | An optional user-supplied  string with the transaction name as it will appear in the Statistics Report,  described in the*Data Drilling- WebLOAD  transaction reports* section of the *WebLOAD  Scripting Guide*.  Use *named transactions* to identify specific HTTP transactions by  name. This simplifies assigning counters when you want WebLOAD to  automatically calculate a specific transaction’s occurrence, success, and  failure rates.  The run-time statistics  for transactions to which you have assigned a name appear in the Statistics  Report. For your convenience, WebLOAD offers an Automatic Transaction option.  In the WebLOAD Console, select Automatic Transaction from the General Tab of  the Global Options dialog box. Automatic Transaction is set to true by default. With Automatic Transaction,  WebLOAD automatically assigns a name to every Get, Post and Put HTTP  transaction. This makes statistical analysis simpler, since all HTTP  transaction activity is measured, recorded, and reported for you  automatically. You do not have to remember to add naming instructions to each  Get, Post and Put command in your script. The name assigned by WebLOAD is  simply the URL used by that Get, Post or Put transaction. If your script  includes multiple transactions to the same URL, the information will be  collected cumulatively for those transactions. |

**Comment**

You may not use the TransName parameter by itself. Put() expects to receive either *no* parameters, in which case it uses the script’s default URL, or *one* parameter, which must be an alternate URL value, or *two* parameters, including both a URL value and the transaction name to be assigned to this transaction.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Delete() (see [*Delete() (HTTP method)*](#_bookmark94)) 
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Head() (see [*Head() (method)* ](#_bookmark194))
* Options() (see [*Options() (method)* ](#_bookmark266))
* Post() (see [*Post() (method)* ](#_bookmark289))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## Range() (method)

**Method of Object**

* wlRand (see [*wlRand (object)* ](#wlrand-object))

**Description**

Return a random integer between start and end.

**Syntax**

wlRand.Range(start, end, [seed])

**Parameters**

| **Parameter Name** | **Description**                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| start                    | Integer signifying start of specified range  of numbers.                                                                 |
| end                      | Integer signifying end of specified range of  numbers.                                                                   |
| [seed]                   | Optional seed integer used on first call to  this method only if there was no previous call to the wlRand.Seed() method. |

**Return Value**

A random integer that falls within the specified range.

**Example** wlRand.Num(12345) **See also**

* Num() (see [*Num() (method)* ](#num-method))
* Seed()
* (see [*Seed() (method)* ](#_bookmark326))
* Select() (see [*Select() (method)* ](#_bookmark329))

## ReceiveTimeout (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

WebLOAD performs read operations in a loop. Each iteration of the loop consists of a wait on the socket until the server is ready, followed by a receive operation, if the read on the socket was successful. This is performed until all the information is read, or until the time spent in the loop exceeds the specified timeout value in the ReceiveTimeout property, or a socket error occurs. If a timeout or socket error occur,

WebLOAD then tries to reestablish a connection (see [*RequestRetries (property)* ](#_bookmark309)). The default value of the ReceiveTimeout property is 900,000 ms.

**Example**

`wlGlobals.ReceiveTimeout = 550000`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* RequestRetries (see [*RequestRetries (property)* ](#_bookmark309))

## RedirectionLimit (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

The maximum number of redirection ‘hops’ allowed during a test session. The default value is **10**.

**GUI mode**

WebLOAD recommends setting the redirection limit through the WebLOAD Console. Check Redirection Enabled and enter a limiting number on the Browser Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also assign a redirection limit value using the wl.RedirectionLimit property.

`wlGlobals.RedirectionLimit = *IntegerValue*`

**Example**

wlGlobals.RedirectionLimit = 10

## Referer (property)

**Property of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))
* wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))

**Description**

The Referer property is used by the recorder to store the referer header and is a synonym for wlHTTP.Headers[“referer”]. The Referer property is used as shorthand for accessing the referer header in the wlHTTP.Headers collection.

**GUI mode**

To tell the system whether or not to record the referer header in the Referer property, select or deselect the **Record Referer Header** checkbox in the Script Content tab of the **Recording and Script Generation Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

`wlHttp.Header[“Referer”] = [“http://www.testaddress.com/](http://www.testaddress.com/)”.`

**Example**

`wlHttp.Header[“Referer”] = [“http://www.easycar.com/](http://www.easycar.com/)”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*

## remove() (method)

**Method of Objects**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

This method deletes the wlOutputFile object and closes the output file.

**Syntax**

`wlOutputFile.remove()`

**Example**

`MyFileObj = new wlOutputFile(*filename*)`

`…`

`MyFileObj.remove()`

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## ReportEvent() (function)

**Description**

This function enables you to record specific events as they occur. This information is very helpful when analyzing website performance with Data Drilling.

**Syntax**

`ReportEvent(EventName[, description])`

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EventName                 | A user-supplied string  that identifies the specific event and appears in the results tables of the  WebLOAD Data Drilling feature. Since this name is used as a table header and  sort key, it must be a short string that is used consistently to identify  events, such as “URLMismatch”. |
| [description]             | An optional user-supplied string that may be  longer and more detailed than the EventName, providing more  information about the specific event.                                                                                                                                               |

**See also**

* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function)))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## ReportLog() (method)

**Method of Object**

* wlException (see [wlException (object) ](#_bookmark446))

**Description**

Sends a message to the Log Window that includes the error message and severity level stored in this wlException object.

**Syntax**

`ReportLog()`

**Example**

`myUserException.ReportLog()`

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

## RequestRetries (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Read operations are performed in a loop until all information is read. If the duration of this loop exceeds a specified timeout (see [*ReceiveTimeout (property)* ](#_bookmark299)) or a socket error occurs, the Virtual Client will then retry to establish a connection.

RequestRetries is the maximum number of times that the Virtual Client will attempt to reconnect to the server. The default value of RequestRetries is **9**.

**Example**

`wlGlobals.RequestRetries = 7`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* ReceiveTimeout (see [*ReceiveTimeout (property)* ](#_bookmark299))

## Reset() (method)

**Method of Object**

* wlOutputFile() (see [*wlOutputFile (object)* ](#_bookmark474))

**Description**

Return to the beginning of the output file.

**Syntax**

`Reset()`

**Example**

`MyFileObj = new wlOutputFile(*filename*)`

`…`

`MyFileObj.Reset()`

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* wlOutputFile() (see [*wlOutputFile() (constructor)* ](#_bookmark476))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

## ResponseContentType (property)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The language in which WebLOAD receives the response from the SUT. This can be HTML, XML, or Not Defined and is used to decide whether or not to parse the response. If ResponseContentType is set to HTML or XML, the content of the response is treated as either HTML or XML, as specified. If not, an algorithm checks the content type of the response. This algorithm uses two other wlGlobals: HtmlContentTypes and XmlContentTypes. These contain a list of content types that specify HTMLs and XMLs, respectively. The algorithm checks whether the content type of the response matches either of these lists.

**Syntax**

`wlGlobals.ResponseContentType = “TextString”`

**Example**

`wlGlobals.ResponseContentType = “HTML”`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## RoundNum (variable)

**Description**

The number of times that WebLOAD has executed the main script of a client during the WebLOAD test, including the current execution. RoundNum is a read-only local variable, reporting the number of rounds for the specific WebLOAD client, no matter how many other clients may be running the same script.

RoundNum does not exist in the global context of a script (InitAgenda(), etc.). In the local context:

* In InitClient(), RoundNum = 0.
* In the main script, RoundNum = 1, 2, 3, ....
* In TerminateClient(), OnScriptAbort(), or

OnErrorTerminateClient(), RoundNum keeps its value from the final round.

The WebLOAD clients do not necessarily remain in synchronization. The RoundNum

may differ for different clients running the same script.

If a thread stops and restarts for any reason, the RoundNum continues from its value before the interruption. This can occur, for example, after you issue a Pause command from the WebLOAD Console.

If you mix scripts in a single Load Generator, WebLOAD maintains an independent round counter for each script. For example, if **WLFileAgendaShared** GUI mode

WebLOAD recommends accessing global system variables, including the RoundNum identification variable, through the WebLOAD Recorder. The variables that appear in this list are available for use at any point in a script file. In the WebLOAD Recorder main window, click **Variables Windows** in the **Debug** tab of the ribbon**.**.

For example, it is convenient to add RoundNum to a Message Node to clarify the round in which the messages that appear in the WebLOAD Console Log window originated.

> **Note:** RoundNum can also be added directly to the code in a script through the IntelliSense Editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18).

**See also**

* GeneratorName() (see [*GeneratorName() (function)* ](#generatorname-function))
* GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](#_bookmark176))
* [*Identification Variables and Functions* ](#_bookmark28)
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432))

## row (object)

**Property of Objects**

row objects are grouped into collections of rows. The rows collection is a property of the following objects:

* wlTables (see [*wlTables (object)* ](#_bookmark493))

**Description**

When working with TextArea element objects, a row object contains the number of rows in the TextArea.

When working with wlTables objects, a row object contains all the data found in a single table row. Individual row objects may be addressed by index number, similar to any object within a collection.

**Syntax**

Individual row objects are addressed by index number, similar to any object within a collection. Access each row’s properties directly using the following syntax:

`document.wlTables.myTable.rows[#].<row-property>`

**Example**

To find out how many row objects are contained within myTable, check the value of:

`document.wlTables.myTable.rows.length`

To access a property of the 16th row in myTable, with the first row indexed at 0, you could write:

`document.wlTables.myTable.rows[15].rowIndex`

To access a property of the 4th cell in the 3rd row in myTable, counting across rows and with the first cell indexed at 0, you could write:

`document.wlTables.myTable.rows[2].cells[3].<*cell-property*>`

**Properties**

Each row object contains information about the data found in the cells of a single table row. The row object includes the following properties:

* cell (see [*cell (object)* ](#_bookmark49)) (row property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)

**Comment**

The row object may be accessed as a member of the wlTables family of table, row, and cell objects.

**See also**

* cell
* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)
*


* 

* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* rowIndex (see [*rowIndex (property)* ](#rowindex-property))
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)

## rowIndex (property)

**Property of Object**

* row (see [*row (object)* ](#_bookmark315))

**Description**

An integer containing the ordinal index number of this row object within the parent table. Rows are indexed starting from zero, so the rowIndex of the first row in a table is 0.

**Comment**

The rowIndex property is a member of the wlTables family of table, row, and cell objects.

**See also**

* cell
* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)
*


* 

* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## SaveHeaders (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Instruct WebLOAD to store the HTML response headers in wlHeaders.

* **false** –Do not store the header. (default)
* **true** – Store the header in document.wlHeaders.

 **Note:** This property can only be inserted manually.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## SaveSource (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Instruct WebLOAD to store the complete HTML source code downloaded in an HTTP command.

* **false** – Do not store the source HTML (default).
* **true** – Store the source HTML in document.wlSource.

If you enable SaveSource, WebLOAD automatically stores the downloaded HTML whenever the script calls the wlHttp.Get() or wlHttp.Post() method. WebLOAD stores the most recent download in the document.wlSource property, refreshing it when the script calls wlHttp.Get() or wlHttp.Post() again. The stored code includes any scripts or other data embedded in the HTML. Your script can retrieve the code from document.wlSource and interpret it in any desired way.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## SaveTransaction (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)

**Description**

Instruct WebLOAD to save detailed information about all transactions, both successes and failures, for later analysis in the Data Drilling reports.

By default, WebLOAD only saves detailed information about transaction failures for later analysis, since most test sessions are focused on tracking down and identifying the causes of errors and failures.

WebLOAD also provides the option of storing and analyzing the data for all transactions in a test session, successes and failures, through the SaveTransaction property. However, this property should be used carefully, since a successful test session may run for an extended period, and saving data on each transaction success could quickly use up all available disk space.

> **Note:** Transaction data is only saved for the number of instances defined in the Instance limit field in the WebLOAD Console (Global Options dialog box, in the Data Drilling tab).

Possible values of the SaveTransaction property are:

* **false** – Do not store detailed data on successful transactions (default).
* **true** – Store detailed data on successful transactions.

The SaveTransaction property works with the following parameters in the Functional Testing tab (Automatic Data Collection area) of the Current Session Options/Default Options dialog box in the WebLOAD Console, as follows:

* **Pages** – When selected, WebLOAD provides timers and counters for every “Get” in the session. When SaveTransaction is set to true, WebLOAD provides an aggregate breakdown for all objects in the page.
* **Object level** – When selected, WebLOAD provides timers and counters for every object in every page. When SaveTransaction is set to true, WebLOAD provides breakdown information for every object in every page.
* **HTTP level** – When selected, WebLOAD provides breakdown information for every failed transaction in every page. When SaveTransaction is set to true, WebLOAD provides breakdown information for every instance of every failed transaction in every page.

**Example**

```javascript
function InitAgenda() 

{ 

wlGlobals.SaveTransaction = true

}
```

**Comment**

As with all wlGlobals configuration properties, the SaveTransaction property must be set in the InitAgenda() function, as illustrated in the preceding example.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## script (object)

**Property of Object**

Scripts on a Web page are accessed through script objects that are grouped into collections of scripts. The scripts collection is a property of the following object:

* document (see [*document (object)* ](#_bookmark100))

**Description**

Specifies a script object in the current document that is interpreted by a script engine.

script objects are grouped together within collections of scripts.

**Syntax**

The scripts collection includes a length property that reports the number of script objects within a document (read-only). To access an individual script’s properties, check the length property of the scripts collection and use an index number to access the individual scripts. For example, to find out how many script objects are contained within a document, check the value of:

`document.scripts.length`

Access each script’s properties directly using the following syntax:

`document.scripts[*index*#].<*scripts-property*>`

**Example**

document.scripts[1].language

**Properties**

* event (see [*event (property)* ](#_bookmark118))
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* language (see [*language (property)* ](#_bookmark232))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)

## search (property)

**Property of Objects**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

The search attribute string of the URL, not including the initial ? symbol (read-only string).

**Example**

`“SearchFor=modems&SearchType=ExactTerm”`

## Seed() (method)

**Method of Object**

* wlRand (see [*wlRand (object)* ](#wlrand-object))

**Description**

Initialize the random number generator. Call the Seed() method in the

InitAgenda() function of a script, using any integer as a seed.

**Syntax**

`wlRand.Seed(seed) ****`

**Example**

`wlRand.Seed(12345)`

**See also**

* Num() (see [*Num() (method)* ](#num-method))
* Range() (see [*Range() (method)* ](#_bookmark300))
* Select() (see [*Select() (method)* ](#_bookmark329))

## Select

### Select() (method)

**Method of Object**

* wlRand (see [*wlRand (object)* ](#wlrand-object))

**Description**

Select one element of a set at random.

**Syntax**

`wlRand.Select(val1, val2, ..., val*N*)`

**Parameters**

| **Parameter  Name** | **Description**                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| val1…val*N*            | Any number of parameters itemizing the elements in  a set. The parameters can be numbers, strings, or any other objects. |

**Return Value**

The value of one of its parameters, selected at random.

**Example**

`wlRand.Select(21, 57, 88, 93)`

**See also**

* Num() (see [*Num() (method)* ](#num-method))
* Range() (see [*R*](#_bookmark300)[*ange() (method)* ](#_bookmark300))
* Seed() (see [*Se*](#_bookmark326)[*ed() (method)* ](#_bookmark326))

## SelectSecondTimeout (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Specify a second option for the amount of time the system will wait for a TCP connection to be established before timing out. The default value of SelectSecondTimeout is **0 milliseconds**.

**Syntax**

wlGlobals.SelectSecondTimeout = number

**Example** wlGlobals.SelectSecondTimeout = 100 **See also**

* SelectSwitchNum (see [*SelectSwitchNum (property)* ](#_bookmark332))
* SelectTimeout (see [*SelectTimeout (property)* ](#_bookmark333))

## SelectSwitchNum (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The number of iterations after which the timeout is made shorter and the sleep time longer to ease the stress on the CPU. The default value of SelectSwitchNum is **100**.

**Syntax**

wlGlobals.SelectSwitchNum = number

**Example** wlGlobals.SelectSwitchNum = 500 **Comment**

The following describes the basic functionality of the Load Engine.

Each read operation is limited by the RecvTimeout property. That is, the entire algorithm described below exits when it reaches the RecvTimeout timeout.

First, a send operation is performed with a request to the server:

```javascript
numberOfIterations = 0

while (wlGlobals.SendTimeout not exceeded) {

if (numberOfIterations < wlGlobals.SelectWriteSwitchNum { timeout = wlGlobals.SelectWriteTimeout

sleepTime = wlGlbobals.SelectWriteSecondTimeout

}

else {

timeout = wlGlobals.SelectWriteSecondTimeout

sleepTime = wlGlbobals.SelectWriteTimeout

}

select for read (timeout) if (socket ready) break

}

send request
```

Then the Load Engine attempts to read the response:

```javascript
numberOfIterations = 0

while (wlGlobals.RecvTimeout not exceeded) {

if (numberOfIterations < wlGlobals.SelecSwitchNum { timeout = wlGlobals.SelecTimeout

sleepTime = wlGlbobals.SelectSecondTimeout

}

else {

timeout = wlGlobals.SelectSecondTimeout sleepTime = wlGlbobals.SelectTimeout

}

select for write (timeout) if (socket ready) break

}

read response
```

The IO operations of the Load Engine are synchronous, basically looping and polling the sockets. The Load Engine performs a select on the socket with a timeout. If the select on the socket fails, a short sleep is performed and the system tries to perform the select again until the timeout specified in the SelectTimeout property is exceeded. This also enables the Load Engine to check with the monitor between selects to see if the session has ended.

**See also**

* SelectSecondTimeout (see [*SelectSecondTimeout (property)* ](#_bookmark331))
* SelectTimeout (see [*SelectTimeout (property)* ](#_bookmark333))

## SelectTimeout (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

A timeout used when performing a select on a socket. If the select on the socket fails, a short sleep is performed and the system tries to perform the select again until the timeout specified in the SelectTimeout property is exceeded. The default value of SelectTimeout is **200 milliseconds**.

**Syntax**

wlGlobals.SelectTimeout = number

**Example** wlGlobals.SelectTimeout = 300 **See also**

* SelectSecondTimeout (see [*SelectSecondTimeout (property)* ](#_bookmark331))
* SelectSwitchNum (see [*SelectSwitchNum (property)* ](#_bookmark332))

## SelectWriteSecondTimeout (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Specify a second option of the amount of time that the connection should stay open while nothing is being written to it. The default value of SelectWriteSecondTimeout is **10 milliseconds**.

**Syntax**

`wlGlobals.*SelectWriteSecondTimeout* = number`

**Example**

wlGlobals.SelectWriteSecondTimeout = 100

**See also**

* SelectWriteSwitchNum (see [*SelectWriteSwitchNum (property)* ](#_bookmark335))
* SelectWriteTimeout (see [*SelectWriteTimeout (property)* ](#_bookmark336))

## SelectWriteSwitchNum (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Indicate the amount of time that elapses before switching from the first write timeout to the second write timeout. The default value of SelectWriteSwitchNum is100 milliseconds.

**Syntax**

wlGlobals.SelectWriteSwitchNum = number

**Example** wlGlobals.SelectWriteSwitchNum = 100 **See also**

* SelectWriteSecondTimeout (see [*SelectWriteSecondTimeout* ](#_bookmark334))
* SelectWriteTimeout (see [*SelectWriteTimeout* ](#_bookmark336))

## SelectWriteTimeout (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Specify the amount of time that the connection should stay open while nothing is being written to it. The default value of SelectWriteTimeout is **200 milliseconds**.

**Syntax**

wlGlobals.SelectWriteTimeout = number

**Example** wlGlobals.SelectWriteTimeout = 300 **See also**

* SelectWriteSecondTimeout (see [*Se*](#_bookmark334)[*lectWriteSecondTimeout (property)* ](#_bookmark334))
* SelectWriteSwitchNum (see [*S*](#_bookmark335)[*electWriteSwitchNum (property)* ](#_bookmark335))

## selected (property)

**Property of Objects**

* option (see [*op*](#_bookmark264)[*tion (object)* ](#_bookmark264))

**Description**

The selected property has a value of true if this `<OPTION>` element has been selected, or false otherwise (read-only).

**See also**

* location (see [*l*](#_bookmark243)[*ocation (object)* ](#_bookmark243))

## selectedindex (property)

**Property of Objects**

* element (see [*el*](#_bookmark102)[*ement (object)* ](#_bookmark102))
* location (see [*location (object)* ](#_bookmark244))

**Description**

Indicates which of the nested `<OPTION>` elements is selected in an element of type

`<SELECT>`. The possible values are 0, 1, 2, For example, if the first `<OPTION>`

element is selected, then selectedindex = 0 (read-only). The default value is **0**.

## SendBufferSize (property)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The SendBufferSize property defines the amount of space allocated to the outgoing data buffer. The default value of SendBufferSize is **-1**, which indicates that the entire request should be sent in one buffer.

 **Note:** This property can only be inserted manually.

**Syntax**

`wlGlobals.SendBufferSize = number`

**Example**

`wlGlobals.SendBufferSize = 300`

## SendClientStatistics (property)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

SendClientStatistics is used to define whether or not to send statistics. It should be set in InitAgenda. The console writes the raw data to C:\Documents and Settings\`<user name>`\Local Settings\Temp\ClientStat.txt. To change the name, add CLIENT_STATISTICS_FILE = “file-name” to webload.ini on the console side. By default, this will save the raw statistics data for all the clients.

Only statistics calculated by the Load Generator are supported. Statistics like hits/second are not sent and empty statistics, for example, RoundTime where no round was completed within a time slice, are sent as -1.

**Example**

wlGlobals.SendClientStatistics = true

**See also**

* SendClientStatisticsFilter (see [*SendClientStatisticsFilter (property)* ](#sendclientstatisticsfilter-property))

## SendClientStatisticsFilter (property)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

This is a very simple filter for choosing clients for which to send statistics. The format is “1;4;8;”. Each number is a client number and you can specify as many client numbers as you want. Ranges and wildcards are not supported. If no client numbers are specified, statistics are sent for all clients.

If spawning is being used and you specify, for example, “1”, statistics for the first VC will be sent for each slave process.

Only statistics calculated by the Load Generator are supported. Statistics like hits/second are not sent and empty statistics, for example, RoundTime where no round was completed within a time slice, are sent as -1.

 **Note:** The filter and file name are not checked.

**Syntax**

wlGlobals.SendClientStatisticsFilter = “`<client number>`;`<client number>`;”

**Example**

`wlGlobals.SendClientStatisticsFilter = “2;3;8”`

**See also**

* SendClientStatistics (see [*SendClientStatistics (property)* ](#sendclientstatistics-property)))

## SendCounter() (function)

**Description**

Use this function to count the number of times an event occurs and output the value to the WebLOAD Console. Call SendCounter() in the main script of a script.

**Syntax**

SendCounter(EventName)

**See also**

* SendMeasurement() (see [*SendMeasurement() (function)* ](#sendmeasurement-function))
* SendTimer() (see [*SendT*](#_bookmark348)[*imer() (function)* ](#_bookmark348))
* SetTimer() (see [*Se*](#sendtimer-function)[*tTimer() (function)* ](#sendtimer-function))
* Sleep() (see [*S*](#sleep-function)[*leep() (function)* ](#sleep-function))
* SynchronizationPoint() (see [*S*](#_bookmark404)[*ynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark36)

## SendMeasurement() (function)

**Description**

Use this function to assign a value to the specified statistical measurement. Call

SendMeasurement() in the main script of a script.

**Syntax**

`SendMeasurement(MeasurementName, value)`

**Parameters**

| **Parameter  Name** | **Description**                                 |
| ------------------------- | ----------------------------------------------------- |
| MeasurementName           | A string with the name of the measurement  being set. |
| value                     | An integer value to set.                              |

**Example**

`NumberOfImagesInPage = document.images.length`

`SendMeasurement(“NumberOfImagesInPage”,NumberOfImagesInPage)`

**GUI mode**

WebLOAD recommends setting measurement functions within script files directly through the WebLOAD Recorder. In WebLOAD Recorder, drag the **Send Measurement** icon from the Load toolbox into the Script Tree at the desired location. The Send Measurement dialog box opens. Select a measurement name and its value and click **OK**. The **Send Measurement** item appears in the Script Tree and the JavaScript code is added to the script. To see the new JavaScript code, view the script in JavaScript Editing mode.

**See also**

* SendCounter() (see [*Send*](#_bookmark343)[*Counter() (function)* ](#_bookmark343))
* SendTimer() (see [*SendT*](#_bookmark348)[*imer() (function)* ](#_bookmark348))
* SetTimer() (see [*Se*](#sendtimer-function)[*tTimer() (function)* ](#sendtimer-function))
* Sleep() (see [*S*](#sleep-function)[*leep() (function)* ](#sleep-function)))
* SynchronizationPoint() (see [*S*](#_bookmark404)[*ynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark36)

## SendTimer() (function)

**Description**

Use this function to output the value of a timer to the WebLOAD Console. Call SendTimer() in the main script of a script, immediately after any step or sequence of steps whose time you want to measure. Before the sequence of steps, you must call SetTimer() to zero the timer.

**Syntax**

`SendTimer(TimerName)`

**Example**

`SendTimer(“Link 3 Time”)`

**GUI mode**

WebLOAD recommends setting timer functions within script files directly through the WebLOAD Recorder. In WebLOAD Recorder, drag the Send Timer  icon from the Load toolbox into the Script Tree at the desired location. The Send Timer dialog box opens. Enter a timer name and click **OK**. The Send Timer item appears in the Script Tree and the JavaScript code is added to the script. To see the new JavaScript code, view the script in JavaScript Editing mode.

**See also**

* SendCounter() (see [*Send*](#_bookmark343)[*Counter() (function)* ](#_bookmark343))
* SendMeasurement() (see [*SendMe*](#sendmeasurement-function)[*asurement() (function)* ](#sendmeasurement-function))
* SetTimer() (see [*Se*](#_bookmark357)[*tTimer() (function)* ](#_bookmark357))
* Sleep() (see [*S*](#sleep-function)[*leep() (function)* ](#sleep-function))
* SynchronizationPoint() (see [*S*](#_bookmark404)[*ynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark36)

## Set() (method)

### Set() (addition method)

**Method of Objects**

* wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450))
* wlSystemGlobal (see [*w*](#_bookmark490)[*lSystemGlobal (object)* ](#_bookmark490))

**Description**

Assigns a number, Boolean, or string value to the specified shared variable. If the variable does not exist, WebLOAD will create a new variable.

**Syntax**

`Set(“SharedVarName”, value, ScopeFlag)`

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SharedVarName             | The name of a shared variable to be set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| value                     | The value to be assigned to the specified  variable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ScopeFlag                 | One of two flags, WLCurrentAgenda or WLAllAgendas, signifying the scope of  the shared variable.  When used as a method of the wlGeneratorGlobal object:`<br>`The WLCurrentAgenda scope flag signifies variable values that you wish  to share between all threads of a single script, part of a single process,  running on a single Load Generator.  `<br>`The WLAllAgendas scope flag signifies variable values that you wish to share between  all threads of one or more scripts, common to a single spawned process,  running on a single Load Generator.  When used as a method of the wlSystemGlobal object:  `<br>`The WLCurrentAgenda scope flag signifies  variable values that you wish to share between all threads of a single  script, potentially shared by multiple processes, running on multiple Load  Generators, system wide.  `<br>`The WLAllAgendas scope flag signifies  variable values that you wish to share between all threads of all scripts,  run by all  processes,  on all Load Generators, system-wide. |

**Example**

`wlGeneratorGlobal.Set(“MySharedCounter”, 0, WLCurrentAgenda)`

`wlSystemGlobal.Set(“MyGlobalCounter”, 0, WLCurrentAgenda)`

**See also**

* Add() (see [*Add() (method)* ](#_bookmark45))
* Get() (see [*Get() (addition method)* ](#_bookmark134))

### Set() (cookie method)

**Method of Object**

* location (see [*location (object)* ](#_bookmark243))
* wlCookie (see [*wlCookie (object)* ](#wlcookie-object))

**Description**

Creates a cookie.

You can set an arbitrary number of cookies in any thread. If you set more than one cookie applying to a particular domain, WebLOAD submits them all when it connects to the domain.

**Syntax**

`wlCookie.Set(name, value, domain, path [, expire])`

**Parameters**

| **Parameter  Name** | **Description**                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| name                      | A descriptive name  identifying the type of information stored in the cookie, for example, “CUSTOMER”.                   |
| value                     | A value for the named cookie, for example, “JOHN_SMITH”.                                                                 |
| domain                    | The top-level domain name to which the  cookie should be submitted, for example,[“www.ABCDEF.com](http://www.ABCDEF.com/)”. |
| path                      | The top-level directory  path, within the specified domain, to which the cookie is submitted, for  example, “/”.         |
| expire                    | An optional expiration  timestamp of the cookie, in a format such as “Wed, 08-Apr-98 17:29:00 GMT”.                      |

**Comment**

Set cookies within the main script of the script. WebLOAD deletes all the cookies at the end of each round. If you wish to delete cookies in the middle of a round, use the Delete() or ClearAll() method.

**Example**

If you combine the examples used to illustrate the parameters for this method, you end up with the following:

`wlCookie.Set(“CUSTOMER”, “JOHN_SMITH”, [“www.ABCDEF.com](http://www.ABCDEF.com/)”, “/”,`

`“Wed, 08-Apr-98 17:29:00 GMT”)`

Where:

* The method creates a cookie containing the data CUSTOMER=JOHN_SMITH. This is the data that the thread submits when it connects to a URL in the domain.
* The domain of our sample cookie is [www.ABCDEF.com/. ](http://www.ABCDEF.com/)The thread submits the cookie when it connects to any URL in or below this domain, for example,[ http://info.www.ABCDEF.com/customers/FormProcessor.exe.](http://info.www.ABCDEF.com/customers/FormProcessor.exe)
* The cookie is valid until the expiration time, which in this case is Wednesday, April 8, 1998, at 17:29 GMT.

## SetClientType (function)

**Description**

The HTTP client has the following sub types, which can be set using the SetClientType function. These sub-types are:

* **Normal** (default) – When the client type is set to Normal, a DOM is created without tables.
* **Thick** – When the client type is set to Thick, the tables structure is included in the DOM.
* **Thin** – When the client type is set to Thin, no DOM or headers are created, and each page is parsed only once. This type is used for very high performance with static pages.

Use the SetClientType function with the Thick sub-type when you want to parse tables or with the Thin sub-type when you want optimize tests for simple writes with static pages.

**Syntax**

setClientType(clientType)

**Example**

setClientType(thick)

**Comment**

When you call SetClientType(“Thin”), the ParseOnce flag is set to true. Each page will only be parsed the first time it is read and the list of all the resources it accesses will be saved. The next time the page is needed, the list will be reused and no additional parsing will be performed.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* ParseOnce (see [*ParseOnce (property)* ](#_bookmark280)*on* page [198](#_bookmark280))
* GetImagesInThinClient (see [*GetImagesInThinClient (property)* ](#_bookmark164))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## SetFailureReason() (function)

**Description**

This function enables you to specify possible reasons for a transaction failure within your transaction verification function. These reasons will also appear in the Statistics Report. The default reason for most HTTP command (Get, Post, and Head) failures is simply HTTP-Failure. Unless you specify another reason for failure, HTTP-Failure will be set automatically whenever an HTTP transaction fails on the HTTP protocol level. SetFailureReason() allows you to add more meaningful information to your error reports.

**Syntax**

SetFailureReason(ReasonName) ****

**Comment**

The SetFailureReason() function accepts a literal string as the parameter. This string identifies the cause of the failure. To get an accurate picture of different failure causes, be sure to use identification strings consistently for each failure type. For example, don’t use both ‘User Not Logged’ *and* ‘User Not LoggedIn’ for the same type of failure, or your reports statistics will not be as informative. If you do not specify a specific reason for the failure, the system will register a ‘General Failure’, the default fail value.

**See also**

* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## setTimeout() (function)

**Description**

Execute the specified callback after a specified number of milliseconds.

The script execution will continue immediately, not waiting for the specified time or the function to execute (unlike the [*Sleep() (function)*, ](#_bookmark364)which instructs the script to pause for a specified time).

**Syntax**

setTimeout (Func, PauseTime)

**Parameters**

| **Parameter  Name** | **Description**                                             |
| ------------------------- | ----------------------------------------------------------------- |
| Func                      | Function to be called after the specified  number of milliseconds |
| PauseTime                 | An integer value specifying the number of  milliseconds to pause. |

**Example**

To pause for 1 second, write:

```javascript
InfoMessage(“before setTimeout”);

setTimeout( function() {

InfoMessage(“in setTimeout”);

} , 1000);

InfoMessage(“after setTimeout”);

Sleep(2000);

InfoMessage(“after sleep”);
```

**See also**

* [*Sleep() (function)* ](#_bookmark364)

## SetTimer() (function)

**Description**

Use this function to zero a timer. Call SetTimer() in the main script of a script, immediately before any step or sequence of steps whose time you want to measure. Be sure to zero the timer in every round of the script; the timer continues running between rounds if you do not zero it.

**Syntax** SetTimer(TimerName) **Parameters**

**Example**

`SetTimer(“Link 3 Time”)`

**GUI mode**

WebLOAD recommends setting timer functions within script files directly through the WebLOAD Recorder. In WebLOAD Recorder, drag the Set Timer icon from the Load toolbox into the Script Tree at the desired location. The Set Timer dialog box opens.

Enter a timer name and click **OK**. The Set Timer item appears in the Script Tree and the JavaScript code is added to the script. To see the new JavaScript code, view the script in JavaScript Editing mode.

**See also**

* SendCounter() (see [*SendCounter() (function)* ](#_bookmark343))
* SendMeasurement() (see [*SendMeasurement() (function)* ](#sendmeasurement-function))
* SendTimer() (see [*SendTimer() (function)* ](#_bookmark348))
* Sleep() (see [*Sleep() (function)* ](#sleep-function))
* SynchronizationPoint() (see [*SynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark35)

## SevereErrorMessage() (function)

**Description**

Use this function to display a severe error message in the Log Window of the WebLOAD Console, stop the session, and abort the Load Generator.

**Syntax**

SevereErrorMessage(msg)

**Comment**

If you call SevereErrorMessage() in the main script, WebLOAD stops all activity in the Load Generator and runs the error handling functions (OnScriptAbort(), etc.), if they exist in the script. You may also use the wlException (see [*wlException*](#_bookmark446) [*(object)* ](#_bookmark446)) object with the built-in try()/catch() commands to catch errors within your script. For more information about error management and execution sequence options, see *Error Management* in the *WebLOAD Scripting Guide*.

**GUI mode**

WebLOAD recommends adding message functions to your script files directly through the WebLOAD Recorder. Drag the Message icon from the WebLOAD Recorder toolbox into the script. The Message dialog box opens. Enter the message text, select a severity level for the message, and click **OK**.

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))
* wlException (see [*wlException (object)* ](#_bookmark446))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

## Severity (property)

**Property of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

Severity is used to define the global severity of a verification fail error. When defined, Severity affects all the verifications in which severity is not defined. If you define the error severity for a specific verification, it overrides the global severity defined in the Severity property.

Possible values of the Severity property are:

* WLSuccess – The transaction terminated successfully.
* WLMinorError – This specific transaction failed, but the test session may continue as usual. The script displays a warning message in the Log window and continues execution from the next statement.
* WLError – This specific transaction failed and the current test round was aborted. The script displays an error message in the Log window and begins a new round.
* WLSevereError – This specific transaction failed and the test session must be stopped completely. The script displays an error message in the Log window and the Load Generator on which the error occurred is stopped.

**Example**

To set the global severity of all verification fail errors to WLError, write:

`wlVerification.Severity = WLError`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* PageTime (see [*PageTime (property)* ](#_bookmark271))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))

## Size (property)

**Property of Object**

* element (see [*element (object)* ](#_bookmark102))
* [*Select* ](#_bookmark328)

**Description**

The size of a File, Password, Select, or Text element. When working with a Select element, determines the number of rows that will be displayed, regardless of the number of options chosen.

## Sleep() (function)

**Description**

Pause for a specified number of milliseconds.

| **Parameter  Name** | **Description**                                             |
| ------------------------- | ----------------------------------------------------------------- |
| PauseTime                 | An integer value specifying the number of  milliseconds to pause. |

**Syntax** Sleep(PauseTime) **Parameters**

**Example**

To pause for 1 second, write:

Sleep(1000)

**GUI mode**

WebLOAD recommends setting sleep functions within script files directly through the WebLOAD Recorder. Drag the **Sleep ** icon from the General toolbox into the Script Tree at the desired location. The Sleep dialog box opens. Enter or select the duration of the sleep and click **OK**. The Sleep item appears in the Script Tree and the JavaScript code is added to the script.

Sleep function command lines may also be added directly to the code in a JavaScript Object within a script through the IntelliSense Editor, described in [*Using the IntelliSense*](#_bookmark18) [*JavaScript Editor* ](#_bookmark18).

**Comment**

Specify one of the sleep options when running a test script in the Sleep Time Control tab, through the WebLOAD Recorder from the **Tools**  **Default** or **Current Project Options** or through the WebLOAD Console from the **Tools**  **Default** or **Current Project Options**:

* **Sleep time as recorded** – Runs the script with the delays corresponding to the natural pauses that occurred when recording the script.
* **Ignore recorded sleep time (default)** – Eliminates any pauses when running the script and runs a worst-case stress test.
* **Set random sleep time** – Sets the ranges of delays to represent a range of users.
* **Set sleep time deviation** – Sets the percentage of deviation from the recorded value to represent a range of users.

For more information on setting the Sleep Time Control settings, see *Configuring Sleep Time Control Options* in the *WebLOAD Recorder User’s Guide*.

**See also**

* DisableSleep (see [*DisableSleep (property)* ](#disablesleep-property))
* SendCounter() (see [*SendCounter() (function)* ](#_bookmark343))
* SendMeasurement() (see [*SendMeasurement() (function)* ](#sendmeasurement-function))
* SendTimer() (see [*SendTimer() (function)* ](#sendtimer-function))
* SetTimer() (see [*SetTimer() (function)* ](#sendtimer-function))
* SleepDeviation (see [*SleepDeviation (property)* ](#sleepdeviation-property))
* SleepRandomMax (see [*SleepRandomMax (property)* ](#sleeprandommax-property))
* SleepRandomMin (see [*SleepRandomMin (property)* ](#sleeprandommin-property))
* SynchronizationPoint() (see [*SynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark35)
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)

## SleepDeviation (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Integer that indicates the percentage by which recreated sleep periods should deviate from the original recorded time.

**Example**

wlGlobals.SleepDeviation = 10

Recreated sleep periods will be within a range of +- 10% of the original recorded time.

**Comment**

Sleep periods during test sessions are by default kept to the length of the sleep period recorded by the user during the original recording session. If you wish to include sleep intervals but change the time period, set DisableSleep to false and assign values to the other sleep properties as follows:

* SleepRandomMin - Assign random sleep interval lengths, with the minimum time period equal to this property value.
* SleepRandomMax - Assign random sleep interval lengths, with the maximum time period equal to this property value.
* SleepDeviation - Assign random sleep interval lengths, with the time period ranging between this percentage value more or less than the original recorded time period.

**GUI mode**

In WebLOAD Recorder, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Console, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Session Options** dialog box or the **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* DisableSleep (see [*DisableSleep (property)* ](#disablesleep-property))
* Sleep() (see [*Sleep() (function)* ](#sleep-function))
* SleepRandomMax (see [*SleepRandomMax (property)* ](#sleeprandommax-property))
* SleepRandomMin (see [*SleepRandomMin (property)* ](#sleeprandommin-property))

## SleepRandomMax (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Integer that indicates the maximum length of a recreated sleep period when not using the original recorded time.

**Syntax**

`wlGlobals.SleepRandomMax = 5000`

Recreated sleep periods will fall within a range whose maximum value is 5000 milliseconds.

**Comment**

Sleep periods during test sessions are by default kept to the length of the sleep period recorded by the user during the original recording session. If you wish to include sleep intervals but change the time period, set DisableSleep to false and assign values to the other sleep properties as follows:

* SleepRandomMin - Assign random sleep interval lengths, with the minimum time period equal to this property value.
* SleepRandomMax - Assign random sleep interval lengths, with the maximum time period equal to this property value.
* SleepDeviation - Assign random sleep interval lengths, with the time period ranging between this percentage value more or less than the original recorded time period.

**GUI mode**

In WebLOAD Recorder, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Console, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Session Options** dialog box or in the **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* DisableSleep (see [*DisableSleep (property)* ](#disablesleep-property))
* Sleep() (see [*Sleep() (function)* ](#sleep-function))
* SleepDeviation (see [*SleepDeviation (property)* ](#sleepdeviation-property))
* SleepRandomMin (see [*SleepRandomMin (property)* ](#sleeprandommin-property))

## SleepRandomMin (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

Integer that indicates the minimum length of a recreated sleep period when not using the original recorded time.

**Syntax**

`wlGlobals.SleepRandomMin = 1000`

Recreated sleep periods will fall within a range whose minimum value is 1000 milliseconds.

**Comment**

Sleep periods during test sessions are by default kept to the length of the sleep period recorded by the user during the original recording session. If you wish to include sleep intervals but change the time period, set DisableSleep to false and assign values to the other sleep properties as follows:

* SleepRandomMin – Assign random sleep interval lengths, with the minimum time period equal to this property value.
* SleepRandomMax – Assign random sleep interval lengths, with the maximum time period equal to this property value.
* SleepDeviation – Assign random sleep interval lengths, with the time period ranging between this percentage value more or less than the original recorded time period.

**GUI mode**

In WebLOAD Recorder, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

In WebLOAD Console, select the sleep mode in the Sleep Time Control tab of the **Default** or **Current Session Options** dialog box or in the **Script Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* DisableSleep (see [*DisableSleep (property)* ](#disablesleep-property))
* Sleep() (see [*Sleep() (function)* ](#sleep-function))
* SleepDeviation (see [*SleepDeviation (property)* ](#sleepdeviation-property))
* SleepRandomMax (see [*SleepRandomMax (property)* ](#sleeprandommax-property))

## src (property)

**Property of Object**

* Image (see [*Image (object)* ](#_bookmark210))
* script (see [*script (object)* ](#_bookmark323))
* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

Retrieves the complete URL of the parent object, that is the URL to an external file that contains the source code or data for this image, script, or XML DOM object.

**Example** [“www.ABCDEF.com/images/logo.gif](http://www.ABCDEF.com/images/logo.gif)” **See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

## SSLBitLimit (property)

**Property of Object**

* [wlGlobals](#wlglobals-object)

**Description**

WebLOAD provides the option of setting a limit to the maximum SSL bit length available to Virtual Clients when contacting the Server. By default, WebLOAD supports a maximum SSLBitLimit of 128 bits. Users may lower the SSLBitLimit as necessary.

You may assign an SSL bit limit value using the wlGlobals.SSLBitLimit property. Check the value of this property if you wish to verify the maximum cipher strength (SSL bit limit) available for the current test session. For example, if all ciphers are enabled, then the maximum cipher strength is 128.

> **Note:** Defining an SSL bit limit with the SSLBitLimit property is a low-level approach to enabling or disabling individual protocols. Even if you prefer to program property values directly rather than working through the GUI, it is usually preferable to use the SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) to define and enable cipher levels and cryptographic strengths using a higher, more categorical approach.

**Syntax**

`wlGlobals.SSLBitLimit` = IntegerValue

**Example**

`wlGlobals.SSLBitLimit = 56`

-Or-

CurrentBitLimit = wlGlobals.SSLBitLimit

**GUI mode**

WebLOAD recommends setting the SSL bit limit through the WebLOAD Console. Check SSL Bit Limit and select a value from the drop-down list on the SSL tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*SSLDisableCipherName() (function)* ](#_bookmark382))
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function)
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLEnableStrength() (see [*SSLEnableStrength() (function)* ](#_bookmark383))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlHttp](#wlhttp-object)

## SSLCipherSuiteCommand() (function)

**Description**

Set the SSL configuration environment before running a test script.

 **Note:** This property can only be inserted manually.

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSLCipherCommand          | One of the following commands, used to set  the SSL configuration environment before running a test script.`<br>`EnableAll –  Enable all SSL protocols (default)  `<br>`DisableAll –  Disable all SSL protocols  `<br>`ShowAll –  List all SSL protocols (provides internal information for RadView Support Diagnostics)  `<br>`ShowEnabled –  List currently enabled SSL protocols (provides internal information for  RadView Support Diagnostics)  Note that the command name should appear in  quotes. |

**Syntax**

`SSLCipherSuiteCommand(“SSLCipherCommand”)`

**Example**

You may wish to test your application with only a single SSL protocol enabled. The easiest way to do that would be to disable all protocols, and then enable the selected protocol in the InitClient() function.

```javascript
InitClient()

{

… SSLCipherSuiteCommand(“DisableAll”) SSLEnableCipherName(“EXP-RC4-MD5”)

…

}
```

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*SSLDisableCipherName() (function)* ](#_bookmark382))
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## SSLClientCertificateFile, SSLClientCertificatePassword (properties)

**Properties of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

SSL Client certificates offer a more secure method of authenticating users in an Internet commerce scenario then traditional username and password solutions. For servers that support client authentication, the server will request an identification certificate that contains information to identify the client and is signed by a recognized certificate authority. WebLOAD supports use of SSL client certificates by supplying the certificate filename and password to the SSL server. SSLClientCertificateFile and SSLClientCertificatePassword are the filename (optionally including a directory path) and password of a certificate, which WebLOAD makes available to SSL

servers. When the script issues an HTTPS Get, Post, or Head command, the server can request the certificate as part of the handshake procedure. In that case, WebLOAD sends the certificate to the server, and the server can use it to authenticate the client transmission.

You may set client certificate values using the wlGlobals properties.

 **Note:** You can obtain a certificate file by exporting an X.509 certificate from Microsoft Internet Explorer or Netscape Navigator. Then use the WebLOAD Certificate Wizard to convert the certificate to an ASCII (*.pem) format.

**Syntax**

`wlGlobals.*SSLProperty* = “TextString”`

**Example**

`wlGlobals.SSLClientCertificateFile = “c:\\certs\\cert1.pem”`

`wlGlobals.SSLClientCertificatePassword = “topsecret”`

**GUI mode**

WebLOAD by default senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console. Enter user authentication information through the Authentication tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*SSLDisableCipherName() (function)* ](#_bookmark382))
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))

## SSLCryptoStrength (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)

**Description**

Used to define the cryptographic categories to be used in the current test session. The following categories are available:

* “SSL_AllCrypto” – Enable cryptography of all strengths (default).
* “SSL_StrongCryptoOnly” – Enable only ciphers with strong cryptography (RSA keys greater than 512-bit and DES/EC keys greater than 40-bit).
* “SSL_ExportCryptoOnly” – Enable only ciphers available for export, including only RSA keys 512-bit or weaker and DES/EC keys 40-bit or weaker.
* “SSL_ServerGatedCrypto” – Verify that the communicating server is legally authorized to use strong cryptography before using stronger ciphers. Otherwise use export ciphers only.

These definitions work with your script’s current set of enabled ciphers. If you have enabled only certain ciphers, then setting SSLCryptoStrength would affect only the subset of enabled ciphers.

**Example**

Assume you have enabled the following ciphers:

* DHE_DSS_ RC4_SHA
* DES_CBC_MD5
* AECDH_NULL_SHA
* EXP_RC4_MD5

If you then set SSLCryptoStrength to SSL_ExportCryptoOnly, then only the last two ciphers, AECDH_NULL_SHA, and EXP_RC4_MD5, will be enabled.

```javascript
InitClient()

{

?

SSLEnableCipherName(“DHE_DSS_RC4_SHA”) SSLEnableCipherName(“DES_CBC_MD5”) SSLEnableCipherName(“AECDH_NULL_SHA”) SSLEnableCipherName(“EXP_RC4_MD5”) wlGlobals.SSLCryptoStrength=“SSL_ExportCryptoOnly”

?

}
```

**Comment**

Defining a global, categorical value for SSLCryptoStrength is a high-level approach to cryptographic strength definition. This ‘smarter’ approach of selecting appropriate categories is usually preferable to the low-level approach of enabling or disabling individual protocols or defining specific SSL bit limits with the SSLBitLimit and SSLVersion properties. However, ideally SSL configuration values should be set through the WebLOAD GUI.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))

## SSLDisableCipherID() (function)

**Description**

Disables the specified SSL cipher for the current session.

**Syntax**

SSLDisableCipherID(CipherID)

**Parameters**

| **Parameter  Name** | **Description**                               |
| ------------------------- | --------------------------------------------------- |
| CipherID                  | The SSL cipher to disable for the current  session. |

**Example**

You may wish to test your application with all but one SSL protocol enabled. The easiest way to do that would be to disable the selected protocol in the InitClient() function.

```javascript
Initclient()

{

…

SSLDisableCipherID(45)

…

}
```

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

## SSLDisableCipherName() (function)

**Description**

Disables the specified SSL cipher for the current session.

**Syntax**

SSLDisableCipherName(CipherName)

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CipherName                | Any of the SSL protocol  names. See[*WebLOAD-supported SSL*](#_bookmark578) [*Protocol Versions* ](#_bookmark578) for a complete list of  protocol names. |

**Example**

You may wish to test your application with all but one SSL protocol enabled. The easiest way to do that would be to disable the selected protocol in the InitClient() function.

```javascript
InitClient()

{

…

SSLDisableCipherName("EXP-RC4-MD5")

…

}
```

**See also**

* *Browser Configuration Components* 
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

## SSLEnableStrength() (function)

**Description**

Enables all ciphers which have encryption strength not greater than specified by the parameter. Function allows you to limit SSL key length without iterating over the whole ciphers list.

**Syntax**

SSLEnableStrength(MaxStrength)

 **Parameters**

| **Parameter  Name** | **Description**                                                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| MaxStrength               | The maximum encryption  strength allowed. Strength must be specified in bits (typical values are 40,  56, 96, 128, 168, 196, 256,  512, 1024, etc.). |

**Example**

Your test session may include a variety of function calls related to specific set of SSL ciphers. For example, you may wish to test your application with weak ciphers only.

The following InitAgenda() function fragment enables all protocols with encryption strength less or equal to 128 bits.

```javvvvvvvvvvvvvvvvvvv
InitAgenda()

{

…

SSLEnableStrength(128)

…

}
```

**See also**

* SSLBitLimit (see "[*SSLBitLimit (property)*](#_bookmark373)" ) (wlGlobals only)
* *SSL Cipher Command Suite* 
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see "[*SSLCipherSuiteCommand() (function)*](#sslciphersuitecommand-function)" )
* SSLClientCertificateFile, SSLClientCertificatePassword (see "[*SSLClientCertificateFile, SSLClientCertificatePassword (properties)*](#sslclientcertificatefile-sslclientcertificatepassword-properties)" )
* SSLCryptoStrength (see "[*SSLCryptoStrength (property)*](#_bookmark379)" ) (wlGlobals only)
* SSLDisableCipherID() (see "[*SSLDisableCipherID() (function)*](#_bookmark381)" )
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherName() (see "[*SSLEnableCipherName() (function)*](#_bookmark386)" )
* SSLGetCipherCount() (see "[*SSLGetCipherCount() (function)*](#sslgetciphercount-function)" )
* SSLGetCipherID() (see "[*SSLGetCipherID() (function)*](#sslgetcipherid-function)" )
* SSLGetCipherInfo() (see "[*SSLGetCipherInfo() (function)*](#sslgetcipherinfo-function)" on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see "[*SSLGetCipherName() (function)*](#sslgetciphername-function)" )
* SSLGetCipherStrength() (see "[*SSLGetCipherStrength() (function)*](#sslgetcipherstrength-function)" )
* SSLUseCache (see "[*SSLUseCache (property)*](#sslusecache-property)" )
* SSLVersion (see "[*SSLVersion (property)*](#_bookmark400)" )
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

## SSLEnableCipherID() (function)

**

**Syntax** SSLEnableCipherID(CipherID)

**Parameters**

**Example**

Your test session may include a variety of function calls related to specific protocols. For example, you may wish to test your application with only a single SSL protocol enabled. Unfortunately, protocol names can be long and awkward. To simplify your script code, you could get the ID number of a selected protocol and refer to the selected protocol by ID number for the remainder of the script. The following InitClient() function fragment disables all protocols, gets a protocol ID number, and enables the selected protocol in the InitClient() function.

```
InitClient()

{

…

SSLCipherSuiteCommand(DisableAll) MyCipherID = SSLGetCipherID("EXP-RC4-MD5") SSLEnableCipherID(MyCipherID)

…

}
```

**See also**

* *Browser Configuration Components* 
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)* ](#_bookmark382))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

## SSLEnableCipherName() (function)

**Description**

Enables the specified SSL cipher for the current session.

**Syntax** SSLEnableCipherName(CipherName)

**Parameters**

**Example**

You may wish to test your application with only a single SSL protocol enabled. The easiest way to do that would be to disable all protocols, and then enable the selected protocol in the InitAgenda() function:

InitAgenda()

```javascript
{

…

SSLCipherSuiteCommand(DisableAll)

SSLEnableCipherName("EXP-RC4-MD5")

…

}
```

**See also**

* [*Browser Configuration Components* ](./using_javascript_ref.md#browser-configuration-components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals

only)

* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)* ](#_bookmark382))
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))

## SSLGetCipherCount() (function)

**Description**

Returns an integer, the number of ciphers enabled for the current test session. While that may seem obvious if your script explicitly enables two or three ciphers, it may be necessary if, for example, you have set a cipher strength limit of 40 and then wish to know how many ciphers are currently available at that limit.

**Syntax**

`SSLGetCipherCount()`

**Return Value**

Returns an integer representing the number of ciphers enabled for the current test session.

**Example**

`CurrentCipherCount = SSLGetCipherCount()`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* [wlHttp](#wlhttp-object)

## SSLGetCipherID() (function)

**Description**

Returns the ID number associated with the specified cipher.

**Syntax**

SSLGetCipherID(CipherName)

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CipherName                | Any of the SSL protocol  names. See[*WebLOAD-supported SSL*](#_bookmark578) [*Protocol Versions* ](#_bookmark578) for a complete list of  protocol names. |

**Return Value**

Returns the ID number associated with the specified cipher.

**Example**

`MyCipherID = SSLGetCipherID(“EXP-RC4-MD5”)`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## SSLGetCipherInfo() (function)

**Description**

Prints a message on the WebLOAD Console with information about the specified SSL protocol.

**Syntax**

SSLGetCipherInfo(CipherName  CipherID)

**Parameters**

Accepts either one of the following parameters:

| **Parameter  Name** | **Description**                         |
| ------------------------- | --------------------------------------------- |
| CipherName                | The name of the SSL cipher.                   |
| CipherID                  | The identification number of the SSL  cipher. |

**Example**

You may specify an SSL protocol using either the protocol name or the ID number. The function accepts either a string or an integer parameter, as illustrated here:

`SSLGetCipherInfo(“EXP-RC4-MD5”)`

-Or-

`SSLGetCipherInfo(2)`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

## SSLGetCipherName() (function)

**Description**

Returns the name of the cipher associated with the specified ID number.


**Syntax** SSLGetCipherName(CipherID)

**Parameters**

| **Parameter  Name** | **Description**               |
| ------------------------- | ----------------------------------- |
| CipherID                  | Any of the SSL protocol ID numbers. |

**Return Value**

Returns the name of the cipher associated with the specified ID number.

**Example**

`MyCipherName = SSLGetCipherName(16)`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## SSLGetCipherStrength() (function)

**Description**

Returns an integer, the maximum cipher strength (SSL bit limit) available for the current test session. For example, if all ciphers are enabled, then the maximum cipher strength is 128.

**Syntax**

SSLGetCipherStrength()

 **Return Value**

Returns an integer representing the maximum available cipher strength for the current session.

**Example**

`CurrentCipherStrength = SSLGetCipherStrength()`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

## SSLUseCache (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Enable caching of SSL decoding keys received from an SSL (HTTPS) server. The value of SSLUseCache may be:

* **false** – Disable caching.
* **true** – Enable caching. (default)

A true value means that WebLOAD receives the key only on the first SSL connection in each round. In subsequent connections, WebLOAD retrieves the key from the cache.

Assign a true value to reduce transmission time during SSL communication. Assign a false value if you want to measure the transmission time of the decoding key in the WebLOAD performance statistics for each SSL connection.

If you enable caching, you can clear the cache at any time by calling the wlHttp.ClearSSLCache() method. The cache is automatically cleared at the end of each round.

**GUI mode**

WebLOAD recommends enabling or disabling the SSL cache through the WebLOAD Console. Enable caching for the Load Generator or for the Probing Client during a test session by checking the appropriate box in the Browser Parameters tab of the **Default Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Comment**

To clear the SSL cache, set the ClearSSLCache() (see [*ClearSSLCache() (method)* ](#_bookmark59)) property.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLVersion (see [*SSLVersion (property)* ](#_bookmark400))

## SSLVersion (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The SSL version that WebLOAD should use for the current test session. The possible values of wlGlobals.SSLVersion are:

* SSL_Version_Undetermined – (Default) WebLOAD can use any SSL protocol version, allowing the broadest interoperability with other SSL installations.  
**Note:** WebLOAD does not recommend changing the default value.

* TLS_Version_1_0_Only
* TLS_Version_1_0
* TLS_Version_1_1_Only
* TLS_Version_1_1
* TLS_Version_1_2_Only
* TLS_Version_1_2
* TLS_Version_1_3_Only
* TLS_Version_1_3

Deprecated versions not supported anymore:

* SSL_Version_3_0_With_2_0_Hello
* SSL_Version_2_0
* SSL_Version_3_0
* SSL_Version_3_0_Only
* TLS_Version_1.0_With_2_0_Hello


To connect to a server using any of the SSL options, include https:// in the URL.

**Example**

```
wlGlobals.SSLVersion = “SSL_Version_3_0_Only”

wlHttp.Get("https://www.ABCDEF.com")
```

See [*WebLOAD-supported SSL Protocol Versions* ](#_bookmark578) for a table illustrating all the Client/Server SSL version handshake combination possibilities and a complete list of SSL/TLS protocol names.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SSLBitLimit (see [*SSLBitLimit (property)* ](#_bookmark373)) (wlGlobals only)
* [*SSL Cipher Command Suite* ](./using_javascript_ref.md#ssl-cipher-command-suite)
* [*SSL Ciphers – Complete List* ](#_bookmark580)
* SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](#sslciphersuitecommand-function))
* SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile,*](#sslclientcertificatefile-sslclientcertificatepassword-properties)[ *SSLClientCertificatePassword (properties)* ](#sslclientcertificatefile-sslclientcertificatepassword-properties))
* SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](#_bookmark379)) (wlGlobals only)
* SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](#_bookmark381))
* SSLDisableCipherName() (see [*S*](#_bookmark382)[*SLDisableCipherName() (function)*](#_bookmark382) )
* SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](#_bookmark385))
* SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](#_bookmark386))
* SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](#sslgetciphercount-function))
* SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](#sslgetcipherid-function))
* SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](#sslgetcipherinfo-function)on page [269](#sslgetcipherinfo-function))
* SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](#sslgetciphername-function))
* SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](#sslgetcipherstrength-function))
* SSLUseCache (see [*SSLUseCache (property)* ](#sslusecache-property))

## StopClient () (function)

**Description**

Stops the execution of the Virtual Client running the script from which StopClient() was called. After StopClient() is called, this client cannot be resumed.

**Syntax**

StopClient ([SeverityLevel], [Reason])

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SeverityLevel            | Optionally, specify the  severity level of the error that occurred. The possible values are:`<br>`WLMinorError. The message is displayed  as a warning message.  `<br>`WLError. The  message is displayed as an error message. If no severity level is specified, WLMinorError is assumed.  **Note:** Error levels are used for display  in the log window and do not define any logical behavior. |
| Reason                   | An optional string containing the reason  for stopping the virtual client running the script.  If no reason is specified, a default message is  displayed. See[*Default   Message* ](#_bookmark402)below.                                                                                                                                                                                                     |

**Default Message**

The following default message is displayed when no reason is specified:

StopClient(WLError, “Client”+%d+”was terminated by a user command in

the script”)

where %d is a parameter that takes the number of the client that was terminated. For example, “Client 38 was terminated by a user command in the script”.

**Examples**

`StopClient(WLError, “Error occurred when running script, client terminated”)`

`StopClient(, “Error occurred when running script, client terminated”)`

`StopClient(WLError)`

## StopGenerator () (function)

**Description**

Stop the script from within the script. The string passed as a parameter is the message that appears when the script is stopped.

**Syntax**

StopGenerator(string)

**Parameters**

| **Parameter Name** | **Description**                                    |
| ------------------------ | -------------------------------------------------------- |
| String                   | The message to be displayed when the script is  stopped. |

**Example**

`StopGenerator(“The script was terminated from within the script”)`

## string (property)

**Property of Object**

* title (see [*title (property)* ](#_bookmark415))

**Description**

Stores the document title in a text string.

## SynchronizationPoint() (function)

**Description**

WebLOAD provides Synchronization Points to coordinate the actions of multiple Virtual Clients. A Synchronization Point is a meeting place where Virtual Clients wait before continuing with a script. When one Virtual Client arrives at a Synchronization Point, WebLOAD holds the Client at the point until all the other Virtual Clients arrive. When all the Virtual Clients have arrived, they are all released at once to perform the next action in the script simultaneously. For more information on Synchronization Points, see *Working with Synchronization Points* in the *WebLOAD Scripting Guide*.

**Syntax**

SynchronizationPoint([timeout])

**Parameters**

**Return Value**

SynchronizationPoint() functions return one of the following values. These values may be checked during the script runtime.

* WLSuccess – Synchronization succeeded. All Virtual Clients arrived at the Synchronization Point and were released together.
* WLLoadChanged – Synchronization failed. A change in the Load Size was detected while Virtual Clients were being held at the Synchronization Point. All Virtual clients were released.
* WLTimeout – Synchronization failed. The timeout expired before all Virtual Clients arrived at the Synchronization Point. All Virtual Clients were released.
* WLError – Synchronization failed. Invalid timeout value. All Virtual Clients were released.

**Example**

The following script fragment illustrates a typical use of synchronization points. To test a Web application with all the Virtual Clients performing a particular Post operation simultaneously, add a Synchronization Point as follows. The various return values are highlighted:

```javascript
wlHttp.Get(“url”)

…

SP = SynchronizationPoint(10000) if (SP == **WLLoadChanged**)

{

InfoMessage(“Syncronization failed, Load Size changed”) InfoMessage(“SP = “ + SP.toString() + “ “ + ClientNum)

}

if (SP == **WLTimeout**)

{

InfoMessage(“Syncronization failed, Timeout expired”) InfoMessage(“SP = “ + SP.toString() + “ “ + ClientNum)

}

if (SP == **WLError**)

{

InfoMessage(“Syncronization failed”)

InfoMessage(“SP = “ + SP.toString() + “ “ + ClientNum)

}

if (SP == **WLSuccess**)

{

InfoMessage(“Synchronization succeeded”) InfoMessage(“SP = “ + SP.toString() + “ “+ ClientNum)

}

wlHttp.Post(url)
```

**GUI mode**

WebLOAD recommends setting synchronization functions within script files directly through the WebLOAD Recorder. Drag the **Synchronization Point**  icon from the Load toolbox into the Script Tree directly before the action you want all Virtual Clients to perform simultaneously. The **Synchronization Point** dialog box opens. Enter or select a timeout value for the Synchronization Point and click **OK**. The **Synchronization Point** item appears in the Script Tree and the JavaScript code is added to the script. The JavaScript code line that corresponds to the Synchronization Point in the Script Tree appears in the JavaScript View.

**Comment**

If there is a change in the Load Size (scheduled or unscheduled) or if any WebLOAD component is paused or stopped during the test session, all Synchronization Points are disabled.

Only client threads running within a single spawned process, on the same Load Generator, are able to share user-defined global variables and synchronization points. So if, for example, you have spawning set to 100 and you are running a total of 300 threads, realize that you are actually running three spawned processes on three separate Load Generators. You will therefore only be able to synchronize 100 client threads at a time, and not all 300.

**See also**

* SendCounter() (see [*SendCounter() (function)* ](#_bookmark343))
* SendMeasurement() (see [*SendMeasurement() (function)* ](#sendmeasurement-function))
* SendTimer() (see [*SendTimer() (function)* ](#_bookmark348))
* SetTimer() (see [*SetTimer() (function)* ](#sendtimer-function))
* Sleep() (see [*Sleep() (function)* ](#sleep-function))
* SynchronizationPoint() (see [*SynchronizationPoint() (function)* ](#_bookmark404))
* [*Timing Functions* ](#_bookmark35)

## tagName (property)

**Property of Object**

* cell (see [*cell (object)* ](#_bookmark49))

**Description**

A string containing the cell type, either `<TD>` or `<TH>`.

**Syntax**

Use the following syntax to check a particular table cell type:

document.wlTables.myTable.cells[*index*#].tagName

**Comment**

The tagName property is a member of the wlTables family of table, row, and cell objects.

**See also**

* cell
* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)
*


* 

* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* row (see [*row (object)* ](#_bookmark315)) (wlTables property)
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* wlTables (see [*wlTables (object)* ](#_bookmark493))

## target (property)

**Property of Object**

* form (see [*form (object)* ](##form-object))
* link (see [*link (object)* ](#_bookmark235))

**Description**

The name of the window or frame into which the form or link should be downloaded (read-only string).

**Example**

In the following code fragment:

`<A HREF=“newpage.htm” TARGET=“_top”> Go to New Page.`

`</A>`

The target property would equal “_top” and the link will load the page into the top frame of the current frameset.

**Comment**

While link and location objects share most of their properties, the target

property is used by the link object only and is not accessed by the location object.

The form.target and link.target properties identify the most recent, immediate location of the target frame using the name string or keyword that was assigned to that frame. Compare this to the wlHttp.wlTarget property of a transaction, which uses the WebLOAD shorthand notation, described in the *WebLOAD Scripting Guide*, to store the complete path of the frame, from the root window of the Web page. The last field of the wlHttp.wlTarget string is the target name stored in the form.target and link.target properties.

**See also**

* wlTarget (see [*wlTarget (property)* ](#_bookmark494))

## Text (function)

**Description**

Verify the absence or presence of a specified text expression within the Web server response.

**Syntax**

wlVerification.Text(searchOption, text, severity)

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| searchOption              | Possible values are: WLFind or WLNotFind.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| text                      | String text to find in the  document.wlSource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| severity                  | Possible values of this parameter are:`<br>`WLSuccess. The transaction  terminated successfully.  `<br>`WLMinorError. This specific  transaction failed, but the test session may continue as usual. The script  displays a warning message in the Log window and continues execution from the next statement.  `<br>`WLError. This specific  transaction failed and the current test  round was aborted. The script displays an error message in the Log window and  begins a new round.  `<br>`WLSevereError. This specific  transaction failed and the test  session must be stopped completely. The script displays an error message in  the Log window and the Load Generator on  which the  error occurred is stopped. |

**Example**

The following code verifies that the server response does not contain the word "error". In case of failure, WebLOAD displays the error message and stops the execution.

`wlVerification.Text(WLNotFind, "error", WLError);`

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))
* Title (see [*Title (function)* ](#_bookmark417))



## ThreadNum() (property)

**Description**

Assigns a unique number to a process based on the client/Load Generator/script. This number is unique across the script’s slave processes and is saved in the ClientNum property. Each client in a Load Generator is assigned a unique number. However, two clients in two different Load Generators may have the same number.

 **Note:** While ClientNum is unique within a single Load Generator, it is not unique system wide. Use VCUniqueID() (see [*VCUniqueID() (function)* ](#_bookmark432)) to obtain an ID number which is unique system-wide.

If there are N clients in a Load Generator, the clients are numbered 0, 1, 2, ..., N-1. You can access ClientNum anywhere in the local context of the script

(InitClient(), main script, TerminateClient(), etc.). ClientNum does not exist in the global context (InitAgenda(), TerminateAgenda(), etc.).

If you mix scripts within a single Load Generator, instances of two or more scripts may run simultaneously on each client. Instances on the same client have the same ClientNum value.

ClientNum reports only the main client number. It does not report any extra threads spawned by a client to download nested images and frames (see [*LoadGeneratorThreads*](#_bookmark241) [*(property)* ](#_bookmark241)).

**Comment**

Earlier versions of WebLOAD referred to this value as ThreadNum. The variable name

ThreadNum will still be recognized for backward compatibility.

**Example**

InfoMessage(“ThreadNum: “ + ThreadNum())

**See also**

* VCUniqueID (see [*VCUniqueID() (function)* ](#_bookmark433))



## TimeoutSeverity (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

When conducting Page Verification tests, TimeoutSeverity stores the error level to be triggered if the full set of verification tests requested for the current page are not completed within the specified time limit.

**GUI mode**

WebLOAD recommends setting page verification severity levels through the WebLOAD Console. Check Verification in the Page Time area and select an error severity level from the drop-down box in the Functional Testing tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also assign a severity level using the TimeoutSeverity property.

wlGlobals.TimeoutSeverity = ErrorFlag

The following error codes are available:

* WLSuccess – The transaction terminated successfully.
* WLMinorError – This specific transaction failed, but the test session may continue as usual. The script displays a warning message in the Log window and continues execution from the next statement.
* WLError – This specific transaction failed and the current test round was aborted. The script displays an error message in the Log window and begins a new round.
* WLSevereError – This specific transaction failed and the test session must be stopped completely. The script displays an error message in the Log window and the Load Generator on which the error occurred is stopped.

**Example**

wlGlobals.TimeoutSeverity = WLError.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* [*Transaction Verification Components* ](#_bookmark39)
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))



## title (property)

**Property of Objects**

* document (see [*document (object)* ](#_bookmark100))
* element (see [*element (object)* ](#_bookmark102))
* frames (see [*frames (object)* ](#frames-object))
* Image (see [*Image (object)* ](#_bookmark210))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* script (see [*script (object)* ](#_bookmark323))

**Description**

Stores the title value associated with the parent object.

When working with document objects, a title property is an object that contains the document title, stored as a text string. When working with window objects, the title is extracted from the document inside the window. title objects are local to a single thread. You cannot create new title objects using the JavaScript new operator, but you can access a document title through the properties and methods of the standard DOM objects. The properties of title are read-only.

When working with element, link, or location objects, a title property contains the title of the parent Button, Checkbox, Reset, or Submit element or link object. May be used as a tooltip string. When working with document objects, a title property is an object that contains the document title, stored as a text string. When working with window objects, the title is extracted from the document inside the window.

**Syntax**

**Document object:**

Access the title’s properties directly using the following syntax:

document.title.`<titleproperty>`

**Example**

**Document object:**

CurrentDocumentTitle = document.title.string

**Properties**

**Document object:**

* string (see [*string (property)* ](#_bookmark405))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* form (see [*form (object)* ](##form-object))
* [*Select* ](#_bookmark329)



## Title (function)

**Method of Object**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))

**Description**

This function enables you to validate a HTML Web page’s title.

**Syntax**

wlVerification.Title(`<ExpectedTitle>`, `<Severity>`\`<FunctionName>` [, `<ErrorMessage>`\`<FunctionArguments>`])

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ExpectedTitle             | A user-supplied string  that identifies the expected title of the HTML Web page. If the string you  enter in this parameter appears in the HTML Web page’s title, the validation  is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Severity                  | Possible values of this parameter are:`<br>`WLSuccess. The transaction  terminated successfully.  `<br>`WLMinorError. This specific  transaction failed, but the test session may continue as usual. The script  displays a warning message in the Log window and continues execution from the next statement.  `<br>`WLError. This specific  transaction failed and the current test  round was aborted. The script displays an error message in the Log window and  begins a new round.  `<br>`WLSevereError. This specific  transaction failed and the test  session must be stopped completely. The script displays an error message in  the Log window and the Load Generator on  which the  error occurred is stopped. |
| FunctionName              | A pre-defined Javascript  function that is called if the verification fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ErrorMessage]            | string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [FunctionArguments]       | The arguments for the  function that is called if the verification fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Example**

For example: when validation fails, an email is sent with a message (errorMessage).

The function sendEmailOnError has the arguments emailAddress and

errorMessage.

```javascript
function sendEmailOnError(emailAddress, errorMessage)

{

sendEmailTo(emailAddress, errorMessage)

}
```

When Title validation fails. The following function is called:

[sendEmailOnError(VP@rrrr.com, ](mailto:sendEmailOnError(VP@rrrr.com)"Title validation failed");

So the Title function syntax is as follows:

wlVerification.Title("compare title", sendEmailOnError, [VP@rrrr.com,](mailto:VP@rrrr.com) "Title validation failed");

**See also**

* wlVerification (see [*wlVerification (object)* ](#_bookmark497))
* PageContentLength (see [*PageContentLength (property)* ](#_bookmark270))
* PageTime (see [*PageTime (property)* ](#_bookmark271))
* Severity (see [*Severity (property)* ](#_bookmark360))
* Function (see [*Function (property)* ](#_bookmark130))
* ErrorMessage (see [*ErrorMessage (property)* ](#_bookmark116))



## TransactionTime (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)

**Description**

Assign a timeout value using the TransactionTime property. Use the TransactionTime property to set a timeout limit for verification on the maximum transaction time.

**GUI mode**

WebLOAD recommends setting page verification timeout values through the WebLOAD Console. Check Page Verification and enter a maximum number of seconds in the Functional Testing tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also assign a timeout value using the TransactionTime property.

`wlGlobals.TransactionTime = TimeValue`

**Example**

The value assigned to TransactionTime may be written in either string or integer format, where the integer represents the number of milliseconds to wait and the string represents the decimal fraction of a whole second. Therefore, the following two lines are equivalent, both setting TransactionTime to one millisecond:

wlGlobals.TransactionTime = 1

-Or-

wlGlobals.TransactionTime = “0.001”

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* [*Transaction Verification Components* ](#_bookmark39)
* VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)*](#_bookmark434)[ *(function)* ](#_bookmark434))

## type (property)

**Property of Objects**

* element (see [*element (object)* ](#_bookmark102))
* form (see [*form (object)* ](##form-object))
* [wlHttp](#wlhttp-object)
* wlHttp.Data (see [*Data (property)* ](#data-property))
* wlHttp.DataFile (see [*DataFile (property)* ](#datafile-property))

**Description**

This property is a string that holds the ‘type’ of the parent object.

If the parent is a form element object, then type holds the HTML type attribute of the form element. For example, an `<INPUT>` element can have a type of “TEXT”, “CHECKBOX”, or “RADIO”. Certain HTML form elements, such as `<SELECT>` do not have a type attribute. In that case, element.type is the element tag itself, for example “SELECT”.

 **Note:** The Type value *does not* change. Even when working with dynamic HTML, the type of a specific object remains the same through all subsequent transactions with that object.

If the parent is a wlHttp.Data or wlHttp.DataFile object, then Type holds the MIME type of the string or form data being submitted through an HTTP Post command.

**Syntax**

element:

When working with element objects, use the lowercase form:

`<NA>`

wlHttp.Data:

When working with wlHttp.Data objects, use the uppercase form:

wlHttp.Data.Type = “application/x-www-form-urlencoded”

**Comment**

The Type property for wlHttp.Data and wlHttp.DataFile objects is written in uppercase.

**See also**

* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Post() (see [*Post() (method)* ](#_bookmark290))
* value (see [*value (property)* ](#value-property))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))
* [wlHttp](#wlhttp-object)

## Url (property)

**Property of Objects**

* element (see [*element (object)* ](#_bookmark102))
* form (see [*form (object)* ](##form-object))
* frames (see [*frames (object)* ](#frames-object))
* Image (see [*Image (object)* ](#_bookmark210))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* [wlHttp](#wlhttp-object)

**Description**

Sets or retrieves the URL of the parent object on the Web page (read-only). If the parent object is of type `<IMG>`, then this property holds the URL of the image element.

If the parent object is wlGlobals, this property holds the URL address to which the

wlGlobals object connects.

If the parent object is wlMetas, then if httpEquiv=“REFRESH” and the content property holds a URL, then the URL is extracted and stored in a link object (read- only).

**Example**

**Area, element, form, frame, image, link, location:**

`<NA>`

**wlGlobals**:

wlGlobals.Url = [“http://www.ABCDEF.com](http://www.ABCDEF.com/)”

**wlMetas**:

When working with wlMetas objects, use the all-uppercase caps form:

CurrentLink = document.wlMetas[0].URL

**Comment**

The URL property for area, element, form, frame, image, link, location, and

wlMetas objects is written in all-uppercase caps.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* content (see [*content (property)* ](#_bookmark68))
* httpEquiv (see [*httpEquiv (property)* ](#_bookmark204))
* Name (see [*Name (property)* ](#_bookmark253))
* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)
* wlMetas (see [*w*](#_bookmark471)[*lMetas (object)* ](#_bookmark471))

## UserAgent (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

A user agent is the client application used with a particular network protocol. The phrase, “user agent” is most commonly used in reference to applications that access the World Wide Web. Web user agents range from web browsers to search engine crawlers (“spiders”), as well as mobile phones, etc. The user agent string can be sent as part of the HTTP request, prefixed with User-agent: or User-Agent:. This string typically includes information such as the application name, version, host, host operating system, and language. Some examples of user agent strings can be found at:

http://en.wikipedia.org/wiki/User_agent#Example_user-agent_strings

The UserAgent property is used to define the user agent string for the scope of the WebLOAD object with which it is associated.

**GUI mode**

WebLOAD recommends setting user agent values through the WebLOAD Console. Select a browser type and user agent through the Browser Parameters tab of the **Default** or **Current Project Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## UserName (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The user name that the script uses to log onto a restricted HTTP site. WebLOAD automatically uses the appropriate access protocol. For example, if a site expects clients

to use the NT Authentication protocol, the appropriate user name and password will be stored and sent accordingly.

**GUI mode**

WebLOAD by default senses the appropriate authentication configuration settings for the current test session.

If you prefer to explicitly set authentication values, WebLOAD recommends setting user authentication values through the WebLOAD Console. Enter user authentication information through the Authentication tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

**Syntax**

You may also set user values using the wlGlobals properties. WebLOAD automatically sends the user name and password when a wlHttp object connects to an HTTP site. For example:

wlGlobals.UserName = “Bill”

wlGlobals.PassWord = “TopSecret”

**Comments**

A user is only authenticated once during a round with a set of credentials. Each subsequent request will use these credentials regardless of what is contained in the script. If the value of these credentials are changed after authentication, they will only be used during the next round, not during the current round.

For example, if you are trying to send a request to a URL with a group of users (user1, user2, and user3), but user1 has already been authenticated, the login is always performed for user1 until the round is complete.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* NTUserName, NTPassWord (see [*NTUserName, NTPassWord (properties)* ](#_bookmark255))

## UseSameProxyForSSL (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

The UseSameProxyForSSL property can have one of the following values:

* **false** (default value) – The engine uses the Proxy, ProxyUserName, ProxyPassWord, ProxyNTUserName, and ProxyNTPassWord properties for both SSL and non-SSL traffic.
* **true** – The engine uses the Proxy, ProxyUserName, ProxyPassWord, ProxyNTUserName, and ProxyNTPassWord properties for non-SSL traffic and the HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord, HttpsProxyNTUserName, and HttpsNTPassWord properties for SSL traffic.

This property is used when you are working with a separate SSL proxy.

 **Note:** This property can only be inserted manually.

**Example** wlGlobals.UseSameProxyForSSL = false **See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* *Security* in the *WebLOAD Scripting Guide*
* HttpsProxy, HttpsProxyUserName, HttpsProxyPassWord (see [*HttpsProxy,*](#httpsproxy-httpsproxyusername-httpsproxypassword-properties))
* HttpsProxyNTUserName, HttpsProxyNTPassWord (see [*HttpsProxyNTUserName, HttpsProxyNTPassWord (properties)*](#proxy-proxyusername-proxypassword-properties))



## UsingTimer (property)

**Property of Object**

* [wlHttp](#wlhttp-object)

**Description**

The name of a timer to use for the Get() or Post() method.

**Example**

WebLOAD zeros the timer immediately before a Get() or Post() call and sends the timer value to the WebLOAD Console immediately after the call. This is equivalent to calling the SetTimer() and SendTimer() functions. Thus the following two code examples are equivalent:

//**Version 1**

`wlHttp.UsingTimer = “Timer1”`

`wlHttp.Get(“http://www.ABCDEF.com](http://www.ABCDEF.com/)”)`

//**Version 2**

`SetTimer(“Timer1”) [wlHttp.Get(“http://www.ABCDEF.com](http://www.ABCDEF.com/)”)` 

`SendTimer(“Timer1”)`

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* SendTimer() (see [*SendTimer() (function)* ](#_bookmark348))
* SetTimer() (see [*SetTimer() (function)* ](#sendtimer-function))



## value (property)

**Property of Objects**

* element (see [*element (object)* ](#_bookmark102))
* option (see [*option (object)* ](#_bookmark264))
* wlHeaders (see [*wlHeaders (object)* ](#_bookmark462))
* wlHttp.Data (see [*Data (property)* ](#data-property))
* wlHttp.Header (see [*Header (property)* ](#header-property))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))

**Description**

Sets and retrieves the value associated with the parent object.

When working with elements or options, this property holds the text associated with this object. This is the value that is returned to the server when a FORM control of type Button, Checkbox, Radiobutton, Reset, or Submit is submitted. Thus the value property holds the HTML value attribute of the object (the `<OPTION>` element). If the element does not have a value attribute, WebLOAD sets the value property equal to the text property.

When working with wlHeaders or wlSearchPairs objects, this property holds the value of the search key.

When working with wlHttp.Data or wlHttp.Header objects, this property holds the value of the data string being submitted through an HTTP Post command.

**Syntax**

**For elements and options:**

`<NA>`

**For wlHeaders:**

`document.wlHeaders[*index#*].value = “TextString”`

For example:

`document.wlHeaders[0].value = “Netscape-Enterprise/3.0F”`

**For wlSearchPairs:**

`document.links[1].wlSearchPairs[*index#*].value = “TextString”`

For example:

`document.links[1].wlSearchPairs[0].value = “OpticsResearch”`

**For wlHttp.Header:**

`wlHttp.Header[“value”] = “TextString”`

**For wlHttp.Data:**

When working with wlHttp.Data objects, use the uppercase form:

`wlHttp.Data.Value = “SearchFor=icebergs&SearchType=ExactTerm”`

**Comment**

The Value property for element and wlHttp.Data objects is written in uppercase.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* element (see [*element (object)* ](#_bookmark102))
* Erase (see [*Erase (property)* ](#erase-property))
* FileName (see [*FileName (property)* ](#filename-property))
* form (see [*form (object)* ](##form-object))
* FormData (see [*FormData (property)* ](#formdata-property))
* Get() (see [*Get() (transaction method)* ](#_bookmark136))
* Header (see [*Header (property)* ](#header-property))
* Image (see [*Image (object)* ](#_bookmark210))
* key (see [*key (property)* ](#_bookmark229))
* option (see [*option (object)* ](#_bookmark264))
* Post() (see [*Post() (method)* ](#_bookmark290))
* [*Select* ](#_bookmark329)
* type (see [*type (property)* ](#type-property))
* value (see [*value (property)* ](#value-property))
* wlClear() (see [*wlClear() (method)* ](#_bookmark440))
* wlHeaders (see [*wlHeaders (object)* ](#_bookmark462))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))



## VCUniqueID() (function)

**Description**

VCUniqueID() provides a unique identification for the current Virtual Client instance which is unique system-wide, across multiple Load Generators, even with multiple spawned processes running simultaneously. Compare this to ClientNum. which provides an identification number that is only unique within a single Load Generator. The identification string is composed of a concatenation of the script name, Load Generator name, current thread number, and round number.

**Syntax** 

VCUniqueID() 



**Return Value**

Returns a unique identification string for the current Virtual Client instance.

**Example**

InfoMessage(VCUniqueID())

The results are

[j@chaimsh.0.1](mailto:j@chaimsh.0.1)

where:

* j is the name of the script.
* chaimsh is the name of the Load Generator.
* 0 is the client number.
* 1 is the round number.

**See also**

* GeneratorName() (see [*GeneratorName() (function)* ](#generatorname-function))
* GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](#_bookmark176))
* [*Identification Variables and Functions* ](#_bookmark28)
* RoundNum (see [*RoundNum (variable)* ](#_bookmark314))

## VerificationFunction() (user-defined) (function)

**Description**

User-defined verification function to be used with a ‘named’ transaction. A function written by the user, tailored to the specific testing and verification needs of the application being tested.

**Syntax**

UserDefinedVerificationFunction(specified by user)

```
{

…

`<any valid JavaScript code>` return value

}
```

**Parameters**

Specified by user.

**Return Value**

The user-defined Verification() function returns a value based on user-specified criterion. You define the success and failure criterion for user-defined transactions. You also determine the severity level of any failures. The severity level determines the execution path when the main script resumes control. Less severe failures may be noted and ignored. More severe failures may cause the whole test to be aborted.

Set the severity level in the verification function return statement. All failures are logged and displayed in the Log Window, similar to any other WebLOAD test failure. Refer to the *WebLOAD Console User’s Guide* for more information on return values and error codes. Transactions may be assigned one of the following return values:

* WLSuccess – The transaction terminated successfully.
* WLMinorError – This specific transaction failed, but the test session may continue as usual. The script displays a warning message in the Log window and continues execution from the next statement.
* WLError – This specific transaction failed and the current test round was aborted. The script displays an error message in the Log window. If you are working with

WebLOAD, a new round is begun only if WebLOAD is configured for multiple iterations.

* WLSevereError – This specific transaction failed and the test session must be stopped completely. The script displays an error message in the Log window. If you are working with WebLOAD Recorder, the test session is stopped. If you are working with WebLOAD, the Load Generator on which the error occurred is stopped.

The default return value is WLSuccess. If no other return value is specified for the transaction, the default assumption is that the transaction terminated successfully.

**Example**

The following sample verification function checks if the current title of the Web

page matches the page title expected at this point. (In this case, the function looks for a match with a Google page.)

```
function Transaction1_VerificationFunction()

{

InfoMessage(document.title) if(document.title.indexOf(“Google”)>0)

return WLSuccess else

return WLMinorError

}
```

**Comment**

All functions must be declared in the script before they can be called.

For a more complete explanation and examples of functional testing and transaction verification, see the *WebLOAD Scripting Guide*.

**See also**

* BeginTransaction() (see [*BeginTransaction() (function)* ](#_bookmark48))
* CreateDOM() (see [*CreateDOM() (function)* ](#_bookmark77))
* CreateTable() (see [*CreateTable() (function)* ](#_bookmark79))
* EndTransaction() (see [*EndTransaction() (function)* ](#erase-property))
* ReportEvent() (see [*ReportEvent() (function)* ](#_bookmark306))
* SetFailureReason() (see [*SetFailureReason() (function)* ](#setfailurereason-function))
* TimeoutSeverity (see [*TimeoutSeverity (property)* ](#_bookmark413))
* TransactionTime (see [*TransactionTime (property)* ](#_bookmark418))
* [*Transaction Verification Components* ](#_bookmark39)

## Version (property)

**Property of Objects**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)
* [wlLocals](#wllocals-object)

**Description**

Sets the HTTP version number for the current test session. 

Current supported versions:

* `1.0` (`1`) 
* `1.1`
* `2.0` (`2`, `2TLS`)
* `3.0` (`3`)

Advanced:

* `2HTTP` - Attempt HTTP/2 over HTTPS, but do not insist on TLS 1.2 or higher even though that is required by the specification.
* `2PRIOR` Issue non-TLS HTTP requests using HTTP/2 without HTTP/1.1 Upgrade. It requires prior knowledge that the server supports HTTP/2 straight away. HTTPS requests still do HTTP/2 the standard way with negotiated protocol version in the TLS handshake.
* `3ONLY` - Attempt to use HTTP/3 directly to server given in the URL and does not downgrade to earlier HTTP version if the server does not support HTTP/3

**GUI mode**

WebLOAD recommends selecting an HTTP version through the WebLOAD Console. Click the appropriate version number radio button in the HTTP Parameters tab of the **Default** or **Current Session Options** dialog box, accessed from the **Tools** tab of the ribbon.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## WarningMessage() (function)

**Description**

Use this function to display a warning message in the Log window.



**Syntax** 

WarningMessage(msg) ****

**Comment**

If you call WarningMessage() in the main script, WebLOAD sends a warning message to the Log window and continues with script execution as usual. The message has no impact on the continued execution of the test session.

**GUI mode**

WebLOAD recommends adding message functions to your script files directly through the WebLOAD Recorder. Drag the Message icon from the WebLOAD Recorder toolbox

into the script. The Message dialog box opens. Enter the message text, select the WLMinorError severity level for the message, and click **OK**.

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlException (see [*wlException (object)* ](#_bookmark446))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))



## window (object)

**Property of Object**

* frames (see [*frames (object)* ](#frames-object))

**Description**

The window object represents an open browser window. window objects store the complete parse results for downloaded HTML pages. Use the window object to gain access to the document in the window. From the window properties you can retrieve the document itself, check the location, and access other subframes that are nested within that window. Typically, the browser creates a single window object when it opens an HTML document. However, if a document defines one or more frames the browser creates one window object for the original document and one additional window object (a *child window*) for each frame. The child window may be affected by actions that occur in the parent. For example, closing the parent window causes all child windows to close.

 **Note:** The 'parent' window item is usually implicitly understood when accessing the HTML document information.

window objects are also accessed through nested frames, where the frame object's

window property points to a child window nested within the given frame (read-only).

**Example**

When working with multiple child windows of a frames collection, access the first child window using the following expressions:

`frames[0]`

-Or-

`document.`frames[0]``

Access the properties (document, location, or frames) of the first child window with the following expressions:

`frames[0]`.`<child-property>`

-Or-

`document.`frames[0]``.`<*child-property*>`

For example:

`frames[0]`.location

-Or-

`document.`frames[0]``.location

**Properties**

* document (see [*document (object)* ](#_bookmark100))
* location (see [*location (object)* ](#_bookmark244))
* Name (see [*Name (property)* ](#_bookmark253))
* title (see [*title (property)* ](#_bookmark415))
* Url (see [*Url (property)* ](#_bookmark422))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)

## wlClear() (method)

**Method of Objects**

The wlHttp object includes the following collections for storing data. These data storage collections each include the method wlClear().

* wlHttp.Data (see [*Data (property)* ](#data-property))
* wlHttp.DataFile (see [*DataFile (property)* ](#datafile-property))
* wlHttp.FormData (see [*FormData (property)* ](#formdata-property))
* wlHttp.Header (see [*Header (property)* ](#header-property))

**Description**

wlClear() is used to clear property values from the specified wlHttp data collection.

**Syntax**

wlHttp.*DataCollection*.wlClear([FieldName])

**Parameters**

[FieldName]-An optional user-supplied string with the name of the field to be cleared.

**Example**

If called with no parameters, then all values set for the collection are cleared:

wlHttp.FormData[“a”] = “DDD” wlHttp.FormData[“B”] = “FFF” wlHttp.FormData.wlClear()

// Clear all value from all fields in FormData InfoMessage (wlHttp.FormData[“a”])

// This statement has no meaning, since there

// is currently no value assigned to “a”

If wlClear() is passed a FieldName parameter, then only the value of the specified field is cleared:

wlHttp.FormData.wlClear(“FirstName”)

// Clears only value assigned to “FirstName”

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Header (see [*Header (property)* ](#header-property))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

## wlCookie (object)

**Description**

The wlCookie object gets, sets and deletes cookies. These activities may be required by an HTTP server.

 **Note:** Cookie management is usually handled automatically through the standard DOM document.cookie property.

WebLOAD supports the wlCookie object as an alternate approach to cookie management. You may use the methods of wlCookie to create as many cookies as needed. For example, each WebLOAD client running a script can set its own cookie identified by a unique name. wlCookie is a local object. WebLOAD automatically creates an independent wlCookie object for each thread of a script. You cannot manually declare wlCookie objects yourself.

By default, WebLOAD always accepts cookies that are sent from a server. When WebLOAD connects to a server, it automatically submits any cookies in the server’s domain that it has stored. The wlCookie object lets you supplement or override this behavior in the following ways:

* A thread can create its own cookies.
* A thread can delete cookies that it created.
* A thread can get the value of a cookie that is created.

Aside from these two abilities, WebLOAD does not distinguish in any way between cookies that it receives from a server and those that you create yourself. For example, if a thread creates a cookie in a particular domain, it automatically submits the cookie when it connects to any server in the domain.

 **Note:** This property can only be inserted manually.

**Syntax** wlCookie.*method()* **Example**

//Set a cookie

wlCookie.Set(“CUSTOMER”, “JOHN_SMITH”, [“www.ABCDEF.com](http://www.ABCDEF.com/)”, “/”, “Wed, 08-Apr-98 17:29:00 GMT”)

//WebLOAD submits the cookie [wlHttp.Get(“www.ABCDEF.com/products/OrderForm.cgi](http://www.ABCDEF.com/products/OrderForm.cgi)”)

//Get the value of a cookie

retValue = wlCookie.Get(“CUSTOMER”, “[www.ABCDEF.com](http://www.abcdef.com/)”, “/” )

//Delete the cookie wlCookie.ClearAll()

**Methods**

* ClearAll() (see [*ClearAll() (method)* ](#_bookmark54))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* Set() (see [*Set() (cookie method)* ](#_bookmark351))
* Get() (see [*Get() (cookie method)* ](#_bookmark135))

## wlDataFileField (method)

**Description**

WLDataFileField creates the data file field parameter.

**Syntax**

fileFieldParam = WLDataFileField(paramName, ColumnNumber);

**Parameters**

| **Parameter  Name** | **Description**                           |
| ------------------------- | ----------------------------------------------- |
| paramName                 | File parameter ID, returned by WLDataFileParam. |
| ColumnNumber              | File column number.                             |



## wlDataFileParam() (parameterization)

**Description**

Define a data file parameter.

**Syntax**

`<paramName>` = wlDataFileParam(FileID, CopyFileId, HeaderLines, Delimiter, AccessMethod, Scope, UsageMethod, EndOfFileBehavior);

**Parameters**

| **Parameter  Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FileID                    | A string which is a unique parameter  identifier.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CopyFileId                | An identifier which refers  to the local file. This value is returned by the CopyFile command.                                                                                                                                                                                                                                                                                                                                                                                 |
| HeaderLines               | A parameter that defines  the number of header lines the file contains. All values are enumerated  numeric values. Possible values are:`<br>`0. The file does not contain any header  lines. This is the default value.  `<br><X>`. Where `<X>` is any  number above zero. The file contains  `<X>` header lines at  the beginning of the file. The values contained in these header lines are not  used as parameters but  as variable  names in the JavaScript code. |
| Delimiter                 | Character used to separate  fields in one line of the input file. The default delimiter character is a  comma.                                                                                                                                                                                                                                                                                                                                                                 |
| AccessMethod | Defines the method for reading the next row  from the file. All values are enumerated numeric values. Possible values are:`<br>`WLParamRandom. Gets a random row from  the file.  `<br>`WLParamOrdered. Every client gets the  next row from the file (order is important).  `<br>`WLParamNotOrdered. Every client gets the  next row from the file (order is not important). |
| Scope | Defines the scope (sharing  policy) of the parameter. Possible values are:`<br>`WLParamGlobal. All virtual clients read  rows from the shared (global ) pool.  `<br>`WLParamLocal. Each virtual client  reads rows from its own copy of the pool.  `<br>`WLParamGlobalLocked. All virtual clients read  a unique row from the global pool, which is shared by all virtual clients  on all load  generators. |
| UsageMethod | Defines when the parameter  is updated, meaning when a new  value will be read. Possible values are:`<br>`WLParamUpdateRound. The script reads a new  row from the file one time for  each round. Using the same parameter again in the same round will result in  the same value.  `<br>`WLParamUpdateOnce. The script reads a new  row from the file once at the beginning of the test (in InitClient). Every usage of the  parameter by that Virtual Client will always result in the same value.  `<br>`WLParamUpdateUse. The parameter’s value  will be read each time it is used. |
| EndOfFileBehavior | Defines how WebLOAD  behaves when it reaches the end of the file. All values are enumerated  numeric values.`<br>`WLParamKeepLast. Keep the last value.  `<br>`WLParamCycle. Start from the beginning  of the file. Each row can be used any number of times.  `<br>`WLParamStopVC. Abort the specific  Virtual Client that tried to read past the end of the file. An error message  is written to the log file. |

**Example**

```javascript
function InitAgenda()

{

myFileParam_File = CopyFile("C:\\My Documents\\WebLOAD\\Sessions\\param1.txt")

}

function InitClient()

{

myFileParam_DataFileParam = wlDataFileParam ( "myFileParam",myFileParam_File, 1,",",wlParamRandom,WLParamGlobalLocked,wlParamUpdateRound,wlParamCycl e);

myFileParam_col1 = wlDataFileField( myFileParam_DataFileParam, 1);

myFileParam_col2 = wlDataFileField( myFileParam_DataFileParam, 2);

}

/***** WLIDE - Message - ID:4 *****/ InfoMessage(myFileParam_col1.getValue())

// END WLIDE

/***** WLIDE - Message - ID:5 *****/ InfoMessage(myFileParam_col2.getValue())
```

**Methods**

* wlDataFileField() (see [*wlDataFileField (method)*](#wldatafilefield-method)))



## wlException (object)

**Description**

script scripts that encounter an error during runtime do not simply fail and die. This would not be helpful to testers who are trying to analyze when, where, and why an error in their application occurs. WebLOAD scripts incorporate a set of error management routines to provide a robust error logging and recovery mechanism whenever possible. The wlException object is part of the WebLOAD error management protocol.

WebLOAD users have a variety of options for error recovery during a test session. The built-in error flags provide the simplest set of options; an informative message, a simple warning, stop the current round and skip to the beginning of the next round, or stop the test session completely. Users may also use try()/catch() commands to enclose logical blocks of code within a round. This provides the option of catching any minor errors that occur within the enclosed block and continuing with the next logical block of code within the current round, rather than skipping the rest of the round completely.

Users may add their own try()/catch() pairs to a script, delimiting their own logical code blocks and defining their own alternate set of activities to be executed in case an error occurs within that block. If an error is caught while the script is in the middle of executing the code within a protected logical code block (by try()),

WebLOAD will detour to a user-defined error function (the catch() block) and then continue execution with the next navigation block in the script.

wlException objects store information about errors that have occurred, including informative message strings and error severity levels. Users writing error recovery functions to handle the errors caught within a try()/catch() pair may utilize the wlException object. Use the wlException methods to perhaps send error messages to the Log Window or trigger a system error of the specified severity level.

**Example**

The following code fragment illustrates a typical error-handling routine:

```javascript
try{

...

//do a lot of things

...

//error occurs here

...

}

catch(e){

myException = new wlException(e,“we have a problem”)

//things to do in case of error

if (myException.GetSeverity() == WLError) {

// Do one set of Error activities myException.ReportLog()

throw myException

}

else {

// Do a different set of Severe Error activities throw myException

}

}
```

**Methods**

* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* wlException() (see [*wlException() (constructor)* ](#_bookmark448))

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))



## wlException() (constructor)

**Method of Object**

* wlException (see [*wlException (object)* ](#_bookmark446))

**Description**

Creates a new wlException object.

**Syntax**

NewExceptionObject = new wlException(severity, message)

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| severity                 | One of the following integer constants:`<br>`WLError. This specific  transaction failed and the current test  round was aborted. The script displays an error message in the Log window and  begins a new round.  `<br>`WLSevereError. This specific  transaction failed and the test  session must be stopped completely. The script displays an error message in  the Log window and the Load Generator on  which the  error occurred is stopped. |
| message                  | The exception message stored as a text  string.                                                                                                                                                                                                                                                                                                                                                                                                         |

**Return Value**

Returns a new wlException object.

**Example**

`myUserException=new wlException(WLError, “Invalid date”)`

**See also**

* ErrorMessage() (see [*ErrorMessage() (function)* ](#errormessage-function))
* GetMessage() (see [*GetMessage() (method)* ](#_bookmark172))
* GetSeverity() (see [*GetSeverity() (method)* ](#_bookmark182))
* InfoMessage() (see [*InfoMessage() (function)* ](#_bookmark217))
* [*Message Functions* ](../scripting/programming_your_javascript.md#standard_message_functions)
* ReportLog() (see [*ReportLog() (method)* ](#reportlog-method))
* SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](#severeerrormessage-function))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* WarningMessage() (see [*WarningMessage() (function)* ](#_bookmark437))



## wlGeneratorGlobal (object)

**Description**

WebLOAD provides a global object called wlGeneratorGlobal. The wlGeneratorGlobal object enables sharing of global variables and values between all threads of a single Load Generator, even when running multiple scripts. (Compare to the wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491))object, which enables sharing of global variables and values system-wide, between all threads of all Load Generators participating in a test session, and to the [wlGlobals](#wlglobals-object) object, which enables sharing of global variables and values between threads of a single script, running on a single Load Generator.)

Globally shared variables are useful when tracking a value or maintaining a count across multiple threads or platforms. For example, you may include these shared values in the messages sent to the Log window during a test session.

WebLOAD creates exactly one wlGeneratorGlobal object for each Load Generator participating in a test session. Use the wlGeneratorGlobal methods to create and access variable values that you wish to share between threads of a Load Generator.

Edit wlGeneratorGlobal properties and methods through the IntelliSense editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18). While global variables may be accessed anywhere in your script, be sure to initially declare wlGeneratorGlobal values in the InitAgenda() *function only*. Do not define new values within the main body of a Script, for they will not be shared correctly by all threads.

**Methods**

The wlGeneratorGlobal object includes the following methods:

* Add() (see [*Add() (method)* ](#_bookmark45))
* Get() (see [*Get() (addition method)* ](#_bookmark134))
* Set() (see [*Set() (addition method)* ](#set-addition-method)))

**Properties**

wlGeneratorGlobal incorporates a dynamic property set that consists of whatever global variables have been defined, set, and accessed by the user through the wlGeneratorGlobal method set only.

**See also**

* wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491))



## wlGet() (method)

**Method of Object**

Each of the different types of collections of elements found in the parsed DOM tree includes the method wlGet().

**Description**

wlGet() is used when getting data from a property in the collection to distinguish between keywords and user-defined variables that share the same names. The need for this care is explained in this section.



**Syntax** 

*Collection*.wlGet(PropertyName) 

**Return Value**

The value of the specified property

**Example** 

`document.forms[0].elements.wlGet(“FirstName”)` 

**Comment**

In JavaScript, users may work interchangeably with either an array[index] or

array.index notation. For example, the following two references are interchangeable:

`wlHttp.FormData[“Sunday”]`

-Or-

`wlHttp.FormData.Sunday`

This flexibility is convenient for programmers, who are able to select the syntax that is most appropriate for the context. However, it could potentially lead to ambiguity. For example, assume a website included a form with a field called length. This could lead to a confusing situation, where the word length appearing in a script could represent either the number of elements in a FormData array, as explained in length, or the value of the length field in the form. Errors would arise from a reasonable assignment statement such as:

wlHttp.FormData[“length”] = 7

This is equivalent to the illegal assignment statement:

wlHttp.FormData.length = 7

WebLOAD therefore uses wlGet() to retrieve field data whenever the name could lead to potential ambiguity. When recording scripts with WebLOAD Recorder, WebLOAD recognizes potential ambiguities and inserts the appropriate wlGet() statements automatically.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))



## wlGetAllForms() (method)

**Method of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

Retrieve a collection of all forms (`<FORM>` elements) in an HTML page and its nested frames.

**Syntax** 

wlGetAllForms() 

**Return Value**

A collection that includes the forms in the top-level frame (from which you called the

method) and all its subframes at any level of nesting.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## wlGetAllFrames() (method)

**Method of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

Retrieve a collection of all frames in an HTML page, at any level of nesting.

**Syntax** wlGetAllFrames() **Return Value**

A collection that includes the top-level frame (from which you called the method) and

all its subframes.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## wlGetAllLinks() (method)

**Method of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

Retrieve a collection of all links (`<A>` elements) in an HTML page and its nested frames.

**Syntax** wlGetAllLinks() **Return Value**

A collection that includes links in the top-level frame (from which you called the

method) and all its subframes at any level of nesting.

**See also**

* [*HTTP Components* ](./using_javascript_ref.md#http_components)

## wlGlobals (object)

**Description**

The wlGlobals object stores the default global configuration properties set by the user through the WebLOAD Recorder or Console, including properties defining expected dialog boxes, verification test selections, and dynamic state management.

wlGlobals is a global object, whose property values are shared by all threads of a script running on a single Load Generator. The wlGlobals object enables sharing of user-defined global variables and values between threads of a single script, running on a single Load Generator. (Compare to the wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal*](#_bookmark450) [*(object)* ](#_bookmark450)) object, which enables sharing of global variables and values between all threads of a single Load Generator, and the wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491)) object, which enables sharing of global variables and values system-wide, between all threads of all Load Generators participating in a test session.)

 **Note:** Most global configuration property values and user-defined variables should be set through the WebLOAD Recorder or Console. The property descriptions here are intended mainly to explain the lines of code seen in the JavaScript View of the WebLOAD Recorder desktop. Syntax details are also provided for the benefit of users who prefer to manually edit the JavaScript code of their scripts through the IntelliSense editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18). If you do decide to edit the global variable values in your script, set wlGlobals properties in the InitAgenda() *function only*. Do not define new values within the main body of a script. The values will not be shared correctly by all script threads.

The configuration properties of the wlGlobals object are almost all duplicated in the wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object)), which contains the local configuration settings for browser actions, and in the wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object)), which contains configuration settings that are limited to a single specific browser action. To understand how there could potentially be three different settings for a single configuration property, see the *WebLOAD Scripting Guide*.

**Properties**

The wlGlobals object includes the following property classes:

* *Automatic State Management for HTTP Protocol Mode* 
* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* [*Transaction Verification Components* ](#_bookmark39)

**Syntax**

Each individual property class includes the syntax specifications that apply to that class.

**GUI mode**

The wlGLobals, property and method descriptions explain how to explicitly set values for these session configuration properties within your JavaScript script files.

The recommended way to set configuration values is through the WebLOAD Recorder, using the Default, Current, and Global Options dialog boxes accessed from the **Tools** tab in the Console desktop ribbon. The dialog boxes provide a means of defining and setting configuration values with ease, simplicity, and clarity.

**See also**

* wlHttp (see [wlHttp (object) ](./actions_objects_functions.md#wlhttp-object))
* wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450))
* wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))
* wlSystemGlobal (see [*wlSystemGlobal (object)* ](#_bookmark491))



## wlHeaders (object)

**Property of Objects**

Headers on a Web page are accessed through wlHeaders objects that are grouped into collections of wlHeaders. The wlHeaders collection is a property of the following objects:

* document (see [*document (object)* ](#_bookmark100))

**Description**

Each wlHeaders object contains a key-value pair. wlHeaders objects provide access to the key/value pairs in the HTTP *response headers*. (Information found in *request headers* is available through the wlHttp.Header property. For key-value pairs found in *URL search strings*, see [*wlSearchPairs (object)* ](#_bookmark480).)

wlHeaders objects are local to a single thread. You cannot create new wlHeaders objects using the JavaScript new operator, but you can access them through the properties and methods of the standard DOM objects. wlHeaders properties are read only.

**Syntax**

wlHeaders objects are grouped together within collections of wlHeaders. To access an individual wlHeaders’s properties, check the length property of the wlHeaders collection and use an index number to access the individual wlHeaders object, with the following syntax:

NumberofHeaderObjects = document.wlHeaders.length document.wlHeaders[*index*#].`<*wlHeaders-property*>`

**Example**

WebLOAD stores the header pairs from the response to the most recent Get, Post, or Head command in the document.wlHeaders collection. The following statement would retrieve an HTTP header:

wlHttp.Head(“[http://www.ABCDEF.com](http://www.ABCDEF.com/)”)

For a header that looks something like this:

HTTP/1.1 200 OK

Server: Netscape-Enterprise/3.0F Date: Sun, 11 Jan 1998 08:25:20 GMT

Content-type: text/html Connection: close

Host: Server2.MyCompany.com

WebLOAD parses the header pairs as follows:

document.wlHeaders[0].key = “Server” document.wlHeaders[0].value = “Netscape-Enterprise/3.0F” document.wlHeaders[1].key = “Date” document.wlHeaders[1].value = “Sun, 11 Jan 1998 08:25:20 GMT”

...

**Properties**

The wlHeaders object includes the following properties:

* key (see [*key (property)* ](#_bookmark229))
* value (see [*value (property)* ](#value-property))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* Header (see [*Header (property)* ](#header-property))
* wlSearchPairs (see [*wlSearchPairs (object)* ](#_bookmark480))



## wlHtml (object)

**Description**

If your script downloads HTML code, you can use the wlHtml object to retrieve parsed elements of the code. The wlHtml object also lets you retrieve the HTTP header fields and status and parse URL addresses into their host, port, and URI components.

wlHtml is a local object. WebLOAD automatically creates an independent wlHtml object for each thread of a script. You cannot manually declare wlHtml objects yourself.

**Methods**

* GetFieldValue() (see [*GetFieldValue() (method)* ](#getfieldvalue-method))
* GetFieldValueInForm() (see [*GetFieldValueInForm() (method)* ](#getfieldvalueinform-method))
* GetFormAction() (see [*GetFormAction() (method)* ](#getformaction-method))
* GetFrameByUrl() (see [*GetFrameByUrl() (method)* ](#getframebyurl-method))
* GetFrameUrl() (see [*GetFrameUrl() (method)* ](#getframeurl-method))
* GetHeaderValue() (see [*GetHeaderValue() (method)* ](#getheadervalue-method))
* GetHost() (see [*GetHost() (method)* ](#gethost-method))
* GetHostName() (see [*GetHostName() (method)* ](#gethostname-method))
* GetLinkByName() (see [*GetLinkByName() (method)* ](#getlinkbyname-method))
* GetLinkByUrl() (see [*GetLinkByUrl() (method)* ](#getlinkbyurl-method))
* GetPortNum() (see [*GetPortNum() (method)* ](#getportnum-method))
* GetQSFieldValue() (see [*GetQSFieldValue() (method)* ](#getqsfieldvalue-method))
* GetStatusLine() (see [*GetStatusLine() (method)* ](#getstatusline-method))
* GetStatusNumber() (see [*GetStatusNumber() (method)* ](#getstatusnumber-method))
* GetUri() (see [*GetUri() (method)* ](#geturi-method))



## wlHttp (object)

**Description**

The wlHttp object stores configuration information for immediate user activities, including properties defining expected dialog boxes, verification test selections, and dynamic state management. Many of these properties are duplicated in the wlGlobals (see [*w*](#_bookmark460)[*lGlobals (object)* ](#_bookmark460)), which contains the default global configuration settings for browser actions, and in the wlLocals (see [*wlLocals (object)*](./actions_objects_functions.md#wllocals-object)), which contains the local configuration settings for browser actions. To understand how there could potentially be three different settings for a single configuration property, see the *WebLOAD Scripting Guide*. The wlHttp object also contains the methods that implement the user activities saved during the WebLOAD Recorder recording session. User activities may be recreated through one of two approaches: the high-level User Action mode or the low-level HTTP Protocol mode. Methods for each of these testing modes are included in the wlHttp object.

**Properties and Methods**

The wlHttp object includes the following property and method classes:

* *Automatic State Management for HTTP Protocol Mode* 
* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* [*Transaction Verification Components* ](#_bookmark39)

**Syntax**

Each individual function class includes the syntax specifications that apply to that class.

**GUI mode**

The wlHttp property and method descriptions explain how to explicitly set values for these session configuration properties within your JavaScript script files.

 **Note:** The recommended way to set configuration values is through the WebLOAD Recorder, using the Default, Current, and Global Options dialog boxes accessed from the **Tools** tab in the Console desktop ribbon. The dialog boxes provide a means of defining and setting configuration values with ease, simplicity, and clarity.

**See also**

* [wlGlobals](#wlglobals-object)
* [wlLocals](#wllocals-object)



## wlInputFile (object)

**Description**

The wlInputFile object supports reading values from an external text file. This is useful when you need to parameterize your script. The input file supports the following access methods:

* Unique access to a parameters file’s record. This ensures that a value that was read by VC1 will not be read by any other VC as long as VC1 is using this value.
* Shared access for a parameters file among Load Generators and Load Machines and among different scripts.
* Sequential and random access to a parameters file.

The wlInputFile object enables Load Generators running on more than one load machine to access a single parameters file in a way that enables unique reading of the parameters from the file. In addition, a single parameters file can be accessed by more

than one script in a way that enables unique reading of parameters from the file by all of the scripts.

Create wlInputFile objects and manage your files using the constructor and methods described in this section.

**Syntax**

MyFileObj = new wlInputFile(fileID)

**Parameters**

| **Parameter Name** | **Description**                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| fileID                   | An identifier which refers  to the local file. This value is returned by the CopyFile command. |

**Example**

```javascript
fileID = CopyFile(`<full path>`)

…

MyFileObj = new wlInputFile(*fileID*)

…

MyFileObj.Open([AccessMethod], [ShareMethod], [UsageMethod], [EndOfFileBehavior], [HeaderLines])
```

**Methods**

* Open() (see [*Open() (method)* ](#open-method))
* GetLine() (see [*G*](#getline-function)[*etLine() (function)* ](#getline-function))

**See also**

* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))



## wlInputFile() (constructor)

**Method of Object**

* wlInputFile (see [*wlInputFile (object)* ](#_bookmark467))

**Description**

Creates a new wlInputFile object. For optimal performance, construct a new file object in the InitClient section of your script. The file is copied from the Console to the Load Generator. The input file specified in the wlInputFile object is opened.

**Syntax**

myFileObj = new wlInputFile(fileID)

**Parameters**

| **Parameter Name** | **Description**                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| fileID                   | An identifier which refers  to the local file. This value is returned by the CopyFile command. |

**Return Value**

A pointer to a new wlInputFile object.

**Example**

```javascript
fileID = CopyFile(`<full path>`)

…

MyFileObj = new wlInputFile(*fileID*)

…

MyFileObj.Open([AccessMethod], [ShareMethod], [UsageMethod], [EndOfFileBehavior], [HeaderLines])
```



## wlLocals (object)

**Description**

The wlLocals object stores the local default configuration information for user activities, such as the URL, user name and password, proxy server, and dialog box management. wlLocals is a local object. WebLOAD creates an independent wlLocals object for *each thread* of a script. You cannot declare wlLocals objects yourself.

The properties of the wlLocals object are all duplicated in the [wlGlobals](#wlglobals-object), which contains the default global settings, and in the  [wlHttp](#wlhttp-object), which contains the settings for an immediate action. To understand how there could potentially be three different settings for a single configuration property, see the *WebLOAD Scripting Guide*.

**Properties**

The wlLocals object includes the following property classes:

* *Automatic State Management for HTTP Protocol Mode* 
* [*HTTP Components* ](./using_javascript_ref.md#http_components)
* [*Transaction Verification Components* ](#_bookmark39)

**Syntax**

Each individual function class includes the syntax specifications that apply to that class.

**GUI mode**

The wlLocals property and method descriptions explain how to explicitly set values for these session configuration properties within your JavaScript script files.

 **Note:** The recommended way to set configuration values is through the WebLOAD Recorder, using the Default, Current, and Global Options dialog boxes accessed from the **Tools** tab in the Console desktop ribbon. The dialog boxes provide a means of defining and setting configuration values with ease, simplicity, and clarity.

**See also**

* [wlGlobals](#wlglobals-object)
* [wlHttp](#wlhttp-object)



## wlMetas (object)

**Property of Objects**

META objects on a Web page are accessed through wlMetas objects that are grouped into collections of wlMetas. The wlMetas collection is a property of the following objects:

* document (see [*document (object)* ](#_bookmark100))

**Description**

Each wlMetas object stores the parsed data for an HTML meta object (`<META>` tag). wlMetas objects are local to a single thread. You cannot create new wlMetas objects using the JavaScript new operator, but you can access them through the properties and methods of the standard DOM objects. wlMetas properties are read only.

**Syntax**

wlMetas objects are grouped together within collections of wlMetas. To access an individual wlMetas’s properties, check the length property of the wlMetas collection and use an index number to access the individual wlMetas object, with the following syntax:

NumberofMetaObjects = document.wlMetas.length document.wlMetas[#].`<*wlMetas-property*>`

**Example**

To find out how many wlMetas objects are contained within a document header, check the value of:

document.wlMetas.length

Access each wlMetas’s properties directly using the preceding syntax. For example:

document.wlMetas[0].key

**Properties**

The wlMetas object includes the following properties:

* content (see [*content (property)* ](#_bookmark68))
* httpEquiv (see [*httpEquiv (property)* ](#_bookmark204))
* Name (see [*Name (property)* ](#_bookmark251))
* Url (see [*Url (property)* ](#_bookmark422))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)



## wlNumberParam() (parameterization)

**Description**

Define a number parameter.

**Syntax**

paramName = wlNumberParam (ParamID, MinValue, MaxValue,Step, AccessMethod, Scope, UsageMethod, OutOfValuesBehavior);

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ParamID                  | A string that is a unique parameter identifier.                                                                                                                                                                                                                                                                                                                                                       |
| MinValue                 | The minimum value of the number range.                                                                                                                                                                                                                                                                                                                                                                |
| MaxValue                 | The maximum value of the number range.                                                                                                                                                                                                                                                                                                                                                                |
| Step                     | The increment between numbers.                                                                                                                                                                                                                                                                                                                                                                        |
| AccessMethod             | Defines the method for  calculating the next value from the range. All values are enumerated numeric  values. Possible values are:`<br>`wlParamRandom. Gets a random value from  the range.  `<br>`wlParamOrdered. Every client gets the  next value from the range (order  is important).  `<br>`wlParamNotOrdered. Every client gets the  next value from the range (order is not important). |
| Scope | Defines the scope (  sharing policy) of the parameter. Possible values are:`<br>`wlParamGlobal. All virtual clients read  values from the shared (global )  pool.  `<br>`wlParamLocal. Each virtual client  reads values from its own pool.  `<br>`wlParamGlobalLocked. All virtual clients read unique values from the shared (global  ) pool. |
| Usage Method | Defines when the parameter  is updated, meaning when a new value will be read. Possible values are:`<br>`WLParamUpdateRound. The script reads a new  value from the file once for each round. Using the same parameter again in the same round will result in  the same value.  `<br>`WLParamUpdateOnce. The script reads a new  value from the file once at the  beginning of the test (in InitClient). All usage of the  parameter by that Virtual Client will always result in the same value.  `<br>`WLParamUpdateUse. The parameter’s value  will be read each time it is used. |
| OutOfValuesBehavior | Defines how WebLOAD  behaves when it reaches the end of the range. All values are enumerated  numeric values. Possible values are:`<br>`WLParamKeepLast. Keep the last value.  `<br>`WLParamCycle. Start from the beginning  of the range.  `<br>`WLParamStopVC. Abort the specific  Virtual Client that tried to read past the end of the range. An error message  is written  to the log  file. |

**Example**

```javascript
function InitClient()

{

NewParam1 = wlNumberParam("NewParam1",1, 100, 1, wlParamRandom, wlParamLocal, wlParamUpdateRound, wlParamCycle);

}

/***** WLIDE - Message - ID:3 *****/ InfoMessage(NewParam1.getValue())

// END WLIDE
```



## wlOutputFile (object)

**Description**

The wlOutputFile object writes script output messages to a global output file. Create wlOutputFile objects and manage your files using the constructor and methods described in this section.

**Syntax**

```javascript
MyFileObj = new wlOutputFile(“*filename”*)

…

MyFileObj.Write(“Happy Birthday”)

…

delete MyFileObj
```

**Example**

Each individual property includes examples of the syntax for that property.

**Methods**

* Close() (see [*Close() (function)* ](#close-function))
* remove() (see [*remove() (method)* ](#delete-cookie-method))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* wlOutputFile() (see [*wlOutputFile() (constructor)* ](#_bookmark476))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))

**Comment**

You may also use the WebLOAD functions listed here to open and close output files.

* To **open** an output file:

Open(filename)

* To **close** an output file:

Close(filename)

When you use the Close() function to close a file data will be flashed to the disk.

>  **Note:** Declaring a new wlOutputFile object creates a new, empty output file. If a file of that name already exists, the file will be completely overwritten. Information will not be appended to the end of an existing file. Be sure to choose a *unique filename* for the new output file if you do not want to overwrite previous script data.



If you declare a new wlOutputFile object in the InitAgenda() function of a script, the output file will be shared by all the script threads. There is no way to specify a specific thread writing sequence-each thread will write to the output file in real time as it reaches that line in the script execution.

If you declare a new wlOutputFile object in the InitClient() function or main body of a script, use the thread number variable as part of the new filename to be sure that each thread will create a unique output file.

If you declare a new wlOutputFile object in the main body of a script, and then run your script for multiple iterations, use the RoundNum variable as part of the new filename to be sure that each new round will create a unique output file.

Generally, you should only create new wlOutputFile objects in the InitAgenda() or InitClient() functions of a script, not in the main script. If a statement in the main script creates an object, *a new object is created each time the statement is executed*. If WebLOAD repeats the main script many times, a large number of objects may be created and the system may run out of memory.

**See also**

* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)



## wlOutputFile() (constructor)

**Method of Object**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

To create a new wlOutputFile object, use the wlOutputFile() constructor.

**Syntax**

new wlOutputFile(filename)

**Parameters**

| **Parameter Name** | **Description**                      |
| ------------------------ | ------------------------------------------ |
| filename                 | Name of the new output file to be created. |

**Return Value**

A pointer to a new wlOutputFile object.

**Example**

`MyFileObj = new wlOutputFile(“FileName”)`



Declaring a new wlOutputFile object creates a new, empty output file. If a file of that name already exists, the file will be completely overwritten. Information will not be appended to the end of an existing file. Be sure to choose a *unique filename* for the new output file if you do not want to overwrite previous script data.

If you declare a new wlOutputFile object in the InitAgenda() function of a script, the output file will be shared by all the script threads. There is no way to specify a specific thread writing sequence-each thread will write to the output file in real time as it reaches that line in the script execution.

If you declare a new wlOutputFile object in the InitClient() function or main body of a script, use the thread number variable as part of the new filename to be sure that each thread will create a unique output file.

If you declare a new wlOutputFile object in the main body of a script, and then run your script for multiple iterations, use the RoundNum variable as part of the new filename to be sure that each new round will create a unique output file.

*Ideally*, create new wlOutputFile objects only in the InitAgenda() function of a script, not in the main script. If a statement in the main script creates an object, a new object is created *each time the statement is executed*. If WebLOAD repeats the main script many times, a large number of objects may be created and the system may run out of memory.

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))
* Write() (see [*Write() (method)* ](#_bookmark504))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))



## wlRand (object)

**Description**

The wlRand object is a random number generator.

wlRand is a local object. WebLOAD automatically creates an independent wlRand

object for the test session script. You cannot declare wlRand objects yourself.

**Syntax** wlRand.*Method*() **Example**

The following example generates three random numbers having the following possible

values:

* Any integer.
* An integer from 1 to 9.
* One of the three numbers 0, 1, or 1.5.

```
function InitAgenda() 

{ 

wlRand.Seed(23)

}
```

`AnyInteger = wlRand.Num() OneToNine = wlRand.Range(1, 9)`

OneOfThreeNumbers = wlRand.Select(0, 1, 1.5)

**Methods**

* Num() (see [*Num() (method)* ](#num-method))

* Range() (see [*Range() (method)* ](#_bookmark300))

* Seed() (see [*Seed() (method)* ](#_bookmark326))

* Select() (see [*Select() (method)* ](#_bookmark329))

  

## wlSearchPairs (object)

**Method of Object**

* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))

**Description**

Each wlSearchPairs object contains a parsed version of the search attribute string, storing the key/value pairs found in a document’s *URL search strings*. (For key-value pairs found in HTTP *response headers*, see wlHeaders (see [*wlHeaders (object)* ](#_bookmark462)). Information found in *request headers* is available through the wlHttp.Header (see [*Header (property)* ](#header-property)) property.)

wlSearchPairs objects are grouped into wlSearchPairs collections, where the collections are themselves properties of the link and location objects.

wlSearchPairs objects are local to a single thread. You cannot create new wlSearchPairs objects using the JavaScript new operator, but you can access them through the properties and methods of the standard DOM objects. wlSearchPairs properties are read only.

**Syntax**

wlSearchPairs objects are grouped together within collections of wlSearchPairs. To access an individual wlSearchPairs’s properties, check the length property of the wlSearchPairs collection and use an index number to access the individual wlSearchPairs object, with the following syntax:

`NumberofSearchPairObjects = document.links[1].wlSearchPairs.length` 

`document.links[1].wlSearchPairs[*index*#].<*wlSearchPairs-property*>`

**Example**

To find out how many wlSearchPairs objects are contained within a document’s link, check the value of:

document.links[1].wlSearchPairs.length

Access each wlSearchPairs’s properties directly through the index number of that item. For example:

document.links[1].wlSearchPairs[0].key

Suppose that the third link on a Web page has the following HTML code:

<A [href=“http://www.ABCDEF.com/ProductFind.exe?](http://www.ABCDEF.com/ProductFind.exe)

Product=modems&Type=ISDN”> ISDN Modems `</A>`

You can download the page and parse the links using the following script:

```javascript
function InitAgenda() {

wlGlobals.Url = "http://www.ABCDEF.com"

//Enable link parsing wlGlobals.ParseLinks = true

}

wlHttp.Get()
```


For the link in question, WebLOAD stores the attribute pairs in the document.links[2].wlSearchPairs property. This property is actually a collection containing two wlSearchPairs objects. The following is a complete listing of the collection.

document.links[2].wlSearchPairs[0].key = “Product” document.links[2].wlSearchPairs[0].value = “modems” document.links[2].wlSearchPairs[1].key = “Type” document.links[2].wlSearchPairs[1].value = “ISDN”

**Properties**

The wlSearchPairs object includes the following properties:

* key (see [*key (property)* ](#_bookmark229))
* value (see [*value (property)* ](#value-property))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* Header (see [*Header (property)* ](#header-property))
* link (see [*link (object)* ](#_bookmark235))
* location (see [*location (object)* ](#_bookmark243))
* wlHeaders (see [*wlHeaders (object)* ](#wlheaders-object))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))



## wlSet() (method)

**Method of Objects**

The wlHttp object includes the following collections for storing data. These data storage collections each include the method wlSet().

* wlHttp.Data (see [*Data (property)* ](#data-property))
* wlHttp.DataFile (see [*DataFile (property)* ](#datafile-property))
* wlHttp.FormData (see [*FormData (property)* ](#formdata-property))
* wlHttp.Header (see [*Header (property)* ](#header-property))

**Description**

wlSet() is used when assigning a value to an element in the collection, to distinguish between keywords and user-defined variables that share the same names. The need for this care is explained in this section.

**Syntax**

wlHttp.*Collection*.wlSet(FieldName, Value)

**Parameters**

| **Parameter Name** | **Description**                                          |
| ------------------------ | -------------------------------------------------------------- |
| FieldName                | A string with the name of the field whose value is  to be set. |
| Value                    | The value to be assigned to the specified  field.              |

**Return Value**

The value of the specified property.

**Example** wlHttp.FormData.wlSet(“FirstName”, “Bill”) **Comment**

In JavaScript, users may work interchangeably with either an array[index] or

array.index notation. For example, the following two references are interchangeable:

wlHttp.FormData[“Sunday”]

-Or-

wlHttp.FormData.Sunday

This flexibility is convenient for programmers, who are able to select the syntax that is most appropriate for the context. However, it could potentially lead to ambiguity. For example, assume a website included a form with a field called length. This could lead to a confusing situation, where the word length appearing in a script could represent either the number of elements in a FormData array, as explained in length, or the value of the length field in the form. Errors would arise from a reasonable assignment statement such as:

wlHttp.FormData[“length”] = 7

This is equivalent to the illegal assignment statement:

wlHttp.FormData.length = 7

WebLOAD therefore uses wlSet() to set field data whenever the name could lead to potential ambiguity. When recording scripts with the AAT, WebLOAD recognizes

potential ambiguities and inserts the appropriate wlSet() statements automatically. In this case:

wlHttp.FormData.wlSet(“length”, 7)

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* Data (see [*Data (property)* ](#data-property))
* DataFile (see [*DataFile (property)* ](#datafile-property))
* FormData (see [*FormData (property)* ](#formdata-property))
* Header (see [*Header (property)* ](#header-property))
* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))



## wlSource (property)

**Property of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

The complete HTML source code of the frame (read-only string).

You can use the HTML source to search for any desired information in an HTML page. For information on JavaScript searching capabilities, see *Regular Expressions* in the *Netscape JavaScript Guide*, which is supplied with the WebLOAD software.

**Syntax** document.wlSource **Comment**

To use the HTML source, you must enable the SaveSource (see [*SaveSource (property)* ](#savesource-property)) property of the wlGlobals, wlLocals, or wlHttp object. To save the source in a file, use the Outfile property (see [*Outfile (property)* ](#outfile-property)).

**See also**

* Outfile (see [*Outfile (property)* ](#outfile-property))
* SaveSource (see [*SaveSource (property)* ](#savesource-property))

## wlStatusLine (property)

**Property of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

The status line of the HTTP header (read-only string, for example “OK”).

**Syntax**

`document.wlHeaders[“status line”]`



## wlStatusNumber (property)

**Property of Object**

* document (see [*document (object)* ](#_bookmark100))

**Description**

The HTTP status value, which WebLOAD retrieves from the HTTP header (read-only integer, for example 200).

**Syntax**

`document.wlStatusNumber`



## wlStringParam() (parameterization)

**Description**

Define a random string parameter.

**Syntax**

`<varName>` = wlStringParam(minLength, maxLength, usage)

**Parameters**

| **Parameter Name** | **Description**                              |
| ------------------------ | -------------------------------------------------- |
| minLength                | The minimum string length (number of characters),  |
| maxLength                | The maximum string length (number of  characters). |
| usage | Defines when the parameter  is updated, meaning when a new value will be calculated. Possible values are:`<br>`wlParamUpdateRound. The parameters value  will be calculated once for each round. Using the same parameter again in the same round will result with the same value.  `<br>`wlParamUpdateOnce. The parameter’s value  will be calculated once per each Virtual Client (in its InitClient function). All usage of  the parameter by that Virtual Client will always result in the same value.  `<br>`wlParamUpdateUse. The parameter’s value  will be calculated each time it is used. |

**Example**

`function InitClient()`

`{`

`NewParam1 = wlStringParam(2, 7, wlParamUpdateUse);`

`}`

`/***** WLIDE - Message - ID:3 *****/ InfoMessage(NewParam1.getValue())`

`// END WLIDE`



## wlSystemGlobal (object)

**Description**

WebLOAD provides a global object called wlSystemGlobal. The wlSystemGlobal object enables sharing of global variables and values between all elements of a test session, across multiple scripts running on multiple Load Generators. (Compare to the wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450)), which enables sharing of global variables and values between all threads of a single Load Generator, and to the wlGlobals (see [*w*](#_bookmark460)[*lGlobals (object)* ](#_bookmark460)), which enables sharing of global variables and values between all threads of a single script, running on a single Load Generator.)

Globally shared variables are useful when tracking a value or maintaining a count across multiple threads or platforms. For example, you may include these shared values in the messages sent to the Log window during a test session.

WebLOAD creates exactly one wlSystemGlobal object per a test session. Use the wlSystemGlobal object methods to create and access variable values that you wish to share system-wide. Edit wlSystemGlobal object properties and methods through the IntelliSense editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18).

While global variables may be accessed anywhere in your script, be sure to initially declare wlSystemGlobal values in the InitAgenda() *function only*. Do not define

new values within the main body of a script, for they will not be shared correctly by all threads.

**Methods**

* Add() (see [*Add() (method)* ](#_bookmark45))
* Get() (see [*Get() (addition method)* ](#_bookmark134))
* Set() (see [*Set() (addition method)* ](#set-addition-method))

**Properties**

wlSystemGlobal incorporates a dynamic property set that consists of whatever global variables have been defined, set, and accessed by the user through the wlSystemGlobal method set only.

**See also**

* wlGeneratorGlobal (see [*w*](#_bookmark450)[*lGeneratorGlobal (object)* ](#_bookmark450))



## wlTables (object)

**Property of Object**

TABLE objects on a Web page are accessed through wlTables objects that are grouped into collections of wlTables. The wlTables collection is a property of the following object:

* document (see [*document (object)* ](#document-object))

**Description**

Each wlTables object contains the parsed data for an HTML table (`<TABLE>` tag), and serves as a means of providing access to the cells of the HTML table. Because table data is organized into rows and cells, the wlTables object is also linked to row and cell objects and their properties.

wlTables objects are grouped together within collections of wlTables. The tables are arranged in the order in which they appear on the HTML page.

**Syntax**

To access an individual wlTables’s properties, check the length property of the wlTables collection and use an index number to access the individual wlTables object, with the following syntax:

NumberofTableObjects = document.wlTables.length document.wlTables[*index*#].`<*wlTables-property*>`

**Example**

Access each wlTables’s properties directly through the index number of that item. For example:

document.wlTables[0].cols

wlTables objects may also be accessed directly using the table ID. This is illustrated in the *id* property description.

**Properties**

Each wlTables object contains information about the data found in the whole table, organized by rows, columns, and cells. The wlTables object includes the following properties:

* cell
* cols (see [*cols (property)* ](#wltables-object)) (wlTables property)

* row (see [*row (object)* ](#_bookmark315)) (wlTables property)

**See also**

* cellIndex
* [*Collections* ](using_javascript_ref.md#collections)
*


* 
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)) (cell property)
* InnerText (see [*InnerText (property)* ](#_bookmark223)) (cell property)
* MatchBy (see [*MatchBy (property)* ](#_bookmark246))
* Prepare() (see [*Prepare() (method)* ](#_bookmark291))
* ReportUnexpectedRows (see [*ReportUnexpectedRows (property)* ](#_bookmark310))
* rowIndex (see [*rowIndex (property)* ](#rowIndex (property))) (row property)
* tagName (see [*tagName (property)* ](#_bookmark407)) (cell property)



## wlTarget (property)

**Property of Object**

* wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

**Description**

The exact location within the Web page of the frame into which the transaction should be downloaded.

**Syntax**

`wlHttp.wlTarget = “LocationString”`

**Comment**

wlTarget uses the WebLOAD shorthand notation, described in the *WebLOAD Scripting Guide*. For example, assume the expected location is set to #1.#1. Since frame numbering begins with 0, this refers to the second subframe located within the second frame on the Web page. Neither frame has been assigned an optional name value.

The wlHttp.wlTarget property of a transaction stores the complete path of the frame, from the root window of the Web page. Compare this to the form.target and link.target properties, which identify the most recent, immediate location of the target frame using the name string or keyword that was assigned to that frame. The last field of the wlHttp.wlTarget string is the target name stored in the form.target and link.target properties.



## wlTimeParam() (parameterization)

**Description**

Return the current date and/or time according to the format specified in the parameter’s properties

**Syntax**

`<varName> = wlTimeParam(format, offset, usage)`

**Parameters**

| **Parameter Name** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| format                   | Formats are comprised from symbols, prefixed with  the ‘%’ sign and from textual characters.  The following are the  symbols used to create the date/time formats:`<br>`c – complete date time as number  `<br>`H – Hours (24 hour clock)  `<br>`I – Hours (12 hour clock)  `<br>`M – minutes  `<br>`S – seconds (S.000 –  seconds with milliseconds)  `<br>`p – AM or PM  `<br>`d – day in month (number)  `<br>`m – month (number)  `<br>`y – year (2 digits)  `<br>`Y – year (4 digits)  `<br>`b – month name (3 letter)  `<br>`B – month name (full)  The following are the formats available to the  user:  `<br>`%c  `<br>`%H:%M:%S  `<br>`%I:%M:%S %p  `<br>`%d-%b-%Y  `<br>`%d/%m/%y  `<br>`%m/%d/%y  `<br>`%d/%m/%Y  `<br>`%m/%d/%Y  `<br>`%Y-%m-%d %H:%M:%S  `<br>`%Y-%m-%d %H:%M:%S.000 |
| offset                   | The offset in days and  time. The offset can be used so the parameter will not consider the current  date but another date in the future or in the past.  A negative value indicates a date/time prior to  current date/time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| usage | Defines when the parameter  is updated, i.e., when a new value will be calculated.  Possible values are:`<br>`wlParamUpdateRound. The parameters value  will be calculated once for each round. Using the same parameter again in the  same round will result in the same value.  `<br>`wlParamUpdateOnce. The parameter’s value  will be calculated once per each Virtual Client (in its InitClient function). Every usage of  the parameter by that Virtual Client  will always result in the same value.  `<br>`wlParamUpdateUse. The parameter’s value  will be calculated each time it is used. |

**Example**

```javascript
function InitClient()

{

NewParam1 = wlTimeParam("%Y-%m-%d %H:%M:%S", 1200, wlParamUpdateRound);

}

/***** WLIDE - Message - ID:3 *****/ InfoMessage(NewParam1.getValue())

// END WLIDE
```



## wlVerification (object)

**Description**

The wlverification object stores the response validation properties set by the user through the WebLOAD Recorder, including HTML Web page title, text within a Web page, time taken to load a Web page, and size of a Web page (in bytes).

 **Note:** Most global configuration property values and user-defined variables should be set through the WebLOAD Recorder. The property descriptions here are intended mainly to explain the lines of code seen in the JavaScript View of the WebLOAD Recorder desktop. Syntax details are also provided for the benefit of users who prefer to manually edit the JavaScript code of their scripts through the IntelliSense editor, described in [*Using the IntelliSense JavaScript Editor* ](#_bookmark18).

**Properties**

The wlVerification object includes the following property classes:

* *Page Time*
* *Page Content Length*
* *Severity*
* *Function*
* *Error Message*

**Methods**

* [*Title (function)*](#title-function)
* [*ContentLength (function)*](#contentlength-function)
* [*MaxPageTime (function)*](#maxpagetime-function)
* [*Text (function)*](#text-function)

**Syntax**

Each individual property class includes the syntax specifications that apply to that class.

**GUI mode**

The wlVerification property and method descriptions explain how to explicitly set values for these response validations within your JavaScript script files.

The recommended way to set response validation values is through the WebLOAD Recorder, using the Response Validation dialog box accessed from the **Home** tab in the WebLOAD Recorder desktop ribbon. The dialog box provide a means of defining and setting response validation values with ease, simplicity, and clarity.

**See also**

* PageContentLength (see [*PageContentLength (property)* ](#pagecontentlength-property))
* PageTime (see [*PageTime (property)* ](#pagetime-property))
* Severity (see [*Severity (property)* ](#severity-property))
* Function (see [*Function (property)* ](#function-property))
* ErrorMessage (see [*ErrorMessage (property)* ](#errormessage-property))
* Title (see [*Title (function)* ](#title-function))

## wlVersion (property)

**Property of Objects**

* document (see [*document (object)* ](#document-object))

**Description**

The HTTP protocol version, which WebLOAD retrieves from the HTTP header (read- only string, for example “1.1”).

**Example**

`currentVersionNumber = document.wlVersion`



## WLXmlDocument() (constructor)

**Method of Object**

* wlXmls (see [*wlXmls (object)* ](#wlxmls-object))

**Description**

Call WLXmlDocument() without any parameters to create a new, blank XML DOM object. The new object may be filled later with any new data you prefer. If the DTD section of your XML document includes any external references, use this form of the WLXmlDocument() constructor to create new XML DOM objects. You may add nodes and post the new XML data to a website as described in the *WebLOAD Scripting Guide*.

Call WLXmlDocument() with a string parameter to create new XML DOM objects from an XML string that includes a completely self-contained DTD section with no external references.

**Syntax**

`new WLXmlDocument([xmlString])`

**Parameters**

| **Parameter Name** | **Description**                                                         |
| ------------------------ | ----------------------------------------------------------------------------- |
| [xmlString]              | Optional string parameter that contains a complete  set of XML document data. |

**Return Value**

Returns a new XML DOM object. If the constructor was called with no parameters, the new object will be empty. If the constructor was called with an XML string, the new object will contain an XML DOM hierarchy based on the XML data found in the parameter string.

**Example**

NewBlankXMLObj = new WLXmlDocument()

-Or-

`NewXMLObj = new WLXmlDocument(xmlStr)`

**Comment**

Objects created by the WLXmlDocument() constructor provide access to the XML DOM Document Interface. They do not expose the HTML property set, (id, innerHTML, and src), as those properties have no meaning for XML DOM objects created this way.

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))



## wlXmls (object)

**Property of Object**

* document (see [*document (object)* ](#document-object))

**Description**

WebLOAD has extended the standard IE Browser DOM document object with the wlXmls collection of XML DOM objects, providing full access to XML structures. Using XML DOM objects, WebLOAD scripts are able to both *access* XML site information, and *generate new XML data* to send back to the server for processing, taking advantage of all the additional benefits that XML provides.

Both WebLOAD and the IE Browser use the MSXML parser to create XML DOM objects. Since WebLOAD XML DOM objects and Browser XML DOM objects are created by the same MSXML parser, the XML DOM objects that are produced for both WebLOAD and the IE Browser are identical.

When working through the IE Browser, XML DOM objects are found in the all collection. When working through WebLOAD, XML DOM objects are found in the wlXmls collection. Since a WebLOAD XML DOM object is identical to an IE Browser XML DOM object, the WebLOAD XML DOM uses the same Document Interface (programming methods and properties) found in the IE Browser XML DOM.

This section describes the wlXmls collection and the properties and methods used most often when working with WebLOAD XML DOM objects. For an explanation of the XML DOM, see the *WebLOAD Scripting Guide*. For a complete list of the XML DOM properties and methods supported by WebLOAD, see *WebLOAD-supported XML DOM Interfaces* .

 **Note:** WebLOAD supports a new method for parsing and manipulating XML data. For more information see [*XML Parser* Object ](#_bookmark563)on page [437.](#_bookmark563)

**Syntax**

XML DOM objects are grouped together within wlXmls collections. The XML DOM objects are arranged in the order in which they appear on the HTML page.

To access an individual XML DOM object’s data and Document Interface, check the length property of the wlXmls collection and use an index number to access the individual XML DOM object.

Access the *HTML properties* for each XML DOM object directly using the following syntax:

document.wlXmls[#].`<*html-DOM property*>`

Access the *XML DOM Document Interface* for each document element directly using the following syntax:

document.wlXmls[#].XMLDocument.documentElement.`<*property*>`

**Example**

To find out how many XML DOM objects are contained within a document, check the value of:

`document.wlXmls.length`

Access the HTML property src as follows:

`document.wlXmls[0].src`

Access the XML DOM document interface as follows:

document.wlXmls[0].XMLDocument.documentElement.nodeName

XML DOM objects may also be accessed directly using the XML ID. For example, if the first XML object on a page is assigned the ID tag myXmlDoc, you could access the object using any of the following:

`MyBookstore = document.wlXmls[0]`

-Or-

`MyBookstore = document.wlXmls.myXmlDoc`

-Or-

`MyBookstore = document.wlXmls[“myXmlDoc”]`

The following example illustrates HTML property usage. Assume you are working with a Web Bookstore site that includes the following inventory database code fragment:

```xml
<xml ID="xmlBookSite">

<?xml version="1.0”?>

<!-- Bookstore inventory database -->

<bookstore>

JavaScript Reference Guide

`<author>`Mark Twain `</author>`

<title>Tom Sawyer</title>

`<price>`$11.00 `</price>`

</book>

JavaScript Reference Guide

`<author>`Oscar Wilde `</author>`

<title>The Giant And His Garden</title>

`<price>`$8.00 `</price>`

</book>

</bookstore>

</xml>
```

When accessing this website, your script may use the standard HTML properties id and innerHTML to print out text strings showing the information found within the XML tags, as follows:

```
var XMLBookstoreDoc = document.wlXmls[0] 

InfoMessage(“ID = “ + XMLBookstoreDoc.id) 

InfoMessage(“HTML text = “ + XMLBookstoreDoc.innerHTML)
```

Running this script produces the following output:

`ID = xmlBookSite`

`HTML text = <?xml version="1.0”?>`

…etc.

**Methods and Properties**

WebLOAD supports all standard W3C XML DOM properties and methods, listed in *WebLOAD-supported XML DOM Interfaces* . These HTML properties and methods are accessed via the XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property)) property. In addition, if the object is constructed from a Data Island, the id (see [*id (property)* ](#_bookmark208)), InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property)), and src (see [*src (property)* ](#src-property)on page [252](#src-property)) HTML properties are exposed. Each property is described in its own section.

* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* WLXmlDocument() (see [*WLXmlDocument() (constructor)* ](#_bookmark500))
* XMLDocument (see [*XMLDocument (property)* ](#xmldocument-property))

**See also**

* [*Collections* ](using_javascript_ref.md#collections)
* [*load() and loadXML() Method Comparison* ](#_bookmark238)
* [*XML Parser* Object ](#_bookmark563)



## Write() (method)

**Method of Object**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

This method writes a string to the output file.



**Parameters**



















































**Syntax** 

Write(string) 

**Example**

MyFileObj = new wlOutputFile(*filename*)

…

MyFileObj.Write(“Happy Birthday”)

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile() (see [*wlOutputFile() (constructor)* ](#_bookmark476))
* Writeln() (see [*Writeln() (method)* ](#_bookmark506))



## Writeln() (method)

**Method of Object**

* wlOutputFile (see [*wlOutputFile (object)* ](#_bookmark475))

**Description**

This method writes a string followed by a newline character to the output file.



**Syntax** 

`Writeln(string)` 

**Parameters**

| **Parameter Name** | **Description**                                |
| ------------------ | ---------------------------------------------- |
| string             | The text string you wish added to the  output. |

**Example**

`MyFileObj = new wlOutputFile(*filename*)`

…

`MyFileObj.Writeln(“Happy Birthday”)`

**See also**

* Close() (see [*Close() (function)* ](#close-function))
* CopyFile() (see [*CopyFile() (function)* ](#_bookmark76))
* Delete() (see [*Delete() (cookie method)* ](#delete-cookie-method))
* [*File Management Functions* ](#_bookmark25)(on page [*28*](#_bookmark25))
* GetLine() (see [*GetLine() (function)* ](#getline-function))
* IncludeFile() (see [*IncludeFile() (function)* ](#_bookmark212))
* Open() (see [*Open() (function)* ](#_bookmark261))
* Reset() (see [*Reset() (method)* ](#_bookmark310))
* [*Using the IntelliSense JavaScript Editor* ](#_bookmark18)
* wlOutputFile() (see [*wlOutputFile() (constructor)* ](#_bookmark476))
* Write() (see [*Write() (method)* ](#_bookmark504))
* 

## XMLDocument (property)

**Method of Object**

* wlXmls (see [*wlXmls (object)* ](#_bookmark502))

**Description**

The XMLDocument property represents the actual XML DOM object. Through XMLDocument you are able to access all the standard XML DOM properties and methods listed in *WebLOAD-Supported XML DOM Interfaces* .

 **Note:** WebLOAD supports a new method for parsing and manipulating XML data. For more information see [*XML Parser* Object ](#_bookmark563)on page [437.](#_bookmark563)

**Syntax**

Use the following syntax:

`document.wlXmls[#].XMLDocument.documentElement.<*property*>` 

XMLDocument is also understood by default. You may access the XML DOM properties and methods without including XMLDocument in the object reference. For

example:

document.wlXmls[0].documentElement.*`<property>`*

However, including XMLDocument is a good programming practice, to emphasize the fact that you are dealing directly with an XML DOM object and not a Data Island.

**Example** document.wlXmls[0].XMLDocument.documentElement.nodeName **See also**

* [*Collections* ](#using_javascript_ref.md#collections)
* id (see [*id (property)* ](#_bookmark208))
* InnerHTML (see [*InnerHTML (property)* ](#innerhtml-property))
* load() (see [*load() (method)* ](#load-method)on page [163](#load-method))
* [*load() and loadXML() Method Comparison* ](./using_javascript_ref.md#collections)
* loadXML() (see [*loadXML() (method)* ](#loadxml-method)on page [167](#loadxml-method))
* src (see [*src (property)* ](#src-property)on page [252](#src-property))
* [*XML Parser* Object ](#_bookmark563)

## XMLParserObject (object)

**Description**

WebLOAD provides an embedded, third-party XML parser object to improve the multi-platform support for XML parsing within the WebLOAD environment. The XML parser object can be used instead of MSXML and Java XML parsing, resulting in lower memory consumption and increased performance during load testing.

The XML parser object can be used to reference any element in an XML document. For example, you can use the XML parser object to generate an Excel file containing the desired details of a specified element.

WebLOAD uses the Open Source Xerces XML parser (see [http://xml.apache.org/xerces-c/](http://xml.apache.org/xercesc/)).

The parse() method, not exposed by the original XML parser, is exposed by WebLOAD. This method is identical to the parseURI() method, except that it receives an XML string instead of a URI.

For more information on the XMLParserObject see [*XML Parser* Object ](#_bookmark563).

**Syntax**

The XML parser object is instanced as follows:

xmlObject = new XMLParserObject();

**Example**

For a detailed example of the implementation of the XML parser object, refer to

[*Example* ](./xmlparser.md#example)

**Methods and Properties**

* For a list of the XMLParserObject’s methods, see [*Methods* ](#_bookmark564).
* For a list of the XMLParserObject’s properties, see [*Properties* ](#_bookmark565).
