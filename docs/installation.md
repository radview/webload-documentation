# Introduction


Welcome to WebLOAD, the premier  performance, scalability, and reliability testing solution for internet applications.  

WebLOAD is easy to use and delivers maximum testing performance and value. WebLOAD verifies the scalability and integrity of internet applications by generating a load composed of Virtual Clients that simulate real-world traffic. Probing Clients let you refine the testing process by acting as a single user that measures the performance of targeted activities, and provides individual performance statistics of the internet application under load.  


## System Requirements

WebLOAD has the following system requirements. WebLOAD Console, WebLOAD Recorder, WebLOAD Analytics, WebLOAD Probing Client, and WebRM can only be run on Windows platforms. WebLOAD Load Machines can be run on Windows, and Linux platforms. 

**Note:** For any installation, you must have Administrator rights for the computer on which you are installing. 



### Windows Platforms



**WebLOAD System Requirements**

| **Requirements**     | **WebLOAD Console, WebLOAD Recorder, WebLOAD Analytics, WebLOAD  Probing Client, and WebRM** | **Load Machine**                                             |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Computer / Processor | 2 Core CPU | 2 Core CPU (4 Core CPU Recommended) |
| Operating System     | Windows supported version: (Windows 10, 11, Server 2012, 2016, 2019, 2022)  | Windows supported version: (Windows 10, 11, Server 2012, 2016, 2019, 2022)  |
| Memory               | 2 GB RAM (minimum); 4 GB  is recommended                     | 2 GB RAM (minimum); 16 GB is recommended                      |
| Free Disk Space      | 20 GB                                                         | 20 GB                                                         |





### Linux Platforms (for WebLOAD Load Machines)

*Table: WebLOAD Load Machine System Requirements* 

| **Requirements** | **Load  Machine**                                            |
| ---------------- | ------------------------------------------------------------ |
| Hardware         | 2 Core CPU (4 Core CPU Recommended) |
| Version          | Linux RHEL 8 and up or equivalent  |
| Free Disk Space  | 20 GB                                                         |
| Swap Space       | RAM*2                                                        |
| Memory           | 2 GB RAM (minimum); 16 GB is recommended                      |



> **Notes:**
>
> WebLOAD components in each major version will work with all other components of the same version. WebLOAD components are not compatible with other components of a different version. Verify that the WebLOAD components have been upgraded to Version 10.0 on all participating hosts. Running WebLOAD Console Version 10.0 with an earlier version of Load Generator (running on different Hosts) may cause unexpected behavior. 
>
> The WebLOAD license file is limited to the computer system (machine) on which WebLOAD is initially installed. Before installing WebLOAD, make sure you are installing on the machine with which you intend to work. 
>
> When installing WebLOAD with Unicode support on a system running an English MS Windows, Japanese must be configured as the default Windows language.





## Installing WebLOAD for Windows

This chapter provides step-by-step instructions for installing WebLOAD on a PC running Windows systems. 

### Installing WebLOAD for Windows 

You can choose either of the following installation methods: 

- [*Command Line Installation* ](#command-line-installation)
- [*Using the Installation Wizard* ](#using-the-installation-wizard)

#### Command Line Installation

To perform a command line installation, run the following command: 

`< WebLOAD executable installation file > [flags]` 

Where the flags (case sensitive) are: 

| Option                          | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| /SILENT                         | Silent mode                                                  |
| /DIR="`<destination  directory>`” | Destination directory                                        |
| /TYPE=Agent                     | Install a Load Generator only                                |
| /TYPE=Dashboard                 | Install the Web Dashboard only                               |
| /SERVICE                        | Install TestTalk as a service                                |
| /DOMAIN="`<domain name>`"         | The domain in  which to install for service installation     |
| /USERNAME="`<user  name>`"        | The user name for service  installation                      |
| /PASS="`<user password>`"         | The password of the service  installation                    |
| /MANUAL                         | How to start the  service. If not set, the service will start automatically |
| /NOCHECK                        | Do not check for a previous installation                     |



#### Using the Installation Wizard

When you install WebLOAD on your computer, the installation program asks you for the components to install. As part of the installation process, WebLOAD installs a database management system (PostgreSQL) for use with WebLOAD Analytics. For more information about PostgreSQL, refer to[ www.postgresql-support.de.](http://www.postgresql-support.de/) 

Install the WebLOAD components as follows: 

- Install the full WebLOAD product on computers that will be used to run the WebLOAD Console. 
- Install only the Load Generator or the Probing Client software on a computer that will be a dedicated Load Machine. There is no need to install the full product on computers that will be used as Load Machines. 

**To install WebLOAD on your system:** 

1. Browse to the location of the WebLOAD executable (`*.exe`) installation file. 
1. Double-click the file. The WebLOAD Installation Wizard appears. 
1. Follow the instructions in the Installation Wizard. 
1. In the Select Components screen. 
    - Select the type of installation. For Load Machines and Probing Clients, select **Load Generator only**. 
    - Specify whether to install the **Load Generator As Service**.  
         - If you select this option, TestTalk is installed as a service. Since a service can be started automatically, this is especially useful for machines that serve only as Load Generators.  
         - If you do not select this option, TestTalk is installed as an executable file. 
    - Specify whether to also install the WebLOAD Cloud. The Web Cloud enables viewing, analyzing and comparing load sessions in a web browser, with full control and customization of the display. 

> **Note:** The installation process is the same for Load Machines and Probing Clients. When the WebLOAD installation is complete, the WebLOAD License dialog box automatically opens to complete the registration process. License registration is discussed in [Registering and Updating the WebLOAD License](#registering-and-updating-the-webload-license). 



### Installing WebRM

**To install WebRM:** 

1. Browse to the location of the `WebRM-10.0.xxx.en.exe` installation file. 

2. Double-click the file. The WebRM Installation Wizard appears. 

3. The WebRM Installation Wizard displays the Select Destination Location dialog box. On the Select Destination Location dialog box, browse to the location where you would like WebRM installed. By default, this location is `C:\Program Files\RadView\WebRM`. 

4. Click **Next**. 

5. The WebRM Installation Wizard displays the Select License Location dialog box. This dialog box displays your HostID and enables you to browse to the License location. 

     **Note:** If you have already received your WebRM License file, skip to step 8.

6. If you have not received your License file, copy the HostID displayed in the text box into an email, together with your name, company, address, and phone number. Send the email to [support@radview.com.](mailto:support@radview.com) 

    A WebRM license file (`*.lic`) will be sent to you.  

7. After receiving the file, save it on the hard drive of your WebRM machine and then double-click the WebRM executable installation file to restart the installation process. 

8. On the Select License dialog box, browse to the location where you saved your WebRM license, select the file and click **Next.**

    ![WebRM Installation Wizard – Select Start Menu Folder](images/webrm_installation_select_start.png)



10. WebRM begins the installation. When the WebRM installation process is complete, a dialog box appears stating that the WebRM installation has completed successfully. Click **Finish**. 

    

#### Upgrading WebLOAD

**To upgrade WebLOAD:** 

1. Close TestTalk. 
1. Close all browser windows that are open.  
1. Uninstall the existing WebLOAD version. 

    For instructions on the uninstall procedure, see [*Uninstalling WebLOAD*](#uninstalling-webload). 

4. Install the new version of WebLOAD. 

    For installation instructions, see [*Installing WebLOAD for Windows*](#installing-webload-for-windows). 
   
   

### Installing and Configuring the WebLOAD Analytics

WebLOAD stores information from Load Sessions in a Postgre SQL database for use with WebLOAD Analytics. You can install Postgre SQL and the WebLOAD Analytics database during the WebLOAD installation or manually after WebLOAD has already been installed. You might want to perform manual installation in the following situations: 

- If Postgre SQL is already installed on your machine and you only need to create the WebLOAD Analytics database. For instructions, refer to [*Creating the Database when Postgre SQL is Already Installed*](#creating-the-database-when-postgre-sql-is-already-installed). 
- If you want to use a different machine as the database server and have several WebLOAD Analytics applications connect to the database. For instructions, refer to [*Installing and Configuring the Database on a Dedicated Machine* ](#installing-and-configuring-the-database-on-a-dedicated-machine). 

#### Creating the Database when Postgre SQL is Already Installed

If Postgre SQL is already installed on your machine, you do not have to reinstall it during the WebLOAD installation. However, you must complete the following steps in order to create the WebLOAD Analytics database in Postgre SQL so that it can be used by WebLOAD Analytics. 

**To create the WebLOAD Analytics database after WebLOAD was installed:** 

- Run `deploy–database.bat` from the `C:\Program Files\RadView\WebLOAD\bin\database` folder. 



#### Installing and Configuring the Database on a Dedicated Machine

You can run the Postgre SQL database using a dedicated machine with several WebLOAD Analytics client applications. 

**To install and configure the database on a dedicated machine:** 

1. Install Postgre SQL.  

    > **Note:** It is recommended to install Postgre SQL Version 13. You can download the application from [http://www.postgresql.org/download/ ](http://www.postgresql.org/download/)and install it using its default installation settings. 

2. Copy all the files from the `C:\Program` `Files\RadView\WebLOAD\bin\database` directory to a temporary folder on the dedicated server. 

3. Run `deploy–database.bat` from the temporary folder to which you copied the files in the previous step. The WebLOAD Analytics database is created. 

4. Configure Postgre SQL to allow remote connections. For more information, see [*Configuring Postgre SQL to Allow Remote Database Connections*](#configuring-postgre-sql-to-allow-remote-database-connections).  

5. Configure the relevant WebLOAD Analytics clients to work with the remote database. For more information, see [*Configuring Clients to Work with the Remote Database*](#configuring-clients-to-work-with-the-remote-database). 

   

### Configuring Postgre SQL to Allow Remote Database Connections

For WebLOAD Analytics clients to work with the remote database, you must perform the following configuration steps on the host machine.  

**To configure a remote database connection through Postgre SQL:** 

1. Run **Start** > **PostgreSql** > **PgAdmin**. The PgAdmin application opens. 
1. Edit the `postgresql.conf` file, as follows: 
    1. Select **File** > **Open**.  
    1. Browse to `C:\program files\Postgres\Data\`, select `postgresql.conf`, and click **Open**. The `postgresql.conf` configuration file opens. 
    1. Change the value of listen\_address to \*. This configures the server to listen to all addresses. 
    1. Enable the value and save the file. 

3. Edit the `Pg_hba.conf` file, as follows: 
    1. Select **File** > **Open**.  
    1. Browse to `C:\program files\Postgres\Data\`, select `Pg_hba.conf`, and click **Open**. The `Pg_hba.conf` configuration file opens. 
    1. Add a new entry with the following parameters:
          - Type = host 
          - Database = all 
          - User = all 
          - IP address = `<IP subnet mask>`.0.1.1/24, where `<IP subnet mask>` is your organization’s IP subnet mask. 
          - Method = md5 
    1. Enable the entry and save the file. 




### Configuring Clients to Work with the Remote Database

**To configure a remote database connection through Postgre SQL:** 

1. Open WebLOAD Analytics on the client machine. 

1. Select **Window** > **Preferences** > **Database**. 

1. Enter the server’s IP address and name in the Database host name field. 

1. Click **OK**. 

   

### Installing Third Party Software for Server-side Monitoring

WebLOAD Console provides a Performance Measurements Manager (PMM) for monitoring the performance of various data sources such as server-side applications, databases, stream technology, system, and Web server measurements in real-time while your test is running. 

Some data sources require initial configuration to enable monitoring by the PMM. For more information, see the *Enabling Data Sources Monitoring* section in the *WebLOAD Console User’s Guide*. 



## Installing WebLOAD for Linux


This chapter contains the instructions for installing the WebLOAD Load Engine on a machine running a Linux operating system. 

### Installing the WebLOAD Load Engine for Linux 

**To install the WebLOAD Load Engine on your system:** 

1. Select or create a directory for installing the WebLOAD Load Engine. This directory will be referred to as the working directory. 
1. Download the `WebLOAD-linux.version.tar.gz` compressed file from a server to the working directory. 
1. Uncompress and extract the `tar` file in the working directory using the following command: 

    `tar –zvxf WebLOAD-linux-version.tar.gz`

1. Change directories by typing the following: 

    `cd radview/webload<version number>/linux/bin`

1. Run setup by typing the following: 

    `./setup` 

    During the setup process, the `webload.ini` configuration file is created. 

1. When prompted, enter the path to the Java runtime libraries. The default path to the libraries is displayed. If you are working with a different version of Java, enter the path of the libraries using the following: 

    `/usr/java/jre/lib/i386/server:/usr/java/jre/lib/i386/native-threads`  

    The path information is stored in the `LD_LIBRARY_PATH` variable. 

> **Note:** The directories containing the Java libraries are separated with a colon (:). 


> **Important:** The WebLOAD Load Generator will not function properly without the correct paths for the Java libraries. 



### Running the Load Engine on Linux

When running the Load Engine on Linux, Load Engine runs with TestTalk. TestTalk enables communication between the different components of the WebLOAD module. When running the Load Generator through Linux you generally need to connect with other WebLOAD modules running on a remote Windows machine (for example WebLOAD Console). To connect with these remote modules, you must run TestTalk. Once TestTalk is running, you can access the remote WebLOAD modules. The remote module then initiates the communication with TestTalk and then TestTalk loads the Load Generator. 

> **Note:** If the Load Generator is running and TestTalk is not running, the remote  WebLOAD application will not be able to access the Load Generator. 

**To run TestTalk on your system:** 

1. Open the `linux/bin` directory within your working directory by typing the following: 

    `cd <working-directory>/linux/bin` 

2. Run TestTalk by typing the following: 
    `./starttestalk` 

    TestTalk starts running. 

**To stop running TestTalk:** 

- From the `linux/bin` directory, run `./stoptesttalk`  

### Installing Third Party Software for Server-side Monitoring

WebLOAD Console provides a Performance Measurements Manager (PMM) for monitoring the performance of various data sources such as server-side applications, databases, stream technology, system, and Web server measurements in real-time while your test is running. 

Some data sources require initial configuration to enable monitoring by the PMM. For more information, see the *Enabling Data Sources Monitoring* section in the *WebLOAD Console User’s Guide*. 



## Registering and Updating the  WebLOAD License 

Your WebLOAD license must be registered before you can start working with WebLOAD. WebLOAD licenses that have expired must also be renewed or updated before you can continue working with WebLOAD. When installing a new major or minor version of WebLOAD, make sure that you have an adequate license for that specific version. All license registration and updating is accomplished through the Update License dialog box. 

You can register and update your WebLOAD license either through an Update License application, or through the Command Line Interface. 

### License administration through the UI

### Standard License Registration

**To open the Update License dialog box:** 

- At the time of WebLOAD installation, when the WebLOAD Installation Wizard is finished, the** License** dialog box opens automatically, 

    **Note:** After a WebLOAD installation, you may be prompted to restart your computer before the Update License dialog box appears. In this case, the License dialog box will appear automatically after the computer restarts. 

    -Or- 

    At any other time, from the Windows desktop, select **Start** > **Programs** > **RadView** > **WebLOAD** > **Utilities** > **Update License**. 

The License dialog box includes the following sections: 

- License Details 
- Update License 

These sections are used to register and update your WebLOAD authorization license information. 

**To complete or update your license registration:** 

1. If you are registering a new license after an initial WebLOAD installation, access the Update License dialog box. The Update License dialog box is opened automatically after a successful WebLOAD installation is completed. 

    -Or- 

    If you are updating your license registration after your current license has expired, from the Windows desktop, select **Start** > **Programs** > **RadView** > **WebLOAD** > **Utilities** > **Update License**. 

    The Update License dialog box appears. 
   
    ![Update License Dialog Box](images/update_license.png)

1. Create an email message with the following information: 
    1. Copy the Host ID displayed in the text box into the email. 
    1. Add your name, company, address, and phone number to the email message. 
1. Send the email to [license@radview.com](mailto:license@radview.com) 
    
     A WebLOAD license file (`*.lic`) will be sent to you. 

1. Select **Start** > **Programs** > **RadView** > **WebLOAD** > **Utilities** > **Update License** to open the Update License dialog box and install the license key. 
1. By default, the **Use a license file** radio button is selected. This assumes that your license file is located on your local computer system. 

    For information on installing a floating license, or connecting to a license server, see [*WebRM Server* ](#webrm-server). 

    For information on installing a license for an evaluation of WebLOAD, see [Trial License ](#trial-license). 

1. Click the browse button next to the **Use a license file** text box to browse to the location of the license (`*.lic`) file sent to you by a RadView representative. 
1. Select the correct license file and click **Open** to return to the Update License dialog box. 
1. Click **OK** to load the new license. 

    If the license registration was successful, a message box appears indicating a successful license update. 

    You can now begin working with WebLOAD. 
   
   

> **Note:** After loading the license, you can optionally click **License Information** to view the license’s full details.

If the license registration was not successful, an error message appears. 

If you are not able to successfully register a valid license file, contact RadView Support for assistance. 

### Trial License

You can install a trial version of WebLOAD, which provides 50 virtual clients, and is available for 30 days. 

**To use the WebLOAD evaluation:** 

1. After installing WebLOAD, the Update License dialog box opens,  
    
    -Or- 

    To open the Update License dialog box manually, select **Start** > **Programs** > **RadView** > **WebLOAD** > **Utilities** > **Update License.** 

    The Update License dialog box appears.

    ![Update License Dialog Box](images/30day_update_licesne.png)


1. Select **30-day trial**. 
1. Click **OK** or **Apply** to install the license for the trial. 

   You can now begin working with the trial version of WebLOAD. 

### WebRM Server

The WebRM Server is a stand-alone tool that manages all resource distribution to WebLOAD Console, which is the machine used to run loads in a WebRM environment. It is the method that controls the number of users allowed to access the product concurrently. 

WebRM for virtual clients is available and defined as a pool of virtual (probing) clients that can concurrently be used by members of a testing team and monitored by the WebRM Server. 

During installation of the WebRM server, you are prompted for the WebRM file that defines: 

- The number of concurrent applications for the WebLOAD Console. 
- The number of concurrent Virtual and Probing Clients. 

Installation also creates a FlexLM Service that controls the operation. 



The WebRM Server displays a list of the number of resources (Virtual and Probing Clients) that the Console is using. The WebRM Server enables a testing team to share resources. 

This section describes how to connect to the WebRM Server and how to view the license details. 

***Connecting to the WebRM Server***
**To connect to the WebRM Server:** 

1. After installing WebLOAD, the Update License dialog box opens, 

    -Or- 

    To open the Update License dialog box manually, select **Start** > **Programs** > **RadView** > **WebLOAD** > **Utilities** > **Update License.** 
   
    The Update License dialog box appears. 

    ![Update License Dialog Box – WebRM Server Installation](images/update_license_webrm.png)


1. Select **Connect to the WebRM License Server**. 
1. Click the **Browse** button and select the machine where WebRM is installed. 
1. Click **OK**. 



A connection to the selected license server is attempted. 

- If the connection is successful, a success message appears. 
- If the connection is not successful, a failure message appears. 

***Viewing License Details*** 

After selecting the license server, you can view the current license details in the License Details section of the Update License dialog box.  

### License administration through the Command Line Interface

You can register or upload a WebLOAD license through a command line interface. You can enter the wlUpdateLicenseApplicationCmd command into a batch file or into an external script to automatically launch a WebLOAD License action, without user intervention, using the parameters you specify. 


## TestTalk Setup Instructions

### Configuring `testtalk.ini`

The following settings are included by default in the `testtalk.ini` configuration file.
You may customize them as needed:

```ini
UseOpenSsl=1
CertificatesPath="path/to/certificates"
VerifyServerCertificate=1
VerifyClientCertificate=1
```

- **UseOpenSsl**: Enables OpenSSL for SSL/TLS if set to `1`. If set to `0`, OpenSSL is disabled.
- **CertificatesPath**: Directory path containing your certificates.
  - Default on **Windows**: `C:\ProgramData\Radview\WebLOAD\certificates\testtalk`
  - Default on **Linux**: `~/radview/webload13.3.0/linux/certificates/testtalk`
- **VerifyServerCertificate**: Set to `1` to enable server certificate verification.
- **VerifyClientCertificate**: Set to `1` to enable client certificate verification.

> **Note:** Certificate files are installed by default. You can point `CertificatesPath` to a different folder if needed.

---

### Required Certificate Files

Ensure the following files exist in your certificates directory:

- `ca.crt`: CA public certificate.
- `ca.key`: CA private key.
- `ca_bundle.crt`: Copy of the CA certificate.
- `server.crt`: Server public certificate.
- `server.key`: Server private key.
- `server.csr`: Server Certificate Signing Request.
- `client.crt`: Client public certificate.
- `client.key`: Client private key.
- `client.csr`: Client Certificate Signing Request.

---

### Script: `generate_certificates.sh`

Use this script to generate all required certificates.

```bash
#!/bin/bash

# Configurable variables for CA subject details
CA_COUNTRY="AU"
CA_STATE="Some-State"
CA_LOCALITY="City"
CA_ORGANIZATION="MyCompany"
CA_ORGANIZATIONAL_UNIT="IT"
CA_COMMON_NAME="MyTestCA"

# Configurable variables for Server subject details
SERVER_COUNTRY="AU"
SERVER_STATE="Some-State"
SERVER_LOCALITY="City"
SERVER_ORGANIZATION="MyCompany"
SERVER_ORGANIZATIONAL_UNIT="IT"
SERVER_COMMON_NAME="127.0.0.1"

# Configurable variables for Client subject details
CLIENT_COUNTRY="AU"
CLIENT_STATE="Some-State"
CLIENT_LOCALITY="City"
CLIENT_ORGANIZATION="MyCompany"
CLIENT_ORGANIZATIONAL_UNIT="IT"
CLIENT_COMMON_NAME="MyClient"

# Other configuration variables
CA_KEY="ca.key"
CA_CERT="ca.crt"
SERVER_KEY="server.key"
SERVER_CSR="server.csr"
SERVER_CERT="server.crt"
CLIENT_KEY="client.key"
CLIENT_CSR="client.csr"
CLIENT_CERT="client.crt"
SERIAL_FILE="ca.srl"
CERT_VALIDITY_DAYS=3650

# Construct the subject strings
CERT_SUBJECT_CA="/C=$CA_COUNTRY/ST=$CA_STATE/L=$CA_LOCALITY/O=$CA_ORGANIZATION/OU=$CA_ORGANIZATIONAL_UNIT/CN=$CA_COMMON_NAME"
CERT_SUBJECT_SERVER="/C=$SERVER_COUNTRY/ST=$SERVER_STATE/L=$SERVER_LOCALITY/O=$SERVER_ORGANIZATION/OU=$SERVER_ORGANIZATIONAL_UNIT/CN=$SERVER_COMMON_NAME"
CERT_SUBJECT_CLIENT="/C=$CLIENT_COUNTRY/ST=$CLIENT_STATE/L=$CLIENT_LOCALITY/O=$CLIENT_ORGANIZATION/OU=$CLIENT_ORGANIZATIONAL_UNIT/CN=$CLIENT_COMMON_NAME"

# Clean up any previously generated files
rm -f $CA_KEY $CA_CERT $SERVER_KEY $SERVER_CSR $SERVER_CERT $CLIENT_KEY $CLIENT_CSR $CLIENT_CERT $SERIAL_FILE

# Step 1: Generate the CA private key
openssl genrsa -out $CA_KEY 2048

# Step 2: Create a self-signed CA certificate
openssl req -x509 -new -nodes -key $CA_KEY -sha256 -days $CERT_VALIDITY_DAYS -out $CA_CERT -subj "$CERT_SUBJECT_CA"

# Step 3: Generate the server private key
openssl genrsa -out $SERVER_KEY 2048

# Step 4: Create a CSR for the server
openssl req -new -key $SERVER_KEY -out $SERVER_CSR -subj "$CERT_SUBJECT_SERVER"

# Step 5: Sign the server CSR with the CA to create the server certificate
openssl x509 -req -in $SERVER_CSR -CA $CA_CERT -CAkey $CA_KEY -CAcreateserial -out $SERVER_CERT -days $CERT_VALIDITY_DAYS -sha256

# Step 6: Generate the client private key
openssl genrsa -out $CLIENT_KEY 2048

# Step 7: Create a CSR for the client
openssl req -new -key $CLIENT_KEY -out $CLIENT_CSR -subj "$CERT_SUBJECT_CLIENT"

# Step 8: Sign the client CSR with the CA to create the client certificate
openssl x509 -req -in $CLIENT_CSR -CA $CA_CERT -CAkey $CA_KEY -CAcreateserial -out $CLIENT_CERT -days $CERT_VALIDITY_DAYS -sha256

# Step 9: Verify the server and client certificates
echo "Verifying server certificate..."
openssl verify -CAfile $CA_CERT $SERVER_CERT
echo "Verifying client certificate..."
openssl verify -CAfile $CA_CERT $CLIENT_CERT

# Copy the CA certificate to the bundle
cp ca.crt ca_bundle.crt

# Output the results
if [ $? -eq 0 ]; then
  echo "All certificates generated and verified successfully:"
  echo "CA Certificate: $CA_CERT"
  echo "Server Certificate: $SERVER_CERT"
  echo "Client Certificate: $CLIENT_CERT"
else
  echo "Error: Certificate verification failed."
fi
```

---


### Important Notes

- **Secure Your Keys:** Keep `ca.key`, `server.key`, and `client.key` safe.
- **Backup Before Running Script:** The script will overwrite existing certificates.
- **Update Certificates Regularly:** Renew certificates before expiration.

## Uninstalling WebLOAD

When you uninstall WebLOAD, you are prompted to remove PostgreSQL .3, which is used to manage the WebLOAD Analytics database. RadView Software recommends that you keep PostgreSQL installed in order to maintain all the information stored in the database. 

**To uninstall WebLOAD:** 

1. Close all WebLOAD modules including TestTalk. 
1. Close all browser windows that are open.  
1. Select **Start** > **Settings** > **Control Panel**. 
1. Double-click the **Add/Remove Programs** icon. 
1. Click the **Change or Remove Programs** tab. 
1. Click **Radview WebLOAD Professional**, and then click **Change/Remove**. 

   The Uninstall Wizard appears. Once the uninstall procedure is complete, you may be prompted to restart your machine. 

> **Note:** Uninstalling WebLOAD removes all the WebLOAD program file directories, including all the WebLOAD installation files. User files that are copied into these directories (such as user-defined extensions) are not deleted. WebLOAD load templates, load sessions, and script files are not removed – they can be used with all WebLOAD upgrades.

> **Caution:** Close TestTalk and all browser windows before uninstalling WebLOAD. Failure to close TestTalk and all browser windows results in outdated files remaining on your disk, which could adversely affect future installations of the program. 
>

**To uninstall WebRM:** 

1. Select **Start** > **Settings** > **Control Panel**. 

1. Double-click the **Add/Remove Programs** icon. 

1. Click the **Add or Remove Programs** tab. 

1. Click **RadView WebRM**, and then click **Change/Remove**.

   The Uninstall Wizard appears. The uninstall procedure is completed following a confirmation request. 


## Sizing WebLOAD Load Generators

When defining a load test, you need to assign Load Generator machines to execute the scripts, send requests, and receive responses.  How many load generators do you need?  

### Start with our “Rule of Thumb”

Radview has found that a standard machine can support about 500 virtual users when running an average script.  A “standard machine” has two CPUs and 6 to 8 gigabytes of RAM and a gigabit NIC card.  The “average script” is harder to define, see note below.  

### Scaling Tests - estimate your scaling factor

**Limiting Factor:** For a standard machine, the limiting resource is usually CPU.  We use a CPU utilization target of 80%.  A one-CPU machine should probably use a CPU utilization target of 70% to 75%.  A machine with 8 or more CPUs should probably use a target of 90%.  When you use very large load generator machines, CPU may not be the limiting factor – you may find that memory or network capacity are the limiting factors.  

**Procedure:** Allocate an external machine, install WebLOAD load generator on it.  Define and run a test with 500 virtual users on that load generator and see what happens.  Open your session in the WebLOAD console and display the load generator memory utilization.  The default Radview scaling factor is: each virtual user should use about 0.16 percent of the CPU. 

 -	If CPU is about 80% then you have an “average script” and our “rule of thumb” is a good fit for you.  Your factor is 80 divided by 500 or 0.16.
 -	If CPU is about 90% then your script is a little heavy and your rule of thumb for this script is about 450 VUs per standard machine.  Your scaling factor is 90 / 500 or 0.18.
 -	If CPU is about 70% then your script is on the lighter side and you rule of thumb for this script is about 600 VUs per standard machine.  Your scaling factor is 70 / 500 or 0.14. 

**Over 100% result:** If your test ran the load generator at 100 percent then you have no measure of the actual CPU demand, you only know that it is more than 100 percent.  Rerun the test with a smaller number of users (maybe 250 virtual users) and calculate your factor from there.  Suppose you reran with 250 users and got 80% CPU – your factor would be 80 / 250 or 0.32.

**Using the scaling factor:** Once you have your scaling factor, you can estimate how many virtual users a given machine can support.  Just divide 80 by your factor.  For example, suppose that you had a factor of 0.1.  80 divided by 0.1 equal 800 so a standard machine should support about 800 virtual users.  Suppose you had a factor of 0.25.  80 divided by 0.25 equals 320 virtual users. 

**Estimating number of load generators:** suppose a scaling factor of .22 and you want to run a 5,000 VU test.  80 divided by .22 equals 363.  Let us round that so one standard machine will support about 350 virtual users.  5,000 divided by 350 equals 14.28 – call that 15 machines.  Maybe you don’t want to use our standard machines or you want fewer load generators.  Let us make a guess that a machine with 4 CPUs and 16 GB of RAM will support twice as many users.  You could do a trial run with 8 load generators each with 4 CPUs and 16 GB of RAM and see how you do.

**Scaling options:** You can run a smaller test in order to estimate your factor – say, 50 virtual users instead of 500.  Keep in mind that the results from a very small test (say 10 virtual users) will contain a lot of operating system overhead.  If you use that to compute your factor you will end up with too-large load generators.  Your factor-determining test should use at least 25% of the CPU, more is better.  

**Non-standard machines:** You may want to run scaling tests for machines that are different from our “standard machine”.  The technique works, you get different factors.  Keep in mind, if you use a very large machine, you may want to use 90 percent as your target CPU and check for other limiting resources. 

**Other limiting factors:** This technique works well for CPU but does not take into account memory or network traffic.  You can use the same technique with memory and network but the utilization targets are different.  

**Average Script**: It is easier to talk about those characteristics that make a script “not average”.  

   - High memory usage
   - High CPU usage
   - Short to zero sleep times
   - Complex – usually goes with high memory and CPU
   - Many simultaneous connections
