# WebSocket Object

 

WebLOAD supports WebSocket, a protocol that provides full-duplex communication channels over a single TCP connection. Unlike HTTP which is a request-response protocol, WebSocket creates connections for sending or receiving messages that are not dependent on one another. In this way, WebSocket provides full-duplex communication. WebSocket also enables streams of messages on top of TCP.

 

WebLOAD’s WebSocket object enables creating and managing a WebSocket connection to a server, as well as sending and receiving data on the connection. Note that you can create multiple WebSocket objects.

## Constructor

**Description**

Creates a new WebSocket for the given URL, and returns a JavaScript object reference.

**Syntax**

`<websocket object name>` = **new WebSocket (`<\*URL\*>`)**;

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

onopen() event is fired, as described in [*onopen (evt)* ](#_bookmark576).

 

**Syntax**

`<websocket object name>`.*connect()*

**Example**

`ws1.connect()`

 

### close() (method)

**Description**

Closes the WebSocket connection.

 

**Syntax**

`<*websocket object name*>`.**close()**

**Example**

`ws1.close()`

 

### send() (method)

**Description**

Sends data to a WebSocket connection.

 

**Syntax**

`<*websocket object name*>`.**send(data[ ,encoded])**

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
## Mothod metails

### WebSocket(url, manualHandleEventsopt)

#### new WebSocket(url, manualHandleEventsopt)

Create new WebSocket object

**Parameters:**

| Name | Type | Attributes | Description |
| --- | --- | --- | --- |
| `url` | string |     | connection string |
| `manualHandleEvents` | boolean | <optional> | if true, will only handle events when manually asked for (for example, using ws.handlePending()). Default is to automatically handle events |

**Example**

```
ws1 = new WebSocket( "wss://echo.websocket.org/?encoding=text" );
ws1.onmessage = function(evt ) {
    DebugMessage("Server said:" + evt.getData());
}
ws1.connect();
Sleep(1000); //Event are handled while in Sleep
ws1.send("hi");
ws1.close();
```

### Members

#### manualHandleEvents :boolean

when true, messages are handled (callbacks called) automatically

**Type:**

*   boolean

Default Value:

*   true

#### onclose :[WebSocket#webSocketEventCallback](#webSocketEventCallback)

Callback called when WebSocket is closed

**Type:**

*   [WebSocket#webSocketEventCallback](#webSocketEventCallback)

#### onerror :[WebSocket#webSocketEventCallback](#webSocketEventCallback)

Callback called when WebSocket has error. Event getData() will hold exception information, or use evt.toString()

**Type:**

*   [WebSocket#webSocketEventCallback](#webSocketEventCallback)

#### onmessage :[WebSocket#onmessageCallback](#onmessageCallback)

Callback to be called when a new message arrives

**Type:**

*   [WebSocket#onmessageCallback](#onmessageCallback)

#### onopen :[WebSocket#webSocketEventCallback](#webSocketEventCallback)

Callback called when WebSocket is opened

**Type:**

*   [WebSocket#webSocketEventCallback](#webSocketEventCallback)

#### reportErrorFunction :function

Function used to log messages

**Type:**

*   function

Default Value:

*   ErrorMessage or WebSocket.prototype.globalReportErrorFunction

#### storeMessages :boolean

when true, messages are stored after being handled for future inspection.

**Type:**

*   boolean

Since:

*   WebLOAD 12.6

Default Value:

*   false

#### waitTime :number

Time in milliseconds before checking new messages

**Type:**

*   number

Default Value:

*   500 or WebSocket.prototype.globalWaitTime

### Methods

#### addHeader(name, value)

Add custom HTTP Header

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string |     |
| `value` | string |     |

#### close()

Close the connection

#### connect()

Connect to WebSocket

#### dynamicReplaceCorrelation(toCorrelationParam, searchValueopt)

Replace send/sendBinary data with value in correlation. Value is looked up using pollCorrelationValue, so if value does not yet exist, wait for it until timeout (30000 millis)

**Parameters:**

| Name | Type | Attributes | Description |
| --- | --- | --- | --- |
| `toCorrelationParam` | string |     | name of parameter to replace. The name is expected to be set via setCorrealtionValue("myParamName", "the value"); |
| `searchValue` | string | <optional> | the replacement value to replace. The default is ${toCorrelationParam}, for example the string "session=${sessionId}" will be replaced with "session="+pollCorrelationValue("sessionId"). |

Since:

*   WebLOAD 12.6

#### expectMessage(expr, timeoutopt, keepMessagesopt)

Wait for some message to be received.

**Parameters:**

| Name | Type | Attributes | Default | Description |
| --- | --- | --- | --- | --- |
| `expr` | string \| RegExp |     |     | can be a "string" or /regex/ to look for in previous or future messages |
| `timeout` | number | <optional> | 30000 | how much time to wait, default is 30000 milis |
| `keepMessages` | boolean | <optional> | false | if true, will not remove messages, if false (default) will remove all messages up to the looked up message. |

Since:

*   WebLOAD 12.6

#### extractMessageValue(prefix, suffix, nameopt, timeoutopt, keepMessagesopt)

Wait for some message to be received.

**Parameters:**

| Name | Type | Attributes | Default | Description |
| --- | --- | --- | --- | --- |
| `prefix` | string |     |     | prefix in message to look for |
| `suffix` | string |     |     | suffix in message to look for |
| `name` | string | <optional> |     | name of correlation value to store. If not specified, value will be returned but not stored |
| `timeout` | number | <optional> | 30000 | how much time to wait, default is 30000 milis |
| `keepMessages` | boolean | <optional> | false | if true, will not remove messages, if false (default) will remove all messages up to the looked up message. |

Since:

*   WebLOAD 12.6

**Returns:**

value extracted, null if not found after timeout

#### handleMessage()

Call to manually handle messages, not normally needed

#### send(data, encoded)

Send message

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | string | to send |
| `encoded` | boolean | if true, value is encoded and will decoded when sent |

#### sendBinary(data)

Sent as Binary Message

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | Object |     |

#### setConnectionTimeout(milis)

Connection timeout

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `milis` | number |     |

#### setIgnoreSslErrors(b)

Call with true to ignore SSL Errors

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `b` | boolean |     |

#### setPerMessageDeflate(b)

Call with true for per-message-deflate extention

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `b` | boolean |     |

#### setProxy(proxy)

Proxy host:port to use

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `proxy` | string |     |

**Example**

```
setProxy("myproxy:8080")
```

#### setTimeout(milis)

Max time to spend handling messages

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `milis` | number | time in milliseconds |

#### setVerifyHost(b)

Call with false to not verify host

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `b` | boolean |     |

### Type Definitions

#### OnMessageType

Event type for messages

**Type:**

*   Object

**Properties:**

| Name | Type | Description |
| --- | --- | --- |
| `getData` | Funtion | Return the message raw data |
| `getEncodedData` | Funtion | returns data, if binary encoded as text |
| `getTimeMillis` | Funtion | get timestamp of event |
| `isBinary` | boolean | Indicates whether message was binary or not. |

#### onmessageCallback(evt)

Event with message details

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `evt` | [WebSocket#OnMessageType](#OnMessageType) |     |

#### webSocketEventCallback(evt)

On open callback

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `evt` | Object | event data |
