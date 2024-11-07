# Appendix F: Integrating with Perfecto Mobile

Perfecto Mobile is a cloud-based real-device mobile testing solution. It tests mobile apps on real devices, in real time, on live carrier networks.

WebLOAD enables creating and running scripts that run Perfecto Mobile scripts on mobile devices in the Perfecto Mobile cloud.

Note that you can only use this feature if you have an account in Perfecto Mobile.



## Creating a Perfecto Mobile Script

In order to create a Perfecto Mobile script, you must first create a Perfecto Mobile script in Perfecto Mobile. The WebLOAD script will execute this Perfecto Mobile script, and gather statistics from the s Perfecto Mobile cript and from the device.

For instructions on how to create a Perfecto Mobile script please refer to Perfecto Mobile tutorials.

**To create a Perfecto Mobile WebLOAD script:**

1. Drag the **Perfecto Mobile  ![](../images/appenfix_f_004.png)**    icon from the Real Clients toolbox into the Script Tree at the desired location.

   The Perfecto Mobile dialog box opens.

   

   ![](../images/appenfix_f_009.png)

   

2. In the **Cloud Name** field, enter the URL for Perfecto Mobile.

3. Enter the Perfecto Mobile credentials:

   - In **Perfecto User**, enter your user name.
   - In **Perfecto Password**, enter your password.

4. Click **Select Script**. WebLOAD accesses the Perfecto Mobile scripts and displays them in the Select Script dialog box.

   Select a desired script and click **OK**.

   ![Select Script Dialog Box](../images/appenfix_f_011.png)

   

5. Click **Select Device**. WebLOAD accesses Perfecto Mobile and displays the list of available devices in the Select Device dialog box.

   Select a desired device and click **OK**.

   ![Select Device Dialog Box](../images/appenfix_f_012.png)

6. Set the **Test timeout**. This is the maximum number of seconds that the test is allowed to run.

7. Set the **Ping Time**. This is the frequency in seconds with which WebLOAD will check test status during test running.

8. Specify whether to **Send Transactions** to WebLOAD. That is, whether to send a list of all the transactions (Groups) that are written in the Perfecto Mobile script (such as: ”Open Chrome”, “Navigate to my application”).

9. Specify whether to **Send All Actions** to WebLOAD. That is, whether to send a list of all the actions that the script performs (such as: ”Press Key”, “Touch Drag”).

10. Click **OK**. The script is created, and is ready to be run.

![Script for Running a Script on a Device in the Perfecto Cloud](../images/appenfix_f_013.png)



If you run the Perfecto Mobile script in WebLOAD Recorder, all you see are the periodic pings. In order to gather device, transaction and action statistics, you need to run the script in the WebLOAD Console, as described in the following section.




## **Viewing Session Results of a Perfecto Mobile Session**

To gather statistics about the Perfecto Mobile script, create in the WebLOAD Console a Load template that runs the Perfecto Mobile script repetitively but for a single user (Probing Client).

The following figure shows an example results window. Note that the example displays also Actions and Transactions. That is, in addition to the various device statistics (such as Battery Level), statistics are also displayed for actions (such as Touch Drag) and transactions (such as Navigate in Chrome).

![Results of Running a Perfecto Mobile Load Session in the WebLOAD Console](../images/appenfix_f_015.png)

