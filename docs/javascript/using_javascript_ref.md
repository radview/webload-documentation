# Using the WebLOAD JavaScript Reference

 

The WebLOAD JavaScript programming tools provide a powerful means of adding sophisticated, complex tailoring to recorded scripts. WebLOAD supports literally hundreds of functions, objects, properties, and methods, to provide optimal programming power for your test session script.

 

To simplify access to the WebLOAD JavaScript toolset, this section organizes the functions and objects into major categories, providing you with information to help you locate a specific tool or capability.

 

> **Note:** These categories do not constitute an exhaustive list of all WebLOAD JavaScript objects, properties, methods, and functions. This is simply a list of the major categories, to help you quickly identify the most commonly used items.

 

The WebLOAD JavaScript toolset includes many additional elements. For a complete, alphabetical reference list of all toolset components, see [*WebLOAD Actions, Objects, and Functions* ](./actions_objects_functions.md#webload-actions-objects-and-functions).

**The WebLOAD JavaScript toolset can be organized into the following categories:**

- **Collections**—Meta-objects that serve as arrays or sets of individual objects. 
- **File Management**—Functions used to manage access to a script’s external files. 
- **Identification Components**—Functions and variables used to identify specific elements or points of time during a test session, for clarity in understanding session results and output reports. 
- **Message Functions**—Functions used to display messages in the WebLOAD Console Log Window. 
- **Objects**—A brief introduction to the WebLOAD JavaScript object set. 

- **SSL Cipher Command Suite**—A set of functions and properties that implement full SSL/TLS 1.0 protocol support. 

- **Timing Functions**—Functions used to time or synchronize any operation or group of user activities in a script. 

- **Transaction Verification Components**—Components used to create customized transaction verification functions. 
- **Parameterization**—A brief introduction explanation and reference to all parameterization objects and functions. 

- **Internet Protocol Support**—Objects that implement full support of the complete range of Internet protocols. 

 



## HTTP Components

 

**Properties and Methods of Objects**

- wlGlobals (see [*wlGlobals (object)* ](./actions_objects_functions.md#wlglobals-object))

- wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

- wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))


**Description**

The wlGlobals, wlLocals, and wlHttp objects share a set of components that manage user HTTP activities. This section lists these browser properties and methods. Some of the components are common to all three objects. Some of the properties or methods are used by only one object, and are marked so in the tables.

 

> **Note:** The values assigned in a `wlHttp` object override any global defaults assigned in `wlGlobals` or local defaults in `wlLocals`. WebLOAD uses the `wlGlobals` or `wlLocals` defaults only if you do not assign values to the corresponding properties in the `wlHttp` object.

 

**Syntax**

`NewValue* = wlGlobals.BrowserMethod()` 

`wlGlobals.BrowserProperty = PropertyValue`



**Example**

Each individual property and method includes examples of the syntax for that property.

 

**Methods**

- ClearDNSCache() (see [*ClearDNSCache() (method)* ](./actions_objects_functions.md#cleardnscache-method))

- ClearSSLCache() (see [*ClearSSLCache() (method)* ](./actions_objects_functions.md#clearsslcache-method))



The following methods are for wlHttp objects only:

- CloseConnection() (see [*CloseConnection() (method)* ](./actions_objects_functions.md#closeconnection-method))

- Get() (see [*Get() (transaction method)* ](./actions_objects_functions.md#get-transaction-method))

- Post() (see [*Post() (method)* ](./actions_objects_functions.md#post-method))

- Head() (see [*Head() (method)* ](./actions_objects_functions.md#head-method))



**Data Methods**

- wlClear() (see [*wlClear() (method)* ](./actions_objects_functions.md#wlclear-method))

- wlGet() (see [*wlGet() (method)* ](./actions_objects_functions.md#wlget-method))

- wlSet() (see [*wlSet() (method)* ](./actions_objects_functions.md#wlset-method))





<a name = "figure5"></a>
![Figure 5](../images/figure5.png)




**Properties**

The following properties are for wlHttp objects only

 

**Data Properties**

- Data (see [*Data (property)* ](./actions_objects_functions.md#data-property))

- DataFile (see [*DataFile (property)* ](./actions_objects_functions.md#datafile-property))

- Erase (see [*Erase (property)* ](./actions_objects_functions.md#erase-property))

- FileName (see [*FileName (property)* ](./actions_objects_functions.md#filename-property))

- FormData (see [*FormData (property)* ](./actions_objects_functions.md#formdata-property))

- Header (see [*Header (property)* ](./actions_objects_functions.md#header-property))


- DataCollection.type (see [*type (property)* ](./actions_objects_functions.md#type-property))

- DataCollection.value (see [*value (property)* ](./actions_objects_functions.md#value-property))




The following properties are used by wlHttp, wlLocals, and wlGlobals objects unless otherwise noted.

 

**Configuration Properties**

- ConnectionSpeed (see [*ConnectionSpeed (property)* ](./actions_objects_functions.md#connectionspeed-property)) (wlGlobals only)

- DisableSleep (see [*DisableSleep (property)* ](./actions_objects_functions.md#disablesleep-property))

- DNSUseCache (see [*DNSUseCache (property)* ](./actions_objects_functions.md#dnsusecache-property))

- KeepAlive (see [*KeepAlive (property)* ](./actions_objects_functions.md#keepalive-property))

- LoadGeneratorThreads (see [*LoadGeneratorThreads (property)* ](./actions_objects_functions.md#loadgeneratorthreads-property))

- MultiIPSupport see [*MultiIPSupport (property)* ](./actions_objects_functions.md#multiipsupport-property)

- NTUserName, NTPassWord (see [*NTUserName, NTPassWord (properties)* ](./actions_objects_functions.md#ntusername-ntpassword-properties))

- Outfile (see [*Outfile (property)* ](./actions_objects_functions.md#outfile-property))

- PassWord (see [*PassWord (property)* ](./actions_objects_functions.md#password-property))

- ProbingClientThreads (see [*ProbingClientThreads (property)* ](./actions_objects_functions.md#probingclientthreads-property))

- Proxy, ProxyUserName, ProxyPassWord (see [*Proxy, ProxyUserName, ProxyPassWord (properties)* ](./actions_objects_functions.md#proxy-proxyusername-proxypassword-properties)

- RedirectionLimit (see [*RedirectionLimit (property)* ](./actions_objects_functions.md#redirectionlimit-property))

- SaveSource (see [*SaveSource (property)* ](./actions_objects_functions.md#savesource-property))

- SaveTransaction (see [*SaveTransaction (property)* ](./actions_objects_functions.md#savetransaction-property)) (wlGlobals only)

- SSLBitLimit (see [*SSLBitLimit (property)* ](./actions_objects_functions.md#sslbitlimit-property)) (wlGlobals only)

- SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](./actions_objects_functions.md#sslcryptostrength-property))) (wlGlobals

- only)

- SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile, SSLClientCertificatePassword (properties)* ](./actions_objects_functions.md#sslclientcertificatefile-sslclientcertificatepassword-properties))

- SSLUseCache (see [*SSLUseCache (property)* ](./actions_objects_functions.md#sslusecache-property))

- SSLVersion (see [*SSLVersion (property)* ](./actions_objects_functions.md#sslversion-property))

- type (see [*type (property)* ](./actions_objects_functions.md#type-property))

- Url (see [*Url (property)* ](./actions_objects_functions.md#url-property))

- UserAgent (see [*UserAgent (property)* ](./actions_objects_functions.md#useragent-property))

- UserName (see [*UserName (property)* ](./actions_objects_functions.md#username-property)))

- UsingTimer (see [*UsingTimer (property)* ](./actions_objects_functions.md#usingtimer-property))

- Version (see [*Version (property)* ](./actions_objects_functions.md#version-property))

- wlTarget (see [*wlTarget (property)* ](./actions_objects_functions.md#wltarget-property))



**See also**

- wlGlobals (see [*wlGlobals (object)* ](./actions_objects_functions.md#wlglobals-object))

- wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

- wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))


 

## Collections

 

**Description**

Collections are arrays or sets of individual objects. For example, the elements collection refers to a collection of individual element objects.

 

Access individual members of a collection either through an index number or directly through the member’s name or ID. The following three syntax choices are equivalent:

- `Collection[index#]`
- `Collection["ID"] `
- `Collection.ID`



Test session scripts work with all browser DOM collections and objects. The recommended way to access these objects is through the classic browser `document` object, via the relevant collection. For example, access a table through:

- `document.links[0]`


 

**Properties**

Each collection of objects includes the single property length, which contains the size of the collection, that is, the number of objects included in this collection. You may also use the index value to access individual objects from within a collection.

 

For example, to find out how many `images` objects are contained within the `images` collection of a document, check the value of:

`document.images.length`



In this *Guide*, the description of each individual object includes information on the collection, if any, to which that object belongs.

 



## File Management Functions

 

**Description**

These functions manage access to a script’s function and input files, including opening and closing files, copying files, specifying include files, and reading lines from ASCII input files.

> **Note:** Input file management is also provided by wlInputFile (see [*wlInputFile (object)* ](./actions_objects_functions.md#wlinputfile-object)). Output file management is also provided by wlOutputFile (see [*wlOutputFile (object)* ](./actions_objects_functions.md#wloutputfile-object)).

 

**See also**

- Close() (see [*Close() (function)* ](./actions_objects_functions.md#close-function))

- CopyFile() (see [*CopyFile() (function)* ](./actions_objects_functions.md#copyfile-function))

- Delete() (see [*Delete() (cookie method)* ](./actions_objects_functions.md#delete-cookie-method))

- GetLine() (wlOutputFile) (see [*GetLine() (function)* ](./actions_objects_functions.md#getline-function))

- GetLine() (wlInputFile) (see [*GetLine() (method)* ](./actions_objects_functions.md#getline-method))

- IncludeFile() (see [*IncludeFile() (function)* ](./actions_objects_functions.md#includefile-function))

- Open() (wlOutputFile) (see [*Open() (function)* ](./actions_objects_functions.md#open-function))

- Open() (wlInputFile) (see [*Open() (method)* ](./actions_objects_functions.md#open-method))

- Reset() (see [*Reset() (method)* ](./actions_objects_functions.md#reset-method))

- Using the IntelliSense JavaScript Editor 

- wlOutputFile() (see [*wlOutputFile (object)* ](./actions_objects_functions.md#wloutputfile-object))

- wlInputFile() (see [*wlInputFile (object)* ](./actions_objects_functions.md#wlinputfile-object)))

- Write() (see [*Write() (method)* ](./actions_objects_functions.md#write-method))

- Writeln() (see [*Writeln() (method)* ](./actions_objects_functions.md#write-method))




 

## Identification Variables and Functions

 

**Description**

For performance statistics to be meaningful, testers must be able to identify the exact point being measured. WebLOAD therefore provides the following identification variables and functions:

- Two variables, ClientNum (see [*ClientNum (property)* ](./actions_objects_functions.md#clientnum-property)) and RoundNum, (see [*RoundNum (variable)* ](./actions_objects_functions.md#roundnum-variable)) identify the client and round number of the current script instance.

- The GeneratorName() (see [*GeneratorName() (function)* ](./actions_objects_functions.md#generatorname-function)) function identifies the current Load Generator.

- The GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](./actions_objects_functions.md#getoperatingsystem-function)) function identifies the operating system of the current Load Generator.

- The VCUniqueID() (see [*VCUniqueID() (function)* ](./actions_objects_functions.md#vcuniqueid-function)) function identifies the current Virtual Client instance.


 

**Example**

The following example illustrates common use of these variables and functions. Use these variables and function to support the WebLOAD measurement features and obtain meaningful performance statistics.

Suppose your script submits data to a server on an HTML form. You want to label one of the form fields so you can tell which WebLOAD client submitted the data, and in which round of the main script.

You can do this using a combination of the` ClientNum` and `RoundNum` variables. Together, these variables uniquely identify the WebLOAD client and round. For example, you can submit a string such as the following in a form field:

 

`"C" + ClientNum.toString() + "R" + RoundNum.toString()`



**GUI mode**

WebLOAD recommends accessing these identification variables and functions through the WebLOAD Recorder. All the variables that appear in this list are available for use at all times in a script file. In the WebLOAD Recorder main window, click **Variable Windows** in the **Debug** tab of the ribbon.

For example, it is convenient to add `ClientNum to a Message Node to clarify which client sent the messages that appear in the WebLOAD Console Log window.



**See also**

- ClientNum (see [*ClientNum (property)* ](./actions_objects_functions.md#clientnum-property))

- GeneratorName() (see [*GeneratorName() (function)* ](./actions_objects_functions.md#generatorname-function))

- GetOperatingSystem() (see [*GetOperatingSystem() (function)* ](./actions_objects_functions.md#getoperatingsystem-function))

- RoundNum (see [*RoundNum (variable)* ](./actions_objects_functions.md#roundnum-variable))

- VCUniqueID() (see [*VCUniqueID() (function)* ](./actions_objects_functions.md#vcuniqueid-function))




## Message Functions

 

**Description**

These functions display messages in the Log Window of WebLOAD Recorder or Console. Some of the functions raise errors and interrupt test session execution. For information on using the Log Window and on message types, see the *WebLOAD Console User’s Guide*.

 

**Example**

In the following example, the script attempts to download an HTML page. If it fails on the first try, it pauses for 3 minutes and tries again. If it fails on the second try, it aborts the current round.

 

```javascript
function InitClient() {
    wlLocals.Url = "http://www.ABCDEF.com/index.html"
}
//First try 
wlHttp.Get()
if (document.wlStatusNumber != 200) { 
    InfoMessage("Thread " + ClientNum.toString() +
    " pausing for 3 min") 
    Sleep(180000)
  //Second try
    wlHttp.Get()
    if (document.wlStatusNumber != 200) { 
      ErrorMessage("Aborting round " + RoundNum.toString() + " 
      of thread " + ClientNum.toString())
    }   // End of second try
}
```



**GUI mode**

 

> **Note:** Message functions are usually accessed and inserted into script files directly through the WebLOAD Recorder. Message function commands can be added to the script in Visual Editing mode using the Toolbox message item and the Insert menu command. The JavaScript code line that corresponds to this message function appears in the JavaScript View pane.
        Message function command lines may also be added directly to the code in a JavaScript Object within a script through the IntelliSense Editor, described in [*Using the IntelliSense JavaScript Editor* ](./intro_java_scripts.md#using-the-intellisense-javascript-editor).
        Messages can also be added to the script using the Toolbox Message icon . Drag the Message icon to the Script Tree. The Message dialog box appears. Type or select the information to appear in the message. Use double quotes to include a string value, or click  to select a variable. Select the severity of the message from the Message Severity drop-down list.

 

**See also**

- *Error Management* in the *WebLOAD Scripting Guide*
- ErrorMessage() (see [*ErrorMessage() (function)* ](./actions_objects_functions.md#errormessage-function))

- GetMessage() (see [*GetMessage() (method)* ](./actions_objects_functions.md#getmessage-method))

- GetSeverity() (see [*GetSeverity() (method)* ](./actions_objects_functions.md#getseverity-method))

- InfoMessage() (see [*InfoMessage() (function)* ](./actions_objects_functions.md#infomessage-function))

- [*Message Functions* ](#message-functions)

- ReportLog() (see [*ReportLog() (method)* ](./actions_objects_functions.md#reportlog-method))

- SevereErrorMessage() (see [*SevereErrorMessage() (function)* ](./actions_objects_functions.md#severeerrormessage-function))

- [*Using the IntelliSense JavaScript Editor* ](./intro_java_scripts.md#using-the-intellisense-javascript-editor)

- WarningMessage() (see [*WarningMessage() (function)* ](./actions_objects_functions.md#warningmessage-function))

- wlException (see [*wlException (object)* ](./actions_objects_functions.md#wlexception-object))

- wlException() (see [*wlException() (constructor)* ](./actions_objects_functions.md#wlexception-constructor))




## Objects

 

**Description**

[*WebLOAD scripts Work with an Extended Version of the Standard DOM* ](./intro_java_scripts.md#webload-scripts-work-with-an-extended-version-of-the-standard-dom)presents an overview of the Document Object Model (DOM), describing some of the basic objects used by standard Web browsers when working with HTML Web pages. The classic browser DOM includes a wide range of objects, properties, and methods for maximum utility and versatility. For more information about the standard DOM structure and components, go to the following websites:

- [http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/introduction.html](http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/introduction.html)

- [http://msdn.microsoft.com/library/default.asp?url=/workshop/author/dom/domoverview.asp](http://msdn.microsoft.com/library/default.asp?url=/workshop/author/dom/domoverview.asp)

- [http://msdn.microsoft.com/library/default.asp?url=/workshop/author/dhtml/refere nce/dhtmlrefs.asp](http://msdn.microsoft.com/library/default.asp?url=/workshop/author/dhtml/refere nce/dhtmlrefs.asp)



Since WebLOAD emulates the HTTP activities included in a test session, WebLOAD supports the standard DOM object set that implements those activities. Only the DOM objects, properties, and methods of special interest to WebLOAD programmers working with test session scripts are listed here. This guide also includes reference material for the objects, properties, and methods that were added by WebLOAD as extensions to the basic DOM, to implement specific test session features.



Website testing usually means testing how typical user activities are handled by the application being tested. Are the user actions managed quickly, correctly and appropriately? Is the application responsive to the user’s requests? Will the typical user be happy working with this application? When verifying that an application handles user activities correctly, WebLOAD usually focuses on the user activities, recording user actions through WebLOAD Recorder when initially creating scripts and recreating those actions during subsequent test sessions. The focus on user activities represents a high-level, conceptual approach to test session design.



Sometimes a tester may prefer to use a low-level, "nuts-and-bolts" approach that focuses on specific internal implementation commands, such as HTTP transactions. The WebLOAD DOM extension set includes objects, methods, properties, and functions that support this approach. Items in the *WebLOAD JavaScript Reference Guide* that are relevant to the HTTP Transaction Mode are noted as such in the entry.



## SSL Cipher Command Suite

 

**Description**

WebLOAD provides full SSL/TLS 1.0/TLS 1.2 protocol support through a set of SSL properties for the wlGlobals object combined with a set of functions called the Cipher Command Suite. These SSL functions allow you to identify, enable, and disable selected SSL protocols or security levels. For a complete list of the supported SSL protocols, see [*SSL Ciphers – Complete List* ](./appendix_a.md#ssl-ciphers-complete-list)

 

**Functions**

The Cipher Command Suite includes the following functions:

- SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](./actions_objects_functions.md#sslciphersuitecommand-function))

- SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](./actions_objects_functions.md#ssldisablecipherid-function))

- SSLDisableCipherName() (see [*SSLDisableCipherName() (function)* ](./actions_objects_functions.md#ssldisableciphername-function))

- SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](./actions_objects_functions.md#sslenablecipherid-function))

- SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](./actions_objects_functions.md#sslenableciphername-function))

- SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](./actions_objects_functions.md#sslgetciphercount-function))

- SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](./actions_objects_functions.md#sslgetcipherid-function))

- SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](./actions_objects_functions.md#sslgetcipherinfo-function))

- SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](./actions_objects_functions.md#sslgetciphername-function))

- SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](./actions_objects_functions.md#sslgetcipherstrength-function))

- SSLEnableStrength() (see [*SSLEnableStrength() (function)* ](./actions_objects_functions.md#sslenablestrength-function))



**Comment**

Use the Cipher Command Suite to check or verify SSL configuration information at any point in your script. However, any *changes* to a script’s SSL property configuration, whether through the `wlGlobals` properties or the Cipher Command Suite functions, must be made in the script’s *initialization functions*. Configuration changes made in the `InitAgenda()` function will affect all client threads spawned during that script’s test session. Configuration changes made in the `InitClient()` function will affect only individual clients. Do not make changes to the SSL property configuration using `wlHttp` or `wlLocals` properties or in a script’s main body. The results will be undefined for all subsequent transactions.

 

**See also**

- [*HTTP Components* ](./using_javascript_ref.md#http-components)
- SSLBitLimit (see [*SSLBitLimit (property)* ](./actions_objects_functions.md#sslbitlimit-property)) (wlGlobals only)

- SSLCipherSuiteCommand() (see [*SSLCipherSuiteCommand() (function)* ](./actions_objects_functions.md#sslciphersuitecommand-function))

- SSLClientCertificateFile, SSLClientCertificatePassword (see [*SSLClientCertificateFile, SSLClientCertificatePassword (properties)* ](./actions_objects_functions.md#sslclientcertificatefile-sslclientcertificatepassword-properties))

- SSLCryptoStrength (see [*SSLCryptoStrength (property)* ](./actions_objects_functions.md#sslcryptostrength-property)) (wlGlobals only)

- SSLDisableCipherID() (see [*SSLDisableCipherID() (function)* ](./actions_objects_functions.md#ssldisablecipherid-function))

- SSLDisableCipherName() (see [*SSLDisableCipherName() (function)* ](./actions_objects_functions.md#ssldisableciphername-function)

- SSLEnableCipherID() (see [*SSLEnableCipherID() (function)* ](./actions_objects_functions.md#sslenablecipherid-function))

- SSLEnableCipherName() (see [*SSLEnableCipherName() (function)* ](./actions_objects_functions.md#sslenableciphername-function))

- SSLGetCipherCount() (see [*SSLGetCipherCount() (function)* ](./actions_objects_functions.md#sslgetciphercount-function))

- SSLGetCipherID() (see [*SSLGetCipherID() (function)* ](./actions_objects_functions.md#sslgetcipherid-function))

- SSLGetCipherInfo() (see [*SSLGetCipherInfo() (function)* ](./actions_objects_functions.md#sslgetcipherinfo-function))

- SSLGetCipherName() (see [*SSLGetCipherName() (function)* ](./actions_objects_functions.md#sslgetciphername-function))

- SSLGetCipherStrength() (see [*SSLGetCipherStrength() (function)* ](./actions_objects_functions.md#sslgetcipherstrength-function))

- SSLUseCache (see [*SSLUseCache (property)* ](./actions_objects_functions.md#sslusecache-property))

- SSLEnableStrength() (see [*SSLEnableStrength() (function)* ](./actions_objects_functions.md#sslenablestrength-function))

- SSLVersion (see [*SSLVersion (property)* ](./actions_objects_functions.md#sslversion-property))

- wlGlobals (see [*wlGlobals (object)* ](./actions_objects_functions.md#wlglobals-object))

- wlHttp (see [*wlHttp (object)* ](./actions_objects_functions.md#wlhttp-object))

- wlLocals (see [*wlLocals (object)* ](./actions_objects_functions.md#wllocals-object))


 

## Timing Functions

 

**Description**

The timer functions let you time or synchronize any operation or group of user activities in a script, such as a navigation or mouse click, and send the time statistics to the WebLOAD Console.

 

**Example**

The following script connects to the home Web page of company. On every fifth round, the script also connects to a second Web page. The script uses different timers to measure the time for each connection.

> **Note:** This script fragment contains a main script only.



WebLOAD reports three time statistics:

- The round time, which includes both connections.

- `Page 1 Time`, reported in every round for the first connection only.

- `Page 2 Time`, reported in every fifth round for the second connection only.



```javascript
SetTimer("Page 1 Time") 
wlHttp.Get("http://www.ABCDEF.com")
SendTimer("Page 1 Time")
if (RoundNum%5 == 0) { 
   SetTimer("Page 2 Time")
   wlHttp.Get("http://www.ABCDEF.com/product_info.html")
   SendTimer("Page 2 Time")
}
```



**Functions**

The set of timer functions includes the following:

- SendCounter() (see [*SendCounter() (function)* ](./actions_objects_functions.md#sendcounter-function)))

- SendMeasurement() (see [*SendMeasurement() (function)* ](./actions_objects_functions.md#sendmeasurement-function))

- SendTimer() (see [*SendTimer() (function)* ](./actions_objects_functions.md#sendtimer-function))

- SetTimer() (see [*SetTimer() (function)* ](./actions_objects_functions.md#settimer-function))

- Sleep() (see [*Sleep() (function)* ](./actions_objects_functions.md#sleep-function))

- SynchronizationPoint() (see [*SynchronizationPoint() (function)* ](./actions_objects_functions.md#synchronizationpoint-function))




## Parameterization

Parameterization enables you to edit a script containing static values and transform it into a script that will run multiple variations of the static values.

When recording a script, WebLOAD captures the data that is being sent, including login details, user selections, and entered text. When running the script under load, simulating many users, it is desirable to use variations in the data, so as to simulate the application more realistically. To do so, you can replace the static values with parameters.

Parameter values can come from a file, or be automatically generated numbers, strings and dates. Using parameterization enables you to specify how the script should select values from the data file. For example:

- Order considerations – Whether to randomly select values from the data file, or use them in the order they appear.

- Uniqueness considerations – Whether the same value can be used at the same time by different virtual clients.




You can also specify the update policy, which defines when a new value will be read or calculated. For example, whether to update the value on each round, or once at the beginning of the test.

In addition to defining a data file, you can also use parameterization to define a random number format, date/time format, and string format. These can also be used to replace static values. For example, if the online shop delivers books between 1-14 days from the date of purchase, you can define a random number format of 1-14 and replace the static desired delivery period value with a call to the random number format.

 

**Functions**

The set of parameterization functions includes the following:

- wlTimeParam() (see [*wlTimeParam() (parameterization)* ](./actions_objects_functions.md#wltimeparam-parameterization))

- wlDataFileParam() (see [*wlDataFileParam() (parameterization)* ](./actions_objects_functions.md#wldatafileparam-parameterization))

- wlNumberParam() (see [*wlNumberParam() (parameterization)* ](./actions_objects_functions.md#wlnumberparam-parameterization))

- wlStringParam() (see [*wlStringParam() (parameterization)* ](./actions_objects_functions.md#wlstringparam-parameterization))




## Transaction Verification Components

 

**Description**

Customized transaction verification functions are created out of the following components:

- BeginTransaction() (see [*BeginTransaction() (function)* ](./actions_objects_functions.md#begintransaction-function)

- CreateDOM() (see [*CreateDOM() (function)* ](./actions_objects_functions.md#createdom-function))

- CreateTable() (see [*CreateTable() (function)* ](./actions_objects_functions.md#createtable-function))

- EndTransaction() (see [*EndTransaction() (function)* ](./actions_objects_functions.md#endtransaction-function))

- ReportEvent() (see [*ReportEvent() (function)* ](./actions_objects_functions.md#reportevent-function))

- SetFailureReason() (see [*SetFailureReason() (function)* ](./actions_objects_functions.md#setfailurereason-function))

- VerificationFunction() (user-defined) (see [*VerificationFunction() (user-defined)(function)* ](./actions_objects_functions.md#verificationfunction-user-defined-function))

  


**See also**

- TimeoutSeverity (see [*TimeoutSeverity (property)* ](./actions_objects_functions.md#timeoutseverity-property))

- TransactionTime (see [*TransactionTime (property)* ](./actions_objects_functions.md#transactiontime-property))




 

 

 

 

 