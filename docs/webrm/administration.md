---
search:
  boost: 2
---

# WebRM administration and troubleshooting

Run WebRM Administration on the WebRM machine. It provides a live view of the
license pool and controls operations that can affect every connected Console.

## View license usage

Open **WebRM** from the Windows Start menu. The resource list contains:

- A **Total resources** row showing the used and licensed quantities.
- One row for each identifiable connected Console.

The connected-Console rows display:

| Column | Description |
| --- | --- |
| Host | The machine running WebLOAD Console. |
| User | The Windows user running the Console. |
| PID | The Console process identifier, when the connected version reports it. |
| Console | The number of Console resources allocated to the row. |
| Virtual Clients | The number of Virtual Clients allocated to the row. |
| Probing Clients | The number of Probing Clients allocated to the row. |

The PID distinguishes multiple Console instances running under the same user on
the same machine. Consoles from older WebLOAD versions might not report a PID
and can appear as a combined legacy row.

For more information about the installed license, select **Tools** > **License
info** or **Tools** > **License Supported Features**.

## Refresh the resource list

To refresh immediately, select **Action** > **Refresh**, click **Refresh**, or
press **F5**.

To configure automatic refresh:

1. Select **Tools** > **Options**.
1. Select **Refresh Every**.
1. Enter the refresh interval in minutes.
1. Click **OK**.

Select **Refresh manually** to disable automatic refresh.

## Revoke resources

Revoking returns a Console's allocated resources to the pool. It can stop a
test that is using those resources.

1. Identify the target Console by its Host, User, and PID.
1. Select one or more connected-Console rows. Do not select the **Total
   resources** row.
1. Select **Action** > **Revoke**, click **Revoke**, or press **Ctrl+D**.
1. Review the confirmation and click **OK**.
1. Refresh the list and confirm that the selected allocation was released.

The affected Console receives a revocation message. If resources are still
needed, the user must reconnect and request them again.

## Start or stop the WebRM service

Use the **Start WebRM Service** and **Stop WebRM Service** shortcuts installed
with WebRM. Administrative permissions can be required.

> **Important:** Stopping or restarting the service disconnects users that
> currently hold resources and can stop their test sessions.

After starting the service, open WebRM Administration and refresh the resource
list to verify that the license loaded successfully.

## View the service log

Select **Tools** > **View Server Log**, or use the **View WebRM Service
logfile** shortcut installed with WebRM. The log records service startup,
license loading, Console connections, resource requests, and errors.

The service log is recycled when the WebRM service restarts. Save a copy before
restarting the service when investigating an intermittent problem.

## Troubleshooting

| Symptom | Checks |
| --- | --- |
| Console cannot find or connect to WebRM | Confirm the server address, name resolution, service status, firewall access, and that the license is valid. |
| Console opens but cannot obtain resources | Check the **Total resources** row and connected-Console allocations. The requested resource might be fully allocated or absent from the license. |
| WebRM Administration shows no connected Consoles | Refresh the list, confirm that the Consoles are configured for this WebRM machine, and check the service log for connection errors. |
| License is expired or does not support the product version | Obtain a suitable license and follow [Update the WebRM license](install_configure.md#update-the-webrm-license). |
| Revoke fails | Confirm that the target Console is still running and reachable. Refresh the list and verify that the Console version is current. |
| Users disconnect unexpectedly | Check whether the WebRM service restarted, the license was updated, resources were revoked, or network connectivity was interrupted. |

When contacting RadView Support, include:

- The WebLOAD and WebRM version and build numbers.
- The WebRM host name and affected Console host names.
- The time of the problem.
- The WebRM service log.
- The affected Console log messages.
- The license details shown in WebRM Administration.
