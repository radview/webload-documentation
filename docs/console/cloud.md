# Cloud Account Types and Their Properties

This document provides a detailed description of various cloud account types and their properties.

## AWS EC2 Cloud

- **Description**: AWS EC2 Cloud

### Parameters

#### Credentials

- **Access Key (String; Optional)**: AWS Access Key. Use 'aws' or blank to use default credentials. Default credentials will try to use: Environment variables, Java system properties, The default credential profiles file, Amazon ECS container credentials, Instance profile credentials.
- **Secret Access Key (Password)**: Secret Access Key matching the Access Key.

#### Region

- **Region Name (List; Required)**:
  - **Values**: us-east-1, us-west-1, us-west-2, eu-west-1, eu-west-2, eu-west-3, eu-central-1, ap-southeast-1, ap-southeast-2, ap-northeast-1, sa-east-1, af-south-1
  - **Default**: us-east-1
  - **Description**: AWS Region to run the instance.

#### Instance

- **Instance Type (String)**: Default is `c5.large`. Machine size to launch. Type needs to be available in the selected region and may have limitations like requiring VPC.
- **Subnet Id (String)**: SubnetId. Required when using VPC. For example: subnet-60e6945c. Subnet should auto-assign a public IPv4 address.

### Advanced Parameters

- **Security Group Id (String)**: Security group id, allowing access from the console on ports 9000, 9010, 21, 10090-10100. If not specified, a 'RadView' security group will be created if it does not exist.
- **Use Elastic IP (String)**: Default is `false`. If `true`, WebLOAD will allocate an elastic-ip to this instance if one is available.
- **Use Private IP (String)**: Default is `false`. If `true`, WebLOAD will use the instance private-ip, not public-ip. This works only in a VPC environment where the console machine can access the load-generator.
- **Custom Tag List (String)**: Custom tags to add to instance. Example: `tag1=value1;tag2=value2`.
- **Image Id (String)**: Default is `Default`. Custom AMI ID expected to have WebLOAD configured and running.
- **Spot Price (String)**: Launches instance as a spot request. Note: Spot instances depend on pricing and capacity and may be terminated without notice if the price goes up.

## AWS EC2 Cloud (Dynamic)

- **Description**: AWS EC2 Cloud (Dynamic) - supports all regions by installing WebLOAD upon launch. Users must select an appropriate region and machine type.

### Parameters

#### Credentials

- **Access Key (String; Optional)**: AWS Access Key. Use 'aws' or blank to use default credentials. Default credentials will try to use: Environment variables, Java system properties, The default credential profiles file, Amazon ECS container credentials, Instance profile credentials.
- **Secret Access Key (Password)**: Secret Access Key matching the Access Key.

#### Region

- **Region Name (String; Required)**:
  - **Default**: us-east-1
  - **Description**: AWS Region to run the instance.

#### Instance

- **Instance Type (String)**: Default is `c5.large`. Machine size to launch.
- **Image Id (String)**: Default is `amzn2-ami-kernel-5.10-hvm-2.0.20240412.0-x86_64-gp2`. Base AMI expected to support CloudInit.

### Advanced Parameters

- **Init Script (String)**: Default is `cloud_init.sh`. Path to the script file to run when starting the instance. This script is expected to install and start WebLOAD. File must be in UNIX format.
- **Download File Name (String)**: Default is `WebLoad-linux-v${VERSION}.${BUILD}.tar.gz`. Used by init-script for file download.
- **Download URL (String)**: Default is `https://radview.s3.amazonaws.com/`. Path for downloading installation during initialization.

## Azure Cloud

- **Description**: Microsoft Azure Cloud

### Parameters

#### Credentials

- **Identity (String; Required)**: Can be found in Azure Portal under Azure Active Directory > App registrations > Application ID.
- **Credentials (Password; Required)**: The password value generated in Azure Active Directory > App registrations > Keys.

#### Tenant and Subscription

- **Tenant Id (String; Required)**: Can be found in Azure Portal under Azure Active Directory > Properties > Directory ID.
- **Subscription Id (String; Required)**: Can be found in Azure Portal under Cost Management + Billing > Subscriptions.

#### Region

- **Region Name (List; Required)**:
  - **Values**: eastasia, southeastasia, centralus, eastus, eastus2, westus, northcentralus, southcentralus, northeurope, westeurope, japanwest, japaneast, brazilsouth, australiaeast, australiasoutheast, southindia, centralindia, westindia, canadacentral, canadaeast, uksouth, ukwest, westcentralus, westus2, koreacentral, koreasouth, francecentral
  - **Default**: westus2
  - **Description**: Region to run the instance.

### Advanced Parameters

- **Instance Spec (String)**: Default is `osFamily=CENTOS,osVersionMatches=8.3`. Specification query for instance.
- **Image Publishers (String)**: Default is `OpenLogic`. Filters images based on publishers.
- **Oauth Endpoint (String)**: Custom endpoint URL if required.
- **Hardware Id (String)**: Specific hardware ID to use. Example: `westus2/Standard_D2as_v4`. Use 'list' to get options.

## Google Compute Engine Cloud

- **Description**: Google Compute Engine. Create a project in [Google Console](https://console.developers.google.com/); enable the Google Compute Engine API under APIs and auth > APIs; create new Client ID as Service Account; download a JSON key and note the email address as identity.

### Parameters

#### Credentials

- **Identity (String; Required)**: Identity is the service account email address.
- **Credentials Path (Password; Required)**: Path to the service account client ID JSON Key file.

#### Region

- **Region Name (List; Required)**:
  - **Values**: asia-east1-a, asia-northeast1-a, asia-south1-a, asia-southeast1-a, australia-southeast1-a, europe-north1-a, europe-west1-b, europe-west2-a, europe-west3-a, europe-west4-a, northamerica-northeast1-a, southamerica-east1-a, us-central1-a, us-east1-b, us-east4-a, us-west1-a, us-west2-a
  - **Default**: us-west1-a
  - **Description**: Region to run the instance.

#### Instance

- **Min Cores (String)**: Default is `2`. Minimum number of CPU cores the machines should have.
- **Min RAM (String)**: Default is `8000`. Minimum RAM in megabytes the machines should have.
- **Min Disk Size (String)**: Minimum disk size in gigabytes the machines should have.

### Advanced Parameters

- **Instance Spec (String)**: Default is `osFamily=CENTOS,osVersionMatches=8`. Specification query for instance.
- **Hardware Id (String)**: Specific hardware ID to use. Use 'list' to get the available options.
- **Credentials Out Path (String)**: When set, WebLOAD will store the access credentials in the specified path.
- **Location Id (String)**: Location inside the region to use.
- **Endpoint URL (String)**: Custom endpoint URL if required.
- **Network (String)**: Network to use.
- **Init Script (String)**: Path to a script file to run when starting the instance. This script is expected to install and start WebLOAD. File must be in UNIX format.
- **Cloud Init (String)**: Default is `true`. Use cloud-init metadata to specify init-script; otherwise, connect using SSH and execute the script.
- **Public Key (String)**: Existing SSH public key to authorize.
- **SSH User (String)**: SSH user to use.
- **SSH Password (String)**: SSH password to use.
- **Private Key Path (String)**: Path to the SSH private key to use.
- **Key Name (String)**: Key name to use for SSH Key pair access.
- **Sudo Command (String)**: Default is `sudo`. Command to use when needing to run as root.
- **Sh-Bang (String)**: Default is `#!/bin/bash`. The init script's first line.
- **Download File Name (String)**: Default is `WebLoad-linux-v${VERSION}.${BUILD}.tar.gz`. Used by the init script to download files.
- **Download URL (String)**: Default is `https://radview.s3.amazonaws.com/`. Used by the init script as the path to download installation files.
- **Async (String)**: Default is `true`. If `true`, the machines will start asynchronously.
- **Selenium Support (String)**: Default is `false`. If `true`, install Google Chrome for Selenium support.
- **Security Group Id (String)**: Security group that allows access from the console on ports 9000, 9010. Created on the fly if not specified.

## Amazon ECS Cloud

- **Description**: Amazon Elastic Container Service (ECS) facilitates containerized application deployment and management.

### Parameters

#### Credentials

- **Access Key (String; Optional)**: AWS Access Key for authentication.
- **Secret Access Key (Password; Optional)**: Matches the Access Key for secure authentication.

#### Region

- **Region Name (List; Required)**:
  - **Values**: Includes various global regions for deploying ECS resources.
  - **Default**: us-east-1
  - **Description**: Defines the deployment region for containerized resources.

#### Instance

- **Subnet Id (String)**: Specifies the subnet for deploying ECS tasks.
- **Cluster (String)**: Default is `default`. Specifies the ECS cluster for resource allocation.
- **CPU (String)**: Default is `2 vCPU`. Configures the number of virtual CPUs.
- **Memory (String)**: Default is `4 GB`. Specifies memory allocation for tasks.

### Advanced Parameters

- **Security Group Id (String)**: Defines security settings for task access.
- **Execution Role (String)**: Default is `ecsTaskExecutionRole`. Specifies the role granting API permissions for ECS tasks.
- **Image Id (String)**: Default is `Default`. Indicates a custom Docker image.
- **Custom Tag List (String)**: Allows custom tagging of ECS tasks for better organization.
- **Proxy Configurations (Multiple Parameters)**: Defines proxy-related configurations for network setups.

## Generic Cloud (Jclouds-based)

The Jclouds-based Generic Cloud supports various cloud providers and offers flexibility for configuring and managing cloud instances. The cloud implementation allows for interoperability across multiple cloud platforms, including AWS, Azure, Google Compute Engine, and others.

### Parameters

#### Cloud Provider
- **Provider (String; Required)**
  - **Default Value**: `aws-ec2`
  - **Description**: Specifies the cloud provider. Supported values include:
    - digitalocean2
    - elastichosts-lon-b
    - elastichosts-lon-p
    - elastichosts-sat-p
    - go2cloud-jhb1
    - gogrid
    - openhosting-east1
    - profitbricks
    - rackspace-cloudservers-uk
    - rackspace-cloudservers-us
    - serverlove-z1-man
    - skalicloud-sdg-my
    - softlayer
    - byon
    - cloudstack
    - docker
    - ec2
    - elasticstack
    - stub
    - openstack-nova
    - openstack-nova-ec2
    - aws-ec2
    - azurecompute
    - azurecompute-arm
    - google-compute-engine

#### Credentials

- **Identity (String; Required)**
  - **Description**: Represents the identity used for authentication, such as a username or AWS Access Key.

- **Credentials (Password; Required)**
  - **Description**: Password or Secret Access Key associated with the identity.

#### Region

- **Location (String; Required)**
  - **Default Value**: `us-east-1`
  - **Description**: Specifies the region or availability zone to use. Use `list` to retrieve the available options.

#### Instance

- **Min Cores (String; Required)**
  - **Default Value**: `2`
  - **Description**: The minimum number of CPU cores the machine should have.

- **Min RAM (String; Required)**
  - **Default Value**: `8000`
  - **Description**: The minimum amount of RAM (in MB) the machine should have.

- **Min Disk Size (String; Optional)**
  - **Description**: The minimum disk size (in GB) the machine should have.

### Advanced Parameters

#### Instance Configuration

- **Hardware Id (String; Optional)**
  - **Description**: Specifies the hardware ID to use. Use `list` to get available options.

- **EC2 AMI Query (String; Optional)**
  - **Default Value**: `owner-id=137112412989;state=available;image-type=machine`
  - **Description**: Filters AMIs based on the specified query. Defaults to Amazon-created AMIs.

- **Instance Spec (String; Optional)**
  - **Default Value**: `osFamily=AMZN_LINUX,imageNameMatches=amzn-ami.*,minCores=1`
  - **Description**: Specification query for the instance.

- **Credentials Out Path (String; Optional)**
  - **Description**: Path to store access credentials generated during setup.

- **Endpoint URL (String; Optional)**
  - **Description**: Custom endpoint URL, if required.

- **Init Script (String; Optional)**
  - **Description**: Path to a script file executed during instance initialization. This script is expected to install and configure services. Files must be in UNIX format.

- **Cloud Init (String; Optional)**
  - **Default Value**: `false`
  - **Description**: When set to `true`, uses cloud-init metadata to specify the init script. Otherwise, connects using SSH to execute the script.

#### Authentication

- **Public Key (String; Optional)**
  - **Description**: An existing SSH public key to authorize.

- **SSH User (String; Optional)**
  - **Default Value**: `ec2-user`
  - **Description**: Specifies the SSH user for accessing the instance.

- **SSH Password (String; Optional)**
  - **Description**: Password for SSH access.

- **Private Key Path (String; Optional)**
  - **Description**: Path to the SSH private key for authentication.

- **Install Private Key Path (String; Optional)**
  - **Description**: Path to the private key to install for SSH access.

#### Additional Settings

- **Key Name (String; Optional)**
  - **Description**: Specifies the name of the SSH Key pair.

- **Download File Name (String; Optional)**
  - **Default Value**: `WebLoad-linux-v${VERSION}.${BUILD}.tar.gz`
  - **Description**: File name used for downloading during the initialization process.

- **Download URL (String; Optional)**
  - **Default Value**: `https://radview.s3.amazonaws.com/`
  - **Description**: URL path for downloading installation files.

- **Sh-Bang (String; Optional)**
  - **Default Value**: `#!/bin/bash`
  - **Description**: The first line of the initialization script.

- **Sudo Command (String; Optional)**
  - **Description**: Command used for running operations as root. Usually not required for AWS.

- **Async (String; Optional)**
  - **Default Value**: `true`
  - **Description**: When set to `true`, allows the machines to start asynchronously.

- **Selenium Support (String; Optional)**
  - **Default Value**: `false`
  - **Description**: When set to `true`, installs Google Chrome for Selenium testing support.

- **Security Group Id (String; Optional)**
  - **Description**: Security group allowing access from the console on ports 9000, 9010. Created dynamically if not specified.

- **Network (String; Optional)**
  - **Description**: Specifies the network configuration for the instance.