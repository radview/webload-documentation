# Appendix D: **Understanding the Templates** 

This appendix describes each template, and provides analysis highlights and tips where applicable. 



## Understanding Load Session Terminology 

> **Note:** All the measurements appearing in the various templates are explained in the glossary. 



Each run of the script body is called a *round*. A round is composed of transactions. Each transaction can include various combinations of the following: 

- Request(s) for a page. The page can include any number of graphics and contents files. Each request for a gif, jpeg, html file, etc., is a single *hit*. 

- Sleep intervals. 

- JavaScript functions. 

  

The following illustrates a sample round: 

| **Round**   |             |      |      |             |      |
| ----------- | ----------- | ---- | ---- | ----------- | ---- |
| Transaction | Transaction |      |      |             |      |
| Page        | Sleep       | Page | Page | JS function |      |
| Hit         | Hit         | Hit  | Hit  | Hit         | Hit  |




| **Hit  Time Breakdown** |               |                    |               |               |
| ----------------------- | ------------- | ------------------ | ------------- | ------------- |
| DNS  Lookup             | Connect  Time | Send Time          | Response Time | Process  Time |
| Time To First Byte      | Receive Time  |                    |               |               |
|                         |               |                    |               |               |
| *TCP Connection*        |               |                    |               |               |
| *HTTP Request*          |               | *HTTP*  *Response* |               |               |



## General Templates

This category of templates provides general statistical information about the Load Session. 

### HTTP Response Status Codes

` `The HTTP Errors Over Time, HTTP Responses, and HTTP Responses Over Time templates display various HTTP response status messages. The following table lists all HTTP response status codes and their descriptions. For a full description, see [*http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html*.](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 

|                   | 304  | Not  Modified                   |
| ----------------- | ---- | ------------------------------- |
|                   | 305  | Use  Proxy                      |
|                   | 307  | Temporary Redirect              |
| **Client  Error** | 400  | Bad Request                     |
|                   | 401  | Unauthorized                    |
|                   | 402  | Payment Required                |
|                   | 403  | Forbidden                       |
|                   | 404  | Not  Found                      |
|                   | 405  | Method Not Allowed              |
|                   | 406  | Not Acceptable                  |
|                   | 407  | Proxy  Authentication Required  |
|                   | 408  | Request Timeout                 |
|                   | 409  | Conflict                        |
|                   | 410  | Gone                            |
|                   | 411  | Length Required                 |
|                   | 412  | Precondition Failed             |
|                   | 413  | Request Entity Too Large        |
|                   | 414  | Request-URI Too Long            |
|                   | 415  | Unsupported Media Type          |
|                   | 416  | Requested Range Not Satisfiable |
|                   | 417  | Expectation Failed              |
| **Server  Error** | 500  | Internal Server Error           |
|                   | 501  | Not Implemented                 |
|                   | 502  | Bad  Gateway                    |
|                   | 503  | Service Unavailable             |
|                   | 504  | Gateway Timeout                 |
|                   | 505  | HTTP  Version Not Supported     |



### Attempted Connections

This template displays a bar graph of successful and failed connections, over time. It also displays the Load Size, for reference. 

Under normal circumstances, you would not expect to see failed connections. Failed connections may indicate a problem. 

### Connection Time

This template displays a bar graph showing the breakdown of connection time into DNS Lookup Time and Connect Time. The template also displays the Load Size, for reference. 

- DNS Lookup Time – The time it takes to resolve the host name and convert it to an IP address by calling the DNS server. Note that the DNS is checked once per virtual-user, for the whole session. 
- Connect Time – The time it takes for a Virtual Client to connect to the System Under Test (SUT), in seconds. In other words, the time it takes from the beginning of the HTTP request to the TCP/IP connection.  

  Note that if the Persistent Connection option is enabled in the WebLOAD Console,  there may not be a value for Connect Time because the HTTP connection remains open between successive HTTP requests. 
  
  

**General Session Information** 

This template displays the following information about the Load Session: 

- Start and end time, and duration. 
- The maximum number of virtual clients. 
- Which scripts are running.  
- General information about the reporter. 
- General information about the System under Test (SUT). This template is useful as an opening page for published reports. 



> **Tip**
>
> You can customize the look of the General Session Information template by editing the settings of the following parameters: PEN\_COMPANY, OPEN\_REPORTER\_NAME, OPEN\_REPORTER\_TITLE, OPEN\_SUT\_DIAGRAM, 
>
> OPEN\_SUT\_NAME, OPEN\_SUT\_VERSION.  
>



### HTTP Errors Over Time

This template displays for each time interval, the number of HTTP client side errors (4xx) and HTTP server side errors (5xx) that occurred during the interval.  

The template also displays the Load Size, for reference. 





### HTTP Responses

This template displays a summary of the HTTP response status messages received during the Load Session. For each type of response status, the template lists the number of responses received and what percentage it represents of all HTTP responses. 

Some common response status messages are: 

- 200 – OK 
- 302 – Found 
- 404 – Not Found 
- 500 – Internal Server Error 

For more information see:[` `*http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html*.](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 



### HTTP Responses Over Time 

This template displays the number of HTTP responses at each time interval, for each response status code. 



### Load Size Summary

This template displays the progress of the Load Session by showing the load size over time. That is, the number of Virtual Clients running over time. 

This template provides an understanding of the nature of the test being conducted. All other templates should be analyzed in the context of load size behavior. 

### Performance Summary 

This template displays the main performance indicators and changes in Load Size, over time: 

- Load Size – The number of Virtual Clients running during the last reporting interval. 
- Page Time – The time it takes to complete a successful upper level request, in seconds. The Page Time is the sum of the Connect Time, Send Time, Response Time, and Process Time for all the hits on a page. 
- Time to First Byte – The time it takes from when a request is sent until the Virtual Client receives the first byte of data. 
- Response Time –The time it takes the SUT to send the object of an HTTP request back to a Virtual Client, in seconds. In other words, the time from the end of the HTTP request until the Virtual Client has received the complete item it requested. 
- Hits Per Second – The number of times the Virtual Clients made an HTTP request, divided by the elapsed time, in seconds. Each request for a gif, jpeg, html file, etc., is a single hit. 
- Throughput – The average number of bytes per second, transmitted from the SUT to the Virtual Clients running the script during the last reporting interval. In other words, this is the value of the Response Data Size divided by the number of seconds in the reporting interval. 

#### *Analysis Highlights* 

Hits Per Second, Page Time, Time to First Byte, and Response Time are ‘lower is better’ measurements. An increase in these measurements as the load increases may indicate performance degradation. Sudden decreases in them may also indicate a problem. 

Under normal circumstances, Throughput is expected to grow linearly with the load. A constant throughout on increased load may indicate a bottle-neck (bandwidth, or server capacity). A decreasing throughput may also indicate a problem, such as the server sending less responses or shorter, erroneous responses. 

### Response Time Breakdown 

This template displays a bar graph showing the breakdown of response time between Time to First Byte and Receive Time, as well as the Send Time.

- Send Time – The time it takes the Virtual Client to write an HTTP request to the SUT, in seconds.  
- Time to First Byte – The time it takes from when a request is sent until the Virtual Client receives the first byte of data. 
- Receive Time – The elapsed time between receiving the first byte and the last byte. The template also displays the Load Size, for reference. 



## Log and Errors Templates 

This category of templates provides information about the errors logged for this Load Session.  

### Errors By Severity

This template displays the total number of errors received, grouped by severity level: Info, Minor Error, Error, and Severe Error.  



By default, only warnings (minor errors) and above are displayed. To change the default setting, edit the settings of the MIN\_SEVERITY parameter. 



### Errors Per Second

This template displays the number of error messages logged over time, for each level of severity. 



### Errors Per Transaction 

This template displays a summary of all failed transactions, and the reason for failure. The following attributes are displayed: 

- Transaction Name – The name of the transaction. 
- Total Count – The total number of times the transaction was executed. 
- Successful Count – The number of successful executions of the transaction. 
- Failed Count – The number of failed executions of the transaction. 
- Marked Count – The number of times a lower level transaction, meaning a transaction nested within a higher level transaction, failed within the current transaction. 

For each type of failure, the template displays a description of the failure and how many times this type of failure occurred. 



### Log Messages 

This is a detailed template of all the log messages logged during the Load Session.  Note that WebLOAD automatically stops logging after a certain number of log events. 



By default, only minor errors and above are displayed. To change the default setting, edit the settings of the MIN\_SEVERITY parameter. 



### Log Summary

This template displays a summary of the Load Session’s logged messages. Similar messages are grouped, and their total count shown. 



## Pages Analysis Templates

 This category of templates provides an analysis of the pages requested during the Load Session.

### Pages Count

This template displays the total number of pages received over time. This represents the total number of times the Virtual Client made upper level requests (both successful and unsuccessful) during the last reporting interval.

The template also displays the Load Size, for reference.

 

### Total Page Time

This template displays the Page Time, over time.

 Page Time is the time it takes to complete a successful upper level request, in seconds. It is the sum of the Connect Time, Send Time, Response Time, and Process Time for all the hits on a page.



## Percentile Templates

This category of templates provides information in the form of percentiles.

A percentile is the value of a variable below which a certain percent of observations fall. For example, if a graph shows 40 Hits Per Second for the 70th percentile, that means that 70 percent of the Hits Per Second observation values are below 40.

 

### Hits Per Second By Percent

This template displays the distribution of Hits Per Second values in the session. Hits Per Second is the number of times the Virtual Clients made an HTTP request,

divided by the elapsed time, in seconds. Each request for a gif, jpeg, html file, etc. is a single hit.

For example, if the graph shows 40 Hits Per Second for the 70th percentile, that means that 70 percent of the Hits Per Second observation values are below 40.

 

### Response Time By Percent

This template displays the distribution of the following response time values in the session:

- Response Time – The time it takes the SUT to send the object of an HTTP request back to a Virtual Client, in seconds. In other words, the time from the end of the HTTP request until the Virtual Client has received the complete item it requested.
- Time To First Byte – The time it takes from when a request is sent until the Virtual Client receives the first byte of data.

For example, if the graph shows a Response Time of 1.3 seconds for the 70th percentile, that means that 70 percent of the Response Time observation values are below 1.3 seconds.

 

### Transaction Response Time By Percent

For each transaction in the session, this template displays the distribution of the transaction response time values in the session.

For example, if the graph shows a Login Time of 10 seconds for the 80th percentile, that means that 80 percent of the Login Time observation values are below 10 seconds.



## Regression Templates

This category of templates enables you to compare one selected “Main” session to one or more additional sessions you specify.

Regression is very useful for comparing two sessions that were run on the same Load Template. The purpose is to gauge whether a small change in the System Under Test has degraded the performance.

Most templates available under the Regression category are identical to templates of the same name available under other categories, with the following enhancement: each displayed measure is shown for all the sessions being compared. A given measure calculated for different sessions will appear with the same color, but a different line style. This enables easy comparison between measurements from different sessions.

For example, in the following Pages Count regression chart, two sessions are compared: “MP_Store” and “interesting”. The Load Size measure for both is shown in green, but the line style (dotted, continuous, round points, square points) is different.



### Errors By Severity

This regression template displays for each Load Session you specified, the total number of errors received, grouped by severity level: Info, Minor Error, Error, and Severe Error.



### Errors Per Second

For each specified Load Session, this regression template displays the number of error messages logged over time, by severity.



### Failed Transactions

For each specified Load Session, this regression template displays information about transactions that had failures during the session.



### Full Comparison

This regression template compares the average values of *all* measurements from two sessions. It is therefore useful for pinpointing possible disparities in measurements that are not normally compared in regression charts.

The template compares the average values of the second session to the average values of the Main session.  

- The higher the ratio between them, the darker the background color of the ratio value.  
- A negative ratio denotes a decrease in average measurement value; a positive ratio denotes an increase in average measurement value. 

#### *Analysis Highlights* 

If a disparity is found, you can explore it further by creating a detailed report on the suspected measurement using the User Defined Blank Regression Template.   



### General Session Information

This regression template displays the following information about the main Load Session: 

- Start and end time, and duration. 
- Which scripts are running.  
- General information about the reporter. 
- General information about the System under Test (SUT). 

The template also displays which additional sessions are specified. 

This template is useful as an opening page for published reports generated from regression templates. 



### HTTP Responses 

This regression template displays a summary of the HTTP response status messages received during the specified Load Sessions. For each type of response status, the template lists the number of responses received and what percentage it represents of all HTTP responses. 

Some common response status messages are: 

- 200 – OK 
- 302 – Found 
- 404 – Not Found 
- 500 – Internal Server Error 

For more information see:[` `*http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html*.](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 



### Load Size Summary 

For each specified Load Session, this regression template displays the progress of the load session by showing the load size over time. That is, the number of Virtual Clients running over time.  

This template provides an understanding of the nature of the tests being conducted. All charts should be analyzed in the context of load size behavior. 



### Pages Count 

For each of the specified Load Sessions, this regression template displays the total number of pages received over time. This represents the total number of times the Virtual Client made upper level requests (both successful and unsuccessful) during the last reporting interval.  

The template also displays the Load Sizes, for reference. 



### Performance Summary 

For each of the specified Load Session, this regression template displays the main performance indicators and changes in Load Size, over time: 

- Load Size – The number of Virtual Clients running during the last reporting interval. 
- Page Time – The time it takes to complete a successful upper level request, in seconds. The Page Time is the sum of the Connect Time, Send Time, Response Time, and Process Time for all the hits on a page. 
- Time to First Byte – The time it takes from when a request is sent until the Virtual Client receives the first byte of data. 
- Response Time – The time it takes the SUT to send the object of an HTTP request back to a Virtual Client, in seconds. In other words, the time from the end of the HTTP request until the Virtual Client has received the complete item it requested. 
- Hits Per Second – The number of times the Virtual Clients made an HTTP request, divided by the elapsed time, in seconds. Each request for a gif, jpeg, html file, etc., is a single hit. 
- Throughput – The average number of bytes per second, transmitted from the SUT to the Virtual Clients running the script during the last reporting interval. In other words, this is the value of the Response Data Size divided by the number of seconds in the reporting interval. 

#### Analysis Highlights 

The Hits Per Second, Page Time, Time to First Byte and Response Time are ‘lower is better’ measurements. An increase in these measurements as the load increases may indicate performance degradation. Sudden decreases in them may also indicate a problem.  

Under normal circumstances, Throughput is expected to grow linearly with the load. A constant throughout on increased load may indicate a bottle-neck (bandwidth, or server capacity). A decreasing throughput may also indicate a problem, such as the server sending less responses or shorter, erroneous responses. 



### PMM Server-side Statistics 

For each of the specified Load sessions, this regression template displays the statistics gathered by the Performance Measurement Monitor 

The selected server side measurements are shown over time. The Load Size is also shown, for reference. Note that server side statistics must be explicitly added at the template definition stage, before executing the load session  

For information on the PMM and how to add server side statistics, see the *WebLOAD Console User  Guide*. 



### Response Time 

This regression template is used to compare the total response time over time of two or more sessions. The compared Load Size is also displayed, for reference. 



### Response Time Breakdown 

For each of the specified Load Sessions, this regression template displays a bar graph showing the breakdown of response time between Time to First Byte and Receive Time, as well as the Send Time. 

- Send Time – The time it takes the Virtual Client to write an HTTP request to the SUT, in seconds.  
- Time to First Byte – The time it takes from when a request is sent until the Virtual Client receives the first byte of data. 
- Receive Time – The elapsed time between receiving the first byte and the last byte. For each Load Session, the template also displays the Load Size, for reference. 



### Slowest Transactions 

For each of the specified Load Sessions, this regression template displays the session’s transactions, ordered by the average transaction time, slowest first. 

You can configure the template to show only a certain number or certain percentage of the slowest transactions. To do so, edit the settings of the TRAN\_PERCENT or TRAN\_QTY parameters. 



### Transactions With Most Failures 

For each of the specified Load Sessions, this regression template displays the transactions, ordered by the highest failure count. 

You can configure the template to show only a certain number or certain percentage of the top failing transactions. To do so, edit the settings of the TRAN\_PERCENT or TRAN\_QTY parameters. 



### Total Page Time 

For each of the specified Load Sessions, this regression template displays the Page Time, over time.  

Page Time is the time it takes to complete a successful upper level request, in seconds. It is the sum of the Connect Time, Send Time, Response Time, and Process Time for all the hits on a page. 

The template also displays the Load Sizes, for reference.



### Transactions Over Load 

For each of the specified Load Sessions, this regression template displays the transaction response time compared with Load Size values, for each transaction in the session.  

This information can be useful when the load size does not change linearly with time. 



### Transactions Over Time

For each of the specified Load Sessions, this regression template displays changes in transaction time over session running time. It also displays the Load Size, for reference. 



### Transactions Summary 

For each of the specified Load Sessions, this regression template displays summary information about the transactions in the session. For each type of transaction, the following information is displayed: 

- Transaction Count – Displays the total number of successful and failed transactions. 

- Transaction Time – For successful transactions, the table displays Transaction Time statistics: Average, Percentile X%, Max, Min, Standard deviation, and Transactions Per Second  

  

The default percentile is 90%. To change the default setting, edit the settings of the PERCENTILE parameter. 

You can use the Transactions Over Time and Transaction Response Time By Percent regression templates instead of this template. 



## Server Side Statistics Templates 

This category of templates provides statistical information related to the server. 

### Imported Statistics 

This template displays statistical information related to the server that was imported from an external source.  For information on how to import external statistics, see the *WebLOAD Console User Guide*. 



### Load Generators Health 

This template displays basic CPU usage and memory usage statistics, for each Load Generator used in the session.  

Use this template to make sure that the Load Generators are not overloaded while running the load. Overloaded Load Generators may not be able to fully load the server, and may skew the test results. 



### PMM Server-Side Statistics 

This template displays the statistics gathered by the Performance Measurement Monitor 

The selected server side measurements are shown over time. The Load Size is also shown, for reference. Note that server side statistics must be explicitly added at the template definition stage, before executing the load session  



For information on the PMM and how to add server side statistics, see the *WebLOAD Console User Guide*. 



## Transaction Analysis Templates 

This category of templates enables you to analyze the Load Session’s transactions. Refer to[` `*Understanding Load Session Terminology* ](#understanding-load-session-terminology) for an explanation of the basic elements of a transaction. 

### Failed Transactions 

This template displays information about transactions that had failures during the session. 

The chart depicts failed transactions and failure reasons. 



### Slowest Transactions 

This template displays the session’s transactions, ordered by the average transaction time, slowest first. 

You can configure the template to show only a certain number or certain percentage of the slowest transactions. To do so, edit the settings of the TRAN\_PERCENT or TRAN\_QTY parameters. 



### Transaction Counters 

This chart shows successful and failed transaction counts for each transaction in the session. 



### Transaction Response Times 

This chart shows the average transaction response time, for each transaction. 



### Transactions Dashboard 

This template displays for each transaction: 

- A graph chart of transaction behavior over time. 
- A bar chart of successful/failed transactions over time. 
- A pie chart of overall success/fail statistics. 



### Transactions Over Load

This template displays for each transaction in the session, the transaction response time compared with Load Size values.

 This information can be useful when the load size does not change linearly with time.

 

### Transactions Over Time

This template displays changes in transaction time over session running time. It also displays the Load Size, for reference.

 

### Transactions With Most Failures

This template displays the transactions, ordered by the highest failure count. You can configure the template to show only a certain number or certain percentage of the top failing transactions. To do so, edit the settings of the TRAN\_PERCENT or TRAN\_QTY parameters.



## **Statistical Correlation**

Statistical correlation templates are used to pinpoint suspect causes for unusual behavior of a certain measurement. 

There are four predefined templates in this category. They differ in the leading measurement (Response Time, Throughput), and in the graphical representation (over time or over the leading measurement). However, you can specify any measurement in any script to be the leading measurement, and you can view its correlation to all other measurements either over time or over the leading measurement. 



### Response Time Correlation 

This template displays the correlation of specified measurements with the Response Time measurement, over Response Time. If you selected a different leading measurement to correlate to, the chart displays correlation with the leading measurement you selected.  

- The Correlation column shows the linear correlation coefficient. It is a number between 0 and 1, with 1 being the highest possible correlation.  

  The measurements are listed in the order of correlation, with the highest first. 

- The Direction column indicates whether the correlation is positive (the measurement goes up when the leading measurement goes up, and down when the leading measurement goes down) or negative (the measurement goes up when the leading measurement goes down, and down when the leading measurement goes up). 

You can apply a Time Filter that restricts the correlation calculation to a specific time frame, to better focus on a certain behavior of the leading measurement.  



### Response Time Correlation Over Time 

This template displays the correlation of specified measurements with the Response Time measurement, over time. If you selected a different leading measurement to correlate to, the chart displays correlation with the leading measurement you selected. 

- The Correlation column shows the linear correlation coefficient. It is a number between 0 and 1, with 1 being the highest possible correlation.  

  The measurements are listed in the order of correlation, with the highest first. 

- The Direction column indicates whether the correlation is positive (the measurement goes up when the leading measurement goes up, and down when the leading measurement goes down) or negative (the measurement goes up when the leading measurement goes down, and down when the leading measurement goes up). 



> **Tip**
>
> You can apply a Time Filter that restricts the correlation calculation to a specific time frame, to better focus on a certain behavior of the leading measurement. 



### Throughput Correlation 

This template displays the correlation of specified measurements with the Throughput measurement, over Throughput. If you selected a different leading measurement to correlate to, the chart displays correlation with the leading measurement you selected. 

- The Correlation column shows the linear correlation coefficient. It is a number between 0 and 1, with 1 being the highest possible correlation.  

  The measurements are listed in the order of correlation, with the highest first. 

- The Direction column indicates whether the correlation is positive (the measurement goes up when the leading measurement goes up, and down when the leading measurement goes down) or negative (the measurement goes up when the leading measurement goes down, and down when the leading measurement goes up). 

> **Tip**
>
> You can apply a Time Filter that restricts the correlation calculation to a specific time frame, to better focus on a certain behavior of the leading measurement. 





### Throughput Correlation Over Time 

This template displays the correlation of specified measurements with the Throughput measurement, over time. If you selected a different leading measurement to correlate to, the chart displays correlation with the leading measurement you selected. 

- The Correlation column shows the linear correlation coefficient. It is a number between 0 and 1, with 1 being the highest possible correlation.  

  The measurements are listed in the order of correlation, with the highest first. 

- The Direction column indicates whether the correlation is positive (the measurement goes up when the leading measurement goes up, and down when the leading measurement goes down) or negative (the measurement goes up when the leading measurement goes down, and down when the leading measurement goes up). 

> **Tip**
>
> You can apply a Time Filter that restricts the correlation calculation to a specific time frame, to better focus on a certain behavior of the leading measurement. 