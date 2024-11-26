# WebLOAD Internet Protocols Reference

This chapter provides detailed reference information on WebLOAD support for the following Internet protocols

- FTP, through the wlFTP Object and wlFTPs Object(for secure SSL connections)

- IMAP, through the wlIMAP Object

- NNTP, through the wlNNTP Object

- POP, through the wlPOP Object and wlPOPs Object (for secure SSL connections)

- SMTP, through the wlSMTP Object and wlSMTPs Object (for secure SSL connections)

- TCP, through the wlTCP Object

- Telnet, through the wlTelnet Object

- UDP, through the wlUDP Object

## wlFTP Object

The wlFTP object provides support for FTP (File Transfer Protocol) load and functional testing within WebLOAD. Support for standard FTP operation is included. FTP over secure connections (SSL) is supported through the [wlFTPs Object ](#_bookmark519).

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate `Logon()` method; otherwise an exception is thrown.

To access the wlFTP object, you must include the wlFtp.js file in your ``InitAgenda()`` function.

 

### wlFTP Properties

#### Data

The Data property lets you specify the local data stream to upload to the host. You use this property to upload data. For example:

`ftp.Data = *datastream*`

 

#### DataFile

The DataFile property lets you specify the local file to upload to the host. For example:

`ftp.DataFile = filename`

 

#### document

The document property is an array containing the files downloaded and uploaded in the current FTP session. For example:

`var recentdownload = *ftp.document[1]`*

 

#### Outfile

The Outfile property lets you specify the name of a downloaded file. You use this property to rename a downloaded file as it is transferred to your computer. This property must be an explicit file name, not a pattern. If you specify the Outfile property, the document property remains empty. If you are downloading a series of files, only the last file downloaded is stored in the Outfile.

 

If you want to store all of the files downloaded, either delete the Outfile property or specify an empty value. The downloaded files are then stored in the document property. For example:

`ftp.Outfile = filename`

 

#### PassiveMode

The PassiveMode property lets you use FTP through firewalls. Valid values are:

- true - passive mode is set, and you may FTP through firewalls.

- false - active mode is set, and you may not FTP through firewalls. For example:

- ftp.PassiveMode = *modesetting*

  

#### PassWord

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted FTP host. WebLOAD automatically sends the password to the FTP host when a wlFTP object connects to an FTP host.

`ftp.PassWord = *password*`



> **Caution:** The password appears in plain text in the script. The password is visible to any user who has access to the script.

 

#### Size

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption.

`var filesize = *ftp.Size*`

 

#### StartByte

The StartByte property lets you specify the byte offset to start transferring from. The default value is **0**. This property automatically resets to zero after each transfer. You use this property to specify a starting point when resuming interrupted transfers.

`ftp.StartByte = *byteoffset*`



#### TransferMode

The TransferMode property lets you specify the transfer mode for uploaded and downloaded files. You must specify the transfer mode before each transfer. If you do not specify a transfer mode, auto, the default mode, is used. Valid values are:

- **auto** - 0
- **text** - 1
- **binary** - 2



You may also specify the transfer mode using the following constants:

- WLFtp.TMODE_ASCII - text

- WLFtp.TMODE_BINARY - binary

- WLFtp.TMODE_DEFAULT - auto



For example:

`ftp.TransferMode = *transfermode*`



 

 

#### UserName

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted FTP host. WebLOAD automatically sends the user name to the FTP host when a wlFTP object connects to an FTP host.

`ftp.UserName = *username*`

 

### wlFTP Methods

 

#### Append()

| **Syntax**       | Append(pattern)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file to which you are appending. This may be a  specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Similar to the Upload() method, Append()  adds the data to the target file instead of overwriting it. If the target  file does not exist, Append() creates it. |

 

#### AppendFile()

| **Syntax**       | AppendFile(filename)                                         |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The remote file to which you want to append data.            |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uploads a local file and  appends it to the specified file on the host. The local file is specified by  the DataFile property. The destination file is specified by the filename  parameter. If  the DataFile property is not specified, then the contents of the Data  property are sent as a datastream to be appended to the file specified by the  filename parameter. If the target  file does not exist, AppendFile() creates it. |

 

#### ChangeDir()

| **Syntax**       | ChangeDir(*name*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the directory to which you want  to move.        |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Changes the current working directory on the host  to the one specified by the name parameter. |

 

#### ChFileMod()

| **Syntax**       | ChFileMod(filename,  *attributes*)                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The name of the file you want to alter. This  parameter may be a specific file name, or it may contain wildcards. |
| attributes       | The new attributes assigned to the file. Values  are specified in the three digit 0-7 format. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Changes attributes of the specified file according  to the values specified in the attribute parameter. |

 

#### ChMod()

| **Syntax**       | ChMod(*pattern*,  *attributes*)                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The name of the files and  directories you want to alter. This parameter may be a specific file name, or  it may contain wildcards. |
| attributes       | The new attributes assigned to the file.  Values are specified in the three digit 0-7 format. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uses a loop to changes attributes of the specified  files and directories according to the values specified in the attribute  parameter. If  an iteration of the loop fails, the loop is cancelled, potentially leaving  some files unchanged. To avoid this risk you must write your own loop with  error handling capability. |

 

#### Delete()

| **Syntax**       | Delete(pattern)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are deleting.  This may be a specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Deletes the specified  files from the FTP host. This function calls the DeleteFile() method in a  loop to delete all the specified files. If an iteration of the loop fails,  the loop is cancelled, potentially leaving some files undeleted. |

 

#### DeleteFile()

| **Syntax**       | Delete(filename)                                             |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The file you are deleting. This must be a  specific file name. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the specified file from the FTP  host.               |

 

#### Dir()

| **Syntax**       | Dir(pattern)                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The name of the file or directory for which  you are searching. This may be a specific file name, or it may contain  wildcards. |
| **Return Value** | Returns a JavaScript array with the  following members if successful, an exception if unsuccessful.  a[].fileName     //  name of file a[].fileAttributes // attribute  string  a[].fileTime     //  date and time of last modification  a[].fileSize     // size of file in bytes  a[].isDir       // 1 if the entry represents a  directory, 0 for a file     
**Note:** If the host supports only basic information, only the  fileName property of the array is defined. |
| **Comments**     | Lists files and directories that match the pattern  parameter in the current directory of the host. This method returns detailed  information if the server supports it. |

 

#### Download()

| **Syntax**       | Download(pattern)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are  downloading. This may be a specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uses a loop to download  the specified files to the local computer. If the property has been set, the  data is saved to the specified file. If the Outfile property has not been  set, the file is saved with its current name. If an iteration of the loop  fails, the loop is cancelled, potentially leaving some files not downloaded. |



####  DownloadFile()

| **Syntax**       | Download(filename)                                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The file you are downloading. This must be  a specific file name. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Downloads a file to the  local computer. If the property has been set, the data is saved to the  specified file. If the Outfile property has not been set, the file is saved  with its current name. |

 

#### GetCurrentPath()



| **Syntax**       | GetCurrentPath()                                             |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the current path if  successful, an exception if unsuccessful. |
| **Comments**     | Returns the current path on the host.                        |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the current path if  successful, an exception if unsuccessful. |
| **Comments**     | A string containing the latest response  string if successful, an exception if unsuccessful. |

 

#### ListLocalFiles()

 

| **Syntax**       | ListLocalFiles(filter)                                       |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filter           | The files you want to  list. The filter may be a patter or a specific file name. |
| **Return Value** | An array of matching objects with following  properties if successful, an exception if unsuccessful.  a[].fileName    // A string containing name of the file  a[].isDir    // A Boolean, true if the entry  represents a directory |
| **Comments**     | Lists files matching the filter parameter in the  current directory of the local computer. |

 

#### Logoff()

 

| **Syntax**       | Logoff()                                           |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the FTP host.           |

 

#### `Logon()`

 

| **Syntax**       | Logon(*host*,  [*port*])                                     |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default FTP port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts a conversation with the FTP host. If you  are logging on to a restricted site, you must have specified the UserName and  PassWord properties before using this method. |

 

#### MakeDir()

 

| **Syntax**       | MakeDir(*name*)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the new directory that you are  creating.        |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Creates a new directory beneath the current  directory on the host. |

 

#### RemoveDir()

 

| **Syntax**       | RemoveDir(*name*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the directory that you are  deleting.            |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the named directory from the host.  <br>**Note:** You may not delete a directory until that directory is empty. Remove  all files from the directory before using the RemoveDir() method. You may use the Delete() method to delete files on the host. |





#### Rename()

 

| **Syntax**       | Rename(*from*,  *to*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| from             | The file that you want to rename.                            |
| to               | The new file name for the  file. If this file already exists, it is overwritten. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Renames the files in the current directory  described by the from  parameter to the name described in the to parameter. |

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without modification.  This method is useful for interacting directly with the host using  non-standard or unsupported extensions. |

 

#### Upload()

 

| **Syntax**       | Upload(*pattern*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are uploading. This may be a specific  file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Uses a loop to upload the  local files specified by the pattern parameter to the host. The  file is not renamed, and values specified by the DataFile and Data property are ignored. If an iteration of the loop  fails, the loop is cancelled, potentially leaving some files not transported. |



 

 

#### UploadFile()

 

| **Syntax**       | UploadFile(filename)                                         |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The destination name of  the local file. This parameter may be the same name as the local file name,  or it may be used to rename the file once it arrives at the host. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uploads a local file to  the host. The local file is specified by the DataFile property. The  destination file name is specified by the filename parameter. If the DataFile property is not specified, then the contents of  the Data property are sent as a datastream to be  saved under the name specified by the filename parameter. |

 

#### UploadUnique()

 

| **Syntax**       | UploadUnique()                                               |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  name of the newly created file if successful, an exception if unsuccessful. |
| **Comments**     | Uploads data or a file to  a newly created, unique file on the host. The file name is created by the  host, and returned as a string value. The local file is specified by the  DataFile property. If the DataFile property is not specified, then the  contents of the Data property are sent as a datastream. |

 

#### WLFtp()

 

| **Syntax**       | new WLFtp()                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlFTP object.                                          |
| **Comments**     | Creates a new wlFTP object, used to  interact with the server. |
| **Example**      | function **InitClient()**{ myNewFtpObject = new WLFtp()  }   |

 

### FTP Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** {

// include the file that enables FTP IncludeFile("wlFtp.js",WLExecuteScript)

}

function **InitClient()**{

 

// Create the FTP object we need to interact with the server ftp=new WLFtp()

}

function **TerminateClient()**{

// Delete the FTP object we used delete ftp

}

//===================================================

 

//**Body Of script**. Give user name and password and login ftp.UserName="UserID" // Set the user name ftp.PassWord="TopSecret"  // Set the password

//this.PassiveMode=true;  // Enable this if firewall is in the way ftp.Logon("localhost") // Login to the server

//===================================================

 

//**Test Download**

ftp.TransferMode = ftp.TMODE_ASCII; // Force all downloads ASCII ftp.Outfile="c:\\downloaded.txt";

// Define a local file to save the downloaded file ftp.Download("file.txt");  // Grab the remote file

// The remote file may be a wildcard, so for each file

// downloaded an entry is made in the document array.

// With this approach an Outfile is not required. Instead the

// document object holds the downloaded files for this client.

// The loop below loops through each entry in the document

// array and writes the file contents out to the log for (var i = 0; i < ftp.document.length; i++)

{

InfoMessage(ftp.document[i]);

}

//============================================================

 

//**Test Upload**

ftp.TransferMode = ftp.TMODE_ASCII; ftp.DataFile="c:\\upload.txt";

// define local file to upload ftp.UploadFile("hello.txt");

// upload it to the remote host as "hello.txt" ftp.Data="hello world";

// define a string to send to the remote host ftp.UploadFile("hello.txt");

// upload the string and save it as "hello.txt"

//=======================================================

 

 

//**Test Append**

ftp.TransferMode = ftp.TMODE_ASCII; ftp.DataFile="c:\\append.txt";

// identify a local file to upload ftp.AppendFile("hello.txt");

// add it to the existing contents of "hello.txt"

//========================================================

 

//**Test Delete**

ftp.Delete("hello.txt");

// delete "hello.txt" from the remote server

//===========================================================

 

//**Test Directory Functions**

ftp.MakeDir("DirectoryName");   // make a new directory ftp.ChangeDir("DirectoryName");  // change to that directory ftp.DataFile="c:\\file1.txt"; // select a local file ftp.Upload("file1.txt");   // upload it to the new directory var files = ftp.Dir("*.*");

// Generate a list of the files in that directory for (var i = 0 ; i < files.length; i++)

{

InfoMessage("the file name is:" + files[i].fileName);

// Print each file's name to the log

}

ftp.Delete("*.*");     // delete the files on the directory ftp.ChangeDir("..");  // go up a level in the tree ftp.RemoveDir("DirectoryName");  // delete the directory itself

//=========================================================

 

//**Test Advanced Directory Handling**

var files = ftp.Dir("*.txt"); // show all the text files

if (files.length > 0)    // **IF** there are any entries to go through

{          // **THEN** print their detailed attributes to the log for (var i = 0 ; i < files.length; i++)

{             // **Print** each file's details to the log InfoMessage(files[0].fileName);   // name InfoMessage(files[0].fileAttributes);  // attributes InfoMessage(files[0].fileTime);     // timestamp InfoMessage(files[0].fileSize);     // size in bytes InfoMessage(files[0].dirFlag);

// set when the object is a directory

}



 

 

}

//==========================================================

 

//**Test General Functions**

status = ftp.GetStatusLine();

// what was the last response from the server?

InfoMessage("status= "+ status);  // print it path = ftp.GetCurrentPath();    // where am I? InfoMessage("path="+ path);   // right here

//==============================================================

 

catch (e)

{

InfoMessage ("Error" + e)

}

ftp.Logoff()       // do not forget to log out of the session InfoMessage("done") // this is the end of the FTP sample script
```

 

 

## wlFTPs Object

 

The wlFTPs object provides support for FTP (File Transfer Protocol) load and functional testing over secure connections (SSL).

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate `Logon()` method; otherwise an exception is thrown.

 

To access the wlFTPs object, you must include the wlFtps.js file in your `InitAgenda()` function.

 

### wlFTPs Properties

 

#### Data

 

The Data property lets you specify the local data stream to upload to the host. You use this property to upload data. For example:

 

`ftp.Data = *datastream*`



 

 

#### DataFile

 

The DataFile property lets you specify the local file to upload to the host. For example:

 

`ftp.DataFile = filename`

 

#### document

 

The document property is an array containing the files downloaded and uploaded in the current FTP session. For example:

 

`var recentdownload = *ftp.document[1]*`

 

#### Outfile

 

The Outfile property lets you specify the name of a downloaded file. You use this property to rename a downloaded file as it is transferred to your computer. This property must be an explicit file name, not a pattern. If you specify the Outfile property, the document property remains empty. If you are downloading a series of files, only the last file downloaded is stored in the Outfile.

 

If you want to store all of the files downloaded, either delete the Outfile property or specify an empty value. The downloaded files are then stored in the document property. For example:

 

`ftp.Outfile = filename`

 

#### PassiveMode

 

The PassiveMode property lets you use FTP through firewalls. Valid values are:

- **true** – Passive mode is set, and you may FTP through firewalls.
- **false** – Active mode is set, and you may not FTP through firewalls. 



For example:

`ftp.PassiveMode = modesetting`

 

#### PassWord

 

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted FTP host. WebLOAD automatically sends the password to the FTP host when a wlFTP object connects to an FTP host.

 

`ftp.PassWord = *password*`



> **Caution:** The password appears in plain text in the script. The password is visible to any user who has access to the script.



####  Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption.

 

`var filesize = *ftp.Size*`

 

#### StartByte

 

The StartByte property lets you specify the byte offset to start transferring from. The default value is **0**. This property automatically resets to zero after each transfer. You use this property to specify a starting point when resuming interrupted transfers.

 

`ftp.StartByte = *byteoffset*`

 

#### TransferMode

 

The TransferMode property lets you specify the transfer mode for uploaded and downloaded files. You must specify the transfer mode before each transfer. 



If you do not specify a transfer mode, auto, the default mode, is used. Valid values are:

- **auto** – 0
- **text** – 1

- **binary** – 2



You may also specify the transfer mode using the following constants: 

- WLFtp.TMODE_ASCII – text

- WLFtp.TMODE_BINARY – binary

- WLFtp.TMODE_DEFAULT – auto 



For example:

`ftp.TransferMode = *transfermode*`

 

#### UserName

 

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted FTP host. WebLOAD automatically sends the user name to the FTP host when a wlFTP object connects to an FTP host.

 

`ftp.UserName = *username*`



### wlFTPs Methods

 

#### Append()

 

| **Syntax**       | Append(pattern)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file to which you are appending. This  may be a specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Similar to the Upload() method, Append()  adds the data to the target file instead of overwriting it. If the target  file does not exist, Append() creates it. |

 

#### AppendFile()

 

| **Syntax**       | AppendFile(filename)                                         |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The remote file to which you want to append  data.           |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uploads a local file and  appends it to the specified file on the host. The local file is specified by  the DataFile property. The destination file is specified by the filename  parameter. If  the DataFile property is not specified, then the contents of the Data  property are sent as a datastream to be appended to the file specified by the  filename parameter. If the target  file does not exist, AppendFile() creates it. |

 

#### ChangeDir()

 

| **Syntax**       | ChangeDir(*name*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the directory to which you want  to move.        |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Changes the current working directory on  the host to the one specified by the name parameter. |

 

#### ChFileMod()

 

| **Syntax**       | ChFileMod(filename,  *attributes*)                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The name of the file you want to alter. This  parameter may be a specific file name, or it may contain wildcards. |
| attributes       | The new attributes assigned to the file.  Values are specified in the three digit 0-7 format. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Changes attributes of the specified file  according to the values specified in the attribute parameter. |

 

#### ChMod()

 

| **Syntax**       | ChMod(*pattern*,  *attributes*)                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The name of the files and  directories you want to alter. This parameter may be a specific file name, or  it may contain wildcards. |
| attributes       | The new attributes assigned to the file.  Values are specified in the three digit 0-7 format. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uses a loop to changes attributes of the  specified files and directories according to the values specified in the attribute  parameter. If  an iteration of the loop fails, the loop is cancelled, potentially leaving  some files unchanged. To avoid this risk you must write your own loop with  error handling capability. |

 

#### Delete()

 

| **Syntax**       | Delete(pattern)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are deleting.  This may be a specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the specified  files from the FTP host. This function calls the DeleteFile() method in a  loop to delete all the specified files. If an iteration of the loop fails,  the loop is cancelled, potentially leaving some files undeleted. |

 

#### DeleteFile()

 

| **Syntax**       | Delete(filename)                                             |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The file you are deleting. This must be a  specific file name. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Deletes the specified file from the FTP host.                |

 

#### Dir()

 

| **Syntax**       | Dir(pattern)                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The name of the file or  directory for which you are searching. This may be a specific file name, or  it may contain wildcards. |
| **Return Value** | Returns a JavaScript array with the  following members if successful, an exception if unsuccessful.  a[].fileName      //  name of file a[].fileAttributes // attribute  string  a[].fileTime       //  date and time of last modification  a[].fileSize        // size of  file in bytes  a[].isDir          // 1 if the entry  represents a directory, 0 for a file  **Note:** If the host supports only  basic information, only the fileName property of the array is defined. |
| **Comments**     | Lists files and directories that match the  pattern parameter in the current directory of the host. This method returns  detailed information if the server supports it. |

 

#### Download()

 

| **Syntax**       | Download(pattern)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are  downloading. This may be a specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uses a loop to download  the specified files to the local computer. If the property has been set, the  data is saved to the specified file. If the Outfile property has not been  set, the file is saved with its current name. If an iteration of the loop  fails, the loop is cancelled, potentially leaving some files not downloaded. |

 

#### DownloadFile()

 

| **Syntax**       | Download(filename)                                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The file you are downloading. This must be a  specific file name. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Downloads a file to the  local computer. If the property has been set, the data is saved to the  specified file. If the Outfile property has not been set, the file is saved  with its current name. |



#### GetCurrentPath()

 

| **Syntax**       | GetCurrentPath()                                             |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the current path if  successful, an exception if unsuccessful. |
| **Comments**     | Returns the current path on the host.                        |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  current path if successful, an exception if unsuccessful. |
| **Comments**     | A string containing the latest response  string if successful, an exception if unsuccessful. |

 

#### ListLocalFiles()

 

| **Syntax**       | ListLocalFiles(filter)                                       |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filter           | The files you want to  list. The filter may be a patter or a specific file name. |
| **Return Value** | An array of matching objects with following  properties if successful, an exception if unsuccessful.  a[].fileName // A string containing name of the  file  a[].isDir      // A Boolean, true if the entry  represents a directory |
| **Comments**     | Lists files matching the filter parameter  in the current directory of the local computer. |

 

#### Logoff()

 

| **Syntax**       | Logoff()                                           |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the FTP host.           |



 

 

#### `Logon()`



| **Syntax**       | Logon(*host*,  [*port*])                                     |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default FTP port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts a conversation with the FTP host. If you  are logging on to a restricted site, you must have specified the UserName and  PassWord properties before using this method. |

 

#### MakeDir()

 

| **Syntax**       | MakeDir(*name*)                                              |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the new directory that you are  creating.        |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Creates a new directory beneath the current  directory on the host. |

 

#### RemoveDir()

 

| **Syntax**       | RemoveDir(*name*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| name             | The name of the directory that you are  deleting.            |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the named directory from the host.  **Note:** You may not delete a directory until that directory is empty. Remove  all files from the directory before using the RemoveDir() method. You may use the Delete() method to delete files on the host. |

 

#### Rename()

 

| **Syntax**       | Rename(*from*,  *to*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| from             | The file that you want to rename.                            |
| to               | The new file name for the  file. If this file already exists, it is overwritten. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Renames the  files in the current directory described by the from  parameter  to the name described in the to  parameter. |



#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |

 

#### Upload()

 

| **Syntax**       | Upload(*pattern*)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The file you are uploading. This may be a  specific file name, or it may contain wildcards. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uses a loop to upload the  local files specified by the pattern parameter to the host. The  file is not renamed, and values specified by the DataFile and Data property are ignored. If an iteration of the loop  fails, the loop is cancelled, potentially leaving some files not transported. |

 

#### UploadFile()

 

| **Syntax**       | UploadFile(filename)                                         |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| filename         | The destination name of  the local file. This parameter may be the same name as the local file name,  or it may be used to rename the  file once it arrives at the host. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Uploads a local file to  the host. The local file is specified by the DataFile property. The  destination file name is specified by the filename parameter. If the DataFile property is not specified, then the contents of  the Data property are sent as a datastream to be  saved under the name specified by the filename parameter. |



  

#### UploadUnique()

 

| **Syntax**       | UploadUnique()                                               |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  name of the newly created file if successful, an exception if unsuccessful. |
| **Comments**     | Uploads data or a file to  a newly created, unique file on the host. The file name is created by the  host, and returned as a string value. The local file is specified by the  DataFile property. If the DataFile property is not specified, then the  contents of the Data property are sent as a datastream. |

 

#### WLFtps()

 

| **Syntax**       | new WLFtps()                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlFTPs object.                                         |
| **Comments**     | Creates a new wlFTPs object, used to  interact with the server. |
| **Example**      | function **InitClient()**{ myNewFtpsObject = new WLFtps()  } |

 

 





## wlHtmMailer Object

 

The wlHtmMailer object provides support for HTM Mail load and functional testing within WebLOAD. Support for standard HTM Mail operation is included. HTM Mail over secure connections (SSL) is not currently supported.

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

You must include catch and try functions in your script to handle exceptions when using the wlHtmMailer object. If you do not, the object may cause your script to freeze. A sample catch appears in the wlHtmMailer code sample at the end of this section.



To access the wlHtmMailer object, you must include the wlHtmMailer.js file in your `InitAgenda()` function.

 

### wlHtmMailer Properties

 

#### AttachmentsArr

 

The AttachmentsArr property lets you specify one or more attachments for an email. The filename variable should contain the name of the local file or datastream that you want to attach to the posting. 



For example:

`wlHtmMailer.Attachments[0] = *filename`*

 

#### Bcc

 

The Bcc property lets you specify the email addresses of additional recipients to be blind copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [m>". For example:

 

`wlHtmMailer.Bcc = *blindcopyaddresses*`

 

#### Cc

 

The Cc property lets you specify the email addresses of additional recipients to be copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name [m>". For example:

 

wlHtmMailer.Cc = copyaddress; *copyaddress*

 

#### From

 

The From property lets you describe the Reply To in plain language. You may use this property to identify your Reply To email address in a plain language format. For example:

 

wlHtmlMailer.From = *replyname*

 

#### Host

 

The Host property lets you specify a host for use in sending HTML email messages.



 

 

#### HtmlFilePath

 

The HtmlFilePath property specifies the full path directory location of the files associated with the email message.

 

#### HtmlText

 

The HtmlText property contains the HTML-formatted version of the email message, for example, potentially including embedded images. The corresponding plain text version of the email message is provided in the Message property.

 

#### Message

 

The Message property contains the plain text version of the email message. If there is a corresponding HTML-formatted version, for example, including embedded images, this version is provided in the HtmlText property.

 

#### MessageDate

 

The MessageDate property contains the date of the email message.

 

#### ReplyTo

 

The ReplyTo property lets you specify the return address of your email. You may specify multiple addresses in a semicolon-separated list. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [](mailto:Me@MyCompany.com)". For example:

 

`wlHtmMailer.ReplyTo = replyaddress`

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. For example:

 

`var filesize = wlHtmMailer.Size`

 

#### Subject

 

The Subject property lets you specify the text appearing the subject field of your email. You use this property to provide a brief description of the contents of your email. For example:

 

`wlHtmMailer.Subject = subjectheader`

 

#### To

The To property lets you specify a recipient's email address. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name ["](mailto:Me@MyCompany.com). For example:

 

`wlHtmMailer.To = recipientaddress; recipientaddress`

 

### wlHtmMailer Methods

 

#### AddAttachment()

 

| **Syntax**       | AddAttachment(*string*,  *type*, [*encoding*])               |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending  to the host. If you are sending a file, the string is the location and name  of the file. If you are sending a data attachment, the string is the data to  be attached. |
| type             | The type of attachment you are sending.  Valid values are:  File (default)  Data |
| [encoding]       | The type of encoding to apply to the file. Valid  values are:  7Bit (default) Quoted Base64 8Bit  8BitBinary |
| **Return Value** | Returns an integer value  Attachment ID if successful, an exception if unsuccessful. |
| **Comments**     | Adds an attachment to the message.                           |

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  describe the host using its DNS number, or by giving its name. |
| [port]           | The port to which you are  connecting. If you do not specify a port, the default session port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts a new session with the host.                          |



 

#### DeleteAttachment()

 

| **Syntax**       | DeleteAttachment(*string*)                         |
| ---------------- | -------------------------------------------------- |
| **Parameters**   |                                                    |
| string           | The ID of the attachment you are deleting.         |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Removes an attachment from the article.            |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the host.               |

 

#### DisplayMetrics()

 

| **Syntax**       | DisplayMetrics()                                             |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string with the current metrics values.                    |
| **Comments**     | Displays all the information gathered from  the last command or data transfer. |

 

#### GetLocalHost()

 

| **Syntax**       | GetLocalHost()                                               |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Identification information for the  currently active local host. |
| **Comments**     | Returns identification information for the  current local host. |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the latest response  string if successful, an exception if unsuccessful. |
| **Comments**     | Returns the latest response string from the  host.           |

 

#### Send()

 

| **Syntax**       | Send()                                                       |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Sends mail to recipients, attaching files using  MIME as necessary. After sending the attachments, data is deleted. |



 

 

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |

 

#### SetLocalHost()

 

| **Syntax**       | SetLocalHost(*hostname*)                                     |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| hostname         | Identification information for the new  local host.          |
| **Return Value** | Assigns a new value for the local host.                      |
| **Comments**     | Defines the local host from which the  emails are being sent. |

 

#### Verify()

 

| **Syntax**       | Verify()                                                     |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Returns a 1 if the address  is valid, a 0 if the address is invalid. If the method is unable to verify  the address due to authentication or other reasons, it returns an exception. |
| **Comments**     | Checks that the address in the To property is valid. To use this method, include  only one address in the To  property. |

 

#### WLHtmMailer()

 

| **Syntax**       | new WLHtmMailer()                                            |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlHtmMailer object.                                    |
| **Comments**     | Creates a new wlHtmMailer  object, used to interact with the server. |
| **Example**      | function **InitClient()** { myNewHtmMailerObject = new WLHtmMailer();  } |



 

##  wlIMAP Object

 

The wlIMAP object provides support for IMAP4 (Internet Message Access Protocol) load and functional testing within WebLOAD. Support for standard IMAP operation is included. IMAP over secure connections (SSL) is not currently supported.

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

To access the wlIMAP object, you must include the wlImap.js file in your

`InitAgenda()` function.

 

### wlIMAP Properties

 

#### CurrentMessage

 

The CurrentMessage property returns the number of the current message. You use this property to track the current message in relation to other messages on the host. 



For example:

`var currentmessagenumber = imap.CurrentMessage`

 

#### CurrentMessageID

 

The CurrentMessageID property returns the ID of the current message. You use this property to track the current message in relation to other messages on the host. For example:

 

`var messagenumber = imap.CurrentMessageID`

 

#### document

 

The document property is an object with four properties:

- Headers – A string containing the header of the message

- MessageText – A string containing the text of the message

- Size – An integer describing the size of the message in bytes

- Attachments – An array of objects, with each attachment existing as an object with the following properties:

- contentencoding – The encoding of the attachment

- contenttype – The content type of the attachment

- filename – The file name of the attachment

- messagetext – The text of the attachment

- partname – The part name of the message

- size – The size of the attachment in bytes\n For example:

- var recentdocument = *imap.document*

- var messageheaders = *recentdocument.MessageHeaders*

- var messagetext = *recentdocument.MessageText*

- var messagesize = *recentdocument.MessageSize*

- var messageattachments = *recentdocument.attachments*




#### Mailbox

 

The Mailbox property specifies the name of the mailbox with which you want to interact. You use this property to create, edit, and delete mailboxes. 



For example: 

`imap.Mailbox = mailboxname`

 

#### MaxLines

The MaxLines property lets you specify the maximum number of lines per email to retrieve from an IMAP host. You use this property to specify the number of lines to retrieve from each email. 



For example: 

`imap.Maxlines = numberoflines`

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save a file or message locally on your computer. When you write to the Outfile, you overwrite the existing content. To avoid overwriting the existing content, you must specify a new Outfile each time you write.



For example: 

`imap.Outfile = filename`

 

#### PassWord

 

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted IMAP host. WebLOAD automatically sends the password to the IMAP host when a wlIMAP object connects to an IMAP host. 



For example: 

`imap.PassWord = password`



#### Size

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. 



For example: 

*`var filesize = imap.Size`*

 

#### UserName

 

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted IMAP host. WebLOAD automatically sends the user name to the IMAP host when a wlIMAP object connects to an IMAP host.



For example: 

`imap.UserName = username`

 

### wlIMAP Methods

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  describe the host using its DNS number, or by giving its name. |
| port             | The port to which you are  connecting. If you do not specify a port, the default IMAP port (port 143) is  used. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Starts an IMAP session  with the host. When you connect, you are connecting to a specific mailbox  within the host, as specified by your User ID. |

 

#### CreateMailbox()

 

| **Syntax**       | CreateMailbox()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Creates the mailbox  specified in the Mailbox property. The created mailboxes continue to exist  after the end of the script. To remove a mailbox, use the DeleteMailbox()  method. |



#### Delete()

 

| **Syntax**       | Delete([*MessageSet*])                                       |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| MessageSet       | The identifier of the  message you want to delete. You may specify a single message number, or you  may specify a range, separated by a colon. For example, 1:10 deletes messages  one through ten. If you do not specify a message ID, the current message is  deleted. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Deletes the message with  the corresponding ID. If no ID is specified, then the current message is  deleted. |

 

#### DeleteMailbox()

 

| **Syntax**       | DeleteMailbox()                                        |
| ---------------- | ------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.     |
| **Comments**     | Deletes the mailbox specified in the Mailbox property. |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                      |
| ---------------- | ------------------------------------------------- |
| **Return Value** | Null if successful, an exception if unsuccessful. |
| **Comments**     | Terminates a connection to the IMAP host.         |

 

#### GetMessageCount()

 

| **Syntax**       | GetMessageCount()                                            |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the number of messages on the  host if successful, an exception if unsuccessful. |
| **Comments**     | Returns the number of messages waiting on  the host.         |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the latest response  string if successful, an exception if unsuccessful. |
| **Comments**     | Returns the latest response string from the  host.           |



#### ListMailboxes()

| **Syntax**       | ListMailboxes(pattern)                                       |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| pattern          | The mailbox that you want to appear in the list.  This may be a specific name, or it may contain wildcards. |
| **Return Value** | A string listing the  matching mailboxes if successful, an exception if unsuccessful. |
| **Comments**     | Lists mailboxes matching the pattern parameter.              |

 

#### RecentMessageCount()

| **Syntax**       | RecentMessageCount()                                         |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  number of new messages on the host if successful, an exception if  unsuccessful. |
| **Comments**     | Returns the number of new messages waiting on the  host.     |

 

#### RenameMailbox()

| **Syntax**       | RenameMailbox(*string*)                                 |
| ---------------- | ------------------------------------------------------- |
| **Parameters**   |                                                         |
| string           | The new name for the mailbox.                           |
| **Return Value** | Null if successful, an exception if  unsuccessful.      |
| **Comments**     | Renames the mailbox specified in the  Mailbox property. |

 

#### Retrieve()

 

| **Syntax**       | Retrieve([*MessageSet*])                                     |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| MessageSet       | The identifier of the  message you want to retrieve. You may specify a single message number, or you  may specify a range, separated by a colon. For example, 1:10 returns messages  one through ten. If you do not specify a message ID, the next message is returned. |
| **Return Value** | A document for each  message specified if successful, an exception if unsuccessful. |
| **Comments**     | Returns the message with the corresponding  ID. If no ID is specified, then the next message is returned. |



 

 

#### Search()

 

| **Syntax**       | Search(*string*)                                             |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The criteria for your search. Valid values are: <br> **ALL** – All messages in the mailbox -  this is the default initial key for AND-ing.  <br/>**ANSWERED** – Messages with the  \\Answered flag set.  <br/>**BCC** – Messages that contain the  specified string in the envelope structure's BCC field.  <br/>**BEFORE** – Messages whose internal date is  earlier than the specified date.  <br/>**BODY** – Messages that contain the  specified string in the body of the message.  <br/>**CC** – Messages that contain  the specified string in the envelope structure's CC field.  <br/>**DELETED** – Messages with the  \\Deleted flag set.  <br/>**DRAFT** – Messages with the  \\Draft flag set.  <br/>**FLAGGED** – Messages with the  \\Flagged flag set.  <br/>**FROM** – Messages that contain the  specified string in the envelope structure's FROM field.  <br/>**HEADER** – Messages that have a header with the specified field- name (as  defined in ) and that contains the specified string in the field-body.  <br/>**KEYWORD** – Messages with the specified keyword set.  <br/>**LARGER** – Messages with an size larger than the specified number of octets.<br/>**NEW**  Messages that have the \\Recent flag set but not the  \\Seen flag. This is functionally equivalent to  "(RECENT UNSEEN)".   <br/>**NOT** – Messages that do not  match the specified search key.   <br/>**OLD** –  Messages that do not have the \\Recent flag set. This is functionally  equivalent to "NOT RECENT" (as opposed to "NOT NEW").  **ON** – Messages whose internal  date is within the specified date.   <br/>**OR** – Messages that match either  search key.  <br/>**RECENT** – Messages that  have the \\Recent flag set.  <br/>**SEEN** –  Messages that have the \\Seen flag set.  <br/> **SENTBEFORE** – Messages whose Date:  header is earlier than the specified date.   <br/>**SENTON** – Messages whose Date: header is  within the specified date.   <br/>**SENTSINCE** – Messages whose Date: header is  within or later than the specified date. <br/>  **SINCE** – Messages whose internal date is  within or later than the specified date.  <br/> **SMALLER** – Messages with an  RFC822.SIZE smaller than the specified number of octets. <br/>  **SUBJECT** – Messages that contain  the specified string in the envelope structure's SUBJECT field. <br/>  **TEXT** – Messages that contain the specified string in the header or body of  the message.  <br/> **TO** – Messages that contain  the specified string in the envelope structure's TO field. <br/>  **UID** – Messages with unique  identifiers corresponding to the specified unique identifier set.  <br/> **UNANSWERED** – Messages that do not have the  \\Answered flag set. <br/>  **UNDELETED** – Messages that do not  have the \\Deleted flag set.  <br/> **UNDRAFT** – Messages that do not  have the \\Draft flag set.  <br/> **UNFLAGGED** – Messages that do not have the \\Flagged flag set.  <br/> **UNKEYWORD** – Messages that do not have the specified keyword set.  <br/> **UNSEEN** – Messages that do not  have the \\Seen flag set. |
| **Return Value** | A string containing the  IDs of messages that meet the search criteria if successful, an exception if  unsuccessful. |
| **Comments**     | Searches the current  mailbox for messages meeting the specified search criteria. |



  

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |

 

#### SubscribeMailbox()

 

| **Syntax**       | SubscribeMailbox()                                           |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Subscribes to the mailbox specified in the Mailbox property. |

 

#### UnsubscribeMailbox()

 

| **Syntax**       | UnsubscribeMailbox()                                         |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Unsubscribes from the mailbox specified in  the Mailbox  property. |

 

#### WLImap()

 

| **Syntax**       | new WLImap()                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlIMAP object.                                         |
| **Comments**     | Creates a new wlIMAP object, used to  interact with the server. |
| **Example**      | function **InitClient()** { myNewImapObject = new WLImap() myNewImapObject.Connect("HostName")  } |



 

 

### IMAP Sample Code

```javascript
// **script Initialization**
function ** `InitAgenda()` ** {
    IncludeFile("wlImap.js", WLExecuteScript)
}

function ** InitClient() ** {
    imap = new WLImap() // create the new IMAP object
    // imap.Connect("HostName"); // connect to the server
}

function ** TerminateClient() ** {
    imap.Disconnect(); // logout from the server delete imap     // delete the IMAP object
}
//===================================================
// **Body Of script**
InfoMessage("Speed: " + wlGlobals.ConnectionSpeed) wlGlobals.Debug = 1;
imap.UserName = "UserID";
imap.PassWord = "TopSecret";
imap.Mailbox = "Inbox";
imap.Connect("00.0.0.00");
//==================================================
//**Test Retrieve**
/*imap.Retrieve("100");

for (var i = 0; i < imap.wlSource.length; i++)

{

InfoMessage(imap.wlSource[i]); InfoMessage(imap.document.length); InfoMessage(imap.document[i].headers); InfoMessage(imap.document[i].messageText); InfoMessage(imap.document[i].size); InfoMessage(imap.document[i].attachments.length);

for (var j = 0; j < imap.document[i].attachments.length; j++)

{

InfoMessage(imap.document[i].attachments[j].contentEncoding); InfoMessage(imap.document[i].attachments[j].contentType); InfoMessage(imap.document[i].attachments[j].filename); InfoMessage(imap.document[i].attachments[j].messageText); InfoMessage(imap.document[i].attachments[j].partName); InfoMessage(imap.document[i].attachments[j].size);

}



 

 

}*/
//===========================================================
//**Test Delete**
imap.Mailbox = "Inbox";
InfoMessage(imap.GetMessageCount());
imap.Mailbox = "Inbox";
imap.Delete("2");
imap.Mailbox = "Inbox";
InfoMessage(imap.GetMessageCount());
//==========================================================
//**Test Mailbox Functions:**
//      list mailboxes, create mailbox, and then list again
/*InfoMessage("mailboxes are:") var v1 = imap.ListMailboxes(); for(var i=0; i < v1.length; i++)

InfoMessage(v1[i]); imap.Mailbox="mailboxname"; imap.CreateMailbox(); InfoMessage("mailboxes are:") var v1 = imap.ListMailboxes(); for(var i=0; i < v1.length; i++)

InfoMessage(v1[i]);

*/
//=======================================================
//      subscribe mailbox, list all subscribed mailboxes
//imap.Mailbox="mailboxname";
//imap.SubscribeMailbox();
/*InfoMessage("subscribed mailboxes are:") var v2 = imap.ListSubscribedMailboxes(); for(var j=0; j < v2.length; j++)

{

InfoMessage(v2[j]); imap.Mailbox=v2[j];

}*/
//=======================================================
//         list subscribed mailboxes,unsubscribe mailbox,
//           and then list all subscribed mailboxes again
/*InfoMessage("subscribed mailboxes are:") var v2 = imap.ListSubscribedMailboxes(); for(var j=0; j < v2.length; j++)

{

InfoMessage(v2[j]);



 

 

imap.Mailbox=v2[j];

}

imap.Mailbox="mailboxname"; imap.UnsubscribeMailbox(); InfoMessage("subscribed mailboxes are:") var v2 = imap.ListSubscribedMailboxes(); for(var j=0; j < v2.length; j++)

{

InfoMessage(v2[j]); imap.Mailbox=v2[j];

}

*/
//====================================================
//            list mailboxes, rename mailbox,
//            and then list mailboxes again
/*InfoMessage("mailboxes are:") var v1 = imap.ListMailboxes(); for(var i=0; i < v1.length; i++)

InfoMessage(v1[i]); imap.Mailbox="boxname"; imap.RenameMailbox("newName"); InfoMessage("mailboxes are:") var v1 = imap.ListMailboxes(); for(var i=0; i < v1.length; i++)

InfoMessage(v1[i]);

*/
//======================================================
//            get number of messages from a mailbox
/*imap.Mailbox="main"; InfoMessage(imap.GetMessageCount()); imap.Mailbox="Inbox"; InfoMessage(imap.GetRecentMessageCount());

*/
//====================================================
//            delete mailbox and list all the mailboxes
/*imap.Mailbox="mailboxname"; 

imap.DeleteMailbox(); InfoMessage("subscribed mailboxes are:") var v2 = imap.ListSubscribedMailboxes(); for(var j=0; j < v2.length; j++)

{

InfoMessage(v2[j]); 

imap.Mailbox=v2[j];

}



 

 

*/
//=========================================================
//            search
/*imap.Mailbox="Inbox";

var found = imap.Search("CC [user@address.com");](mailto:user@address.com) InfoMessage("found:")

for(var j=0; j < found.length; j++)

{

InfoMessage(found[j]);

}

catch (e)

{

InfoMessage ("Error" + e)

}

*/
//===========================================================
imap.Disconnect();
delete imap
InfoMessage("done")
```

 





## wlNNTP Object

 

The wlNNTP (Network News Transfer Protocol) object provides support for NNTP load and functional testing within WebLOAD. Support for standard NNTP operation is included. NNTP over secure connections (SSL) is not currently supported.

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

You must include catch and try functions in your script to handle exceptions when using the wlNNTP object. If you do not, the object may cause your script to freeze. A sample catch appears in the NNTP code sample at the end of this section.

 

To access the wlNNTP object, you must include the wlNntp.js file in your

`InitAgenda()` function.



 

 

### wlNNTP Properties

 

#### ArticleText

 

The ArticleText property lets you specify the text appearing in the body of your article. You use this property to write the text of the article itself. 



For example:

`nntp.ArticleText = *articlecontent*`

 

#### Attachments

 

The Attachments property lets you specify an attachment to a posting. The filename variable should contain the name of the local file or datastream that you want to attach to the posting. For example:

 

`nntp.Attachments = filename`

 

#### AttachmentsEncoding

 

The AttachmentsEncoding property lets you specify the type of encoding you are applying to a message attachment. This property must be specified for each attachment. 



Valid values are:

- 7Bit
- Quoted

- Base64

- 8Bit

- 8BitBinary



You may also specify the encoding using the following constants: 

- WLNntp.ENC_7BIT – 7bit encoding

- WLNntp.ENC_QUOTED – Quoted Printable encoding

- WLNntp.ENC_BASE64 – Base64 encoding

- WLNntp.ENC_8BIT – 8Bit encoding

- WLNntp.ENC_8BITBINARY – Binary encoding For example:

- nntp.AttachmentsEncoding = *encodingtype*








#### AttachmentsTypes

 

The AttachmentsTypes property lets you specify the type of attachment you are including in a posting. This property must be specified for each attachment. 

Valid values are: 

- **true** – Specifies a type of file
- **false** – Specifies a type of data 



For example:

`nntp.AttachmentsTypes = typeofattachment`

 

#### Document

 

The Document property is an object with two properties. One is a string, MessageText containing the text of the article, and the other is an array containing the article attachments and headers. 



For example:

var recentdocument = *nntp.document*

var messagetext = *recentdocument.MessageText*

var messageattachments = *recentdocument.attachments*

var firstattachment = *messageattachments[0]*

var secondattachment = *messageattachments[1]*

 

#### From

 

The From property lets you describe the Reply To in plain language. You may use this property to identify your Reply To email address in a plain language format. 



For example: 

`nntp.From = replyname`

 

#### Group

 

The Group property specifies the article group with which you are interacting. You use this to limit searches, posts, and other activities to a specific group. For example:

 

`nntp.Group = groupname`

 

#### MaxHeadersLength

 

The MaxHeadersLength property lets you specify the maximum length for headers in an article. You use this property to prevent line folding. For example:

 

`nntp.MaxHeadersLength = headersize`

 

#### Organization

 

The Organization property identifies the affiliation of the author. You use this property to identify your professional or personal affiliation. For example:

 

`nntp.Organization = organizationname`

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save a file or article locally on your computer. For example:

 

`nntp.Outfile = filename`

 

#### PassWord

 

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted NNTP host. WebLOAD automatically sends the password to the NNTP host when a wlNNTP object connects to an NNTP host. For example:

 

`nntp.PassWord = *password*`

> **Caution:** The password appears in plain text in the script. The password is visible to any user who has access to the script.

 

#### References

 

The References property lets you specify articles that the posted article follows. You use this property to create a thread of related articles. If the resulting reference header is longer than the limit specified in the MaxHeadersLength property, it is folded.

References must be separated by commas with no spaces in between. For example:

 

`nntp.References = article1,article2`

 

#### ReplyTo

 

The ReplyTo property lets you specify the reply address for additional postings. For example:

 

`nntp.ReplyTo = replyaddress`

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. For example:

 

`var filesize = nntp.Size`



 

 

#### Subject

 

The Subject property lets you specify the text appearing the subject field of your email. You use this property to provide a brief description of the contents of your article. For example:

 

`nntp.Subject = subjectheader`

 

#### To

 

The To property lets you specify the newsgroup to receive your posting. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every article. For example:

 

`nntp.To = alt.newsgroup.name; rec.newsgroup.name`

 

#### UserName

 

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted NNTP host. WebLOAD automatically sends the user name to the NNTP host when a wlNNTP object connects to an NNTP host. For example:

 

`nntp.UserName = username`

 

### wlNNTP Methods

 

#### AddAttachment()

 

| **Syntax**       | AddAttachment(*string*,  *type*, [*encoding*])               |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending  to the host. If you are sending a file, the string is the location and name  of the file. If you are sending a data attachment, the string is the data to  be attached. |
| type             | The type of attachment you are sending.  Valid values are:  File (default)  Data |
| [encoding]       | The type of encoding to apply to the file.  Valid values are:  7Bit (default) Quoted Base64 8Bit  8BitBinary |
| **Return Value** | Returns an integer value  Attachment ID if successful, an exception if unsuccessful. |
| **Comments**     | Adds an attachment to the message.                           |



####  Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You  may describe the host using its DNS number, or by giving its name. |
| [port]           | The port to which you are  connecting. If you do not specify a port, the default session port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts a new session with the host.                          |

 

#### DeleteAttachment()

 

| **Syntax**       | DeleteAttachment(*string*)                         |
| ---------------- | -------------------------------------------------- |
| **Parameters**   |                                                    |
| string           | The ID of the attachment you are deleting.         |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Removes an attachment from the article.            |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the host.               |

 

#### GetArticle()

 

| **Syntax**       | GetArticle(*messageNumber*)                                  |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| message  Number  | The number of the message that you want to  retrieve.        |
| **Return Value** | Null if successful. The article is stored  in the document property. An exception if unsuccessful. |
| **Comments**     | Gets the headers and body  of the article specified in the messageNumber parameter for the group specified in the Group  property. If  the Outfile property is specified, the  returned article is stored in the output file as well as in the document  property. |



  

#### GetArticleCount()

 

| **Syntax**       | GetArticleCount()                                            |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | An integer count of the  number of articles in the group if successful, an exception if unsuccessful. |
| **Comments**     | Returns the number of articles in the group  specified by the  Group property. |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  latest response string if successful, an exception if unsuccessful. |
| **Comments**     | Returns the latest response string from the host.            |

 

#### GroupOverview()

 

| **Syntax**       | GroupOverview([*range*])                                     |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| [range]          | The range for articles you  want to view. The format for range is first-last, where first is "" (an empty string) or  positive number, and last is "", a positive number, or the token end. |
| **Return Value** | An array of objects if  successful. Each object contains one article, and the properties articleDate, articleLines, articleNumber, from, messageID, otherHeaders, references, and subject. The method returns an  exception if unsuccessful. |
| **Comments**     | Returns an overview for  the articles in range for the group specified in the Group property. |

 

#### ListGroups()

 

| **Syntax**       | ListGroups([*startDate*])                                    |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| [startDate]      | The earliest creation date  to search. Groups created before this date are not listed. If you do not  specify a start date, all groups are listed.  The format for startDate is YYMMDD HHMMSS. |
| **Return Value** | An array of objects if  successful. Each object contains the following properties, Canpost, lastArticle, firstArticle, and group. The method returns an  exception if unsuccessful. |
| **Comments**     | Lists the newsgroups available on the host.                  |



  

#### PostArticle()

 

| **Syntax**       | PostArticle()                                                |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful. The article is stored  in the document property. An exception if unsuccessful. |
| **Comments**     | Posts the article to the  host, attaching files using MIME as necessary. The article is constructed  using the following properties and methods:  **Header  Properties**  From Subject  Organization To  ReplyTo References MaxHeadersLength  **Body Properties/Methods** ArticleText() AddAttachment()  DeleteAttachment() |

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |



 

 

#### WLNntp()

 

| **Syntax**       | new WLNntp()                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlNNTP object.                                         |
| **Comments**     | Creates a new wlNNTP object, used to interact with  the server. |
| **Example**      | myNewNntpObject  = new WLNntp()                              |

 

### NNTP Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** { IncludeFile("wlNntp.js",WLExecuteScript)

}

//===================================================

 

//**Body Of script**

InfoMessage("Speed: "+wlGlobals.ConnectionSpeed) nntp=new WLNntp()

wlGlobals.Debug=1; InfoMessage("before login") nntp.UserName="UserID" nntp.PassWord="TopSecret" nntp.Connect("hostname")

//=========================================================

 

//**Test ListGoups**

/*v = nntp.ListGroups(); InfoMessage(v.length);

for (var i = 0; i < v.length; i++)

{

InfoMessage("canPost = "+v[i].canPost); InfoMessage("first article = "+v[i].firstArticle); InfoMessage("group = "+v[i].group); InfoMessage("last article = "+v[i].lastArticle);

}

*/

//===========================================================

 

//**Test GroupOverview**

/*nntp.Group="alt.groupname"; v = nntp.GroupOverview(); InfoMessage(v.length);

for (var i = 0; i < v.length; i++)



 

 

{

InfoMessage("article date = "+v[i].articleDate); InfoMessage("article lines = "+v[i].articleLines); InfoMessage("article number = "+v[i].articleNumber); InfoMessage("article size = "+v[i].articleSize); InfoMessage("from = "+v[i].from); InfoMessage("messageId = "+v[i].messageId); InfoMessage("other headers = "+v[i].otherHeaders); InfoMessage("references = "+v[i].references); InfoMessage("subject = "+v[i].subject);

}

*/

//=========================================================

 

//**Test GetArticleCount**

//nntp.Group="alt.groupname";

//InfoMessage(nntp.GetArticleCount()); nntp.Group="alt.groupname"; InfoMessage(nntp.GetArticleCount());

//=========================================================

 

//**Test GetArticle**

/*nntp.Group="alt.groupname"; nntp.Outfile="c:\\temp\\article.txt"; nntp.GetArticle(1); InfoMessage(nntp.document);

*/

//==========================================================

 

//**Test post article** nntp.From="poster name"; nntp.Subject="nntp test posting"; nntp.Organization="OrgName";

nntp.To="control.cancel, alt.groupname"; [nntp.ReplyTo="poster@organization.org";](mailto:poster@organization.org) [nntp.References="anization.org>"; nntp.MaxHeadersLength=100;

nntp.ArticleText="hello world";

//id1 = nntp.AddAttachment

//        ("c:\\temp\\file1.txt", "file", WLNntp.ENC_7BIT);

//id2 = nntp.AddAttachment

//        ("c:\\temp\\file2.txt", "file", WLNntp.ENC_7BIT);

//id5 = nntp.AddAttachment

//        ("c:\\downloded.gif", "file", WLNntp.ENC_BASE64);



 

 

//id3 = nntp.AddAttachment

//        ("c:\\temp\\file3.txt", "file", WLNntp.ENC_7BIT);

//id4 = nntp.AddAttachment

//        ("c:\\temp\\file4.txt", "file", WLNntp.ENC_7BIT);

//nntp.DeleteAttachment(id3);

//nntp.DeleteAttachment(id1);

//nntp.DeleteAttachment(id4);

try      //catch to handle exceptions

{

nntp.PostArticle();

}

catch (e)

{

InfoMessage ("Error" + e)

}

//==========================================================

//InfoMessage(nntp.GetStatusLine()); nntp.Disconnect()

delete nntp InfoMessage("done")
```

 





## wlPOP Object

 The wlPOP object provides support for POP3 (Post Office Protocol) load and functional testing within WebLOAD. Support for standard POP operation is included. POP over secure connections (SSL) is supported through the [wlPOPs Object ](#_bookmark538).

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

To access the wlPOP object, you must include the wlPop.js file in your

`InitAgenda()` function.

 

### wlPOP Properties

 

#### AutoDelete

 

The AutoDelete property lets you specify whether or not to automatically delete an email once it has been read. You use this property to save or remove messages from your host. For example:

 

`pop.AutoDelete = status`

 

#### document

 

The document property is an object with four properties:

- Headers – A string containing the header of the message

- MessageText – A string containing the text of the message

- Size – An integer describing the size of the message in bytes

- Attachments – An array of objects, with each attachment existing as an object with the following properties:

- contentencoding – The encoding of the attachment

- contenttype – The content type of the attachment

- filename – The file name of the attachment

- messagetext – The text of the attachment

- partname – The part name of the message

- size – The size of the attachment in bytes For example:

- var recentdocument = *pop.document*

- var messageheaders = *recentdocument.MessageHeaders*

- var messagetext = *recentdocument.MessageText*

- var messagesize = *recentdocument.MessageSize*

- var messageattachments = *recentdocument.attachments*




#### Headers[]

 

The Headers property is an array of objects containing header information from the host. Each object contains a key and an array of headers. For example:

`var headersvalue = *pop.Headers[0]*`

`var headerskey=*headersvalue.key*`

`var headerstringvalues=*headersvalue.values[0]`*

 

#### MaxLines

 

The MaxLines property lets you specify the maximum number of lines per email to retrieve from a POP host. You use this property to specify the number of lines to retrieve from each email. For example:

 

`pop.Maxlines = numberoflines`



 

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save a file or message locally on your computer. When you write to the Outfile, you overwrite the existing content. To avoid overwriting the existing content, you must specify a new Outfile each time you write. For example:

 

`pop.Outfile = filename`

 

#### PassWord

 

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted POP host. WebLOAD automatically sends the password to the POP host when a wlPOP object connects to a POP host. For example:

 

`pop.PassWord = password`



> **Caution:** The password appears in plain text in the script. The password is visible to any user who has access to the script.

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption For example:

 

`var filesize = pop.Size`

 

#### UserName

 

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted POP host. WebLOAD automatically sends the user name to the POP host when a wlPOP object connects to a POP host. For example:

 

`pop.UserName = username`

 

#### wlSource

 

The wlSource property contains the encoded multipart source of the message. This is the format in which the message is stored in the Outfile property. For example:

 

`var messagesource = pop.wlSource`



 

 

### wlPOP Methods

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You  may describe the host using its DNS number, or by giving its name. |
| [port]           | The port to which you are  connecting. If you do not specify a port, the default POP port is used. |
| **Return Value** | An exception if  unsuccessful. On success the return value is undefined. |
| **Comments**     | Starts a POP session with the host. When you  connect, you are connecting to a specific mailbox within the host, as  specified by your UserID. |

 

#### Delete()

 

| **Syntax**       | Delete([*MessageID*])                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| messageID        | The identifier of the message you want to delete.  If you do not specify a message ID, the current message is deleted. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the message with  the corresponding ID. If no ID is specified, then the current message is  deleted. |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the POP server.         |

 

#### GetCurrentMessageID()

 

| **Syntax**       | GetCurrentMessageID()                                        |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | The ID of the current  message if successful, an exception if unsuccessful. |
| **Comments**     | Returns the ID of the current message.                       |



 

 

#### GetMailboxSize()

 

| **Syntax**       | GetMailboxSize()                                             |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string describing the size of the mailbox  in bytes if successful. |
| **Comments**     | Returns the total size of the mailbox in bytes.              |

 

#### GetMessageCount()

 

| **Syntax**       | GetMessageCount()                                            |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the number of messages  on the host if successful. |
| **Comments**     | Returns the number of messages waiting on  the host.         |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  latest response string if successful, an exception if unsuccessful. |
| **Comments**     | Returns the latest response string from the  host.           |

 

#### Reset()

 

| **Syntax**       | Reset()                                                      |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Undoes all actions,  including deletions, returning the host to its state at the start of the  session. If this call is not made, disconnecting from the POP host applies  all actions. |

 

#### Retrieve()

 

| **Syntax**       | Retrieve([*MessageID*])                                      |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| MessageID        | The identifier of the  message you want to retrieve. If you do not specify a message ID, the next  message is returned. |
| **Return Value** | Returns the message and populates the  document property.    |
| **Comments**     | Returns the message with the corresponding  ID. If no ID is specified, then the next message is returned |



 

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |

 

#### WLPop()

 

| **Syntax**       | new WLPop()                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlPOP object.                                          |
| **Comments**     | Creates a new wlPOP object, used to  interact with the server. |
| **Example**      | var  myNewPopObject = new WLPop();                           |

 

### POP Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** { IncludeFile("wlPop.js",WLExecuteScript)

}

/*function **InitClient()** {

 

}*/

/*function **TerminateClient()** { delete pop;

}*/

//===================================================

 

//**Body Of script**.

//InfoMessage("Speed: "+wlGlobals.ConnectionSpeed) wlGlobals.Debug=1

var pop=new WLPop(); pop.UserName="UserID" pop.PassWord="TopSecret" pop.Connect("00.0.0.00");

//======================================================

 

//**Test General Functions**

/*count = pop.GetMessageCount();



 

 

InfoMessage("number of messages= "+ count); count = pop.GetMailboxSize(); InfoMessage("size= "+ count);

status = pop.GetStatusLine(); InfoMessage("status= "+ status); pop.SendCommand("hello"); status = pop.GetStatusLine(); InfoMessage("status= "+ status);

*/

//=======================================================

 

//**Test Delete And Reset**

//two tests:

//1. if run as is, # of msgs should remain the same

//2. if run with pop.Reset commented out, # of   msgs should be smaller

InfoMessage("number of messages= "+ pop.GetMessageCount());

//InfoMessage(pop.GetCurrentMessageID);

//pop.MaxLines=0; pop.Delete(15);

InfoMessage("number of messages= "+ pop.GetMessageCount());

//InfoMessage(pop.GetCurrentMessageID);

//pop.Reset(); pop.Disconnect(); pop.Connect("00.0.0.00")

InfoMessage(pop.GetStatusLine());

//InfoMessage(pop.GetCurrentMessageID); InfoMessage("number of messages= "+ pop.GetMessageCount());

//==========================================================

 

//**Test Retrieve**

//InfoMessage("number of messages= "+ pop.GetMessageCount());

//InfoMessage(pop.GetCurrentMessageID);

//pop.AutoDelete=true

/*pop.Outfile="*.xyz";

//pop.MaxLines=0;

var count = pop.GetMessageCount(); InfoMessage(count);

for(var w = 1; w <= count; w++)

{

pop.Retrieve(w); InfoMessage(pop.document.headers); InfoMessage(pop.document.messageText); InfoMessage(pop.document.size);



 

 

InfoMessage(pop.document.attachments.length);

for (var j = 0; j < pop.document.attachments.length; j++)

{

InfoMessage(pop.document.attachments[j].contentEncoding); InfoMessage(pop.document.attachments[j].contentType); InfoMessage(pop.document.attachments[j].filename); InfoMessage(pop.document.attachments[j].messageText); InfoMessage(pop.document.attachments[j].partName); InfoMessage(pop.document.attachments[j].size);

}

InfoMessage("Headers:");

for (var i = 0; i < pop.Headers.length; i++)

{

for (var j = 0; j < pop.Headers[i].values.length; j++)

{

InfoMessage(pop.Headers[i].key + " = " +

pop.Headers[i].values[j]);

}

}

InfoMessage("body"+pop.wlSource);

}*/

catch (e)

{

InfoMessage ("Error" + e)

}

pop.Disconnect();

//==========================================================
```

 

 





## wlPOPs Object

 

The wlPOPs object provides support for POP3 (Post Office Protocol) load and functional testing over secure connections (SSL).

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

To access the wlPOPs object, you must include the wlPops.js file in your

`InitAgenda()` function.



 

 

### wlPOPs Properties

 

#### AutoDelete

 

The AutoDelete property lets you specify whether or not to automatically delete an email once it has been read. You use this property to save or remove messages from your host. For example:

 

`pop.AutoDelete = status`

 

#### document

 

The document property is an object with four properties:

- Headers – A string containing the header of the message

- MessageText – A string containing the text of the message

- Size – An integer describing the size of the message in bytes

- Attachments – An array of objects, with each attachment existing as an object with the following properties:

- contentencoding – The encoding of the attachment

- contenttype – The content type of the attachment

- filename – The file name of the attachment

- messagetext – The text of the attachment

- partname – The part name of the message

- size – The size of the attachment in bytes For example:

- var recentdocument = *pop.document*

- var messageheaders = *recentdocument.MessageHeaders*

- var messagetext = *recentdocument.MessageText*

- var messagesize = *recentdocument.MessageSize*

- var messageattachments = *recentdocument.attachments*




#### Headers[]

 

The Headers property is an array of objects containing header information from the host. Each object contains a key and an array of headers. For example:

 

- var headersvalue = *pop.Headers[0]*

- var headerskey=*headersvalue.key*

- var headerstringvalues=*headersvalue.values[0]*








#### MaxLines

 

The MaxLines property lets you specify the maximum number of lines per email to retrieve from a POP host. You use this property to specify the number of lines to retrieve from each email. For example:

 

`pop.Maxlines = numberoflines`

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save a file or message locally on your computer. When you write to the Outfile, you overwrite the existing content. To avoid overwriting the existing content, you must specify a new Outfile each time you write. For example:

 

`pop.Outfile = filename`

 

#### PassWord

 

The PassWord property lets you specify a password when logging on to a host. You use this property to log onto a restricted POP host. WebLOAD automatically sends the password to the POP host when a wlPOP object connects to a POP host. For example:

 

`pop.PassWord = password`

> **Caution:** The password appears in plain text in the script. The password is visible to any user who has access to the script.

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption For example:

 

`var filesize = pop.Size`

 

#### UserName

 

The UserName property lets you specify a User ID when logging on to a host. You use this property to log onto a restricted POP host. WebLOAD automatically sends the user name to the POP host when a wlPOP object connects to a POP host. For example:

 

`pop.UserName = username`



 

 

#### wlSource

 

The wlSource property contains the encoded multipart source of the message. This is the format in which the message is stored in the Outfile property. For example:

 

`var messagesource = pop.wlSource`

 

### wlPOPs Methods

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You  may describe the host using its DNS number, or by giving its name. |
| [port]           | The port to which you are  connecting. If you do not specify a port, the default POP port is used. |
| **Return Value** | An exception if  unsuccessful. On success the return value is undefined. |
| **Comments**     | Starts a POP session with the host. When  you connect, you are connecting to a specific mailbox within the host, as  specified by your UserID. |

 

#### Delete()

 

| **Syntax**       | Delete([*MessageID*])                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| messageID        | The identifier of the message you want to  delete. If you do not specify a message ID, the current message is deleted. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Deletes the message with  the corresponding ID. If no ID is specified, then the current message is  deleted. |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the POP server.         |

 

#### GetCurrentMessageID()

 

| **Syntax**       | GetCurrentMessageID()                                        |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | The ID of the current  message if successful, an exception if unsuccessful. |
| **Comments**     | Returns the ID of the current message.                       |



#### GetMailboxSize()

 

| **Syntax**       | GetMailboxSize()                                             |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string describing the size of the mailbox in  bytes if successful. |
| **Comments**     | Returns the total size of the mailbox in  bytes.             |

 

#### GetMessageCount()

 

| **Syntax**       | GetMessageCount()                                            |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the  number of messages on the host if successful. |
| **Comments**     | Returns the number of messages waiting on  the host.         |

 

#### GetStatusLine()

 

| **Syntax**       | GetStatusLine()                                              |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A string containing the latest response  string if successful, an exception if unsuccessful. |
| **Comments**     | Returns the latest response string from the  host.           |

 

#### Reset()

 

| **Syntax**       | Reset()                                                      |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Undoes all actions,  including deletions, returning the host to its state at the start of the  session. If this call is not made, disconnecting from the POP host applies  all actions. |

 

#### Retrieve()

 

| **Syntax**       | Retrieve([*MessageID*])                                      |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| MessageID        | The identifier of the  message you want to retrieve. If you do not specify a message ID, the next  message is returned. |
| **Return Value** | Returns the message and populates the  document property.    |
| **Comments**     | Returns the message with the corresponding ID. If  no ID is specified, then the next message is returned |



  

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without  modification. This method is useful for interacting directly with the host  using non-standard or unsupported extensions. |

 

#### WLPops()

 

| **Syntax**       | new WLPops()                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlPOPs object.                                         |
| **Comments**     | Creates a new wlPOPs object, used to  interact with the server. |
| **Example**      | var  myNewPopObject = new WLPops();                          |

 



## wlSMTP Object

 

The wlSMTP object provides support for Simple Mail Transfer Protocol (SMTP) load and functional testing within WebLOAD. Support for standard SMTP operation is included. SMTP over secure connections (SSL) is supported through the [*wlSMTPs*](#_bookmark545) [*Object* ](#_bookmark545).

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception should be thrown.

 

To access the wlSMTP object, you must include the wlSmtp.js file in your

`InitAgenda()` function.

 



### wlSMTP Properties

 

#### Attachments

 

The Attachments property lets you specify an attachment to an email message. The *filename* parameter is the name of the local file or datastream that you want to attach to the email message. For example:

 

`smtp.Attachments = filename`

 

#### AttachmentsEncoding

 

The AttachmentsEncoding property lets you specify the type of encoding you are applying to an email attachment. This property must be specified for each attachment. 

Valid values are: 

- 7Bit
- Quoted

- Base64

- 8Bit

- 8BitBinary



You may also specify the encoding using the following constants: 

- WLSmtp.ENC_7BIT – 7bit encoding

- WLSmtp.ENC_QUOTED – Quoted Printable encoding

- WLSmtp.ENC_BASE64 – Base64 encoding

- WLSmtp.ENC_8BIT – 8Bit encoding

- WLSmtp.ENC_8BITBINARY – Binary encoding For example:

- smtp.AttachmentsEncoding = *encodingtype*




#### AttachmentsTypes

 

The AttachmentsTypes property lets you specify the type of attachment you are including in an email message. This property must be specified for each attachment. 

Valid values are: 

- **true** – Specifies a type of file
- **false** – Specifies a type of data

 

For example:

 

`smtp.AttachmentsTypes = typeofattachment`

 

#### Bcc

 

The Bcc property lets you specify the email addresses of additional recipients to be blind copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [m>". 



For example:

`smtp.Bcc = blindcopyaddresses`

 

#### Cc

 

The Cc property lets you specify the email addresses of additional recipients to be copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name [m>". For example:

 

`smtp.Cc = copyaddress; copyaddress`

 

#### From

 

The From property lets you describe the Reply To in plain language. You may use this property to identify your Reply To email address in a plain language format. For example:

 

`smtp.From = replyname`

 

#### Message

 

The Message property lets you specify the text appearing in the body of your email. You use this property to write the text of the email message itself.

 

#### ReplyTo

 

The ReplyTo property lets you specify the return address of your email. You may specify multiple addresses in a semicolon-separated list. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [](mailto:Me@MyCompany.com)". 



For example:

`smtp.ReplyTo = replyaddress`



#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. 



For example: 

`var filesize = smtp.Size`

 

#### Subject

 

The Subject property lets you specify the text appearing the subject field of your email. You use this property to provide a brief description of the contents of your email. 

For example: 

`smtp.Subject = subjectheader`

 

#### To

The To property lets you specify a recipient’s email address. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name ["](mailto:Me@MyCompany.com). For example:

 

`smtp.To = recipientaddress; recipientaddress`

 

#### Type

 

The Type property lets you specify the type of server with which you are working. The default value for this property is **SMTP**. 



Valid values are:

- **SMTP** – A standard STMP server

- **ESMTP** – An extended SMTP server 



For example:

`smtp.Type = servertype`

 

### wlSMTP Methods

 

#### AddAttachment()

 

| **Syntax**       | AddAttachment(*string*,  *type*, [*encoding*])               |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| String           | The string you are sending  to the host. If you are sending a file, the string is the location and name  of the file. If you are sending a data attachment, the string is the data to  be attached. |
| Type             | The type of  attachment you are sending. The default value is  File. Valid values are:   File   Data |
| encoding         | The type of encoding to apply to the file. The default value is  7Bit. Valid values are:   7Bit   Quoted   Base64   8Bit   8BitBinary |
| **Return Value** | Returns an integer value  Attachment ID if successful, an exception if unsuccessful. |
| **Comments**     | Adds an attachment to the email message.                     |



 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You  may express the host using either the DNS number or the full name of the  host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default SMTP port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts an SMTP session with the host.                        |

 

#### DeleteAttachment()

 

| **Syntax**       | DeleteAttachment(*ID*)                             |
| ---------------- | -------------------------------------------------- |
| **Parameters**   |                                                    |
| ID               | The ID of the attachment you are deleting.         |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Removes an attachment from the email  message.     |

 

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the SMTP host.          |



  

#### Send()



| **Syntax**       | Send()                                                       |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends mail to recipients, attaching files  using MIME as necessary. After sending the attachments, data is deleted. |

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host  without modification. This method is useful for interacting directly with the  host using non-standard or unsupported extensions. SendCommand automatically  appends “\r\n” at the end of the string. You can add additional instances of  “\r\n” within the string, however do not add “\r\n” at the end of the string.  For example, SendCommand(“Line1\r\n Line2\r\n Line3”) |

 

#### Verify()

 

| **Syntax**       | Verify()                                                     |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Returns a 1 if the address  is valid, a 0 if the address is invalid. If the method is unable to verify  the address due to authentication  or other reasons, it returns an exception. |
| **Comments**     | Checks that the address in the To property is valid. To use this method, include  only one address in the To  property. |

 

#### WLSmtp()

 

| **Syntax**       | new WLSmtp()                                                 |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlSMTP object.                                         |
| **Comments**     | Creates a new wlSMTP object, used to  interact with the server. |
| **Example**      | function **InitClient()** { myNewSmtpObject = new WLSmtp()  } |



 

 

### SMTP Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** { IncludeFile("wlSmtp.js",WLExecuteScript)

// include the file that enables SMTP

}

function **InitClient()** {

Smtp=new WLSmtp()     // create the new SMTP object Smtp.Connect("HostName"); // connect to the server

}

function **TerminateClient()** {

Smtp.Disconnect();    // logout from the server delete Smtp    // delete the SMTP object

}

//================================================

 

// **Body Of script**

//**Test Send Attachments**

Smtp.To=" \"Recipient Name\" [";](mailto:Recipient@recipient.com) Smtp.From= ["Sender@sender.com";](mailto:Sender@sender.com) [Smtp.Cc="Copy1@copy.here.org, ](mailto:Copy1@copy.here.org)[Copy2@copy.there.org";](mailto:Copy2@copy.there.org)

// multiple CC's [Smtp.ReplyTo="Sender@sender.com";](mailto:Sender@sender.com)

// optional different reply to address Smtp.Subject="Message Subject ";  // Text string Smtp.Message="Greetings from the wlSMTP class"; // Message text

// Add attachments from local file using different

// encoding techniques

// 7BIT are text files, the BASE64 is for a binary file

// (in this case an image) id1 = Smtp.AddAttachment



 

id2 = Smtp.AddAttachment id3 = Smtp.AddAttachment id4 = Smtp.AddAttachment

id5 = Smtp.AddAttachment



("c:\\file1.txt","file",WLSmtp.ENC_7BIT); ("c:\\file2.txt","file",WLSmtp.ENC_7BIT); ("c:\\file3.txt","file",WLSmtp.ENC_7BIT); ("c:\\file4.txt","file",WLSmtp.ENC_7BIT);



("c:\\downloded.gif","file",WLSmtp.ENC_BASE64);

// You may delete attachments prior to sending the mail message Smtp.DeleteAttachment(id3);

Smtp.DeleteAttachment(id1);



 

 

Smtp.DeleteAttachment(id4); Smtp.Send();      // and send it! InfoMessage(Smtp.GetStatusLine());

// print out the last response from the server

catch (e)

{

InfoMessage ("Error" + e)

}

//=======================================================

InfoMessage("done")   // End of SMTP sample script
```

 





## wlSMTPs Object

 

The wlSMTP object provides support for SMTP (Mail Transfer Protocol) load and functional testing over secure connections (SSL).

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception should be thrown.

 

To access the wlSMTPs object, you must include the wlSMTPs.js file in your

`InitAgenda()` function.

 

### wlSMTPs Properties

 

#### Attachments

 

The Attachments property lets you specify an attachment to an email message. The *filename* parameter is the name of the local file or datastream that you want to attach to the email message. 



For example:

`smtp.Attachments = filename`

 

#### AttachmentsEncoding

 

The AttachmentsEncoding property lets you specify the type of encoding you are applying to an email attachment. This property must be specified for each attachment. 

The AttachmentsEncoding property lets you specify the type of encoding you are applying to an email attachment. This property must be specified for each attachment. 

Valid values are: 

- 7Bit
- Quoted
- Base64
- 8Bit
- 8BitBinary



You may also specify the encoding using the following constants: 

- WLSmtp.ENC_7BIT – 7bit encoding
- WLSmtp.ENC_QUOTED – Quoted Printable encoding
- WLSmtp.ENC_BASE64 – Base64 encoding
- WLSmtp.ENC_8BIT – 8Bit encoding
- WLSmtp.ENC_8BITBINARY – Binary encoding For example:
- smtp.AttachmentsEncoding = *encodingtype*



 

#### AttachmentsTypes

 

The AttachmentsTypes property lets you specify the type of attachment you are including in an email message. This property must be specified for each attachment. 



Valid values are:

- **true** – Specifies a type of file

- **false** – Specifies a type of data 



For example:

`smtp.AttachmentsTypes = typeofattachment`

 

#### Bcc

 

The Bcc property lets you specify the email addresses of additional recipients to be blind copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [m>". 



For example:

`smtp.Bcc = blindcopyaddresses`

 

#### Cc

 

The Cc property lets you specify the email addresses of additional recipients to be copied in an email. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name [m>".



For example: 

`smtp.Cc = copyaddress; copyaddress`



 

#### From

 

The From property lets you describe the Reply To in plain language. You may use this property to identify your Reply To email address in a plain language format. 



For example:

`smtp.From = replyname`

 

#### Message

 

The Message property lets you specify the text appearing in the body of your email. You use this property to write the text of the email message itself.

 

#### ReplyTo

 

The ReplyTo property lets you specify the return address of your email. You may specify multiple addresses in a semicolon-separated list. Addresses may be specified in the format of ["Me@MyCompany.com](mailto:Me@MyCompany.com)" or as "My Name [m>". 



For example:

`smtp.ReplyTo = replyaddress`

 

#### Size

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. 



For example:

`var filesize = smtp.Size`

 

#### Subject

 

The Subject property lets you specify the text appearing the subject field of your email. You use this property to provide a brief description of the contents of your email.



For example: 

`smtp.Subject = subjectheader`

 

#### To

The To property lets you specify a recipient’s email address. You may specify multiple addresses in a semicolon-separated list. You must specify this property with every email. Addresses may be specified in the format of ["Me@MyCompany.com" ](mailto:Me@MyCompany.com)or as "My Name ["](mailto:Me@MyCompany.com). For example:

 

`smtp.To = recipientaddress; recipientaddress`

 

#### Type

 

The Type property lets you specify the type of server with which you are working. The default value for this property is **SMTP**. 



Valid values are:

- **SMTP** – A standard STMP server
- **ESMTP** – An extended SMTP server 



For example:

`smtp.Type = servertype`

 

### wlSMTPs Methods

 

#### AddAttachment()

 

| **Syntax**       | AddAttachment(*string*,  *type*, [*encoding*])               |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| String           | The string you are sending  to the host. If you are sending a file, the string is the location and name  of the file. If you are sending a data attachment, the string is the data to  be attached. |
| Type             | The type of attachment you are sending. The  default value is  File. Valid values are:   File   Data |
| encoding         | The type of encoding to apply to the file.  The default value is  7Bit. Valid values are:   7Bit   Quoted   Base64   8Bit   8BitBinary |
| **Return Value** | Returns an integer value  Attachment ID if successful, an exception if unsuccessful. |
| **Comments**     | Adds an attachment to the email message.                     |

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default SMTP port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts an SMTP session with the host.                        |



  

#### DeleteAttachment()

 

| **Syntax**       | DeleteAttachment(*ID*)                            |
| ---------------- | ------------------------------------------------- |
| **Parameters**   |                                                   |
| ID               | The ID of the attachment you are deleting.        |
| **Return Value** | Null if successful, an exception if unsuccessful. |
| **Comments**     | Removes an attachment from the email  message.    |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the SMTP host.          |

 

#### Send()

 

| **Syntax**       | Send()                                                       |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends mail to recipients, attaching files using  MIME as necessary. After sending the attachments, data is deleted. |

 

#### SendCommand()

 

| **Syntax**       | SendCommand(*string*)                                        |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| string           | The string you are sending to the host.                      |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Sends a string to the host without modification.  This method is useful for interacting directly with the host using  non-standard or unsupported extensions. |

 

#### Verify()

 

| **Syntax**       | Verify()                                                     |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Returns a 1 if the address  is valid, a 0 if the address is invalid. If the method is unable to verify  the address due to authentication  or other reasons, it returns an exception. |
| **Comments**     | Checks that the address in the To property is valid. To use this method, include  only one address in the To  property. |



  

#### WLSmtps()

| **Syntax**       | new WLSmtps()                                                |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlSMTPs object.                                        |
| **Comments**     | Creates a new wlSMTPs object, used to  interact with the server. |
| **Example**      | function **InitClient()** { myNewSmtpObject = new WLSmtps()  } |

 

 





## wlTCP Object

 

The wlTCP object provides support for TCP (Transfer Control Protocol) load and functional testing within WebLOAD. Support for standard TCP operation is included. TCP over secure connections (SSL) is not currently supported.

 

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method; otherwise an exception is thrown.

 

To access the wlTCP object, you must include the wlTcp.js file in your

`InitAgenda()` function.

 

### wlTCP Properties

 

#### document

 

The document property contains all responses from the host since the last time the `Send()` method was used. Each time a message is returned, it is concatenated to the document object. The document may be cleared manually using the `Erase()` method. 



For example:

*`var recentdocument = tcp.document`*



#### InBufferSize

 

The InBufferSize property specifies the size, in bytes, of the incoming data buffer. To remove this setting, either delete the property, or set it to a negative value. 



For example:

tcp.InBufferSize = *maximuminsize*

 

#### LocalPort

 

The LocalPort property specifies the TCP port to which you are connecting. If you do not specify the LocalPort property, you connect to a randomly selected port.

For example:

`tcp.LocalPort = portnumber`

 

#### NextPrompt

The NextPrompt property specifies the text for the script to look for in the next prompt from the host. A `Receive()` call is viewed as successful if the prompt contains the text string specified by the NextPrompt variable. To specify a prompt with no message, specify a NextPrompt with an empty value, or delete the NextPrompt property. Once this property is specified, it limits all subsequent instances of the `Receive()` method. Either delete the property or set it to zero to remove the limitation. 



For example: 

`tcp.NextPrompt = promptmessage`

 

#### NextSize



The NextSize property specifies the size, in bytes, of the expected data. If you specify a NextSize of 100 bytes, for example, the `Receive()` method returns to the script when the document object contains 100 bytes of data. Once this property is specified, it limits all subsequent instances of the `Receive()` method. Either delete the property or set it to zero to remove the limitation. For example:

 

`tcp.NextSize = expectedsize`

 

#### OutBufferSize

 

The OutBufferSize property specifies the size, in bytes, of the outgoing data buffer. To remove this setting, either delete the property, or set it to a negative value. For example:

 

`tcp.OutBufferSize = maximumoutsize`



#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save the responses from the host locally on your computer. You must specify the output file before calling the `Receive()` method to save the responses to that file.

 

You write to the output file each time you use the ``Receive()`` method. If you call the `Receive()` method more than once, you must specify a different output file each time, or you overwrite the previous output file. 



For example:

`tcp.Outfile = filename`

 

#### ReceiveMessageText

 

The ReceiveMessageText property returns the reason why the host stopped responding. You use this property to determine the state of the host. 

Possible values are: 

- **Prompt was found** – The host returned the prompt specified in the NextPrompt property.
- **Timeout** – The last command exceeded the time limit specified by the Timeout property.
- **Byte length reached** – The host received the amount of data specified in the NextSize property.



For example: 

`InfoMessage(TCP.ReceiveMessageText);`

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. 



For example:

`var filesize = tcp.Size`

 

#### Timeout

 

The Timeout property lets you specify the length of the delay, in milliseconds, before the script breaks its connection with the host. If you do not specify the timeout property, the script may freeze if the host does not respond as you expect it to. To set an unlimited timeout, specify a value of zero, or a negative value. 



For example:

`tcp.Timeout = timedelay`



> **Note:** It is recommended that you include a Timeout property in all scripts that use the wlTCP object. If you do not, and the script fails to return a prompt, your session may freeze.

 

### wlTCP Methods

 

#### Connect()



| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default TCP port is used. |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Starts a TCP session with the host.                          |

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                       |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Terminates a connection to the TCP host.           |

 

#### Erase()

 

| **Syntax**       | Erase()                                            |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Clears the contents of the document object.        |

 

#### Receive()

 

| **Syntax**       | `Receive()`                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Returns all responses from  the host since the last time the `Send()` method was used. A `Receive()`  method  returns to the script when the NextPrompt, NextSize, or Timeout  properties  are met. If more than one of these properties is specified, the method  returns to the script when the first one is met. Subsequent uses of `Receive()`  find the next  instance of the limiting property, returning additional information from the  buffer. The content returned depends upon which of the three limiting  properties triggered the return. |



 

#### Send()

| **Syntax**       | Send(data_to_send)                                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| data_to_send     | The data that you want to send to the host.                  |
| **Return Value** | A string containing the response from the host if  successful, an exception if unsuccessful. |
| **Comments**     | Sends data to the host via TCP and clears the  document object. |

 

#### WLTcp()

| **Syntax**       | new WLTcp()                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlTCP object.                                          |
| **Comments**     | Creates a new wlTCP object, used to  interact with the server. |
| **Example**      | function **InitClient()** { myNewTcpObject = new WLTcp();  } |

 

### TCP Sample Code

```javascript
// **script Initialization**

function InitAgenda() { 
    IncludeFile("wlTcp.js",WLExecuteScript)
}

function InitClient() { 
    tcp=new WLTcp();
}

function TerminateClient() {
    delete tcp;
}
//**Body Of script**.


tcp.Outfile = "c:\\tcp.txt"; 
tcp.Timeout = 2000; 
tcp.NextPrompt = "\r\n\r\n";

//tcp.NextSize=1900;

tcp.Connect("www.sitename.com", 80);
tcp.Send("GET /products/index.htm HTTP/1.0\r\n\r\n");

//Sleep(3000); 
tcp.Receive(); 
InfoMessage(tcp.document);
InfoMessage(tcp.ReceiveMessageText); 

tcp.NextSize=10091; 
tcp.NextPrompt="";
tcp.Erase(); 
tcp.Receive(); 
InfoMessage(tcp.document);

InfoMessage(tcp.ReceiveMessageText);

```

## wlTelnet Object

The wlTelnet object provides support for Telnet load and functional testing within WebLOAD. Support for standard Telnet operation is included. Telnet over secure connections (SSL) is not currently supported.

If a connection is required but has expired or has not yet been established, the underlying code attempts to login. Logging in requires you to call the appropriate Connect() method otherwise an exception is thrown.

 

To access the wlTelnet object, you must include the wlTelnet.js file in your

`InitAgenda()` function.



 

 

### wlTelnet Properties

 

#### document

 

The document property contains all responses from the host since the last time the `Send()` method was used. Each time a message is returned, it is concatenated to the document object. The document may be cleared manually using the `Erase()` method. For example:

 

var recentdocument = *telnet.document*

 

#### NextPrompt

 

The NextPrompt property specifies the text for the Agenda to look for in the next prompt from the host. A `Receive()` call is viewed as successful if the prompt contains the text string specified by the NextPrompt variable. To specify a prompt with no message, specify a NextPrompt with an empty value, or delete the NextPrompt property. Once this property is specified, it limits all subsequent instances of the `Receive()` method. Either delete the property or set it to zero to remove the limitation. 



For example:

`telnet.NextPrompt = promptmessage`

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save the responses from the host locally on your computer. You must specify the output file before calling the `Receive()` method to save the responses to that file.

 

You write to the output file each time you use the `Receive()` method. If you call the `Receive()` method more than once, you must specify a different output file each time, or you overwrite the previous output file. For example:

 

`telnet.Outfile = filename`

 

#### ReceiveMessageText

 

The ReceiveMessageText property returns the reason why the host stopped responding. You use this property to determine the state of the host. 

Possible values are:

- **Prompt was found** – The host returned the prompt specified in the NextPrompt property.
- **Timeout** – The last command exceeded the time limit specified by the Timeout property
- **Byte length reached** – The host received the amount of data specified in the NextSize property.

For example: 

`InfoMessage(Telnet.ReceiveMessageText);`

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption.



For example:

`var filesize = telnet.Size`

 

#### Timeout

The Timeout property lets you specify the length of the delay, in milliseconds, before the script breaks its connection with the host. If you do not specify the timeout property, the script may freeze if the host does not respond as you expect it to. To set an unlimited timeout, specify a value of zero, or a negative value. 



For example: 

`telnet.Timeout = timedelay`



> **Note:** It is recommended that you include a Timeout property in all scripts that use the wlTelnet object. If you do not, and the script fails to return a prompt, your session may freeze.

 

### wlTelnet Methods

 

#### Connect()

 

| **Syntax**       | Connect(*host*,  [*port*])                                   |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are  connecting. If you do not specify a port, the default Telnet port is used. |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Starts a Telnet session with the host.                       |



 

 

#### Disconnect()

 

| **Syntax**       | Disconnect()                                      |
| ---------------- | ------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful |
| **Comments**     | Terminates a connection to the Telnet host.       |

 

#### Erase()

 

| **Syntax**       | Erase()                                            |
| ---------------- | -------------------------------------------------- |
| **Return Value** | Null if successful, an exception if  unsuccessful. |
| **Comments**     | Clears the contents of the document object.        |

 

#### Receive()

 

| **Syntax**       | `Receive()`                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Returns all responses from  the host since the last time the `Send()` method was used. A `Receive()`  method  returns to the script when the NextPrompt, NextSize, or Timeout  properties  are met. If more than one of these properties is specified, the method  returns to the script when the first one is met. Subsequent uses of `Receive()`  find the next  instance of the limiting property, returning additional information from the  buffer. The content returned depends upon which of the three limiting  properties triggered the return. |

 

#### Send()

 

| **Syntax**       | Send(data_to_send)                                           |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| data_to_send     | The data that you want to send to the host.                  |
| **Return Value** | A string containing the response from the host if  successful, an exception if unsuccessful. |
| **Comments**     | Sends data to the host via Telnet and  clears the document object. |

 

#### WLTelnet()

 

| **Syntax**       | new WLTelnet()                                               |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlTelnet object.                                       |
| **Comments**     | Creates a new wlTelnet object, used to  interact with the server. |
| **Example**      | `function **InitClient()** { myNewTelnetObject = new WLTelnet()  }` |





### Telnet Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** { IncludeFile("wlTelnet.js",WLExecuteScript)

// include the file that enables Telnet

}

function **InitClient()** {

Telnet=new WLTelnet()  // create a new telnet object

}

function **TerminateClient()**

{

delete Telnet      // delete the object we were using

}

//================================================

 

// **Body Of script**

// Set timeout and prompt

// IMPORTANT: Set a timeout when setting a prompt. Otherwise,

// If the prompt is unexpected or incorrect the script will

// freeze while waiting for a prompt that will never arrive Telnet.Timeout=1000;   // one second Telnet.NextPrompt="User name: "; // text to look for Telnet.Connect("000.0.0.0");   // connect

Telnet.`Receive()`;        // wait for data from the remote host

Telnet.Send("myname");      // send login name InfoMessage(Telnet.document);  // write out the data received InfoMessage(Telnet.ReceiveMessageText);

// write out why the call returned Telnet.NextPrompt="Password: ";   // next prompt to look for Telnet.`Receive()`;    // wait for data Telnet.Outfile="c:\\filename.txt";

// save this next response to file as well InfoMessage(Telnet.document);   // what did we get?

InfoMessage(Telnet.ReceiveMessageText);

// write out why the call returned Telnet.Send("mypassword");   // send password Telnet.NextPrompt=">";      // new prompt to wait for Telnet.`Receive()`;        // wait for a response Telnet.Send("command");     // send command text to the host



 

 

Telnet.`Receive()`;        // wait for a response InfoMessage(Telnet.document); // what did we get?

InfoMessage(Telnet.ReceiveMessageText);

// write out why the call returned

Telnet.Disconnect();       // finally disconnect

//============================================================

//This is another way to work with telnet. When no prompt

//is set the timeout is ignored. Instead the script writer

//must manually keep receiving the data by calling the receive

//command. `Receive()` returns the response as well as assigning

//the value to the this.document property. It is up to the user

//to perform a delay before he/she receives the data. Telnet.Connect("000.0.0.0"); // log in to a remote host

// In this case we receive three times.

// In your script you may keep calling `Receive()` until the

// telnet object's document property contains the data you are

// looking for, or until you decide to do something else Telnet.`Receive()`;      // fetch the data

Telnet.`Receive()`;        // Wait for more

Telnet.`Receive()`;        // Wait for more InfoMessage(Telnet.document);  // Contains text from ALL receives InfoMessage(Telnet.ReceiveMessageText);  // reason calls returned Telnet.Send("Command");  // clears the document object Telnet.`Receive()`;     // fetch the data

Telnet.`Receive()`;        // Wait for more

Telnet.`Receive()`;        // Wait for more InfoMessage(Telnet.document); InfoMessage(Telnet.ReceiveMessageText); Telnet.Send("command");

Telnet.`Receive()`;

Telnet.`Receive()`;        // Wait for more

Telnet.`Receive()`;        // Wait for more InfoMessage(Telnet.document); InfoMessage(Telnet.ReceiveMessageText); Telnet.Send("dir");

Telnet.`Receive()`;

Telnet.`Receive()`;        // Wait for more

Telnet.`Receive()`;        // Wait for more InfoMessage(Telnet.document); InfoMessage(Telnet.ReceiveMessageText);

catch (e)

{

InfoMessage ("Error" + e)

}



 

 

Telnet.Disconnect();       // log out from the remote host

InfoMessage("done")       // End of telnet sample script
```

 

 



## wlUDP Object

 

The wlUDP object provides support for UDP (User Datagram Protocol) load and functional testing within WebLOAD. Support for standard UDP operation is included. UDP over secure connections (SSL) is not currently supported.

 

To access the wlUDP object, you must include the wlUdp.js file in your

`InitAgenda()` function.

 

### wlUDP Properties

 

#### document

 

The document property is an array of objects sent in the current session, with each object containing the following properties:

- datagram – The datagram retrieved from the database

- address – The address of the datagram

- port – The port used to communicate with the database


The document property contains all responses from the host since the last time the `Send()` method was used. Each time a message is returned, it is concatenated to the document object. The document may be cleared manually using the `Erase()` method. 



For example:

`var recentdocument = udp.document`

 

#### InBufferSize

 

The InBufferSize property specifies the size, in bytes, of the incoming data buffer. For example:

 

`udp.InBufferSize = maximuminsize`

 

#### LocalHost

 

The LocalHost property lets you specify a local host for use in broadcasting via UDP. For example:

 

`udp.LocalHost = localhostname`



#### LocalPort

 

The LocalPort property specifies the UDP port to which you are connecting. If you do not specify the LocalPort property, you connect to a randomly selected port. 

For example: 

`udp.LocalPort = portnumber`

 

#### MaxDatagramSize



The MaxDatagramSize property specifies the maximum size, in bytes, of datagrams that you may send or receive via UDP. For example:

 

`udp.MaxDatagramSize = maximumsize`

 

#### NumOfResponses

 

The NumOfResponses property specifies the number of responses the testing machine waits for before proceeding. You use this property to make sure that all of your hosts have responded. To specify an unlimited number of responses, specify a NumOfResponses value of zero. For example:

 

`udp.NumOfResponses = numberofhosts`

 

#### OutBufferSize

 

The OutBufferSize property specifies the size, in bytes, of the outgoing data buffer. For example:

 

`udp.OutBufferSize = maximumoutsize`

 

#### Outfile

 

The Outfile property lets you specify the name of an output file. You use this property to save the responses from the host locally on your computer. You must specify the output file before calling the `Receive()` method to save the responses to that file.

 

You write to the output file each time you use the `Receive()` method. If you call the `Receive()` method more than once, you must specify a different output file each time, or you will overwrite the previous output file. 



For example:

`udp.Outfile = filename`



 

 

#### ReceiveMessageText

 

The ReceiveMessageText property returns the reason why the host stopped responding. You use this property to determine the state of the host. 

Possible values are:

- **Prompt was found** – The host returned the prompt specified in the NextPrompt property.
- **Timeout** – The last command exceeded the time limit specified by the Timeout property
- **Byte length reached** – The host received the amount of data specified in the NextSize property.

For example: 

`InfoMessage(Telnet.ReceiveMessageText);`

 

 

#### RequestedPackets

 

The RequestedPackets property specifies the number of packets the testing machine waits for before proceeding. To specify an unlimited number of packets, specify a RequestedPackets value of zero. 



For example:

`udp.RequestedPackets = numberofpackets`

 

#### Size

 

The Size property returns the byte length of data transferred to the host. You use this property to compare starting and finishing sizes to verify that files have arrived without corruption. For example:

 

`var filesize = udp.Size`

 

#### Timeout

 

The Timeout property lets you specify the length of the delay, in milliseconds, before the script breaks its connection with the host. If you do not specify the timeout property, the script may freeze if the host does not respond as you expect it to. For example:

 

`udp.Timeout = timedelay`

> **Note:** It is recommended that you include a Timeout property in all scripts that use the wlUDP object. If you do not, and the script fails to return a prompt, your session may freeze.



 

 

### wlUDP Methods

 

#### Bind()

 

| **Syntax**       | Bind()                                                       |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if unsuccessful.            |
| **Comments**     | Creates a UDP port and  sets the OutBufferSize, InBufferSize, MaxDatagramSize, LocalHost, and LocalPort  properties.  The value of these properties is fixed when the Bind()  method is  used. To change the value of any of these properties, you must use the UnBind() method, change the value of the property and using  the Bind() method  again. |

 

#### Broadcast()

 

| **Syntax**       | Broadcast(*port,  data_to_send*)                             |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| Port             | The port to which you are connecting.                        |
| data_to_send     | The data that you want to send to the local  net.            |
| **Return Value** | A string containing the response from the host if  successful, an exception if unsuccessful. |
| **Comments**     | Broadcasts data to the local net.                            |

 

#### Erase()

 

| **Syntax**       | Erase()                                                      |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Clears the contents of the  document property, setting it to an empty array. |

 

#### Receive()

 

| **Syntax**       | `Receive()`                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Returns all responses from  the host since the last time the `Send()` method was used. The `Receive()`  method  returns to the script when the RequestedPackets or Timeout property is met.  Subsequent uses of `Receive()` find the next instance of the limiting property,  returning additional information from the  buffer. |



 

 

#### Send()

 

| **Syntax**       | Send(*host,  port, data_to_send*)                            |
| ---------------- | ------------------------------------------------------------ |
| **Parameters**   |                                                              |
| Host             | The host to which you are connecting. You may  express the host using either the DNS number or the full name of the host. |
| port             | The port to which you are connecting.                        |
| data_to_send     | The data that you want to send to the host.                  |
| **Return Value** | A string containing the response from the  host if successful, an exception if unsuccessful. |
| **Comments**     | Sends data to the host via UDP.                              |

 

#### UnBind()

 

| **Syntax**       | UnBind()                                                     |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | Null if successful, an exception if  unsuccessful.           |
| **Comments**     | Closes a UDP socket. You  must use this command to close an existing UDP socket before you may use the Bind() again. |

 

#### WLUdp()

 

| **Syntax**       | new WLUdp()                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Return Value** | A new wlUDP object.                                          |
| **Comments**     | Creates a new wlUDP object, used to  interact with the server. |
| **Example**      | function **InitClient()** { myNewUDPObject = new WLUdp()  }  |

 

### UDP Sample Code

```javascript
// **script Initialization**

function **`InitAgenda()`** {

IncludeFile(“wlUdp.js”,WLExecuteScript)

// enable the UDP objects

}

function **InitClient()** {

udp=new WLUdp();    // create a new UDP object

}

function **TerminateClient()** {

delete udp       // delete the UDP object

}



 

 

//===================================================

 

//**Body Of script**.

//**Test Send:** set the buffer sizes appropriately for the data try

{

udp.OutBufferSize=10; udp.InBufferSize=12; udp.MaxDatagramSize=10;

udp.Timeout=10000;    // 10 second timeout

udp.NumOfResponses=1;   // return after one remote machine responds

udp.Outfile=“c:\\serialize.txt”;   // file to save responses to

udp.Bind();

udp.Send(“00.0.0.00”, 7, “good morning”);

// send a datagram to one machine on port

7

udp.`Receive()`;      // wait for a response InfoMessage(udp.ReceiveMessageText); // This is what happened

// show the properties of the response

// note that the udp.document object is an array InfoMessage(udp.document[0].datagram); // get the response InfoMessage(udp.document[0].address);  // which machine responded? InfoMessage(udp.document[0].port);   // the port

// now broadcast to seven machines

udp.NumOfResponses=7;   // we expect seven machines to respond udp.Outfile=“c:\\serialize.txt”; // send the responses udp.Broadcast(7, “good morning”);

// send the message (again on port 7)

udp.`Receive()`;      // wait for the responses InfoMessage(udp.ReceiveMessageText);  // print the return reason

// For each host that responded there will be an entry

// in the array. This loop examines each one for (var i = 0; i < udp.document.length; i++)

{

InfoMessage(“datagram= “+udp.document[i].datagram); InfoMessage(“address= “+udp.document[i].address); InfoMessage(“port= “+udp.document[i].port);

}

}

catch (e)

{

InfoMessage (“Error” + e)

}

//============================================================



 

 

InfoMessage(“done”)   // end of the UDP sample script
```



 



