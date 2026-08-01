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

## 2.2 User Identities

- Human Users who access Microsoft services

- Member users :
  - Employees created directly in Entra ID or Active Directory

- Guest Users :
  - External users invited through B2B collaboration
  - Identity is managed but granted limited access

## 2.3 Service Principles

- Represent application or services that need to authenticate and access resources
- Automatically created when an app is registered in Entra ID
- Used for assigning permissions, running automation or secure access without human interaction
  - E.g. Web app needs to read/write to Microsoft Graph or SQL 

- Main advantage is :
  - Application Authentication  : Ensures secure access for applications and services
  - Automated permissions       : Facilitates permission assignments without human intervention
  - Secure Access               : Provides secure resource access without human interaction

## 2.4 Managed Identities

- Special identities for Azure resources like VMs or Function Apps to access other Azure services securely
  > <b>Without Storing Credentials</b>

<br>

- There are 2 types
  - System assigned
    - Tied to one resource and lifecycle matches the resource

  - User assigned
    - Standalone identity resuseable across multiple reources
    - E.g. Azure VM accessing a storage account using system assigned identity

## 2.5. Difference between Service Principles and Managed Identities

- Service Principles are either created by user or registered by apps
  - Admins will managed the accounts like passwords and certificates
  - Can be used for logging on and authenticating with Azure 
  - Cen be used for external or 3rd party services

- Managed Identities have no need to manage any secrets or credentials
  - Only work within Azure, not for 3rd party services

## 2.6 Device Identities

- Every Device that is joined to Entra ID gets an identity
- It is used for :
  - Conditional Access
  - Intune Management
  - Device Compliance

- Device can be joined by:
  - Entra ID joined   : Devices directly joined to Entra ID
  - Hybrid AD joined  : Devices are joined to on premises Active Directory
  - Entra ID registred: Devices are registered for BYOD

