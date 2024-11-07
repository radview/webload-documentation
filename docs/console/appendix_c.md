# Integrating with Nagios

This section describes how to integrate WebLOAD with Nagios. After integrating WebLOAD with Nagios, you can utilize data collected by Nagios to be used for WebLOAD monitoring purposes

Nagios is a free and open source computer-software application that monitors systems, networks and infrastructure. Nagios offers monitoring and alerting services for servers, switches, applications and services. It alerts users when things go wrong and alerts them a second time when the problem has been resolved.

The integration assumes you have installed and set up Nagios monitoring in your network.



## Instructing PMM to Collect Data from Nagios

Nagios integration is carried out by adding the Nagios data source in the Performance Measurements Manager (PMM), and instructing the PMM which data, collected by Nagios, to retrieve.

**To instruct PMM to collect data from Nagios:**

1. Run the Performance Measurements Manager wizard, as described in [Opening the](#_bookmark459)[ Performance Measurements Manager ](#_bookmark459)(on page [364](#_bookmark459)).
1. In the Selecting a Data Source screen, select **External** > **Nagios**.




![Selecting Nagios in Data Source Screen](../images/console_users_guide_3033.png)





3. In the Selecting a Host screen, enter the Nagios host name, username and password.

![Specifying Nagios Server in Host Selection Screen](../images/console_users_guide_3034.jpeg)





4. In the Selecting the Measurements to Monitor screen, do the following for each site/OS/host/device you wish to monitor

   1. Expand a site/OS/host/device by clicking the **+ a**djacent to the item.

      ![Selecting the Item to Monitor](../images/console_users_guide_3035.png)

   1. The sub components list all the statistics collected by Nagios for this item. Select the desired statistics.

![Selecting the Measurements to Monitor Screen](../images/console_users_guide_3036.png)



5. After all the desired items and statistics are selected, click **Next**. The Wizard displays a summary of the host, data source, and measurements configured for monitoring.

6. To accept the PMM configuration, click **Finish**.

   The PMM Wizard closes and the selected configuration is added to the PMM main window.



![PMM Wizard Configuration Summary](../images/console_users_guide_3037.png)




## Selecting the Nagios Statistics to Display in Reports

After integrating WebLOAD with Nagios, you can specify, while running a session, which Nagios statistics to view in the report view.

1. Open a report as described in [*Opening Reports* ](#_bookmark342)(on page [298](#_bookmark342)).
1. In the **PM@<Nagios-host>** node, select the statistics you wish to display in the report.



![Selecting the Statistics to Display in a Report](../images/console_users_guide_3038.png)





The following figure shows a report in Report view, displaying the statistics collected by Nagios that were selected to appear in the report.

![Viewing Nagios Statistics in Report View](../images/console_users_guide_3039.png)






