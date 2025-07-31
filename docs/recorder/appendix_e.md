# Appendix E: Recording Mobile Applications

WebLOAD enables recording mobile applications in two ways:

- Native Mobile Recording – recording traffic from an actual mobile device. This works for both mobile web applications and native mobile applications.
- Simulate mobile in browser – records mobile web applications in the desktop by simulating a mobile browser. Does not require a mobile device, but only works for mobile web applications.

In addition, you can playback a recording as if it were a recording from a mobile application. This is performed in the WebLOAD Console using the Current Project Options window. In the **Browser Type** tab, specify the mobile application in the **Browser Parameters** section. The browser type you select overrides the settings that were defined during the recording, and plays back the recording according to the new settings.



## Native Mobile Recording

**To record traffic from an actual mobile device:**

1. Start native mobile recording, as follows:

    1. In WebLOAD Recorder, click **Start** in the **Home** tab of the ribbon. The Recording dialog appears.

          ![Selecting Native Mobile Recording](../images/select_native_recording.png)

    1. In the **Open** drop-down list, select **Native Mobile Recording**.

    1. Click **OK**.

1. Set up the mobile device proxy, as follows:

    1. Connect the mobile device to a Wireless network that can access your WebLOAD machine.

    1. Configure the device’s wireless proxy settings to go through the WebLOAD machine, on the noted port.

       This step depends on the device OS type and version. For example, see [*Setting Proxy Settings in iPhone* ](#setting-proxy-settings-in-iphone)* and [*Setting Proxy Settings in Android* ](#setting-proxy-settings-in-android-emulator).

1. Perform actions in your mobile device application or web browser; the HTTP requests will be recorded in the test script.

1. Stop recording, as follows:

    1. In WebLOAD Recorder, click **Stop Recording**.
    1. In the mobile device, change the Proxy settings back to off.

> **Note:**
>
> You may need to open you firewall to accept connections to proxynator.exe, on port 9884.
>
> To record secure traffic (HTTPS), the root certificate needs to be imported to the phone. For example, see [*Recording HTTPS Traffic on iPhone](#recording-https-traffic-on-iphone) *[HTTPS traffic on Android (4.0 and above)* ](#recording-https-traffic-on-android-40-and-above)
>
> When not recording, the mobile device will not be able to access the network (because the proxy is not available) – to use the network normally, revert the **HTTP Proxy** setting back to **Off**.

### Setting Proxy Settings in iPhone

**To set iPhone proxy settings:**

1. Open **Settings**, and access the **Wi-Fi** network settings:

    ![Accessing Wi-Fi iPhone Settings](../images/access_wifi_settings.jpeg)

1. Select edit current Wi-Fi Network settings:

    ![Edit Current Wi-Fi iPhone Settings](../images/edit_wifi_settings.jpeg)

1. Scroll down the **HTTP Proxy** section. Change proxy to **Manual** and set the **Server** and **Port** to point to the WebLOAD machines.

    The default port for the proxy-recorder is 9884. You may need to use the machine’s IP-address instead of name.

    ![Setting Wi-Fi iPhone Settings](../images/setting_iphone_wifi.jpeg)





#### **Recording HTTPS Traffic on iPhone**

In order to record HTTPS traffic, the WebLOAD root certificate needs to be trusted by the phone. To import the root certificate:

1. Locate the root certificate, in:

    `c:\Program Files\RadView\WebLOAD\bin\Certificates\root.pem`

1. Open the root.pem file on the phone. This can be done by sending the file via e-mail, or accessing the file from a web-server.

1. Click **Install**.

    ![Installing the Root CA](../images/install_root_ca.jpeg)

1. A warning will appear; click **Install**. The certificate should now be trusted

    ![Trust root CA](../images/root_ca.jpeg)

1. You need to turn on SSL trust for that certificate, go to:
 Settings > General > About > Certificate Trust Settings. Under "Enable full trust for root certificates", turn on trust for the certificate.

    ![Enable Trust root CA](../images/trust_root_ca_iphone.png)

1. After recording is completed, the certificate may be removed. To remove the certificate, select the following: **Settings** > **General** > **Profile ‘RadView Root CA’** > **Remove**.

### Setting Proxy Settings in Android Emulator

Follow these steps exactly as shown. Any small change will likely cause it not to work!

Watch the video here: [Android Recording](https://youtu.be/Hc9QQ-J5nI8)

#### Install emulator

- Download Android studio/SDK: [https://developer.android.com/studio](https://developer.android.com/studio)
- Standard install
- Open ‘Virtual Device Manager’
- Choose a device WITHOUT google play, for example Pixel 3a XL
- Download "Q" system level and select it.

#### Install RadView root certificate

Needed in order to record https traffic - practically this is always needed.

Use adb commands, adb will be in:
C:\Users\myuser\AppData\Local\Android\Sdk\platform-tools

Emulator will be in :
c:\users\myuser\AppData\Local\Android\Sdk\emulator\emulator.exe

(See below these command as a script - Script to set-up emulator)

List devices.
Should show:
Pixel_3a_XL_API_29

`emulator.exe -list-avds`

Start the emulator in writable mode (make sure it's *not* turned on before running). Should start the emulator in a new window, wait for it to load ("boot completed")

`emulator -avd Pixel_3a_XL_API_29 -writable-system`

start adb root, should say: restarting adbd as root

`adb root`

diable verification, should say: Successfully disabled verification.

`adb shell avbctl disable-verification`

Reboot the device for changes to take effect. WAIT for reboot to start and end. Emulator window will have "boot completed" again - this takes time!

`adb reboot`

start as root, should not display anything

`adb root`

remount, should say: remount succeeded

`adb remount`

copy cert, should say: 1 file pushed

`adb push "c:\Program Files (x86)\RadView\WebLOAD\bin\Certificates\root.pem" /system/etc/security/cacerts/3b4f28f8.0`

chmod, should not display anything

`adb shell chmod 664 /system/etc/security/cacerts/3b4f28f8.0`

Final reboot, wait for it to start and end, start recording in WebLOAD, change WiFi proxy settings to 10.0.2.2 port 9884 and record scenario

`adb reboot`

#### Record in WebLOAD

Set proxy settings:

On the desktop machine:

Open Firewall settings, advanced, add rule to allow traffic on TCP port 9884

Start WebLOAD Recorder.

- Start Recording (Click ‘Start’ on the red circle icon).
- Choose "Native Mobile Recording" (Preior to WebLOAD 13.2 - Choose "Chrome" and click Ok. This will open a Chrome window, leave it open and ignore it until the end of recording)
- On the Mobile device (emulator) change proxy to use WebLOAD:
  - Open WiFi Settings, find the "AndoirdWiFi" and change settings:
  - Click the Pencil to edit:
  - Expand the ‘Advanced options’
    - Set ‘Proxy’ to ‘manual’
    - Set ‘Proxy hostname’ to ‘10.0.2.2’ (this will point to the machine running the emulator. localhost/127.0.0.1 means the android device)
    - Set ‘Proxy port’ to 9884
![Android Wifi Settings](../images/android_wifi_settings.png)

Now traffic from the apps and browser should be captured in WebLOAD.

### Setting Proxy Settings in Android (Legacy phones)

**To set Android proxy settings:**

1. Using the menu button, select **Settings**.

1. Select **Wireless & networks**.

1. Select **Wi-Fi settings**.

1. Switch on and connect to your designated Wi-Fi network.

1. Once connected, press the Menu button again and select **Advanced**.

1. Set **Proxy** to the WebLOAD machine IP-address, and **Port** to 9884.

    ![Proxy Settings in Android – Two Examples](../images/proxy_settings_adroid.png)




#### Recording HTTPS traffic on Android (4.0 and above)

In order to record HTTPS traffic, the WebLOAD root certificate needs to be trusted by the phone. To import the root certificate:

1. Locate the root certificate, in:

    c:\Program Files\RadView\WebLOAD\bin\Certificates\root.pem

1. Copy locally, as root.crt.

1. Copy root.crt from your computer to the root of your device's internal storage (that is, not in a folder).

1. From a Home or All Apps screen, tap the **Settings** icon.

1. Go to **Personal** > **Security** > **Credential storage** > **Install from storage**.


## **Simulating a Mobile in a Browser**

In Simulate mode, the recording is done using the desktop browser, identified to the server as a mobile user agent.

**To simulate a mobile:**

1. In WebLOAD Recorder, click **Start Recording**.

    ![Simulating a Mobile](../images/simulating_mobile.png)

1. Check the **Identify As** checkbox.

1. Select the **Browser** family and **Version**.

1. Click **OK**.

> **Notes:** 
>
> - This approach is only applicable to some mobile web-sites, which rely on server- side mobile detection
> - Some mobile sites may not render as expected in the desktop browser.
> - For best results, use a Chrome browser.


