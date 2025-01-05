# Appendix A: Scripting Samples

This chapter provides sample scripts which you can adapt to your own scripts. Each scripting sample demonstrates different features that can be performed by editing your script’s script.

The following scripting samples are provided:

- Basic Recording

- Correlation

- Parameterizing a script

- Using AJAX and Web services

- Using AJAX and JSON

  

## Scripting Sample of a Basic Recording

The sample script in this section demonstrates how a basic script is recorded. This script is used as a basis for the scripts that appear in the following sections.

### What the Script Does

- Records user actions in the website. This is done by recording the HTTP traffic between the browser and the Web server.
- Records Html form data sent from the browser.
- Records the Get() and Post() methods.

### How to Create the Script

The basic script is created by starting to record in the WebLOAD Recorder, browsing through the [www.webloadmpstore.com ](http://www.webloadmpstore.com/)website, stopping the recording, and saving the script.



#### Step 1 – Starting to Record the script

1. In WebLOAD Recorder open a new script.
1. ![](../images/script_guide_119.png)Click	to start recording.
1. Browse to [www.webloadmpstore.com ](http://www.webloadmpstore.com/)in the browser that opens. The following script describing your action appears in the script.

```
wlGlobals.GetFrames = false

wlGlobals.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"

wlHttp.Header["DNT"] = "1" wlHttp[.Get("http://www.webloadmpstore.com/")](http://www.webloadmpstore.com/) Sleep(9094)
```



#### Step 2 – Logging in to the Site

1. Click **Login** in the webloadmpstore website and the Login page appears. The script for this action is as follows:

   `wlHttp.Header["Referer"] = ["http://www.webloadmpstore.com/"](http://www.webloadmpstore.com/)` 

   `wlHttp.Get(["http://www.webloadmpstore.com/login.php"](http://www.webloadmpstore.com/login.php))`

   `Sleep(7704)`

1. In the username and password fields, enter demo-username and demo- password to log in to the website.

WebLOAD Recorder records the login action and simulates a script containing the username and password that you entered in the login page.

`wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/login.php>"`

`wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["login"] = "demo" wlHttp.FormData["password"] = "demo"`

`wlHttp.FormData["sessionID"] = "webloadmpstore.62.90.23.122.ae97bc7877d7bd4ebcb64c4c0e21ba1c"`

`wlHttp.FormData["event"] = "login" wlHttp.FormData["Submit"] = "Login" wlHttp.Post("<http://www.webloadmpstore.com/login.php>")`

`Sleep(3015)`

The site approves your login information and the WebLOAD MP Store home page appears.

`wlHttp.Get`(["http://www.webloadmpstore.com/index.php"](http://www.webloadmpstore.com/index.php)) Sleep(5282)



#### Step 3 – Purchasing a Product

1. From the product page, click **Debugging and Handling Dynamic Data** to view the product’s additional details. A page with the product description for Debugging and Handling Dynamic Data appears.

   `wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/index.php>"`

   `wlHttp.FormData["id"] = "1" wlHttp.Get("<http://www.webloadmpstore.com/product.php>")`

   `Sleep(4984)`

2. Click **Add to Cart** to purchase the product.

   `wlHttp.Header["Referer"] = ["ht](http://www.webloadmpstore.com/product.php?id=1)[tp://www.webloadmpstore.com/product.php?id=1"](http://www.webloadmpstore.com/product.php?id=1)`

   `wlHttp.FormData["event"] = "addproduct"` 

   `wlHttp.FormData["id"] = "1"` 

   `wlHttp.Get(["http://www.webloadmpstore.com/cart.php"](http://www.webloadmpstore.com/cart.php))`



#### Step 4 – Saving the script

1. In WebLOAD Recorder, click to stop recording the script.
1. Select **File > Save As** to save the script. The Save As dialog box appears.
1. In the Save As dialog box browse to the following location: D:\\Radview\\<Sample scripts folder>\\ script 1-Basic Recording script.wlp
1. Click **Save**.

### The Full script: script 1-Basic Recording script

> **Note:** The WLIDE – URL comments throughout the script are modified to give the Agenda nodes meaningful names.

```javascript
/\*\*\*\*\* WLIDE - URL : Open webloadmpstore home page - ID:2 \*\*\*\*\*/ wlGlobals.GetFrames = false wlHttp.Get("<http://www.webloadmpstore.com/>")

// END WLIDE



/\*\*\*\*\* WLIDE - Sleep - ID:3 \*\*\*\*\*/ Sleep(9094)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Open login page - ID:4 \*\*\*\*\*/ wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/>" wlHttp.Get("<http://www.webloadmpstore.com/login.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:5 \*\*\*\*\*/ Sleep(7704)

// END WLIDE

/\*\*\*\*\* WLIDE - URL :Insert login and password - ID:6 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/login.php>"

wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["login"] = "demo" wlHttp.FormData["password"] = "demo"

wlHttp.FormData["sessionID"] = "webloadmpstore.62.90.23.122.ae97bc7877d7bd4ebcb64c4c0e21ba1c"

wlHttp.FormData["event"] = "login" wlHttp.FormData["Submit"] = "Login" wlHttp.Post("<http://www.webloadmpstore.com/login.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:7 \*\*\*\*\*/ Sleep(3015)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : [http://www.webloadmpstore.com/index.php ](http://www.webloadmpstore.com/index.php)- ID:8 \*\*\*\*\*/

wlHttp.Get("<http://www.webloadmpstore.com/index.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:9 \*\*\*\*\*/ Sleep(5282)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Select show product details - ID:10 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/index.php>"



wlHttp.FormData["id"] = "1" wlHttp.Get("<http://www.webloadmpstore.com/product.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:11 \*\*\*\*\*/ Sleep(4984)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Add to cart - ID:12 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/product.php?id=1>"

wlHttp.FormData["event"] = "addproduct" wlHttp.FormData["id"] = "1" wlHttp.Get("<http://www.webloadmpstore.com/cart.php>")

// END WLIDE
```


## Scripting Sample Using AJAX and Web Services

WebLOAD supports automatic recording of AJAX calls into the test script, enabling debugging and full access to all request data (headers and body), both in the script and during runtime. WebLOAD supports various formats for the AJAX payload: XML, JSON, other text-based formats, and binary data.

Besides demonstrating the use of AJAX calls, this script demonstrates the use of functions and external files in the script.

Storing sections of the logic in a function enables you to reuse the same lines of code without duplications, making the script more modular. A function can be part of your main script file or can be stored in a separate, external JavaScript file. When storing the function in a separate file, the main script file includes the function so that it can be used within the script.

One of the main benefits of including files in the script, is to reduce the maintenance needed for the scripts. The same included file can be used in a number of scripts simply by adding the include command and calling the function in the script.

Using included files is also more efficient. When the information in the included file needs to be updated, the included file is the only place that needs to be modified and the whole script will be affected. Without using an included file, you would need to search for every place that the information is used and update the information manually.



### What the Script Does

- Demonstrates how to record user actions in a website that is accessed on a secure server.
- Demonstrates how WebLOAD supports AJAX and Web services.
- Demonstrate how to validate a Web Service reply by parsing the XML content of its SOAP message.
- Demonstrates how to modify a recorded script where a specific option is selected, so that the script can accept additional options during runtime.
- Demonstrates adding a function to the script.
- Demonstrates how to extract a login script to an external JavaScript file and then reuse the code in the script.

### How to Create the Script

In this script, you will record a webpage that is accessed on a secure server. Once the script is recorded, you will modify the script so that during runtime, an InfoMessage notifies you whether your credit card information has been validated. This is done by adding a function that uses a Web Service to check the validation of the credit card and a parameter to store the result of the function.

You will create a function to store the script of the login process. Then, you can extract the function to an external file, which enables you to create a generic scenario, instead of a specific case. The function checks the login information received from the site and determines whether the user’s login information is accurate. Although the login information was correct when the script was recorded, by modifying the script you can add additional scenarios to be accepted during runtime, such as, when the login information is incorrect.

This script also demonstrates WebLOAD’s support of AJAX and Web services. During the recording, when the credit card information is being validated, the WebLOAD Recorder records the Web service transactions that take place within the application.

#### Step 1 – Entering Credit Card Information and Checking Out

1. Open the script3-Parametrizing a script.

1. Open a browser, navigate to the Cart page, and copy the URL of the page.

1. In the WebLOAD Recorder, click ![](../images/script_guide_121.png) or select **Record > Start Record** to start recording.

1. Paste the URL of the cart page in the browser that opens. The new script is appended to the end of the existing script.

1. In the cart page, click **Checkout**.

1. The credit card information page appears. This page is an HTTPS page and is appended to the script as follows:

   `wlGlobals.GetFrames = false` 

   `wlHttp.Header["Referer"] ="[http://www.webloadmpstore.com/cart.php?event=update&id=](http://www.webloadmpstore.com/cart.php?event=update&id) 2&quantity=3"`

   `wlHttp.Get(["https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"`

   `)`

1. In the credit card information page, enter your credit card information and click **Done**. The script is recorded as follows:

   ```
   wlGlobals.GetFrames = false
   
   wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"
   
   wlHttp.FormData["wsdl"] = "$WL$VOID$STRING$"
   
   wlHttp.Get("[https://www.webloadmpstore.com/soap/server.p](http://www.webloadmpstore.com/soap/server.p) hp")
   
   wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"
   
   wlHttp.Data["Type"] = "text/xml; charset=utf-8"
   
   wlHttp.Data["Value"] = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=[\"http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema-instance\)-[instance\](http://www.w3.org/2001/XMLSchema-instance\)" xmlns:xsd=\["http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema\)\" xmlns:soap=\["http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/\)\"
   
   \><soap:Body><checkValidity xmlns=[\"http://example.org/CreditCardProcess](http://example.org/CreditCardProcess\)\"><strCardN umber>ABCD</strCardNumber><strHolderID>AB1234</strHolder ID></checkValidity></soap:Body></soap:Envelope>"
   
   wlHttp.Post("[https://www.webloadmpstore.com/soap/server.](http://www.webloadmpstore.com/soap/server) php")
   
   wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["name"] = "Radview" wlHttp.FormData["address"] = "Hamelacha 14" wlHttp.FormData["shippingAddress"] = "Park Afek" wlHttp.FormData["cardNumber"] = "ABCD" wlHttp.FormData["idNumber"] = "AB1234" wlHttp.FormData["event"] = "process"
   
   wlHttp.Post("[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php) ")
   
   
   ```

   

1. In WebLOAD Recorder, click	to stop recording the script.

#### Step 2 – Adding the Results Parameter and ResultParser Function

1. Add a results parameter to the Validate Cred – Pass Node of the script.

   The results parameter stores a value received from the resultParser function, which checks whether your credit card information is valid. The HTTP response containing the result of the credit card validation Web Service (document.wlXmls[0]) that is extracted from the script, is sent to the resultParser function.

   The results parameter appears in the Validate Cred – Pass Node of the script as follows:

   ```xml
   wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"
   
   wlHttp.Data["Type"] = "text/xml; charset=utf-8"
   
   wlHttp.Data["Value"] = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=[\"http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema-instance\)-[instance\](http://www.w3.org/2001/XMLSchema-instance\)" xmlns:xsd=\["http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema\)\" xmlns:soap=\["http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/\)\"
   
   \><soap:Body><checkValidity xmlns=[\"http://example.org/CreditCardProcess](http://example.org/CreditCardProcess\)\"><strCardN umber>ABCD</strCardNumber><strHolderID>AB1234</strHolder ID></checkValidity></soap:Body></soap:Envelope>"
   
   wlHttp.Post("[https://www.webloadmpstore.com/soap/server.](http://www.webloadmpstore.com/soap/server) php")
   
   results = resultParser( document.wlXmls[0] )	
   
   
   ```

   

2. Create an infoMessage to notify you whether your credit card has been validated or not according to the result parameter value.

   ```javascript
   wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"
   
   wlHttp.Data["Type"] = "text/xml; charset=utf-8"
   
   wlHttp.Data["Value"] = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=[\"http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema-instance\)-[instance\](http://www.w3.org/2001/XMLSchema-instance\)" xmlns:xsd=\["http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema\)\" xmlns:soap=\["http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/\)\"
   
   \><soap:Body><checkValidity xmlns=[\"http://example.org/CreditCardProcess](http://example.org/CreditCardProcess\)\"><strCardN umber>ABCD</strCardNumber><strHolderID>AB1234</strHolder ID></checkValidity></soap:Body></soap:Envelope>"
   
   
   
   
   
   wlHttp.Post("htt[ps://www.webloadmpstore.com/soap/server.](http://www.webloadmpstore.com/soap/server) php")
   
   results = resultParser( document.wlXmls[0] ) if (results == "1")
   
   InfoMessage("Validation check return ‘Check OK’ like it should")
   
   else
   
   InfoMessage("Validation check is not working correctly")
   ```

   

3. Add the resultParser function to the script, which checks whether your credit card information is valid. The function retrieves the information from document.wlXmls[0] in the results parameter and uses the built-in WebLOAD XML DOM to parse and return XML data to the parameter.

   ```javascript
   function resultParser (doc)
   
   {
   
   //get ‘Result’ tags, we expect exactly one result:
   
   ResultsElements = doc.getElementsByTagName("Result")
   
   if ( ResultsElements.length != 1 )
   
   // Verify only one element with that name exists
   
   throw "Expecting a single Result tag. received " + ResultsElements.length + "elements"
   
   ResultElm = ResultsElements.item(0)
   
   if ( ResultElm.childNodes.length == 0 ) return null
   
   else
   
   {
   
   
   }
   
   }
   
   
   
   Result = ResultElm.firstChild 
   
   return Result.nodeValue
   
   }
   
   }
   ```

   



#### Step 3 – Creating the External Login JavaScript File

1. Select the section of the script that is responsible for the login process.

1. Copy the script to a separate JavaScript file and save the file as login\_js.js. The script in the login\_js.js file is as follows:

   ```javascript
   function Login() {
   
   strGlobalInputFileLine = GetLine(InFile1,",") user\_name = strGlobalInputFileLine[1] password = strGlobalInputFileLine[2]
   
   wlGlobals.GetFrames = false wlHttp.Get(["http://www.webloadmpstore.com/"](http://www.webloadmpstore.com/))
   
   Sleep(9094)
   
   wlHttp.Header["Referer"] = ["http://www.webloadmpstore.com/"](http://www.webloadmpstore.com/)
   
   wlHttp.Get(["http://www.webloadmpstore.com/login.php"](http://www.webloadmpstore.com/login.php)) Sleep(7704)
   
   session\_id = document.forms[1].elements[2].value
   
   wlHttp.Header["Referer"] = ["http://www.webloadmpstore.com/login.php"](http://www.webloadmpstore.com/login.php)
   
   wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["login"] = user\_name wlHttp.FormData["password"] = password wlHttp.FormData["sessionID"] = session\_id wlHttp.FormData["event"] = "login" wlHttp.FormData["Submit"] = "Login" wlHttp.Post(["http://www.webloadmpstore.com/login.php"](http://www.webloadmpstore.com/login.php))
   
   }
   ```

   





#### Step 4 – Including and Using the External File in the script

1. Include the external JavaScript file in the script by copying the following into the InitAgenda() function of the script:

   `IncludeFile("login\_js.js")`

2. Drag the JavaScript object Building Block into the script.

3. Add the rs parameter that calls the login function from the included

   `login\_js.js file.`

   `rs = Login()`

4. Save the script as script 4–Ajax and Web services.



### The Full script: script 4-AJAX and Web Services

```javascript
function InitAgenda()

{

InFile1 = CopyFile("P:\\Supporting Tools\\Sample Scripts\\New\\InFile1.txt")

Open(InFile1) IncludeFile("login\_js.js")

}

/\*\*\*\*\* WLIDE -function resultParser - ID:33 \*\*\*\*\*/ function resultParser (doc)

{

//get ‘Result’ tags, we expect exactly one result: ResultsElements = doc.getElementsByTagName("Result")

if ( ResultsElements.length != 1 )

// Verify only one element with that name exist

throw "Expecting a single Result tag. received " + ResultsElements.length + "elements"

ResultElm = ResultsElements.item(0)

if ( ResultElm.childNodes.length == 0 ) return null

else

{


}

}



Result = ResultElm.firstChild return Result.nodeValue

// END WLIDE

/\*\*\*\*\* WLIDE - Login Function - ID:19 \*\*\*\*\*/ rs = Login()

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:7 \*\*\*\*\*/ Sleep(3015)

// END WLIDE



/\*\*\*\*\* WLIDE - URL : [http://www.webloadmpstore.com/index.php ](http://www.webloadmpstore.com/index.php)- ID:8 \*\*\*\*\*/

wlHttp.[Get("http://www.webloadmpstore.com/index.php")](http://www.webloadmpstore.com/index.php)

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:9 \*\*\*\*\*/ Sleep(5282)

// END WLIDE

/\*\*\*\*\* WLIDE - Parameterizing product ID and category number	-

ID:28 \*\*\*\*\*/

product\_id = wlRand.Range(1,9) quantity = wlRand.Range(1,12)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Select show product details - ID:10 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/index.php>"

wlHttp.FormData["id"] = product\_id wlHttp.Get("<http://www.webloadmpstore.com/product.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:11 \*\*\*\*\*/ Sleep(4984)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Add to cart - ID:12 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/product.php?id=product_id>"

wlHttp.FormData["event"] = "addproduct" wlHttp.FormData["id"] = product\_id wlHttp.Get("<http://www.webloadmpstore.com/cart.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Product quantity - ID:17 \*\*\*\*\*/ wlGlobals.GetFrames = false

wlHttp.FormData["event"] = "update" wlHttp.FormData["id"] = product\_id wlHttp.FormData["quantity"] = quantity wlHttp.Get("<http://www.webloadmpstore.com/cart.php>")

// END WLIDE



/\*\*\*\*\* WLIDE - URL : HTTPS - ID:22 \*\*\*\*\*/ wlGlobals.GetFrames = false wlHttp.Header["Referer"] =

"[http:](http://www.webloadmpstore.com/cart.php?event=update&id=2&quanti)[//www.webloadmpstore.com/cart.php?event=update&id=2&quanti](http://www.webloadmpstore.com/cart.php?event=update&id=2&quanti) ty=3"

wlHttp.Get("[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)")

// END WLIDE

/\*\*\*\*\* WLIDE - URL : [https://www.webloadmpstore.com/soap/server.php?wsdl ](http://www.webloadmpstore.com/soap/server.php?wsdl)- ID:23

\*\*\*\*\*/

wlGlobals.GetFrames = false

wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"

wlHttp.FormData["wsdl"] = "$WL$VOID$STRING$" wlHttp.Get("[https://www.webloadmpstore.com/soap/server.php](http://www.webloadmpstore.com/soap/server.php)")

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Validate Cred - Pass - ID:26 \*\*\*\*\*/

wlHttp.Header["Referer"] = "[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)"

wlHttp.Data["Type"] = "text/xml; charset=utf-8"

wlHttp.Data["Value"] = "<?xml version=\"1.0\" encoding=\"utf- 8\"?><soap:Envelope xmlns:xsi=[\"http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema-instance\)-[instance\](http://www.w3.org/2001/XMLSchema-instance\)" xmlns:xsd=\["http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema\)\"

xmlns:soap=\["http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/\)\"><soap:B ody><checkValidity xmlns=\["http://example.org/CreditCardProcess](http://example.org/CreditCardProcess\)\"><strCardNumber>AB CD</strCardNumber><strHolderID>AB1234</strHolderID></checkValidi ty></soap:Body></soap:Envelope>"

wlHttp.Post("[https://www.webloadmpstore.com/soap/server.php](http://www.webloadmpstore.com/soap/server.php)")

results = resultParser( document.wlXmls[0] ) if (results == "1")

InfoMessage("Validation check return ‘Check OK’ like it should")

else

InfoMessage("Validation check is not working correctly")

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Confirm Order - ID:27 \*\*\*\*\*/ wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["name"] = "Radview"



wlHttp.FormData["address"] = "Hamelacha 14" wlHttp.FormData["shippingAddress"] = "Park Afek" wlHttp.FormData["cardNumber"] = "ABCD" wlHttp.FormData["idNumber"] = "AB1234" wlHttp.FormData["event"] = "process" wlHttp.Post("[https://www.webloadmpstore.com/checkout.php](http://www.webloadmpstore.com/checkout.php)")

// END WLIDE


```


## Scripting Sample Using AJAX and JSON to Validate a Web Server Response
WebLOAD supports automatic recording of AJAX calls into the test script using JSON, enabling debugging and full access to all request data (headers and body), both in the script and during runtime.

### What the Script Does

- Demonstrates how WebLOAD supports AJAX and JSON.
- Demonstrates how to validate a Web service response.

### How the Script Works

In this script, you will search for a product in the webloadmpstore site and in the

search results page, you will request to see the site’s statistics. The statistics displayed include the number of users online and the date and time. These statistics are updated every ten seconds to ensure their accuracy by using an asynchronous AJAX call. Each time the information is updated, the AJAX script is recorded in the script by WebLOAD Recorder.

The following steps demonstrate how to modify the AJAX script so that the WebLOAD Recorder displays the JSON information in the log view during runtime. This is done by adding an InfoMessage to the script, which displays the information based on the JSON response.

#### Step 1 – Recording AJAX Calls in the script

1. Start recording a new script and browse to [www.webloadmpstore.com.](http://www.webloadmpstore.com/) The script is recorded as follows: 

   `wlGlobals.GetFrames = false `

   `wlHttp.Get("<http://www.webloadmpstore.com/index.php>")`

2. In the webloadmpstore website, enter WebLOAD in the Search field and click **SEARCH**. 

   The search results for WebLOAD appear. In the IDE the following script is recorded: 

   `wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/index.php>"`

   `wlHttp.ContentType = "application/x-www-form-urlencoded"` 

   `wlHttp.FormData["event"] = "search"` 

   `wlHttp.FormData["searchTerm"] = "webload"` 

   `wlHttp.Post("<http://www.webloadmpstore.com/search.php>")`

   

3. Check the **Show statistics** checkbox. The script in the script appears as follows:

   `wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"`

   `wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecou> nter.php")`

   New nodes are recorded repeatedly and added to the script as the site automatically refreshes itself every ten seconds.

4. After a few nodes have been added to the script, click in WebLOAD Recorder to stop recording the script.

   

#### Step 2 – Parsing the JSON Response

1. In the InitAgenda() function in the script, define the global variable values of the SaveSource property as follows:

   ```javascript
   function InitAgenda()
   
   {
   
   wlGlobals.SaveSource = true
   
   }
   ```

   This instructs WebLOAD to store the complete HTML source code downloaded in the document.wlSource object.

   

2. Drag the JavaScript object Building Block from the Toolbox to the Script Tree. In the Building Block, add a function that receives the document.wlSource object and manipulates it to retrieve the statistics. The script is as follows:

   ```javascript
   function evalResponse (source) 
   
   {
   
   json\_response = eval("(" + source + ")")
   
   }
   
   
   ```

   

3. Create an InfoMessage to notify you of the statistic values during runtime. The edited script is as follows:

   ```javascript
   function evalResponse (source) 
   
   { json\_response = eval("(" + source + ")")
   
   InfoMessage ( "The number of online users is: " + json\_response.usersOnline + " and The current time is: "
   
   \+ json\_response.time)
   
   }
   ```

   

4. In each of the AJAX calls recorded in the script, add a call to the newly created function:

   `wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"`

   `wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecou> nter.php")`

   `evalResponse(document.wlSource)`	

5. Save the script as script 5-AJAX and JSON.

   

#### Step 3 – Displaying JSON Information During Runtime

Run the script. Each time the browser refreshes itself, a message in the log view is displayed. The message contains the statistics recorded in the browser, including the time and number of users online:

`The number of online users is: 1 and The current time is: 11:23:11am`

### The Full script: script 5-AJAX and JSON

```javascript
function InitAgenda()

{

wlGlobals.SaveSource = true

// END WLIDE

}

/\*\*\*\*\* WLIDE - URL : Home Page	- ID:20 \*\*\*\*\*/ wlGlobals.GetFrames = false wlHttp.Get("<http://www.webloadmpstore.com/index.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:22 \*\*\*\*\*/ Sleep(8371)

// END WLIDE

/\*\*\*\*\* WLIDE -Search page - ID:23 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/index.php>"

wlHttp.ContentType = "application/x-www-form-urlencoded" wlHttp.FormData["event"] = "search"



wlHttp.FormData["searchTerm"] = "webload" wlHttp.Post("<http://www.webloadmpstore.com/search.php>")

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:24 \*\*\*\*\*/ Sleep(8542)

// END WLIDE

/\*\*\*\*\* WLIDE - JavaScriptObject - ID:27 \*\*\*\*\*/ function evalResponse (source) {

json\_response = eval("(" + source + ")")

InfoMessage ( "The number of online users is: " + json\_response.usersOnline + " and The current time is: " + json\_response.time)

}

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Ajax - ID:7 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"

wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecounter.php> ")

evalResponse(document.wlSource)

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:8 \*\*\*\*\*/ Sleep(10811)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Ajax - ID:9 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"

wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecounter.php> ")

evalResponse(document.wlSource)

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:10 \*\*\*\*\*/ Sleep(10640)

// END WLIDE





/\*\*\*\*\* WLIDE - URL : Ajax - ID:11 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"

wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecounter.php> ")

evalResponse(document.wlSource)

// END WLIDE

/\*\*\*\*\* WLIDE - Sleep - ID:12 \*\*\*\*\*/ Sleep(10655)

// END WLIDE

/\*\*\*\*\* WLIDE - URL : Ajax - ID:13 \*\*\*\*\*/

wlHttp.Header["Referer"] = "<http://www.webloadmpstore.com/search.php>"

wlHttp.Get("<http://www.webloadmpstore.com/usersonlinecounter.php> ")

evalResponse(document.wlSource)

// END WLIDE
```









