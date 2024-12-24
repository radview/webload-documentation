

# Before You Begin using WebLOAD Recorder

This section provides information before you begin using WebLOAD Recorder.

## Before You Begin

Before you begin recording scripts using WebLOAD Recorder, there are configuration steps that you may have to complete, depending on the Web application you want to test.

If you plan to record a script that includes retrieving a page that you accessed previously during that script, you should clear the cache and cookies in the browser. See [Clearing the Cache and Cookies in Your Browser ](#clearing-the-cache-and-cookies-in-your-browser).

When you have completed these startup steps, you can either start working with WebLOAD Recorder immediately, or you can configure the recording options first. For more information about configuring the recording options, see [*Configuring the Recording and Script Generation Options* ](./configuring_recorder_options.md#configuring-the-recording-and-script-generation-options)*.



## Clearing the Cache and Cookies in Your Browser

If your browser is set to use a cache file, steps such as loading a page that you have already visited are bypassed when you record a script.

If your browser loads a page from the cache file, that action is not recorded because retrieving a file from the cache is not an HTTP protocol call. Typically, this behavior is appropriate because you want to emulate the behavior of an actual browser during a test. However, if you want each visit to a page during a test to connect through an actual GET statement, you must work without a cache file when you record a script.

When you start recording, WebLOAD automatically changes the browser’s proxy settings to clear the cache and cookies, according to the definitions in the Recording and Script Generation dialog box (see [*Configuring the Recording and Script Generation Options* ](./configuring_recorder_options.md#configuring-the-recording-and-script-generation)). This enables WebLOAD Recorder to record all HTTP traffic. If you do not want to clear the cache and cookies automatically, you can manually clear the cache and cookies in your browser by following the instructions provided by your browser.

## Configuring the Proxy Value for Your Browser

Before you begin recording scripts using WebLOAD Recorder, your browser must be configured to use a specific proxy setting. This is usually done automatically when opening WebLOAD Recorder, but can also be done manually in the browser.

> **Note:** If your system is already configured to use a proxy setting, WebLOAD will preserve this setting for internal use, and will restore the setting after recording is complete.

The procedures described here describe how to configure the proxy server for Internet Explorer, Netscape Navigator, and Mozilla Firefox. If you are using a different browser, read through the proxy setting procedures and modify them as necessary for configuring your browser.

> ]**Note:** If your system is already using the WebLOAD Recorder default port (9884) for another application, you may designate an alternate port number (see [*Setting the Proxy Options* ](./configuring_recorder_options.md#setting-the-proxy-options)).
>

When recording is finished, reset the browser proxy to its original setting.

### Configuring the Proxy Value in Internet Explorer

**To configure the proxy value in Internet Explorer:**

1. Open WebLOAD Recorder (see [*Starting WebLOAD Recorder* ](#_bookmark35)).

1. Locate the Proxy Port number in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame. Usually this port number is 9884 (see [*Setting the Proxy Options* ](./configuring_recorder_options.md#setting-the-proxy-options)).

1. Determine if your organization has a Proxy Server that must be used to access the Internet when you record scripts.

1. If your organization *has a Proxy Server*:
   1. Determine the proxy name and port number.
   1. If the proxy port that it uses *is not* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 6.
   1. If the proxy port number *is* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 7.

1. If your organization *does not use a Proxy Server*, go to step 7.

1. Configure your organization’s proxy as the application proxy in WebLOAD Recorder:

   1. Open WebLOAD Recorder.

   1. Click **Recording and Script Generation Options** in the **Tools** tab of the ribbon and then select the **Proxy Options** tab.

   1. Select the **Use the following definitions for the application’s proxy server**  option.

   1. In the **HTTP Proxy**/**Port** fields, type the name and port number of your organization’s proxy.

   1. Click **OK.**

1. Open Internet Explorer.

1. Select **Tools** > **Internet Options** and then select the **Connections** tab.

1. Click **LAN Settings**.

1. In the Local Area Network LAN Settings dialog box, select the **Use a proxy server option**.

1. In the **Address** field, type localhost.

1. In the **Port** field, type the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame.

1. Verify that the **Bypass proxy server for local addresses** checkbox is cleared.

1. Click **OK.**

    You are finished configuring your proxy value.

    

### Configuring the Proxy Value in Netscape Navigator

**To configure the proxy value in Netscape Navigator:**

1. Open WebLOAD Recorder (see [*Starting WebLOAD Recorder* ](#_bookmark35)).

1. Locate the Proxy Port number in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame. Usually this port number is 9884 (see [*Setting the Proxy Options* ](./configuring_recorder_options.md#setting-the-proxy-options)).

1. Determine if your organization has a Proxy Server that must be used to access the Internet when you record scripts.

1. If your organization *has a Proxy Server*:

   1. Determine the proxy name and port number.
   1. If the proxy port that it uses *is not* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 6.
   1. If the proxy port number *is* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 7.

1. If your organization *does not use a Proxy Server*, go to step 7.

1. Configure your organization’s proxy as the application proxy in the WebLOAD Recorder:

   1. Open WebLOAD Recorder.

   1. Click **Recording and Script Generation Options** in the **Tools** tab of the ribbon and then select the Proxy Options tab.

   1. Select the **Use the following definitions for the application’s proxy server**  option.

   1. In the **HTTP Proxy**/**Port** fields, type the name and port number of your organization’s proxy.

   1. Click **OK.**

1. Open Netscape Navigator and do one of the following:

   - If you are using Navigator 3.x, select **Options** > **Network Preferences**.
   - If you are using Navigator 4.x, select **Edit** > **Preferences**.

1. Within Netscape Navigator, do one of the following:

   - If you are using Navigator 3.x, in the Preferences dialog box, select the Proxies tab.
   - If you are using Navigator 4.x, in the Preferences dialog box, under Category, expand Advanced and then select Proxies.

1. Select the **Manual Proxy Configuration** option.

1. In the Manual Proxy Configuration dialog box, in the **HTTP Address** field, type localhost.

1. In the corresponding **Port Number** field, type the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame.

1. Click **OK** to close the Manual Configuration dialog box.

1. Click **OK** to close the Preferences dialog box. You are finished configuring your proxy value.



### Configuring the Proxy Value in Mozilla Firefox

**To configure the proxy value in Mozilla Firefox:**

1. Open WebLOAD Recorder (see [*Starting WebLOAD Recorder* ](#_bookmark35)).

1. Locate the Proxy Port number in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame. Usually this port number is 9884 (see [*Setting the Proxy Options* ](#./configuring_recorder_options.md#setting-the-proxy-options)).

1. Determine if your organization has a Proxy Server that must be used to access the Internet when you record scripts.

1. If your organization *has a Proxy Server*:

   1. Determine the proxy name and port number.
   1. If the proxy port that it uses *is not* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 6.
   1. If the proxy port number *is* the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame, go to step 7.

1. If your organization *does not use a Proxy Server*, go to step 7.

1. Configure your organization’s proxy as the application proxy in the WebLOAD Recorder:

   1. Open WebLOAD Recorder.

   1. Click **Recording and Script Generation Options** in the **Tools** tab of the ribbon and then select the **Proxy Options** tab.

   1. Select the **Use the following definitions for the application’s proxy server** option.

   1. In the **HTTP Proxy**/**Port** fields, type the name and port number of your organization’s proxy.

   1. Click **OK.**

1. Open Mozilla Firefox.

1. Select **Tools** > **Options**.

1. Click **Advanced** and then click the **Network** tab.

1. In the Connection area, click **Settings**.

1. Click **Manual proxy configuration**.

1. In the **HTTP Proxy** field, type localhost.

1. In the **Port** field, type the proxy port number found in the Recording and Script Generation Options dialog box – Proxy Options tab – Recording Proxy Options frame.

1. Select the **Use this proxy for all protocols** checkbox.

1. Click **OK.**

    You are finished configuring your proxy value.



