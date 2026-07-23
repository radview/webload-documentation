---
search:
  boost: 2
---

# WebRM (WebLOAD Resource Manager) overview

This online WebRM help covers the WebLOAD Resource Manager, also known as the
WebRM license server. WebRM keeps licensed resources in one central pool so
that multiple WebLOAD Consoles can use them as needed.

WebRM can be installed on a dedicated Windows machine or on a machine that also
runs WebLOAD components. The WebRM machine must remain reachable while Consoles
are using floating resources.

## Resources managed by WebRM

The WebRM license determines the total number of resources available in each
category:

| Resource | Description |
| --- | --- |
| Consoles | The number of WebLOAD Console instances that can be connected concurrently. |
| Virtual Clients | The total number of Virtual Clients that connected Consoles can use concurrently. |
| Probing Clients | The total number of Probing Clients that connected Consoles can use concurrently. |

A Console checks out a Console resource when it connects. It then requests the
Virtual Client and Probing Client resources needed for a test. Those resources
remain allocated until the Console releases them, closes, or an administrator
revokes them.

## WebRM components

A WebRM environment consists of:

- **WebRM license service** -- Runs on the WebRM machine and owns the floating
  license pool.
- **WebRM Administration** -- Displays the license totals, connected Consoles,
  and current allocations. Administrators use it to refresh the display, update
  the license, inspect the service log, and revoke resources.
- **WebLOAD Console** -- Connects to the WebRM machine and requests resources
  from the shared pool.

## How WebRM works

1. The WebRM service starts and loads the license installed for that machine.
1. A configured WebLOAD Console connects to the WebRM machine.
1. WebRM verifies that a Console resource is available.
1. The user requests Virtual Client and Probing Client resources.
1. WebRM grants the available resources and records the allocation in WebRM
   Administration.
1. When the resources are released, they return to the shared pool.

If the WebRM service is unavailable, the Console cannot obtain or retain
floating resources. A running test can also be affected if an administrator
revokes its resources or stops the WebRM service.

## Next steps

- [Install and configure WebRM](install_configure.md)
- [Request and update resources from WebLOAD Console](resource_management.md)
- [Administer and troubleshoot WebRM](administration.md)
