# 1. Foundation of Active Directory Domains

## 1.1 Domain Controller, Active Directory and Domain Name Service
- Domain Controller
  - Active Directory uses the database in the domain controller
  - Replicate between each other if redundancy is setup (2 or more DC are setup)
  - Authentication protocol : Kerberos, NTLM(Legacy)
  - Uses the Directory Service Language called LDAP (Lightweight Directory Access Protocol)

- Active Directory
  - All machines in the AD have to have a name and name must be associated with an IP address

- Domain Name Service (DNS)
  - DNS is the name of the domain you are using
  - Server that associate names and IP addresses
  - All machines in the domain will need to register themselves to DNS
    - Allows the centralization of Name Resolution
    - Meaning they register the IP addresses to DNS and anytime any other machine needs to find another machine, they can query the DNS for the address.

- For syncing of Entra ID with on-premises AD, we use a program called Entra Connect for syncing
  - It will only be a one way sync from on-premise AD to Entra ID

## 1.2 RAS (Remote Access Service)

- Server supports VPN connection by allowing encypted VPN tunnels to be created

## 1.3 DMZ (Demilitarized Zone) or Perimeter

![](images/2026-07-29-08-49-16.png)

- Zone between 2 firewalls which one of them faces outwards towards the WWW and the other faces inwards to the domain.

- Used mainly for applications that are open to the public 
- The first firewall which faces outwards towards the WWW will allow traffic only to the applications.
- The second firewall will prevent any users to access domain resources.
  - Only the application is allowed to access resources if needed.

## 1.4 IaaS, Infrastructure as a Service

- A service that provides infrastructure for a fee.
  - E.g. Instead of hosting web server at home, we can host the web server in Azure at a price per month.

- Some services offered for example:
  - VMs, Virtual Machines
  - vNETs, Virtual Networks
  - vStorage, Virtual Storages
  - Many Others

## 1.5 SaaS, Software as a Service

- A fully functional application / software ready for user usage.

## 1.6 PaaS, Platform as a Service

- Ready platform for admins to use but admins have to administer it.
- Platforms where admins need to go in to add users and set settings to make things work.
  - E.g. Entra ID where you need to add user permissions to access resources
  - E.g. Printer Server Webpage where you need to configure settings and add users so that they can print

<br>

# 2. Manage Microsoft Entra Users and Groups

## 2.1 Microsoft Entra Identities

- Multiple ways to manage Identities
  - Azure Portal
  - Microsoft 365 Admin Center
  - Entra Portal
  - On-Premise AD with account sync using Azure AD Connect
  - Powershell and Azure CLI

<<<<<<< HEAD
### 2.1.1 User Identities
=======
## 2.2 User Identities
>>>>>>> 20f0109138e0a2be60b1b8feffa929e437e9189d

- Human Users who access Microsoft services

- Member users :
  - Employees created directly in Entra ID or Active Directory

- Guest Users :
  - External users invited through B2B collaboration
  - Identity is managed but granted limited access

<<<<<<< HEAD
### 2.1.2 Service Principles
=======
## 2.3 Service Principles
>>>>>>> 20f0109138e0a2be60b1b8feffa929e437e9189d

- Represent application or services that need to authenticate and access resources
- Automatically created when an app is registered in Entra ID
- Used for assigning permissions, running automation or secure access without human interaction
  - E.g. Web app needs to read/write to Microsoft Graph or SQL 

- Main advantage is :
  - Application Authentication  : Ensures secure access for applications and services
  - Automated permissions       : Facilitates permission assignments without human intervention
  - Secure Access               : Provides secure resource access without human interaction

<<<<<<< HEAD
### 2.1.3 Managed Identities
=======
## 2.4 Managed Identities
>>>>>>> 20f0109138e0a2be60b1b8feffa929e437e9189d

- Special identities for Azure resources like VMs or Function Apps to access other Azure services securely
  > <b>Without Storing Credentials</b>

<br>

- There are 2 types
  - System assigned
    - Tied to one resource and lifecycle matches the resource

  - User assigned
    - Standalone identity resuseable across multiple reources
    - E.g. Azure VM accessing a storage account using system assigned identity

<<<<<<< HEAD
### 2.1.4 Difference between Service Principles and Managed Identities
=======
## 2.5. Difference between Service Principles and Managed Identities
>>>>>>> 20f0109138e0a2be60b1b8feffa929e437e9189d

- Service Principles are either created by user or registered by apps
  - Admins will managed the accounts like passwords and certificates
  - Can be used for logging on and authenticating with Azure 
  - Cen be used for external or 3rd party services

- Managed Identities have no need to manage any secrets or credentials
  - Only work within Azure, not for 3rd party services

<<<<<<< HEAD
### 2.1.5 Device Identities
=======
## 2.6 Device Identities
>>>>>>> 20f0109138e0a2be60b1b8feffa929e437e9189d

- Every Device that is joined to Entra ID gets an identity
- It is used for :
  - Conditional Access
  - Intune Management
  - Device Compliance

- Device can be joined by:
  - Entra ID joined   : Devices directly joined to Entra ID
  - Hybrid AD joined  : Devices are joined to on premises Active Directory
  - Entra ID registred: Devices are registered for BYOD

<<<<<<< HEAD
## 2.2 Groups in Entra ID

- Microsoft 365 Groups
  - Comprehensive suite for enhanced team productivity
  - Collaboration Ready which includes a shared mailbox, calender, SharePoint site, OneNote and Planner
  - Used as backbone for Microsoft Teams, enabling chat, meetings and file sharing
  - Supports Guest Access as external users can be added securely for collaboration
  - Membership can be assigned manually or dynamically based of user attributes by using dynamic rules
  - <b> This group cannot contain Device Identities </b>

- Distribution Groups
  - Used to send email messages to multiple recipents at once
      -  <b>There are no shared workspace or collaboration tools</b>
  - Membership can be static or dynamic
  - Primarily intended for internal announcements or department wide emails
  - Cannot be used to assign permissions to resources like SharePoint or Teams.
  - <b> Group has an email address and any mail sent to that email will be distributed to all the members of the Group </b>

- Mail Enabled Security Group
  - Has a group email address which can also be given permissions to resources
  - Used for both email distribution and assigning permissions to Microsoft 365 resrouces
  - Has a shared email address, allowing group members to receive messages like a distribution list
  - Can be used to manage access to SharePoint, OneDrive, Intune and other resources
  - <b>Has no collaboration Features</b>

- Security Group
  - Primarily used to assign permissions to resources like SharePoint sites, apps and Intune Policies
  - <b> Cannot send or receive email </b>
  - Can include users, devices and service principals for flexible management
  - Membership can be managed manually or through dynamic rules based on Entra ID attributes

### 2.2.1 Assigned vs Dynamic Groups
- Assigned Groups
  - Members are manually added or removed by an admin
- Dynamic Groups
  - Membership is based on rules
    - E.g. Department = "IT"
  - Users/Devices automatically added or removed as attribute change

<br>

# 3. Managing Azure using command line tools

## 3.1 Microsoft Graph

- A unified API endpoint for M365 and Azure Services
- Lets you access data from Entra ID, Teams, Outlook and more
- Works through a single endpoint
  > https://graph.microsoft.com
- Supports modern aythentication (OAuth 2.0)
- Enables automation, reporting and app intergration across services

## 3.2 Why Microsoft moved to Graph

- Unified access model reduces complexity
- Works across Windows, macOS and Linux
- Supports token based auth and conditional access
- Supports modern developer tools and automation
- Enables scalable, performant data access

## 3.3 Microsoft Graph PowerShell Advantages

- Singale module called <b>Microsoft.Graph</b> for many services
- No need for remote sessions
- More efficient and scalable for bulk operations 
- Continuously updated with new M365 features

## 3.4 Connecting to Graph using Powershell

- You will need to open an Administrator Powershell to install all the cmdlets.
- Use the cmd below to check your execution policy status
  > Get-ExecutionPolicy

- You need the execution policy to be set to either <b>Unrestricted or Bypass</b> to allow scripts to run on the machine.
  > Set-ExecutionPolicy -ExecutionPolicy Bypass

- To install Microsoft Graph into the machine
  > Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -force

  - Install-Module Microsoft.Graph
    - Install the Module call Microsoft.Graphe

  - -Scope CurrentUser
    - Install the Module for the current user not all users

  - -Repository PSGallery
    - Find the repository called PSGallery and install from there

  - -force
    - Install the module and do not display any prompts

- You might also need to install Nougat if there is a prompt for it

### 3.4.1 To connect to Microsoft Graph

  - Command to connect :
  > Connect-MgGraph -Scopes "Organization.Read.All","Group.ReadWrite.All","User.ReadWrite.All" -TenantId "< TenantID >"

  - The above command only allows access to users and groups, so to have access to other things go to this URL to check out 
  > https://learn.microsoft.com/en-us/graph/permissions-reference


