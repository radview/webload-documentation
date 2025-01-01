# Appendix B: LiveConnect Overview

This appendix describes using LiveConnect technology to let Java and JavaScript code communicate with each other. LiveConnect is a registered trademark of Netscape Communications Corporation. This information is provided by Netscape, and can be found in the JavaScript Reference site at

[http://www.js-examples.com/page/reference	partjava.html](http://www.js-examples.com/page/reference__partjava.html)).

This appendix assumes you are familiar with Java programming. For additional information on LiveConnect, see the LiveConnect information on the Mozilla Developer Center (`<http://developer.mozilla.org/en/docs/LiveConnect>`).



## Working with Wrappers

In JavaScript, a *wrapper* is an object of the target language data type that encloses an object of the source language. On the JavaScript side, you can use a wrapper object to access methods and fields of the Java object; calling a method or accessing a property on the wrapper results in a call on the Java object. On the Java side, JavaScript objects are wrapped in an instance of the class netscape.javascript.JSObject and passed to Java.

When a JavaScript object is sent to Java, the runtime engine creates a Java wrapper of type JSObject. When a JSObject is sent from Java to JavaScript, the runtime engine unwraps the JSObject revealing the original JavaScript object type. The JSObject class provides an interface for invoking JavaScript methods and examining JavaScript properties.



## JavaScript to Java Communication

When you refer to a Java package or class, or work with a Java object or array, you use one of the special LiveConnect objects. All JavaScript access to Java takes place with these objects, which are summarized in the following table.




|**Object**|**Description**|
| :- | :- |
|JavaArray|A wrapped Java array, accessed from within JavaScript code.|
|JavaClass|A JavaScript reference to a Java class.|
|JavaObject|A wrapped Java object, accessed from within JavaScript code.|
|JavaPackage|A JavaScript reference to a Java package.|

> **Note:** Because Java is a strongly typed language and JavaScript is weakly typed, the JavaScript runtime engine converts argument values into the appropriate data types for the other language when you use LiveConnect.

In some ways, the existence of the LiveConnect objects is transparent, because you interact with Java in a fairly intuitive way. For example, you can create a Java String object and assign it to the JavaScript variable myString by using the new operator with the Java constructor, as follows:

`var myString = new java.lang.String("Hello world")`

In the previous example, the variable myString is a JavaObject because it holds an instance of the Java object String. As a JavaObject, myString has access to the public instance methods of java.lang.String and its superclass, java.lang.Object. These Java methods are available in JavaScript as methods of the JavaObject, and you can call them as follows:

`myString.length() // returns 11`

### The Packages Object
If a Java class is not part of the java, sun, or netscape packages, you access it with the Packages object. For example, suppose the Redwood Corporation uses a Java package called redwood to contain various Java classes that it implements.

To create an instance of the HelloWorld class in redwood, you access the constructor of the class as follows:

`var red = new Packages.redwood.HelloWorld()`

You can also access classes in the default package (that is, classes that don’t explicitly name a package). For example, if the HelloWorld class is directly in the CLASSPATH and not in a package, you can access it as follows:

`var red = new Packages.HelloWorld()`





The LiveConnect java, sun, and netscape objects provide shortcuts for commonly used Java packages. For example, you can use the following:

`var myString = new java.lang.String("Hello world")`

instead of the longer version:

`var myString = new Packages.java.lang.String("Hello world")`

### Working with Java Arrays
When any Java method creates an array and you reference that array in JavaScript, you are working with a JavaArray. For example, the following code creates the JavaArray x with ten elements of type int:

`x = java.lang.reflect.Array.newInstance(java.lang.Integer, 10)`

Like the JavaScript Array object, JavaArray has a length property that returns the number of elements in the array. Unlike Array.length, JavaArray.length is a read-only property, because the number of elements in a Java array are fixed at the time of creation.

### Package and Class References
Simple references to Java packages and classes from JavaScript create the JavaPackage and JavaClass objects. In the earlier example about the Redwood corporation, for example, the reference Packages.redwood is a JavaPackage object. Similarly, a reference such as java.lang.String is a JavaClass object.

Most of the time, you don’t have to worry about the JavaPackage and JavaClass objects—you just work with Java packages and classes, and LiveConnect creates these objects transparently.

In JavaScript 1.3 and earlier, JavaClass objects are not automatically converted to instances of java.lang.Class when you pass them as parameters to Java methods--you must create a wrapper around an instance of java.lang.Class. In the following example, the forName method creates a wrapper object theClass, which is then passed to the newInstance method to create an array.

`// JavaScript 1.3`

`theClass = java.lang.Class.forName("java.lang.String")` 

`theArray = java.lang.reflect.Array.newInstance(theClass, 5)` 



In JavaScript 1.4 and later, you can pass a JavaClass object directly to a method, as shown in the following example:

`// JavaScript 1.4 theArray =`

`java.lang.reflect.Array.newInstance(java.lang.String, 5)`



### Arguments of Type Char
In JavaScript 1.4 and later, you can pass a one-character string to a Java method that requires an argument of type char. For example, you can pass the string "H" to the Character constructor as follows:

`c = new java.lang.Character("H")`

In JavaScript 1.3 and earlier, you must pass such methods an integer that corresponds to the Unicode value of the character. For example, the following code also assigns the value "H" to the variable c:

`c = new java.lang.Character(72)`



### Handling Java Exceptions in JavaScript
When Java code fails at run time, it throws an exception. If your JavaScript code accesses a Java data member or method and fails, the Java exception is passed on to JavaScript for you to handle. Beginning with JavaScript 1.4, you can catch this exception in a try...catch statement.

For example, suppose you are using the Java forName method to assign the name of a Java class to a variable called theClass. The forName method throws an exception if the value you pass it does not evaluate to the name of a Java class. Place the forName assignment statement in a try block to handle the exception, as follows:

```javascript
function getClass(javaClassName) 

{ try 

{

var theClass = java.lang.Class.forName(javaClassName);

} catch (e) {

return ("The Java exception is " + e);

}

return theClass

}

```



In this example, if javaClassName evaluates to a legal class name, such as "java.lang.String", the assignment succeeds. If javaClassName evaluates to an invalid class name, such as "String", the getClass function catches the exception and returns something similar to the following:

The Java exception is java.lang.ClassNotFoundException: String See [*Exception Handling Statements* ](#exception-handling-statements), for more information about JavaScript exceptions.



## Java to JavaScript Communication

If you want to use JavaScript objects in Java, you must import the netscape.javascript package into your Java file. This package defines the following classes:

- netscape.javascript.JSObject allows Java code to access JavaScript methods and properties.
- netscape.javascript.JSException allows Java code to handle JavaScript errors.



Starting with JavaScript 1.2, these classes are delivered in a .jar file; in previous versions of JavaScript, these classes are delivered in a .zip file. 

To access the LiveConnect classes, place the .jar or .zip file in the CLASSPATH of the JDK compiler in either of the following ways:

- Create a CLASSPATH environment variable to specify the path and name of .jar or .zip file.

- Specify the location of .jar or .zip file when you compile by using the -classpath command line parameter.

For example, in Navigator 4.0 for Windows NT, the classes are delivered in the java40.jar file in the Program\Java\Classes directory beneath the Navigator directory.

**To specify an environment variable in Windows NT:**

1. Double-click the **System** icon in the Control Panel.

2. Create a user environment variable called CLASSPATH with a value similar to the following:

   `D:\Navigator\Program\Java\Classes\java40.jar`

   See the Sun JDK documentation for more information about CLASSPATH.

> **Note:** Because Java is a strongly typed language and JavaScript is weakly typed, the JavaScript runtime engine converts argument values into the appropriate data types for the other language when you use LiveConnect. See [*Data Type Conversions* ](#data-type-conversions), for complete information.



### Using the LiveConnect Classes

All JavaScript objects appear within Java code as instances of netscape.javascript.JSObject. When you call a method in your Java code, you can pass it a JavaScript object as one of its argument. To do so, you must define the corresponding formal parameter of the method to be of type JSObject.

Also, any time you use JavaScript objects in your Java code, you should put the call to the JavaScript object inside a try...catch statement that handles exceptions of type netscape.javascript.JSException. This allows your Java code to handle errors in JavaScript code execution that appear in Java as exceptions of type JSException.

#### Accessing JavaScript with JSObject

For example, suppose you are working with the Java class called JavaDog. As shown in the following code, the JavaDog constructor takes the JavaScript object jsDog, which is defined as type JSObject, as an argument:

```javascript
import netscape.javascript.\*; public class JavaDog

{

public String dogBreed; public String dogColor; public String dogSex;

// define the class constructor public JavaDog(JSObject jsDog)

{

// use try...catch to handle JSExceptions here this.dogBreed = (String)jsDog.getMember("breed"); this.dogColor = (String)jsDog.getMember("color"); this.dogSex = (String)jsDog.getMember("sex");

}
```



> **Note:** The getMember method of JSObject is used to access the properties of the JavaScript object. The previous example uses getMember to assign the value of the JavaScript property jsDog.breed to the Java data member JavaDog.dogBreed.

A more realistic example would place the call to getMember inside a try...catch statement to handle errors of type JSException. See [Handling JavaScript Exceptions in Java](#handling-javascript-exceptions-in-java), for more information.

To get a better sense of how getMember works, look at the definition of the custom JavaScript object Dog:

```javascript
function Dog(breed,color,sex) 

{ 

this.breed = breed this.color = color

this.sex = sex

}
```



You can create a JavaScript instance of Dog called gabby as follows:

`gabby = new Dog("lab","chocolate","female")`

If you evaluate gabby.color, you can see that it has the value "chocolate". Now suppose you create an instance of JavaDog in your JavaScript code by passing the gabby object to the constructor as follows:

`javaDog = new Packages.JavaDog(gabby)`

If you evaluate javaDog.dogColor, you can see that it also has the value "chocolate", because the getMember method in the Java constructor assigns dogColor the value of gabby.color.

#### Handling JavaScript Exceptions in Java

When JavaScript code called from Java fails at run time, it throws an exception. If you are calling the JavaScript code from Java, you can catch this exception in a try...catch statement. The JavaScript exception is available to your Java code as an instance of netscape.javascript.JSException.

JSException is a Java wrapper around any exception type thrown by JavaScript, similar to the way that instances of JSObject are wrappers for JavaScript objects. Use JSException when you are evaluating JavaScript code in Java.

When you are evaluating JavaScript code in Java, the following situations can cause run-time errors:

- The JavaScript code is not evaluated, either due to a JavaScript compilation error or to some other error that occurred at run time.

  The JavaScript interpreter generates an error message that is converted into an instance of JSException.

- Java successfully evaluates the JavaScript code, but the JavaScript code executes an unhandled throw statement.

  JavaScript throws an exception that is wrapped as an instance of JSException. Use the getWrappedException method of JSException to unwrap this exception in Java.

For example, suppose the Java object eTest evaluates the string jsCode that you pass to it. You can respond to either type of run-time error the evaluation causes by implementing an exception handler such as the following:

```javascript
import netscape.javascript.JSObject; import netscape.javascript.JSException;

public class eTest {

public static Object doit(JSObject obj, String jsCode) {



try {

obj.eval(jsCode);

} catch (JSException e) {

if (e.getWrappedException()==null) return e;

return e.getWrappedException();

}

return null;

}

}
```

In this example, the code in the try block attempts to evaluate the string jsCode that you pass to it. Let’s say you pass the string "myFunction()" as the value of jsCode. If myFunction is not defined as a JavaScript function, the JavaScript interpreter cannot evaluate jsCode. The interpreter generates an error message, the Java handler catches the message, and the doit method returns an instance of netscape.javascript.JSException.

However, suppose myFunction is defined in JavaScript as follows:

```javascript
function myFunction() { try {

if (theCondition == true) { return "Everything’s ok";

} else {

throw "JavaScript error occurred" ;

}

} catch (e) {

if (canHandle == true) { handleIt();

} else {

throw e;

}

}

}
```

If theCondition is false, the function throws an exception. The exception is caught in the JavaScript code, and if canHandle is true, JavaScript handles it. If canHandle is false, the exception is rethrown, the Java handler catches it, and the doit method returns a Java string:

JavaScript error occurred

See [*Exception Handling Statements* ](#exception-handling-statements), for complete information about JavaScript exceptions.



#### Backward Compatibility

In JavaScript 1.3 and earlier versions, the JSException class had three public constructors that optionally took a string argument, specifying the detail message or other information for the exception. The getWrappedException method was not available.

Use a try...catch statement such as the following to handle LiveConnect exceptions in JavaScript 1.3 and earlier versions:

```javascript
try {

global.eval("foo.bar = 999;");

} catch (Exception e) {

if (e instanceof JSException) { jsCodeFailed()";

} else {

otherCodeFailed();

}

}
```

In this example, the eval statement fails if foo is not defined. The catch block executes the jsCodeFailed method if the eval statement in the try block throws a JSException; the otherCodeFailed method executes if the try block throws any other error.



## Data Type Conversions

Because Java is a strongly typed language and JavaScript is weakly typed, the JavaScript runtime engine converts argument values into the appropriate data types for the other language when you use LiveConnect.



### **JavaScript to Java Conversions**
When you call a Java method and pass it parameters from JavaScript, the data types of the parameters you pass in are converted according to the rules described in the following sections:

- [*Number Values* ](#number-values)
- [*Boolean Values* ](#boolean-values)
- [*String Values* ](#string-values)
- [*Undefined Values* ](#undefined-values)
- [*Null Values* ](#null-values)
- [*JavaArray and JavaObject Objects* ](#javaarray-and-javaobject-objects)
- [*JavaClass Objects* ](#javaclass-objects)
- [*Other JavaScript Objects* ](#other-javascript-objects)

The return values of methods of netscape.javascript.JSObject are always converted to instances of java.lang.Object. The rules for converting these return values are also described in these sections.

For example, if JSObject.eval returns a JavaScript number, you can find the rules for converting this number to an instance of java.lang.Object in [*Number Values* ](#number-values).

#### Number Values

When you pass JavaScript number types as parameters to Java methods, Java converts the values according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|double|The exact value is transferred to Java without rounding and without a loss of magnitude or sign.|
|lava.lang.Double java.lang.Object|A new instance of java.lang.Double is created, and the exact value is transferred to Java without rounding and without a loss of magnitude or sign.|
|float|<p>Values are rounded to float precision.</p><p>Values that are unrepresentably large or small are rounded to +infinity or -infinity.</p>|
|<p>byte	char</p><p>int	long short</p>|<p>Values are rounded using round-to-negative- infinity mode.</p><p>Values that are unrepresentably large or small result in a run-time error.</p><p>NaN values are converted to zero.</p>|
|java.lang.String|<p>Values are converted to strings. For example:</p><p>237 becomes "237"</p>|
|boolean|<p>0 and NaN values are converted to false.</p><p>Other values are converted to true.</p>|


When a JavaScript number is passed as a parameter to a Java method that expects an instance of java.lang.String, the number is converted to a string. Use the == operator to compare the result of this conversion with other string values.



#### Boolean Values

When you pass JavaScript Boolean types as parameters to Java methods, Java converts the values according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|boolean|All values are converted directly to the Java equivalents.|
|lava.lang.Boolean java.lang.Object|A new instance of java.lang.Boolean is created. Each parameter creates a new instance, not one instance with the same primitive value.|
|java.lang.String|<p>Values are converted to strings. For example: true becomes "true"</p><p>false becomes "false"</p>|
|<p>byte	char</p><p>double	float</p><p>int	long short</p>|<p>true becomes 1</p><p>false becomes 0</p>|

When a JavaScript Boolean is passed as a parameter to a Java method that expects an instance of java.lang.String, the Boolean is converted to a string. Use the == operator to compare the result of this conversion with other string values.



#### String Values

When you pass JavaScript string types as parameters to Java methods, Java converts the values according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|lava.lang.String java.lang.Object|<p>JavaScript 1.4:</p><p>A JavaScript string is converted to an instance of java.lang.String with a Unicode value.</p><p>JavaScript 1.3 and earlier:</p><p>A JavaScript string is converted to an instance of java.lang.String with an ASCII value.</p>|
|<p>byte	double</p><p>float	int</p><p>long	short</p>|All values are converted to the appropriate numbers.|
|char|<p>JavaScript 1.4:</p><p>One-character strings are converted to Unicode characters.</p><p>All other values are converted to numbers. JavaScript 1.3 and earlier:</p><p>All values are converted to numbers.</p>|
|boolean|<p>The empty string becomes false.</p><p>All other values become true.</p>|



#### Undefined Values

When you pass undefined JavaScript values as parameters to Java methods, Java converts the values according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|lava.lang.String java.lang.Object|The value is converted to an instance of java.lang.String whose value is the string "undefined".|
|boolean|The value becomes false.|
|double	float|The value becomes NaN.|
|<p>byte	char</p><p>int	long Short</p>|The value becomes 0.|


The undefined value conversion is possible in JavaScript 1.3 and later versions only. Earlier versions of JavaScript do not support undefined values.

When a JavaScript undefined value is passed as a parameter to a Java method that expects an instance of java.lang.String, the undefined value is converted to a string. Use the == operator to compare the result of this conversion with other string values.



#### Null Values

When you pass null JavaScript values as parameters to Java methods, Java converts the values according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|Any class, any interface type|The value becomes null.|
|<p>byte		char double			float int	long</p><p>short</p>|The value becomes 0.|
|boolean|The value becomes false.|

#### JavaArray and JavaObject Objects

In most situations, when you pass a JavaScript JavaArray or JavaObject as a parameter to a Java method, Java simply unwraps the object; in a few situations, the object is coerced into another data type according to the rules described in the following table:

*Table: JavaArray and JavaObject type conversion rules*

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|Any interface or class that is assignment-compatible with the unwrapped object.|The object is unwrapped.|
|java.lang.String|The object is unwrapped, the toString method of the unwrapped Java object is called, and the result is returned as a new instance of java.lang.String.|
|<p>byte	char</p><p>double	float</p><p>int	long short</p>|<p>The object is unwrapped, and either of the following situations occur:</p><p>- If the unwrapped Java object has a doubleValue method, the JavaArray or JavaObject is converted to the value returned by this method.</p><p>- If the unwrapped Java object does not have a</p><p>&emsp;doubleValue method, an error occurs.</p>|
|boolean|<p>In JavaScript 1.3 and later versions, the object is unwrapped and either of the following situations occur:</p><p>- If the object is null, it is converted to false.</p><p>- If the object has any other value, it is converted to true.</p><p>In JavaScript 1.2 and earlier versions, the object is unwrapped and either of the following situations occur:</p><p>- If the unwrapped object has a booleanValue method, the source object is converted to the return value.</p><p>- If the object does not have a booleanValue</p><p>&emsp;method, the conversion fails.</p>|




An interface or class is assignment-compatible with an unwrapped object if the unwrapped object is an instance of the Java parameter type. That is, the following statement must return true:

`*unwrappedObject* instanceof *parameterType*`

#### JavaClass Objects

When you pass a JavaScript JavaClass object as a parameter to a Java method, Java converts the object according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|java.lang.Class|The object is unwrapped.|
|<p>java.lang.JSObject</p><p>java.lang.Object</p>|The JavaClass object is wrapped in a new instance of java.lang.JSObject.|
|java.lang.String|The object is unwrapped, the toString method of the unwrapped Java object is called, and the result is returned as a new instance of java.lang.String.|
|boolean|<p>In JavaScript 1.3 and later versions, the object is unwrapped and either of the following situations occur:</p><p>- If the object is null, it is converted to false.</p><p>- If the object has any other value, it is converted to true.</p><p>In JavaScript 1.2 and earlier versions, the object is unwrapped and either of the following situations occur:</p><p>- If the unwrapped object has a booleanValue method, the source object is converted to the return value.</p><p>- If the object does not have a booleanValue method, the conversion fails.</p>|



#### Other JavaScript Objects

When you pass any other JavaScript object as a parameter to a Java method, Java converts the object according to the rules described in the following table:

|**Java parameter type**|**Conversion rules**|
| :- | :- |
|<p>java.lang.JSObject</p><p>java.lang.Object</p>|The object is wrapped in a new instance of java.lang.JSObject.|
|java.lang.String|The object is unwrapped, the toString method of the unwrapped Java object is called, and the result is returned as a new instance of java.lang.String.|
|<p>byte	char</p><p>Double	float</p><p>int	long</p><p>short</p>|The object is converted to an appropriate value using the logic of the ToPrimitive operator. The *PreferredType* hint used with this operator is Number.|
|boolean|<p>In JavaScript 1.3 and later versions, the object is unwrapped and either of the following situations occur:</p><p>- If the object is null, it is converted to false.</p><p>- If the object has any other value, it is converted to true.</p><p>In JavaScript 1.2 and earlier versions, the object is unwrapped and either of the following situations occur:</p><p>- If the unwrapped object has a booleanValue method, the source object is converted to the return value.</p><p>- If the object does not have a booleanValue</p><p>&emsp;method, the conversion fails.</p>|



### Java to JavaScript Conversions
Values passed from Java to JavaScript are converted as follows:

- Java byte, char, short, int, long, float, and double are converted to JavaScript numbers.
- A Java Boolean is converted to a JavaScript Boolean.
- An object of class netscape.javascript.JSObject is converted to the original JavaScript object.
- Java arrays are converted to a JavaScript pseudo-Array object; this object behaves just like a JavaScript Array object: you can access it with the syntax arrayName[index] (where index is an integer), and determine its length with arrayName.length.
- A Java object of any other class is converted to a JavaScript wrapper, which can be used to access methods and fields of the Java object:
  - Converting this wrapper to a string calls the toString method on the original object.
  - Converting to a number calls the doubleValue method, if possible, and fails otherwise.
  - Converting to a Boolean in JavaScript 1.3 and later versions returns false if the object is null, and true otherwise.
  - Converting to a Boolean in JavaScript 1.2 and earlier versions calls the booleanValue method, if possible, and fails otherwise.



> **Note:** Instances of java.lang.Double and java.lang.Integer are converted to JavaScript objects, not to JavaScript numbers. Similarly, instances of java.lang.String are also converted to JavaScript objects, not to JavaScript strings.

Java String objects also correspond to JavaScript wrappers. If you call a JavaScript method that requires a JavaScript string and pass it this wrapper, you’ll get an error. Instead, convert the wrapper to a JavaScript string by appending the empty string to it, as shown here:

`var JavaString = JavaObj.methodThatReturnsAString(); var JavaScriptString = JavaString + "";`


## Exception Handling Statements

You can throw and catch exceptions using the throw and try...catch statements. You also use the try...catch statement to handle Java exceptions. See [*Handling Java Exceptions in JavaScript* ](#handling-java-exceptions-in-javascript), and [*Handling JavaScript Exceptions in Java* ](#handling-javascript-exceptions-in-java), for information.

### The Throw Statement
Use the throw statement to throw an exception. When you throw an exception, you specify an expression containing the value of the exception:

throw expression

The following code throws several exceptions.

throw "Error2"	// generates an exception with a string value throw 42	// generates an exception with the value 42 throw true	// generates an exception with the value true

You can specify an object when you throw an exception. You can then reference the

object’s properties in the catch block. The following example creates an object

myUserException of type UserException and uses it in a throw statement.

```javascript
// Create an object type UserException function UserException (message) {

this.message=message this.name="UserException"

}

// Create an instance of the object type and throw it myUserException=new UserException("Value too high") throw myUserException
```



### The Try...Catch Statement
![ref8]The try...catch statement marks a block of statements to try, and specifies a response should an exception be thrown. If an exception is thrown, the try...catch statement catches it.

**Note:** There are some exceptions that are not caught with the try...catch statement. This includes the HTTP errors, which are thrown by the HTTP server.

The try...catch statement consists of the following:

- A try block, which contains one or more statements.
- A catch block, containing statements that specify what to do if an exception is thrown in the try block.

  That is, you want the try block to succeed, and if it does not succeed, you want control to pass to the catch block.

If any statement within the try block (or in a function called from within the try block) throws an exception, control immediately shifts to the catch block. If no exception is thrown in the try block, the catch block is skipped.

- The finally block executes after the try and catch blocks execute but before the statements following the try...catch statement.

The following example uses a try...catch statement. The example calls a function that retrieves a month name from an array based on the value passed to the function. If the value does not correspond to a month number (1-12), an exception is thrown with the value "InvalidMonthNo" and the statements in the catch block set the monthName variable to "unknown".

```javascript
function getMonthName (mo) {

// Adjust month number for array index (1=Jan, 12=Dec) mo=mo-1

var months=new Array ("Jan","Feb","Mar","Apr","May",

"Jun","Jul","Aug","Sep","Oct","Nov","Dec") if (months[mo] != null) {

return months[mo]

} else {

throw "InvalidMonthNo"

}

}

try {

// statements to try monthName=getMonthName(myMonth)

// function could throw exception



}

catch (e) { monthName="unknown" logMyErrors(e)

// pass exception object to error handler

}
```




### The Catch Block
Use the try...catch statement’s catch block (*recovery* block) to execute error- handling code. A catch block looks as follows:

```javascript
catch (catchID) 

{ statements

}


```

Every catch block specifies an identifier (catchID in the preceding syntax) that holds the value specified by the throw statement; you can use this identifier to get information about the exception that was thrown. JavaScript creates this identifier when the catch block is entered; the identifier lasts only for the duration of the catch block; after the catch block finishes executing, the identifier is no longer available.

For example, the following code throws an exception. When the exception occurs, control transfers to the catch block.

```javascript
try 

{

throw "myException" // generates an exception

}

catch (e) {

// statements to handle any exceptions

logMyErrors(e) // pass exception object to error handler

}
```



### The Finally Block
The finally block contains statements to execute after the try and catch blocks execute but before the statements following the try...catch statement. The finally block executes whether or not an exception is thrown. If an exception is thrown, the statements in the finally block execute even if no catch block handles the exception.

You can use the finally block to make your script fail gracefully when an exception occurs; for example, you may need to release a resource that your script has tied up. The following example opens a file and then executes statements that use the file (server-side JavaScript allows you to access files). If an exception is thrown while the file is open, the finally block closes the file before the script fails.

```javascript
try {

openMyFile()	// tie up a resource writeMyFile(theData)

}

finally {

closeMyFile() // always close the resource

}
```



### Nesting Try...Catch Statements
You can nest one or more try...catch statements. If an inner try...catch statement does not have a catch block, the enclosing try...catch statement’s catch block is checked for a match.




## JSException and JSObject Classes

This section describes the JSException and JSObject Classes.

### **JSException Class**
The public class JSException extends RuntimeException.

```
java.lang.Object

|

	+---java.lang.Throwable

		|

		+---java.lang.Exception

			|

			+---java.lang.RuntimeException

				|

				+	netscape.javascript.JSException
```

#### Description

JSException is an exception that is thrown when JavaScript code returns an error.



#### Constructor Summary

The netscape.javascript.JSException class has the following constructors:

*Table: JSException constructors*

|**Constructor**|**Description**|
| :- | :- |
|JSException|Deprecated constructors optionally let you specify a detail message and other information.|

#### Method Summary

The netscape.javascript.JSException class has the following method:

|**Method**|**Description**|
| :- | :- |
|GetWrappedException|Instance method getWrappedException.|

The following sections show the declaration and usage of the constructors and method.

#### Backward Compatibility

JavaScript 1.1 through 1.3. JSException had three public constructors that optionally took a string argument, specifying the detail message or other information for the exception. The getWrappedException method was not available.



#### JSException Constructor

Constructors, deprecated in JavaScript 1.4. Construct a JSException with an optional detail message.

**Declaration**

1. public JSException()
1. public JSException(String s)
1. public JSException(String s, String filename,

   int lineno, String source, int tokenIndex)



**Arguments**

|**Argument Name**|**Description**|
| :- | :- |
|s|The detail message.|
|filename|The URL of the file where the error occurred, if possible.|
|lineno|The line number if the file, if possible.|
|source|The string containing the JavaScript code being evaluated.|
|tokenIndex|The index into the source string where the error occurred.|

#### GetWrappedException

Instance method getWrappedException.

**Declaration**

public Object getWrappedException()

### JSObject Class
The public final class netscape.javascript.JSObject extends Object.

```
java.lang.Object

	|

	+	netscape.javascript.JSObject
```



#### Description

JavaScript objects are wrapped in an instance of the class netscape.javascript.JSObject and passed to Java. JSObject allows Java to manipulate JavaScript objects.

When a JavaScript object is sent to Java, the runtime engine creates a Java wrapper of type JSObject; when a JSObject is sent from Java to JavaScript, the runtime engine unwraps it to its original JavaScript object type. The JSObject class provides a way to invoke JavaScript methods and examine JavaScript properties.

Any JavaScript data brought into Java is converted to Java data types. When the JSObject is passed back to JavaScript, the object is unwrapped and can be used by JavaScript code. See [*Data Type Conversions* ](#data-type-conversions), for more information about data type conversions.



#### Method Summary

The netscape.javascript.JSObject class has the following methods:

|**Method**|**Description**|
| :- | :- |
|call|Calls a JavaScript method.|
|equals|Determines if two JSObject objects refer to the same instance.|
|eval|Evaluates a JavaScript expression.|
|getMember|Retrieves the value of a property of a JavaScript object.|
|getSlot|Retrieves the value of an array element of a JavaScript object.|
|removeMember|Removes a property of a JavaScript object.|
|setMember|Sets the value of a property of a JavaScript object.|
|setSlot|Sets the value of an array element of a JavaScript object.|
|toString|Converts a JSObject to a string.|

**Static Method**

|getWindow|Gets a JSObject for the window containing the given applet.|
| :- | :- |



The following sections describe the declaration and usage of these methods.

#### call

Method. Calls a JavaScript method. Equivalent to

"this.methodName(args[0], args[1], ...)" in JavaScript.

**Declaration**

public Object call(String methodName, Object args[])



#### equals

Method. Determines if two JSObject objects refer to the same instance. Overrides: equals in class java.lang.Object

**Declaration**

public boolean equals(Object obj)

**Backward compatibility**

JavaScript 1.3. In JavaScript 1.3 and earlier versions, you can use either the equals method of java.lang.Object or the == operator to evaluate two JSObject objects.



#### eval

Method. Evaluates a JavaScript expression. The expression is a string of JavaScript source code that will be evaluated in the context given by "this".

**Declaration**

public Object eval(String s)

#### getMember

Method. Retrieves the value of a property of a JavaScript object. Equivalent to "this.name" in JavaScript.

**Declaration**

public Object getMember(String name)



#### getSlot

Method. Retrieves the value of an array element of a JavaScript object. Equivalent to "this[index]" in JavaScript.

**Declaration**

public Object getSlot(int index)



#### getWindow

Static method. Returns a JSObject for the window containing the given applet. This method is useful in client-side JavaScript only.

**Declaration**

public static JSObject getWindow(Applet applet)



#### removeMember

Method. Removes a property of a JavaScript object.



**Declaration**

public void removeMember(String name)



#### setMember

Method. Sets the value of a property of a JavaScript object. Equivalent to "this.name = value" in JavaScript.

**Declaration**

public void setMember(String name, Object value)



#### setSlot

Method. Sets the value of an array element of a JavaScript object. Equivalent to "this[index] = value" in JavaScript.

**Declaration**

public void setSlot(int index, Object value)



#### toString

Method. Converts a JSObject to a String. Overrides: toString in class java.lang.Object

**Declaration**

public String toString()



