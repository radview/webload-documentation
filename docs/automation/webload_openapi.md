# Running WebLOAD using the Open REST API

You can run WebLOAD using a new REST Open API. With this API, you can remotely activate a test, remotely create Analytics Reports, and access any statistics that WebLOAD saves during a test.



## Accessing the REST Open API

**To access the REST Open API:**

1. Install the WebLOAD Dashboard, which is part of the regular WebLOAD installation, as follows:

   In the Select Components window of the WebLOAD installation wizard, select either of the following options:

   - Select **Full Installation** and check the **WebLOAD Dashboard** checkbox to have the dashboard installed locally as part of a full installation.
   - Select **Dashboard Server** to only install a central dashboard server.

   ![Web Dashboard Installation Options](../images/automation_users_guide_044.png)

   

2. See [REST API Reference](../dashboard/appendix_b.md)


## Understanding how to use the WebLOAD REST Open API
A description of the method and its parameters is embedded within each method in the Open API.

- The result of the Get Analytics method is an Analytics report, in the specified format (PDF, by default).
- The result of the Post Session method is that a specified load session starts running in the Console.
- The result of the other Open API methods is retrieved data in JSON format.




