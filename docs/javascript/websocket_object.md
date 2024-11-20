# WebSocket Object

 

WebLOAD supports WebSocket, a protocol that provides full-duplex communication channels over a single TCP connection. Unlike HTTP which is a request-response protocol, WebSocket creates connections for sending or receiving messages that are not dependent on one another. In this way, WebSocket provides full-duplex communication. WebSocket also enables streams of messages on top of TCP.

 

WebLOAD’s WebSocket object enables creating and managing a WebSocket connection to a server, as well as sending and receiving data on the connection. Note that you can create multiple WebSocket objects.

 

 

## Constructor

 

**Description**

Creates a new WebSocket for the given URL, and returns a JavaScript object reference.

 

**Syntax**

`<websocket object name>` = **new WebSocket (<\*URL\*>)**;

**Parameters**

| **Parameter Name** | **Description**              |
| ------------------ | ---------------------------- |
| URL                | The URL to which to connect. |

**Example**

`ws1 = new WebSocket("ws://echo.websocket.org");`



## Methods



### connect() (method)

 

**Description**

Creates a WebSocket connection to the given URL address. When connected, an

onopen() event is fired, as described in [*onopen (evt)* ](#_bookmark576)(on page [447](#_bookmark576)).

 

**Syntax**

`<websocket object name>`.*connect()*

**Example**

`ws1.connect()`

 

### close() (method)

**Description**

Closes the WebSocket connection.

 

**Syntax**

<*websocket object name*>.**close()**

**Example**

`ws1.close()`

 

### send() (method)

**Description**

Sends data to a WebSocket connection.

 

**Syntax**

<*websocket object name*>.**send(data[ ,encoded])**

**Parameters**

 

| **Parameter Name** | **Description**                                              |
| ------------------ | ------------------------------------------------------------ |
| data               | The data to be sent, enclosed in quote marks.                |
| [encoded]          | An optional Boolean value (true or false). <br> True indicates that the  data contains an ASCII encoded string  in the format %xx, where xx is the hexadecimal ASCII code. <br> False indicates the data  does not contain an ASCII encoded string. This is the default value. |

 

**Examples**

`ws1.send(“hi”)`

`ws1.send(“next line %0A here”, true)`

 

## Events

 

A WebSocket emits events. An Event handler should be registered in order to react to events.

 

### onmessage (evt)

An event that occurs when a new message is received.

 

- evt.getData() – Gets the data. This can be a string or binary data.

- evt.isBinary() – Indicates whether the data is binary or not.

- evt.getEncodedData() – Gets the data in encoded format. This is useful for binary messages.


 

**Example**

```javascript
ws1.onmessage = function(evt) {

InfoMessage(“got message “ + evt.getData() )

if (evt.isBinary() ) {

InfoMessage(“Message is binary”);

}

}
```

 

### onerror (evt)

An event that occurs when an error message is received. The default behavior is to show a warning message with the error details.

 

`Evt.getData()` – gets the underlying exception details.

 

### onopen (evt)

An event that occurs when the socket is opened (connected).

 

**Example**

```javascript
ws1.onopen = function(evt) 

{ 

DebugMessage("WebSocket is opened, say hello"); 

ws1.send(“hello”);

}
```



## WebSocket Sample Code

 

```javascript
// Create a WebSocket object

ws1 = new WebSocket( "ws://echo.websocket.org" );

// Define an event handler, to handle events (incoming messages) when they occur

ws1.onmessage = function(evt) {

// Display in the Log the text that was sent in the message body DebugMessage("Server said:" + evt.getData());

}

// Create a websocket connection ws1.connect();

//Note that events are handled while in Sleep Sleep(1000);

// Send a message with the text “hi”

ws1.send("hi");

Sleep(1000);

// Close the websocket connection ws1.close();

Sleep(1000);
```
