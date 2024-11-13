# Introduction to JavaScript scripts

 

The *WebLOAD JavaScript Reference Guide* provides a detailed description of the syntax and usage of the full set of WebLOAD JavaScript features, including the actions, objects, and functions used to create sophisticated test session scripts.

 

![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)**Note:** Most WebLOAD users do not need this level of detail to create effective testing sessions for their website. Scripts are usually recorded and edited using WebLOAD Recorder, a simple, intuitive interface that provides users with a comprehensive set of testing tools literally at their fingertips, through point-and-click or drag-and-drop convenience. The details in this guide are provided for the convenience of more sophisticated programmers, who may wish to add specific, perhaps complex tailoring to their recorded scripts.

This chapter provides a general introduction to JavaScript scripts.

 

 

##  What are scripts?

 

WebLOAD runs test sessions that simulate the actions of a real user through the use of script files. Scripts are client programs that access the server you want to test. Users create scripts by recording a series of typical activities with the application being tested using WebLOAD Recorder WebLOAD Recorder automatically converts the user activities into script programs. You do not need to know anything about writing scripts to test an application with WebLOAD. No programming or editing skills are required to create or run a successful test session.

 

Scripts are created using WebLOAD Recorder. WebLOAD Recorder operates in conjunction with a Web browser such as Microsoft’s Internet Explorer. As a user navigates the test application in the browser, (for example, navigating between pages, typing text into a form, or clicking the mouse), WebLOAD Recorder records all user actions in a script. During later website testing sessions, WebLOAD simulates every action of the original user and automatically handles all Web interactions, including parsing dynamic HTML, and full support for all security requirements, such as user authentication or SSL protocol use.

 

A simple recorded script is ideal if your WebLOAD test involves a typical sequence of Web activities. These activities are all recorded in your script, and are represented in



 

 

the WebLOAD Recorder by a Script Tree, a set of clear, intuitive icons and visual devices arranged into a logical hierarchical sequence. Each of these activity icons actually represents a block of code within the underlying test script. Scripts are constructed automatically out of ‘building blocks’ of test code, and most users create and run test sessions quite easily, without ever looking into those building blocks to see the actual code inside.

 

Some users prefer to manually edit the code of a recorded script to create more complex, sophisticated test sessions. For example, for a script to work with Java or COM components, a certain degree of programming is required. This guide documents the syntax of the JavaScript objects and functions available to programmers who wish to add more complex functionality to their scripts.

 

Scripts are written in JavaScript. JavaScript is an object-oriented scripting language developed by Netscape Communications Corporation. JavaScript is best known for its use in conjunction with HTML to automate World Wide Web pages. However, JavaScript is actually a full-featured programming language that can be used for many purposes besides Web automation. WebLOAD has chosen JavaScript as the scripting language for test session scripts. WebLOAD JavaScript scripts combine the ease and simplicity of WebLOAD’s visual, intuitive programming environment with the flexibility and power of JavaScript object-oriented programming.

 

For detailed information on using WebLOAD, including creating scripts, running test sessions, and analyzing the results, see the *WebLOAD Recorder User’s Guide* and the

*WebLOAD Console User’s Guide*.

 

 

 

|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image004.gif) |





## WebLOAD scripts Work with an Extended Version of the Standard DOM

WebLOAD Recorder operates in conjunction with a Web browser such as Microsoft’s Internet Explorer. As you execute a sequence of HTTP actions in the browser, WebLOAD Recorder records your actions in a JavaScript script. All Web browsers rely on an extended Document Object Model, or DOM, for optimum handling of HTML pages. The standard browser DOM defines both the logical structure of HTML documents and the way a document is accessed and manipulated. WebLOAD scripts use a standard browser DOM to access and navigate Internet Web pages, including Dynamic HTML and nested links and pages. To facilitate website testing, WebLOAD extends the standard browser DOM with many features, objects, and functions that expedite site testing and evaluation.

 

This section provides a brief overview of the standard DOM structure. Most of the information in this overview was provided by the World Wide Web Consortium (W3C), which develops interoperable technologies (specifications, guidelines, software, and tools) to lead the Web to its full potential as a forum for information, commerce,



 

 

communication, and collective understanding. For more information about the standard DOM structure and components, go to the following websites:

 

http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/introduction.html

 

http://msdn2.microsoft.com/en-us/library/ms533043.aspx

 

http://msdn.microsoft.com/library/default.asp?url=/workshop/author/dhtml/reference/ dhtmlrefs.asp

 

### What is the Document Object Model?

The Document Object Model (DOM) is an application programming interface (API) for valid HTML and well-formed XML documents. The DOM defines the logical structure of documents and the way a document is accessed and manipulated. With the Document Object Model, programmers can build documents, navigate their structure, and add, modify, or delete elements and content. Anything found in an HTML or XML document can be accessed, changed, deleted, or added using the Document Object Model, with a few exceptions—in particular, the DOM interfaces for the XML internal and external subsets have not yet been specified.

 

As a W3C specification, one important objective for the Document Object Model is to provide a standard programming interface that can be used in a wide variety of environments and applications. The DOM is designed to be used with any programming language.

 

Essentially, the DOM is a programming API for documents based on an object structure that closely resembles the structure of the documents it models. For instance, consider this table, taken from an HTML document:

 

```html
<TABLE>

<TBODY>

<TR>

<TD>Shady Grove</TD>

<TD>Aeolian</TD>

</TR>

<TR>

<TD>Over the River, Charlie</TD>

<TD>Dorian</TD>

</TR>

</TBODY>

</TABLE>
```



 

 

### Understanding the DOM Structure

In the DOM, documents have a logical structure that is very much like a tree; to be more precise, that is like a “forest” or “grove”, which can contain more than one tree. Each document contains zero or one doctype nodes, one root element node, and zero or more comments or processing instructions; the root element serves as the root of the element tree for the document. However, the DOM does not specify that documents must be implemented as a tree or a grove, nor does it specify how the relationships among objects be implemented. The DOM is a logical model that may be implemented in any convenient manner. In this specification, we use the term *structure model* to describe the tree-like representation of a document. We also use the term “tree” when referring to the arrangement of those information items which can be reached by using “tree-walking” methods; (this does not include attributes). One important property of DOM structure models is *structural isomorphism*: if any two Document Object Model implementations are used to create a representation of the same document, they will create the same structure model, in accordance with the XML Information Set [Infoset].

 

> **Note:** There may be some variations depending on the parser being used to build the DOM. For instance, the DOM may not contain white spaces in element content if the parser discards them.

The name “Document Object Model” was chosen because it is an “object model” in the traditional object oriented design sense. Documents are modeled using objects, and the model encompasses not only the structure of a document, but also the behavior of a document and the objects of which it is composed. In other words, the nodes in the above diagram do not represent a data structure; they represent objects, which have functions and identity. As an object model, the DOM identifies:

 

- The interfaces and objects used to represent and manipulate a document.
- The semantics of these interfaces and objects - including both behavior and attributes.
- The relationships and collaborations among these interfaces and objects.

The structure of SGML documents has traditionally been represented by an abstract data model, not by an object model. In an abstract data model, the model is centered around the data. In object oriented programming languages, the data itself is encapsulated in objects that hide the data, protecting it from direct external manipulation. The functions associated with these objects determine how the objects may be manipulated, and they are part of the object model.

 

The information in this section has been excerpted from the World Wide Web Consortium introduction to the DOM. For the complete text of the DOM overview, see[ http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/introduction.html. ](http://www.w3.org/TR/2000/WD-DOM-Level-1-20000929/introduction.html)The complete document is found at http://www.w3.org/TR/2001/WD-DOM-Level-3-Core- 20010913/.



Copyright © 1994-2001 World Wide Web Consortium (http://www.w3.org/), (Massachusetts Institute of Technology (http://www.lcs.mit.edu/), Institut National de Recherche en Informatique et en Automatique (http://www.inria.fr/), Keio University (http://www.keio.ac.jp/)).

 

All Rights Reserved. http://www.w3.org/Consortium/Legal/ W3C® DOCUMENT NOTICE AND LICENSE

Copyright © 1994-2001 World Wide Web Consortium (http://www.w3.org/), (Massachusetts Institute of Technology (http://www.lcs.mit.edu/), Institut National de Recherche en Informatique et en Automatique (http://www.inria.fr/), Keio University (http://www.keio.ac.jp/)).

 

All Rights Reserved. http://www.w3.org/Consortium/Legal/

 

Public documents on the W3C site are provided by the copyright holders under the following license. The software or Document Type Definitions (DTDs) associated with W3C specifications are governed by the Software Notice. By using and/or copying this document, or the W3C document from which this statement is linked, you (the licensee) agree that you have read, understood, and will comply with the following terms and conditions:

 

Permission to use, copy, and distribute the contents of this document, or the W3C document from which this statement is linked, in any medium for any purpose and without fee or royalty is hereby granted, provided that you include the following on *ALL* copies of the document, or portions thereof, that you use:

 

1. A link or URL to the original W3C document.
2. The pre-existing copyright notice of the original author, or if it doesn’t exist, a notice of the form: “Copyright © [$date-of-document] World Wide Web Consortium (http://www.w3.org/), (Massachusetts Institute of Technology (http://www.lcs.mit.edu/), Institut National de Recherche en Informatique et en Automatique (http://www.inria.fr/), Keio University (http://www.keio.ac.jp/)). All Rights Reserved. [http://www.w3.org/Consortium/Legal/ ](http://www.w3.org/Consortium/Legal/)(Hypertext is preferred, but a textual representation is permitted.)
3. *If it exists*, the STATUS of the W3C document.

When space permits, inclusion of the full text of this **NOTICE** should be provided. We request that authorship attribution be provided in any software, documents, or other items or products that you create pursuant to the implementation of the contents of this document, or any portion thereof.

 

No right to create modifications or derivatives of W3C documents is granted pursuant to this license. However, if additional requirements (documented in the Copyright FAQ) are satisfied, the right to create modifications or derivatives is sometimes granted by the W3C to individuals complying with those requirements.



THIS DOCUMENT IS PROVIDED “AS IS,” AND COPYRIGHT HOLDERS MAKE NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, OR TITLE; THAT THE CONTENTS OF THE DOCUMENT ARE SUITABLE FOR ANY PURPOSE; NOR THAT THE IMPLEMENTATION OF SUCH CONTENTS WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS.

 

COPYRIGHT HOLDERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THE DOCUMENT OR THE PERFORMANCE OR IMPLEMENTATION OF THE CONTENTS THEREOF.

 

The name and trademarks of copyright holders may NOT be used in advertising or publicity pertaining to this document or its contents without specific, written prior permission. Title to copyright in this document will at all times remain with copyright holders.

 

-----------------



This formulation of W3C’s notice and license became active on April 05 1999 so as to account for the treatment of DTDs, schemas and bindings. See the older formulation for the policy prior to this date. Please see our Copyright FAQ for common questions about using materials from our site, including specific terms and conditions for packages like libwww, Amaya, and Jigsaw. Other questions about this notice can be directed to [site-policy@w3.org ](mailto:site-policy@w3.org)(mailto:site-policy@w3.org).

 

(Last updated by reagle on 1999/04/99.)

 

### DOM Objects Commonly Used in a script

On Internet websites, a simple HTML document may be constructed of a single page, or the document may be constructed of many nested pages, each one including multiple ‘child’ windows, in a recursive structure. Browser DOMs were designed to reflect this flexible approach.

 

When using the DOM, a single Web page document has a logical structure that resembles a single tree. In nested Web pages, each child window is simply one tree in a recursive forest of trees. The typical DOM is ideal for representing Internet Web page access because it provides a flexible, generic model that encompasses both the attributes of the object itself and its interfaces and behaviors. Typical DOM objects include:

 

- The document itself.
- The frames nested in an HTML page, together with any additional nested windows.
- The location information.
- The links, forms, and images on the page.
- The tables, scripts, XML Data Islands, and Meta objects on the page.
- Individual elements of a specific form or frame.

The following table provides a brief overview of the main DOM object components of a typical Web page.

 

**DOM objects commonly used in scripts**

The following table lists the DOM objects commonly used in scripts. A detailed description of each of these objects can be found in the following sections. 

| **Object**                   | **Description**                                              |
| ---------------------------- | ------------------------------------------------------------ |
| **window**                   | The window  object  represents an open browser window. Typically, the browser creates a single window  object when  it opens an HTML document. However, if a document defines one or more frames  the browser creates one window object for the original  document and one additional window object (*a child window*) for each frame. The  child window may be affected by actions that occur in the parent. For  example, closing the parent window causes all child windows to close. |
| **document**                 | The document  object  represents the HTML document in a browser window, storing the HTML data in a  parsed format. Use the document object to retrieve links,  forms, nested frames, images, scripts, and other information about the  document. By default, document used alone represents the  document in the current window. You usually refer directly to the document;  the window  part is  optional and is understood implicitly. |
| **frame**                    | Each frame  object  represents one of the frames imbedded within a Web page. Frames and windows  are essentially comparable. The recursive aspect of the DOM is implemented at  this level. A window may contain a collection of frames. Each frame may  contain multiple child windows, each of which may contain more frames that  contain more windows, and so on. |
| **location**                 | The location object contains  information on the current window URL. |
| **link**                     | A link object contains  information on an external document to which the current document is linked. |
| **form, element, and input** | A form  object  contains the set of elements and input controls (text, radio buttons,  checkboxes, etc.) that are all components of a single form. Each element  object stores the parsed data for a single HTML form element such as <INPUT>, <BUTTON>, or <SELECT>. Each input object  stores the information defining one of the input controls in the form.  Controls are organized by type, for example input type=checkbox.  Forms enable client-side  users to submit data to a server in a standardized format. A form is designed  to collect the required data using a variety of controls, such as INPUT or SELECT. Users viewing the form  fill in the data and then click the SUBMIT button to send it to the server. A script on the server then  processes the data. Notice that the object syntax corresponds to a path  through the DOM hierarchy tree, beginning at the root window and continuing  until the specified item’s properties. |
| **image**                    | Each image  object  contains one of the embedded images found in a document. |
| **script**                   | A script  object  defines a script for the current document that will be interpreted by a  script engine. |
| **title**                    | The title  object  contains the document title, stored as a text string. |



 

### WebLOAD Extension Set

WebLOAD has added the following extensions to the standard DOM properties and methods. This guide provides syntax specifications for these objects.

 

**WebLOAD DOM extension set highlights**

| **WebLOAD  object extensions**                   | **Description**                                              |
| ------------------------------------------------ | ------------------------------------------------------------ |
| **wlCookie**                                     | Sets and deletes cookies.                                    |
| **wlException**                                  | WebLOAD error management object.                             |
| **wlGeneratorGlobal and wlSystemGlobal objects** | Handles global values  shared between script threads or Load Generators. |
| **wlGlobals**                                    | Manages global system and configuration  values.             |
| **wlHeaders**                                    | Contains the key/value pairs in the HTTP  command headers that brought the document. (Get, Post, etc.) |
| **wlHttp**                                       | Performs HTTP transactions and stores  configuration property values for individual transactions. |
| **wlLocals**                                     | Stores local configuration property values.                  |
| **wlMetas**                                      | Stores the parsed data for an HTML meta object.              |
| **wlOutputFile**                                 | Writes script output messages to a global  output file.      |
| **wlRand**                                       | Generates random numbers.                                    |
| **wlSearchPairs**                                | Contains the key/value  pairs in a document’s URL search strings. |
| **wlTables, row, and cell objects**              | Contains the parsed data from an HTML  table.                |
| **XML DOM  objects**                             | XML DOM object set that  generates new XML data to send back to the server for processing. |



Website testing usually means testing how typical user activities are handled by the application being tested. Are the user actions managed quickly, correctly, appropriately? Is the application responsive to the user’s requests? Will the typical user be happy working with this application? When verifying that an application handles user activities correctly, WebLOAD usually focuses on the user activities, recording user actions through the WebLOAD Recorder when initially creating scripts and recreating those actions during subsequent test sessions. The focus on user activities represents a high-level, conceptual approach to test session design.

 

Sometimes a tester may prefer to use a low-level, “nuts-and-bolts” approach that focuses on specific internal implementation commands, such as HTTP transactions. The WebLOAD DOM extension set includes objects, methods, properties, and functions that support this approach. Items in this guide that are relevant to the HTTP Transaction Mode are noted as such in the entries.

 

 

## When Would I Edit the JavaScript in My scripts?

 

WebLOAD Recorder automatically creates JavaScript scripts for test sessions based on the actions performed by the user during recording. You don’t have to be familiar with the JavaScript language to work with WebLOAD and test Web applications. However, as your testing needs increase, you may want to edit and expand the set of scripts that were already recorded. Many users prefer to design test sessions around a set of basic scripts created through WebLOAD Recorder and then expand or tailor those scripts to meet a particular testing need. Some of the reasons for editing JavaScript scripts include:

 

- Recycling and updating a useful library of test scripts from earlier versions of WebLOAD.
- Creating advanced, specialized verification functions.
- Debugging the application being tested.
- Optimization capabilities, to maximize your application’s functionality at minimal cost.

This guide documents the syntax and usage of the actions, functions, objects, and variables provided by WebLOAD to add advanced functionality and tailoring to the JavaScript scripts created through WebLOAD Recorder. JavaScript is very similar to other object-oriented programming languages such as C++, Java, and Visual Basic. The syntax of JavaScript is also very similar to C. If you know any of these other languages, you will find JavaScript very easy to learn. You can probably learn enough about JavaScript to start programming just by studying the examples in this book.

 

> **Note:** For detailed information about the JavaScript language, please refer to the section entitled *The Core JavaScript Language* in the *Netscape JavaScript Guide*, which is supplied in Adobe Acrobat format with the WebLOAD software. You may also learn the elements of JavaScript programming from many books on Web publishing. Keep in mind that some specific JavaScript objects relating to Web publishing do not exist in the WebLOAD test environment.

 

 

## Accessing script Components

 

WebLOAD uses test session scripts to simulate user activities at a website. A script is initially created by WebLOAD Recorder during a recording session. As a user works with a test application in a browser, (for example, navigating between pages, typing text into a form, or clicking the mouse), WebLOAD Recorder stores information about all user actions in a script. Scripts are also edited using WebLOAD Recorder. Users may add functionality or customize their scripts through the objects, functions, and other features described in this guide.

 

Customizing scripts may involve nothing more than dragging an icon from the WebLOAD Recorder toolbar and dropping it into a graphic representation of the script. It may involve entering or changing data through a user-friendly dialog box, or with the help of a Wizard. Some users may even add special features to their scripts by editing the underlying code of the script itself. When working with scripts, users may be working on many different levels. For that reason, the WebLOAD Recorder desktop includes multiple view options, providing information on multiple levels. See the *WebLOAD Scripting Guide* for a more extensive, illustrated explanation of the WebLOAD Recorder desktop components.

 

Most users access scripts primarily through a *Script Tree*, a set of clear, intuitive icons and visual devices representing user activities during a recording session, arranged into a logical structure. Each user activity in the Script Tree is referred to as a node. Nodes are organized in a hierarchical arrangement. The outmost level, or *root* level, is a single script node. The second level directly under the root script node includes all the Web pages to which the user navigated over the course of the recording session. The third level, organized under each Web page, includes all the



 

 

user activities that occurred on the parent Web page. These activities are themselves organized into additional levels. For example, all data input on a single form in a Web page is organized into a single sub-tree of user input nodes collected under the node for that form. The Script Tree appears on the left side of the WebLOAD Recorder desktop.

Web page nodes are added to the Script Tree in one of two ways. Some Web pages are the result of a user action on the previous page, such as clicking a link and jumping to a new page. Other Web pages are created as a result of direct or indirect navigation, such as entering a URL in the browser window, or pop-up windows triggered by a previous navigation. The sets of user activities contained between two direct-navigation Web pages in a Script Tree parallel the *navigation blocks* found within the JavaScript script code.

During a WebLOAD Recorder recording session, a new navigation block is created each time a user completes a direct navigation, manually entering a new URL into the WebLOAD Recorder address bar. Each navigation block is surrounded by a try{} catch{} statement in the corresponding JavaScript script code.

Navigation blocks are useful for error management, especially when running “hands-free” test sessions. For example, the user can define the default testing behavior to be that if an error is encountered during a test session, WebLOAD should throw the error, skip to the next navigation block, and continue with the test session. Errors during playback are indicated by a red X appearing beside the problematic action in the Script Tree.

 

The graphic nodes in a Script Tree actually represent blocks of code within the underlying recorded script. The JavaScript code corresponding to a selected node is automatically displayed in the *JavaScript View pane*. The JavaScript View pane is one of the tabs available in the WebLOAD Recorder desktop.

The graphic nodes in a Script Tree represent user actions on a website. An exact replica, or snapshot, of each user activity is stored during recording and available in the Browser View to aid in debugging and help users remember what each action accomplished. The *Browser View pane* is one of the tabs available in the WebLOAD Recorder desktop.

Web pages are created through HTML programs. The HTML code that underlies each stored Web page is also stored during recording sessions. For easy reference, the HTML code of the Web page associated with a selected node is displayed in the *HTML View pane*. The HTML View pane is one of the tabs available in the WebLOAD Recorder desktop.

Web pages have a logical structure that may be represented through a series of DOM object trees. The DOM tree for a selected Web page is essentially a hierarchically structured, more easily understood representation of the DOM objects found in the HTML code for that Web page. The DOM tree of the Web page associated with a selected node is displayed in the *DOM View pane*. The DOM View pane is one of the tabs available in the WebLOAD Recorder desktop. When



 

 

working with the DOM View, the center pane is actually split in half, with the upper half displaying the DOM View and the lower half displaying the corresponding Web page, seen in the Browser View.

The following figure illustrates a WebLOAD Recorder desktop displaying the Script Tree and DOM and Browser Views. The Script Tree is on the left. The Browser View pane on the lower right focuses on a piece of the selected form as it appeared on the Web page at the time this script was recorded. The DOM View pane on the upper right displays the DOM objects that represent the selected form, arranged in a tree that corresponds to the user activity in the selected form.

 

 

|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image009.jpg) |





 

*Figure 1: Script Tree, DOM, and Browser Views*



 

 

![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image010.gif)

## Editing the JavaScript Code in a script

 

### Accessing the JavaScript Code within the Script Tree

WebLOAD Recorder provides a complete graphic user interface for creating and editing script files. Additions or changes to a script are usually made through the WebLOAD Recorder, working with intuitive icons representing user actions in a graphic Script Tree. For greater clarity, the JavaScript code that corresponds to each user action in a script is also visible in the JavaScript View pane on the WebLOAD Recorder desktop.

 

While most people never really work with the JavaScript code within their script, some users do wish to manually edit the JavaScript code underlying their Script Tree. For example, some test sessions may involve advanced WebLOAD testing features that cannot be completely implemented though the GUI, such as Java or XML objects.

Editing the JavaScript code in a script does not necessarily mean editing a huge JavaScript file. Most of the time users only wish to add or edit a specific feature or a small section of the code. WebLOAD Recorder provides access to the JavaScript code in a script through JavaScript Object nodes, which are seen on the following levels:

 

JavaScript Object nodes—individual nodes in the Script Tree. Empty JavaScript Object nodes may be dragged from the WebLOAD Recorder toolbar and dropped onto the Script Tree at any point selected by the user, as described in the *WebLOAD Scripting Guide.* Use the IntelliSense Editor, described in [*Using the IntelliSense*](#_bookmark18)[ *JavaScript Editor* ](#_bookmark18)(on page [18](#_bookmark18)), to add lines of code or functions to the JavaScript Object.

![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image005.jpg)Converted Web page—the sub-tree or branch of a Script Tree that represents all user activity within a single Web page, converted to a single JavaScript Object node. A Web page branch is ‘rooted’ in the Script Tree with an icon that represents the user’s navigation to that page’s URL. The icons on that branch represent all user activities from the point at which that Web page was first accessed until the point at which the user navigated to a different Web page. Some testing features may require manually editing or rewriting the JavaScript code for user activities within a Web page. To manually edit code in a recorded script, the Web page branch that includes that code must be converted to a JavaScript Object. Converting a Web page branch to a JavaScript Object is simple. Right click the preferred Web page node in the Script Tree and select Convert to JavaScript Object from the pop-up menu. The entire Web page branch becomes a single JavaScript Object, which can then be edited through the IntelliSense Editor.

 

**Note:** Once a branch has been converted to a single JavaScript Object, the various user activity icons that were on that branch are no longer individually accessible.

Imported JavaScript File—an external JavaScript file that should be incorporated within the body of the current script. Select **Edit** **** **Import JavaScript File** from the



 

 

WebLOAD Recorder menu to import the file of your choice. Often testers work with a library of pre-existing library files from which they may choose functions that are relevant to the current test session. This modular approach to programming simplifies and speeds up the testing process, and is fully supported and endorsed by WebLOAD.

Converted Script Tree—if necessary, an entire Script Tree can be converted to a single JavaScript Object node consisting of a straight JavaScript text file. Right click the Script Tree’s root node and choose Convert to JavaScript Object from the pop- up menu. However, this conversion is not recommended unless manual editing of an entire script file is truly required for the test session.

 

### Using the IntelliSense JavaScript Editor

For those users who wish to manually edit their scripts, WebLOAD Recorder provides three levels of programming assistance:

 

An IntelliSense Editor mode for the JavaScript View pane.

Add new lines of code to your script or edit existing JavaScript functions through the IntelliSense Editor mode of the JavaScript View pane. The IntelliSense Editor helps you write the JavaScript code for a new function by formatting new code and prompting with suggestions and descriptions of appropriate code choices and syntax as programs are being written. IntelliSense supports the following shortcut keys:

 

**Period (“.”)** – Enter a period after the object name, to display a drop-down list of the object’s available properties that can be added to the script (see

[Figure 2](#_bookmark19)).

**<CTRL> <Space>** – While typing the name of an object, you can type <CTRL>

<Space> to display a drop-down list of the available objects that begin with the letters that you entered. For example, if you type wl the IntelliSense Editor displays a drop-down list of all of the objects that begin with wl (such as wlhttp).

In addition, the IntelliSense Editor gives a structure to the code with the outline bar and line numbering.

 

Collapsing the code enables you to view the heading of the section, without seeing the code within the section. To expand or collapse different sections of the code:

 

Click the plus sign (+) or minus sign (-) on the outline bar,

-Or-

 

Right-click within the IntelliSense Editor and select Outlining from the pop-up menu. The available outlining options are:



 

 

**Toggle outline** – Collapses or expands the section at the mouse location.

**Toggle all outline** – Collapses or expands all outlines.

**Collapse to definition** – Collapses all outlines.

You can enable or disable both the outline bar and line numbering features by:

 

Selecting **Edit** **** **Enable Outlining** or **Line Numbers**,

-Or-

 

Right-clicking within the IntelliSense Editor and selecting **Enable Outlining** or

**Line Numbers** from the pop-up menu.

When these features are enabled, a checkmark appears next to the name in the Edit and pop-up menus. By default, these features are enabled, but WebLOAD opens with the settings that were saved during the previous WebLOAD session. During playback and debug modes, all outlines are expanded.

 

Use WebLOAD Recorder’s predefined delimiters to keep your code structured and organized. The available delimiters include:

 

For JavaScript functions, use the “{“ as the start delimiter and the “}” end delimiter.

For script tree nodes, insert a WLIDE comment from the General WebLOAD Recorder toolbox. This automatically inserts a start delimiter “//” and end

delimiter “End WLIDE”.

For more information, see the *WebLOAD Scripting Guide.*

 

 

|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg) |





*Figure 2: IntelliSense Editor Mode for JavaScript View Pane*

 

A selection of the most commonly used functions and commands, available through the **Insert** menu.



 

 

You can choose to program your own JavaScript Object code within your script and take advantage of the WebLOAD Recorder to simplify your programming efforts. Rather than manually typing out the code for each command, with the risk of making a mistake, even a trivial typographical error, and adding invalid code to the script file, you may select an item from the **Insert** menu, illustrated in the following figure, to bring up a list of available commands and functions for the selected item. WebLOAD Recorder automatically inserts the correct code for the selected item into the JavaScript Object currently being edited. You may then change specific parameter values without any worries about accidental mistakes in the function syntax.

 

 

|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg) |





*Figure 3: Insert Menu*

 

In addition to the Insert menu, you may select an item from the Insert Variable menu, to add system and user-defined parameters to the script. This eliminates the need for manual coding.



 

 

![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

 

*Figure 4: Insert Variable Menu*

 

![img](file:///C:/Users/ASURA/AppData/Local/Temp/msohtmlclip1/01/clip_image005.jpg)A Syntax Checker that checks the syntax of the code in your script file and catches simple syntax errors before you spend any time running a test session. While standing in the JavaScript View pane of the WebLOAD Recorder desktop, select **Tools** **** **Check Syntax** to check the syntax of the code in your script file.

 

**Important:** WebLOAD Recorder scripts should be edited only within the confines of WebLOAD Recorder, not an external editor. If you use an external editor to modify the JavaScript code in a script file generated by WebLOAD Recorder, your visual script will be lost.

Script code that you wish to write or edit must be part of a JavaScript Object in the Script Tree. Adding or converting JavaScript Objects in a Script Tree is described in [*Accessing the JavaScript Code within the Script Tree* ](#_bookmark17)(on page [17](#_bookmark17)).