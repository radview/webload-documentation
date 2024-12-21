# Using Asynchronous Requests



## Asynchronous HTTP Requests in WebLOAD

Regular HTTP requests in WebLOAD are synchronous, meaning that script execution is blocked whenever an HTTP request (such as wlHttp.Get, wlHttp.Post, etc.) is made, and continues once the request data is fully received. The response is then made available in the ‘document’ object. For example:

```javascript
wlHttp.SaveSource=true;

 [wlHttp.Get("http://make/s](http://make/sync/request)ync/request");

//execution blocked here until the full request is retrieved InfoMessage(document.wlSource);
```

However in asynchronous requests, execution is not blocked, rather it immediately

continues. Asynchronous requests are executed by calling the ‘wlHttp.Async’ property.

### Using wlHttp.Async to Execute Requests Asynchronously
‘wlHttp.Async’ makes HTTP requests asynchronous. When using asynchronous requests, the script does not wait for the request to complete before moving on to the next statement. In order to work with the response, you can use the asynchronous callback functions:

- [*onDocumentComplete ](../javascript/actions_objects_functions.md#ondocumentcomplete-property)*–* Defines a callback function to be called after the asynchronous request has been completed. For example, it validates the response and makes a further request.
- [*onDataReceived ](../javascript/actions_objects_functions.md#ondatareceived-property)*–* Defines a callback function to be called every time more data is received for the request. This is useful for working with asynchronous requests that need to be inspected before they are completed, for example in an HTTP streaming push scenario.

#### Using onDocumentComplete in Asynchronous Execution

In the regular HTTP request example shown above, the document cannot be accessed after the request is made because it is not yet available. In order to access the response




document, you need to register a function that will be called when the response is available, using the ‘onDocumentComplete’ property. For example:

```javascript
wlHttp.Async = true;

wlHttp.onDocumentComplete = function(document)

{ 
    InfoMessage("full response:" + document.wlSource);

}

[wlHttp.Get("http://make/async/request");](http://make/async/request)

//document.wlSource is not available here. Sleep(1000);
```



#### Using onDataReceived in Asynchronous Execution

To inspect the partial response as it is being received, use the ‘onDataReceived’ property. For example:

```javascript
wlHttp.Async = true;

wlHttp.onDataReceived = function(document)

{ 

InfoMessage("response so far:" + document.wlSource);

}

[wlHttp.Get("http://make/async/request");
```



## Push Protocols

The HTTP protocol is a request/response protocol, meaning that the server can respond to client requests, but cannot initiate unsolicited responses. Yet there are scenarios

when the server is required to ‘push’ data to the client, for example, chat applications, user notifications, etc.

There are several techniques that can be used to achieve server push:

- **Polling**: the client (browser) sends a request to the server at regular intervals. For more information refer to [*Using Polling Protocol in WebLOAD* ](#using-polling-protocol-in-webload).
- **Long polling**: the client request is kept on hold until the server can deliver a valid response. When data from the server needs to be pushed, the server responds and closes the connection. The client is then expected to start a new connection and

  wait for the server’s next message (response).

  For more information refer to [*Using Long Polling in WebLOAD* ](#using-long-polling-in-webload).

- **Streaming**: the client make a request. The server builds the response progressively as more data is available (for example, using ‘chunked data’). The client reads and handles this data but keeps the connection open, waiting for more data to arrive. For more information refer to [*Using HTTP Streaming in WebLOAD* ](#using-http-streaming-in-webload).




### Using Polling Protocol in WebLOAD
Polling requests are regular, short requests, so there is no need for asynchronous code to implement them. Because the message sequence in playback can be different from the recorded one, it is useful to convert the polling requests to a loop.

For example, if the recorded agenda was:

```javascript
wlHttp.Get("http://get](http://get-update/)-update");

Sleep(2000); 

[wlHttp.Get("http://get](http://get-update/)-update"); 

Sleep(2000); [wlHttp.Get("http://get](http://get-update/)-update"); 

Sleep(2000);
```

...

It can be converted to the following loop:

```javascript
keepUpdating=true; 
while(keepUpdating) {

[wlHttp.Get("http://get](http://get-update/)-update");

if (document.wlSource=="LAST\_MESSAGE") { keepUpdating=false;

}

Sleep(2000);

}
```



### Using Long Polling in WebLOAD
Long polling is similar to polling, but the requests are blocked for longer.

Long polling can be implemented like polling above, but because it blocks script execution, other tasks cannot be performed, such as polling on two different URLs or running the polling in the background while performing other HTTP requests.

To run long polling alongside other tasks, asynchronous requests must be used. For example:

```javascript
function getUpdates() { wlHttp.Async=true;

wlHttp.onDocumentComplete=function(document){ if (document.wlSource=="LAST\_MESSAGE") {

return;

} else { //keep polling recursively: setTimeout(getUpdates,0);

}



}

[wlHttp.Get("http://get](http://get-update/)-update");

}

getUpdates();

//execution continues here... [wlHttp.Get("http://other](http://other-thing/)-thing");
```


### Using HTTP Streaming in WebLOAD
In HTTP streaming, the server response is never ending (or very long), and each new response data is considered a new ‘message’ (or it can be delimited with some delimiter).

To handle the server partial responses, the ‘[*onDataReceived*’ ](../javascript/actions_objects_functions.md#ondatareceived-property)callback function should be used.

For example:

```javascript
var prevIdx	= 0; //data seen so far wlHttp.onDataReceived= function(document) {

var currIdx = document.wlSource.length; if (currIdx <= prevIdx ) { //no new data

return;

}

var msg = document.wlSource.substr(prevIdx, currIdx); prevIdx = currIdx;

InfoMessage(msg );

}
```


## Using setTimeout for Delayed Function Execution

The setTimeout() function is used to execute a callback function after a specified number of milliseconds, in a non-blocking manner. That is, script execution continues immediately, not waiting for the specified time or the function to execute.

The following example shows how setTimeout () is used when executing synchronous requests. In the example, a function is starting a long request that is waiting for a message to be sent two seconds after the request started. :

```javascript
function sendMessage(){

[wlHttp.Post(“http://send](http://send-some-message/)-some-message”);

}

setTimeout(sendMessage, 2000);	//2 - after 2 seconds, send.



[wlHttp.Get(“http://long](http://long-request/)-request”); //1 - start the long request
```

Callback functions are expected to run in a timely manner, because a callback blocks the execution of other callback functions. Therefore Sleep() should not be used inside a callback function (for example, the functions used in onDocumentComplete, onDataReceived and setTimeout itself). Instead, use setTimeout() inside a callback function. For example:

```javascript
wlHttp.Async=true; wlHttp.onDocumentComplete=function(document){

InfoMessage(“got response, now send a reply after

3 seconds…”);

setTimeout(function(){ wlHttp.Async=true;

[wlHttp.Get(“http://send](http://send-reply-message/)-reply-[message”);](http://send-reply-message/)

}, 3000);

}

[wlHttp.Get(“http://send](http://send-first-message/)-first-[message”);](http://send-first-message/)


```


