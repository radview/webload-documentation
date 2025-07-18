# WebSocket Object

WebLOAD supports WebSocket, a protocol that provides full-duplex communication channels over a single TCP connection. Unlike HTTP which is a request-response protocol, WebSocket creates connections for sending or receiving messages that are not dependent on one another. In this way, WebSocket provides full-duplex communication. WebSocket also enables streams of messages on top of TCP.

WebLOAD’s WebSocket object enables creating and managing a WebSocket connection to a server, as well as sending and receiving data on the connection. Note that you can create multiple WebSocket objects.

## WebSocket Sample Code using messages handler

With message handler, you write a function that handles that message as they are received, in the `onmessage()` function.

This mode is useful in general purpose WebSocket, where it is not know when and what messages are expected to be received.

```javascript
// Create a WebSocket object
ws1 = new WebSocket( "ws://echo.websocket.org" );

// Define an event handler, to handle events (incoming messages) when they occur
ws1.onmessage = function(evt) {
  // Display in the Log the text that was sent in the message body 
  DebugMessage("Server said:" + evt.getData());
}

// Create a websocket connection 
ws1.connect();

//Note that events are handled while in Sleep 
Sleep(1000);

// Send a message with the text “hi”
ws1.send("hi");

Sleep(1000);

// Close the websocket connection 
ws1.close();

Sleep(1000);
```

## WebSocket Stored Messages Sample Code

Stored messages mode is a mode that allows handling messages closer to where they are actually needed.

This mode is useful when the protocol behaeves in some expected way, for example, after sending a "connect" message it will repond with a "connected" reply you can expect.

This mode makes it easier to correlate values - from WebSocket reply to another WebSocket or HTTP Request, and from HTTP Response to a WebSocket message.

Since: WebLOAD 12.6

```javascript
// Create a WebSocket object
ws1 = new WebSocket( "ws://echo.websocket.org" );
ws1.storeMessages=true; //messages will be kept in ws1.messages array.
ws1.connect()

//Received  string ws1
//"WebSocket Connected!"

//wait here for a message with this string in it
ws1.expectMessage("Connected!");        

//Received  string ws1
//"connection details: sessionid='5333455693' "

//extract or wait for a message with prefix, suffix
ws1.extractMessageValue("sessionid='", "'", "mySessionId");  

//can use the value in HTTP/WebSocket request:
wlHttp.Get("http://someurl?" + getCorrelationValue("mySessionId"))

//replace the value ${mySessionId} with the correlation "mySessionId"
ws1.dynamicReplaceCorrelation("mySessionId");

//this send will replace ${mySessionId} with session id value if it existed
ws1.send("sessionid=${mySessionId}");                         
 
// Close the websocket connection 
ws1.close();

```

## Object details

### WebSocket(url, manualHandleEventsopt)

#### new WebSocket(url, manualHandleEventsopt)

Create new WebSocket object

**Parameters:**

| Name | Type | Attributes | Description |
| --- | --- | --- | --- |
| `url` | string |     | connection string |
| `manualHandleEvents` | boolean | <optional> | if true, will only handle events when manually asked for (for example, using `ws.handlePending()`). Default is to automatically handle events |

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

### Events

#### onclose

Callback called when WebSocket is closed

**Type:**

*   close-event

#### onerror

Callback called when WebSocket has error. Event `getData()` will hold exception information, or use `evt.toString()`

**Type:**

*   error-event

#### onmessage

Callback to be called when a new message arrives

**Type:**

*   Event type for messages

**Properties:**

| Name | Type | Description |
| --- | --- | --- |
| `getData` | Funtion | Return the message raw data |
| `getEncodedData` | Funtion | returns data, if binary encoded as text |
| `getTimeMillis` | Funtion | get timestamp of event |
| `isBinary` | boolean | Indicates whether message was binary or not. |


#### onopen 

Callback called when WebSocket is opened

**Type:**

*   open-event


### Members

#### manualHandleEvents :boolean

when true, messages are handled (callbacks called) automatically

**Type:**

*   boolean

Default Value:

*   true


#### reportErrorFunction :function

Function used to log messages

**Type:**

*   function

Default Value:

*   ErrorMessage or `WebSocket.prototype.globalReportErrorFunction`

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

*   500 or `WebSocket.prototype.globalWaitTime`

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

Replace send/sendBinary data with value in correlation. Value is looked up using `pollCorrelationValue`, so if value does not yet exist, wait for it until timeout (30000 millis)

**Parameters:**

| Name | Type | Attributes | Description |
| --- | --- | --- | --- |
| `toCorrelationParam` | string |     | name of parameter to replace. The name is expected to be set via setCorrealtionValue("myParamName", "the value"); |
| `searchValue` | string | <optional> | the replacement value to replace. The default is `${toCorrelationParam}`, for example the string `"session=${sessionId}"` will be replaced with `"session="+pollCorrelationValue("sessionId")`. |

Since:

*   WebLOAD 12.6

#### expectMessage(expr, timeoutopt, keepMessagesopt)

Wait for some message to be received.

**Parameters:**

| Name | Type | Attributes | Default | Description |
| --- | --- | --- | --- | --- |
| `expr` | string \| RegExp |     |     | can be a `"string"` or `/regex/` to look for in previous or future messages |
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

