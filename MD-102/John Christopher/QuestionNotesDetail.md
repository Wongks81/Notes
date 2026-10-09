- [Licensing requirements](#licensing-requirements)
- [Bitlocker](#bitlocker)
- [Cloud Policy Service](#cloud-policy-service)
- [App Control for Business](#app-control-for-business)
- [Policies](#policies)
  - [App Protection Policy](#app-protection-policy)
  - [Application Configuration Policies](#application-configuration-policies)
  - [Quiet time Policies](#quiet-time-policies)
- [Administrative Templates](#administrative-templates)
- [Break Glass Accounts](#break-glass-accounts)
- [Autopilot](#autopilot)
  - [Modes of Autopilot](#modes-of-autopilot)
  - [Device Preparation](#device-preparation)
- [Security Baseline](#security-baseline)
- [Security Copilot](#security-copilot)
- [KQL Queries](#kql-queries)
- [Update Rings](#update-rings)
- [Microsoft Tunnel Gateway](#microsoft-tunnel-gateway)
- [Multi-admin approval](#multi-admin-approval)
- [Microsoft Graph](#microsoft-graph)
- [Delivery Optimization Profile](#delivery-optimization-profile)
- [Local Administrators Password Solution (LAPS)](#local-administrators-password-solution-laps)
- [Enterprise App Catalog](#enterprise-app-catalog)
- [Remote Help](#remote-help)
- [FIDO2 Keys](#fido2-keys)
- [Android or Google Related](#android-or-google-related)
- [Apple or iOS related](#apple-or-ios-related)
  - [Apple Business Manager (ABM)](#apple-business-manager-abm)
  - [Apple User Enrollment](#apple-user-enrollment)
  - [Automated Device Enrollment (ADE) via Apple Business Manager](#automated-device-enrollment-ade-via-apple-business-manager)
  - [Apple Volume Purchase Program (VPP)](#apple-volume-purchase-program-vpp)
- [Linux related](#linux-related)


# Licensing requirements
- Windows Autopatch requires a Enterprise E3 or E5 license per user or device
- Enterprise App Catalog is part of Microsoft Intune Suite add-on
  - Can be purchase as a standalone Enterprise App Management add-on as well.

# Bitlocker
- BitLocker key rotation is a security feature that is designed to rotate BitLocker recovery key for individual devices.
  - Performed on a per-device basis and is not available as a `bulk action` for multiple devices at once



# Cloud Policy Service
> How should the M365 apps behave

- Allows you to enforce Office Policy settinngs that follow the user across different devices, regardless domain joined or enrolled in Intune

- Feature ennsures consistent applicationn of policies for users

- Policy settings are generally applied only when the Office app is restarted
  - Some privacy control policies are exception

- User need to be signed in aand has a valid license for the policies to be applied successfully

# App Control for Business
- A windows security feature that controls which applications is allowed for the device.

# Policies
## App Protection Policy
> What can the user do with the data inside the app

- Data protection policy for the application

- Enforce specific Intune app protection policy set by the organization

- Device must be registered in Entra ID and a broker app like `Microsoft Company Portal` is required for sign in.
  - Broker apps helps identify the identity and Device relationship with Intune or Entra

## Application Configuration Policies
- Managed devices app configurationnnnn policies are delivered through MDM and require the device to be enrolled to Intune.

-  Managed apps app configuration policies are delivered through the App Protection Policy (MAM) channel and do not need device enrollment.

## Quiet time Policies
- Quiet time policies are a dedicated policy type to mute Microsoft Outlook and Teams notifications at certain time period (E.g 6PM to 7AM) on iOS and Android.

# Administrative Templates
- Imported Administrative Templates
  - These are mainly templates from 3rd parties when settings for their product are not available in the built in settings catalog

# Break Glass Accounts
> The account to use when everything else is locked out

- Accounts that is an emergency administrator account to use when normal administrator accoutns cannot access the environmennt.

# Autopilot 

## Modes of Autopilot
  - Pre-provisioning mode
    - This mode requires minimum sign in experience on first boot

  - User driven mode
    - This mode requires the end user to authenticate with their Microsoft Entra ID during OOBE
    - Specifically designed for scenarios where remote employees receive devices and complete setup themselves without IT involvement on-site.

  - Existing device deployment mode
    - Is used to reimage and enroll devices that are not yet registered in Autopilot

  - Self-deploying mode
    - Does not require any user interaction or authentication during OOBE
    - Leveraging the device's TPM to authenticate to Microsoft Entra ID and Intune automatically

## Device Preparation
![](images/2026-10-05-04-19-37.png)

  - Device Preparation trackes Intuen Management Extension installation
  - Device Setup tracks apps, certs and policies assigned to the device
  - Account Setup tracks apps, certs and policies assignend to the user

# Security Baseline
- A group of preconfigured settings recommended by Microsoft security team.
  - You can deploy the defaults or customize them accoding to needs

- Some example of the baseline templates:
  - Windows 10/11 security baseline
  - Microsoft Defender for Endpoinnt
  - Microsoft 365 Apps for Enterprise (Office) 

# Security Copilot
- Security Copilot agent in Intune surfaces recommendations across 3 primary catergories:
  - Device compliance issues (Devices that are out of compliance)
  - Configuration drift (Managed devices whose settings have deviated from their assigned policies)
  - Vulnerability Remediation (guidance on addressing software vulnerabilities)

# KQL Queries
- On demand device query is gated by the dedicated `Managed devices > Query` RBAC permission
  - Role need to have this permission in order for them to run Queries

# Update Rings

| Policy                | Simple analogy                    |
| --------------------- | --------------------------------- |
| Update Ring           | Rules for how updates are handled |
| Feature policy        | Which Windows versions to install |
| Quality update policy | Which monthly fixes to deploy and when |

- Update deferral
  - Refers to when the devices will get the update

- Update Deadline
  - Ensures that the update is installed within the stated days of release

- Deadline Grace Period
  - The amount of days to allow users to postphone the required restart after the update.

# Microsoft Tunnel Gateway 
- To install it on a Linux server, it must run on a currently supported Linux distribution, be reachable by mobile devices at its published address and have a supported container runtime installed.

# Multi-admin approval
- Multi-admin approval is a tenant level feature in Microsoft Inntune that is designed to add an additionnnnal layer of oversight by required a second administrator to approve certainnn high-impact changes.

- Multi-admin approval can be enabled by navigating to `Tenant administrationn > Multi-admin approval` in Microsoft Intune admin center.

# Microsoft Graph
- Process to install MS Graph :
  - Open PowerShell as Administrator
  - `Install-Module Microsoft.Graph -Scope AllUsers`
  - Install NuGet provider if prompted
  - Verify the innstallation by `Get-InstalledModule Microsoft.Graph` 

- Distinction betweenn Delagated permission and Application permission
  - Delagated permission refers to scripts thats needs user interaction manually

  - Application permission refers to scripts that are scheduled or automated and will run by itself with no human interaction.

- Microsoft Graph server side large collections returns an @odata.nextLink URL whenever more results remain.
  - To retrieve the full results, you will need to follow that link until it is no longer present
  - In scripting, we will need to loop the @odata.nextLink property till the end to get all the results.

# Delivery Optimization Profile
- A dedicated profile type that provides settings such as Download mode, which controls whether devices use peer to peer, group or internet only downloads, directl addressing the bandwidth reduction requirement.

# Local Administrators Password Solution (LAPS)
- A policy which manages the local administrator's password for the device
  - password is also automatically rotated for security purpose.
- Policy is found under Endpoint Security > Account Protection
- Policy has a template that surfaces all key settings, including:
  - Backup Directory
  - Password age
  - Complexity
  - Length

- LAPS backup directory is Entra ID, password is held as a directory object
  - To read the password, we will need the role to have `deviceLocalCredentials/password/read` authorized in it.
  - Examples of roles that have this permissions are Cloud Device Administrator or Intune Administrator

# Enterprise App Catalog
- Enterprise App Catalog automatically manintains publishes updated application packages as vendors release new versions.
  
- Administrators can choose to have updates applied automatically to devices or manually select a specific version.

# Remote Help
- Requires application to be deployed and installed on client devices
- App must be deployed through Intune as a managed Windows applications to all devices that require remote support.

# FIDO2 Keys
- To use FIDO2 keys as an option to login, you will need to enable FIDO2 security key method in Entra ID and scoped it to the respective users or groups.

# Android or Google Related
- OEMConfig is a standardized Google backed framework that allows OEMs to publish a managed configuration schema via a dedicated app.

# Apple or iOS related
## Apple Business Manager (ABM)
- Intergration between Apple Business Manager and Microsoft Intune requires a specific token exchange.
  - Intune generates a public key (.pem file)
  - Key is uploaded to ABM when creating or deiting MDM server entry
  - ABM issues a server token (.p7m file) to be downloaded
  - Upload the .p7m file to Intune to establish trust link

## Apple User Enrollment
- Designed for personally owned iOS/iPadOS devices
  - Creates a separation between personal and work data using a managed Apple ID.
  - Limits Intune management scope to work apps and accounts, prevent full device wipes

## Automated Device Enrollment (ADE) via Apple Business Manager
- Intended for corporate-owned devices 

## Apple Volume Purchase Program (VPP)
- VPP app licenses can be revoked by administrators in Intune directly from Intune Portal.
- This Action can be performed regardless of whether the device is still enrolled.


# Linux related
