---
search:
  boost: 2
---

# Requesting and managing resources

After WebLOAD Console is configured to use WebRM, it connects to the WebRM
machine whenever the Console starts.

## Request resources

When the Console opens, the **Request Resources** dialog displays the available
floating resources.

1. Enter the number of **Virtual Clients** required for the test.
1. Enter the number of **Probing Clients** required for the test.
1. To reuse these quantities on later connections, select **Always request same
   number of clients**.
1. Click **OK**.

If the request is larger than either the licensed total or the resources
currently available, the Console reports the available quantities. Reduce the
request or ask the WebRM administrator to check the current allocations.

The resources are reserved for that Console while it remains connected. Close
unused Consoles and release resources that are no longer needed so that other
users can obtain them.

## Change an allocation

You can change the allocation without restarting the Console:

1. In WebLOAD Console, open the **Home** tab.
1. Select **Update Floating License Resources**.
1. In the **Request Resources** dialog, change the Virtual Client and Probing
   Client quantities.
1. Click **OK**.

When you reduce an allocation, the released resources return to the WebRM pool.
An increase succeeds only when enough resources are currently available.

## Request resources from the command line

When starting a test from the command line, use the WebLOAD command-line
options for floating resources:

- `-vc <number>` requests Virtual Clients.
- `-pc <number>` requests Probing Clients.
- `-server <server-address>` selects the WebRM server.

See [Running WebLOAD from the Command Line](../automation/webload_cli.md) for the
complete command syntax.

## Revoked or disconnected resources

WebRM Administration can revoke resources from a connected Console. The
Console reports the revocation in its log, and a test using those resources can
stop.

The same can occur if the WebRM service is stopped or becomes unreachable.
After connectivity is restored, open or reconnect the Console and request the
resources again.

For administrative procedures, see
[WebRM administration and troubleshooting](administration.md).
