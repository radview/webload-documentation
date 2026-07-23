# Installing and configuring WebRM

Install WebRM on a Windows machine that is reachable from every WebLOAD Console
that will use the floating license.

## Before you install

Make sure that:

- You have Windows administrator permissions on the WebRM machine.
- The machine has a stable host name or IP address.
- The machine's Host ID is the one for which the WebRM license was issued.
- The license supports the WebLOAD product version that will connect to it.
- Firewalls and network policy allow the Consoles to reach the license service.

For supported Windows versions and other requirements, see
[System Requirements](../installation.md#system-requirements).

## Install the WebRM server

1. Run the WebRM installer as an administrator.
1. Select the installation folder.
1. When the installer displays the Host ID, do one of the following:

    - Select the WebRM license file issued for that Host ID.
    - Record the Host ID and obtain the license before continuing the
      installation.

1. Complete the installation.
1. Confirm that the **RadView WebRM Service** starts.
1. Open **WebRM** from the Windows Start menu.
1. Confirm that the **Total resources** row displays the Console, Virtual
   Client, and Probing Client quantities from the license.

The installer also creates shortcuts for starting and stopping the service,
viewing the service log, opening WebRM Administration, and opening the locally
installed WebRM help.

For the installer walkthrough, see
[Installing WebRM](../installation.md#installing-webrm).

## Connect WebLOAD Console to WebRM

Configure each WebLOAD installation that will use the floating license:

1. Open **Update License** from the WebLOAD **Utilities** group in the Windows
   Start menu.
1. Select **Connect to the WebRM License Server**.
1. Click **Browse** and select the WebRM machine, or enter its resolvable host
   name.
1. Click **OK**.
1. Confirm that the connection succeeds and that the license details are
   displayed.
1. Open WebLOAD Console and request the required floating resources.

If the Console cannot connect, verify the WebRM host name, service status,
license validity, product version, and network access. See
[Troubleshooting](administration.md#troubleshooting).

## Update the WebRM license

Update the license from WebRM Administration on the WebRM machine:

1. Open **WebRM** from the Windows Start menu.
1. Select **Action** > **Update license**.
1. Browse to the new `.lic` file and select it.
1. Approve the update when prompted.
1. Wait for the service to restart and for the resource list to refresh.
1. Confirm the new totals with **Tools** > **License info** and **Tools** >
   **License Supported Features**.

> **Important:** If Consoles currently hold resources, WebRM warns that the
> resources will be revoked before the license is updated. Active test sessions
> can stop. Schedule the update for a maintenance window or coordinate it with
> the connected users.

A license is tied to its WebRM machine's Host ID. Obtain a replacement license
before moving WebRM to a different machine.
