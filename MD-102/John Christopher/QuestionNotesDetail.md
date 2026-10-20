- [Licensing requirements](#licensing-requirements)
  - [Types of Activation](#types-of-activation)
- [Device join type](#device-join-type)
- [Bitlocker](#bitlocker)
- [Scope Tags](#scope-tags)
- [Cloud Policy Service](#cloud-policy-service)
- [App Control for Business](#app-control-for-business)
- [Device Configuration Profile](#device-configuration-profile)
  - [Settings Catalog](#settings-catalog)
  - [Templates](#templates)
- [Policies](#policies)
  - [Application Protection Policy](#application-protection-policy)
  - [Application Configuration Policies](#application-configuration-policies)
  - [Quiet time Policies](#quiet-time-policies)
  - [Driver update policy](#driver-update-policy)
- [Administrative Templates](#administrative-templates)
- [Break Glass Accounts](#break-glass-accounts)
- [Windows Hello for Business](#windows-hello-for-business)
  - [Cloud Deployment](#cloud-deployment)
  - [Hybrid Deployment](#hybrid-deployment)
- [Autopilot](#autopilot)
  - [Modes of Autopilot](#modes-of-autopilot)
  - [Device Preparation](#device-preparation)
  - [Device name Templates](#device-name-templates)
- [Intune Enrollment Restrictions](#intune-enrollment-restrictions)
  - [Device Platform restrictions](#device-platform-restrictions)
  - [Device limit restrictions](#device-limit-restrictions)
- [Windows Configuration Designer (WCD)](#windows-configuration-designer-wcd)
- [Office Customization Tool](#office-customization-tool)
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
- [Attack Surface Reduction (ASR)](#attack-surface-reduction-asr)
- [Azure Monitor Workbook](#azure-monitor-workbook)
- [Cloud PKI(Public Key Infrastructure) for Microsoft Intune](#cloud-pkipublic-key-infrastructure-for-microsoft-intune)
- [Android or Google Related](#android-or-google-related)
  - [Teams Rooms on Android devices](#teams-rooms-on-android-devices)
  - [Android Open Source Project (AOSP) management](#android-open-source-project-aosp-management)
  - [Firmware over the air (FOTA) deployment](#firmware-over-the-air-fota-deployment)
- [Apple or iOS related](#apple-or-ios-related)
  - [.mobileconfig](#mobileconfig)
  - [Apple Business Manager (ABM)](#apple-business-manager-abm)
  - [Apple User Enrollment](#apple-user-enrollment)
  - [Automated Device Enrollment (ADE) via Apple Business Manager](#automated-device-enrollment-ade-via-apple-business-manager)
  - [Apple Volume Purchase Program (VPP)](#apple-volume-purchase-program-vpp)
- [Linux related](#linux-related)


# Licensing requirements
- Windows Autopatch requires a Enterprise E3 or E5 license per user or device
- Enterprise App Catalog is part of Microsoft Intune Suite add-on
  - Can be purchase as a standalone Enterprise App Management add-on as well.

## Types of Activation

|Activation Type|How it works|
|---|---|
|Subscription Activation| User signs in and Microsoft verifies the Microsoft 365 license|
|Product Key Activation| Product key is used / redeemed |
|Volume Activation| Organization uses 1 Product key to activate X number of devices| 

# Device join type
- Entra registered
  - Mainly for Personnel or BYOD devices

  - Device is Entra registered when a user connects their work/school account to a device that isn't necessarily owned by the organization

  - Device gets an identity in Entra ID but Windows does not necessarily use the company's Entra account as the primary device.
  > Primary device login would be the laptop account login for the BYOD device.

- Entra joined
  - Mainly for devices that are given to you by company

  - Device is Entra joined when Windows device is joined directly to organization's Entra tenant

- Entra hybrid joined
  - Mainly for devices that are joined to traditional on premises AD and then registered to Entra ID

# Bitlocker
- BitLocker key rotation is a security feature that is designed to rotate BitLocker recovery key for individual devices.
  - Performed on a per-device basis and is not available as a `bulk action` for multiple devices at once

# Scope Tags
- Scope tags filter visibility and management rights for role based administrators across distributed IT teams

# Cloud Policy Service
> How should the M365 apps behave

- Allows you to enforce Office Policy settinngs that follow the user across different devices, regardless domain joined or enrolled in Intune

- Feature ennsures consistent applicationn of policies for users

- Policy settings are generally applied only when the Office app is restarted
  - Some privacy control policies are exception

- User need to be signed in aand has a valid license for the policies to be applied successfully

# App Control for Business
- A windows security feature that controls which applications is allowed for the device.

# Device Configuration Profile
## Settings Catalog
- A large searchable library of settings
- Start from scratch and add the settings you want

## Templates
- Predefined collection fro a particular purpose
- Start with a specific configuration type

# Policies
## Application Protection Policy
> What can the user do with the data inside the app

- Data protection policy for the application, what and where you can copy and paste, can be disabled.

- Enforce specific Intune app protection policy set by the organization

- Device must be registered in Entra ID and a broker app like `Microsoft Company Portal` is required for sign in.
  - Broker apps helps identify the identity and Device relationship with Intune or Entra

- Tunnel for MAM extends secure per-app VPN connectivity to unmanaged (MAM-only) devices using app protection policies.

## Application Configuration Policies
- Managed devices app configurationnnnn policies are delivered through MDM and require the device to be enrolled to Intune.

-  Managed apps app configuration policies are delivered through the App Protection Policy (MAM) channel and do not need device enrollment.

- App Configuration Policy allows for app settings to be configured regardless of enrollment status

## Quiet time Policies
- Quiet time policies are a dedicated policy type to mute Microsoft Outlook and Teams notifications at certain time period (E.g 6PM to 7AM) on iOS and Android.

## Driver update policy
- Let admins review, approve and control the rollout of driver updates distributed via Windows Update for Business

# Administrative Templates
- Imported Administrative Templates
  - These are mainly templates from 3rd parties when settings for their product are not available in the built in settings catalog

# Break Glass Accounts
> The account to use when everything else is locked out

- Accounts that is an emergency administrator account to use when normal administrator accoutns cannot access the environmennt.

# Windows Hello for Business 
## Cloud Deployment
>Entra ID handles the identity and sign in, no trust model is needed
  - Device is joined to Entra ID rather then On Premise AD
  - Lets user sign in with PIN or biometrics instead of password
  - For normal cloud sign in, no separate trust model is needed.
  
## Hybrid Deployment
>Entra ID handles the identity but trust model maybe needed to access on-premises AD DS resources
  - lets users sign in to Windows using Windows Hello for Business while organization still uses on premises Active Directory Domain Service alongside Microsoft Entra ID.
  - Replaces password based sign in with a PIN or biometric gesture, such as fingerprint or facial recognition.
  - PIN is tied to device and protects a cryptographic key

  | Trust Model          | Explanation                                                                                                                                              |
  | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Cloud kerberos Trust | Recommended for most new hybrid deployments. <br><br>No user certificates or Enterprise PKI required.<br><br> Uses Entra Kerberos for on premises access |
  | Key Trust            | User public key is synchronized to on premises AD <br><br> Domain Controllers still need certificates                                                    |
  | Certificate trust    | Issues authentication certificates to users<br><br> Requires enterprise PKI and AD FS in hybrid model. |

- Users can reset a forgotten Windows Hello for Business PIN if it is enabled in Intune Policy.

# Autopilot 

## Modes of Autopilot
  - Pre-provisioning mode (white glove)
    - This mode requires minimum sign in experience on first boot

  - User driven mode
    - This mode requires the end user to authenticate with their Microsoft Entra ID during OOBE
    - Can be configured to create a Standard type of account (Non-admin) when the user logs during OOBE.
    - Specifically designed for scenarios where remote employees receive devices and complete setup themselves without IT involvement on-site.

  - Existing device deployment mode
    - Is used to reimage and enroll devices that are not yet registered in Autopilot

  - Self-deploying mode (Kiosk Mode)
    - Does not require any user interaction or authentication during OOBE
    - Leveraging the device's TPM to authenticate to Microsoft Entra ID and Intune automatically

## Device Preparation
![](images/2026-10-05-04-19-37.png)

  - Device Preparation trackes Intuen Management Extension installation
  - Device Setup tracks apps, certs and policies assigned to the device
  - Account Setup tracks apps, certs and policies assignend to the user

## Device name Templates
- Limited to 15 characters, matching NetBIOs limit
- Can include %RAND:x%, where x is the number of random string characters
- Can include %SERIAL% variable to include the serial number as part of the device name

# Intune Enrollment Restrictions
## Device Platform restrictions
- Controls which platforms and ownership types can enroll
  - Allows or block Windows, macOS, iOS and Android
  - Block BYOD for supported platforms

## Device limit restrictions
- Controls how many devices a user can enroll

# Windows Configuration Designer (WCD)
- Microsoft tool used to create provisioning packages (.ppkg) that can configure Windows devices without requiring a full traditional imaging process

# Office Customization Tool
- Tool to build the deployment configuration for M365 Apps during Autopilot
- Allows customization of various settings such as 64 bit Apps, Montly Enterprise Channel and more
- Can be done without the need for manual XML editing

# Security Baseline
- A group of preconfigured settings recommended by Microsoft security team.
  - You can deploy the defaults or customize them accoding to needs

- Some example of the baseline templates:
  - Windows 10/11 security baseline
  - Microsoft Defender for Endpoinnt
  - Microsoft 365 Apps for Enterprise (Office) 

- Valid Platforms for security baselines
  - Windows
  - macOS
  - iOS
  - Android

- Can also detect report configuration drift against assigned devices

# Security Copilot
- Security Copilot agent in Intune surfaces recommendations across 3 primary catergories:
  - Device compliance issues (Devices that are out of compliance)
  - Configuration drift (Managed devices whose settings have deviated from their assigned policies)
  - Vulnerability Remediation (guidance on addressing software vulnerabilities)

# KQL Queries
- On demand device query is gated by the dedicated `Managed devices > Query` RBAC permission
  - Role need to have this permission in order for them to run Queries

- Single device query device requirements is that, the device must be managed by Intune and marked as corporate owned
  
- Device must be Entra joined or Entra Hybrid joined
  
- For multiple device queries, a Windows properties catalog policy is required

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
  - Password is also automatically rotated for security purpose.

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

# Attack Surface Reduction (ASR)
- Designed to block risky Office child process behavior and suspicious script activity.

- If Windows Defender in ASR profile is set to `Passive` mode, the antivirus will not actively block any threats and will only monitor and report them.

# Azure Monitor Workbook
- An interactive reporting tool visualize data from logs and metrics into tables, charts and other visualizations

# Cloud PKI(Public Key Infrastructure) for Microsoft Intune
- Cloud PKI is a cloud based, fully managed PKI service offered as part of Intune Suite, eliminating the need for on premises CA infrastructure.
-----

# Android or Google Related
- OEMConfig is a standardized Google backed framework that allows OEMs to publish a managed configuration schema via a dedicated app.

## Teams Rooms on Android devices
- Dedicated `meeting room systems` that run Microsoft Teams

## Android Open Source Project (AOSP) management
- AOSP is the device management platform for Android devices to Enroll into Intune.

## Firmware over the air (FOTA) deployment
- Lets Intune schedule and control delivery of full OS firmware updates to supported managed Android devices

----

# Apple or iOS related
## .mobileconfig
- .mobileconfig is an Apple configuration profile containing settings called payloads
  - Payloads define the settings to apply, such as WIFI, VPN certs or restrictions

- Intune macOS custom profiles let admins upload a .mobileconfig file containing the desired payload settings

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
