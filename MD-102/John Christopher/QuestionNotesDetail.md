- [Licensing requirements](#licensing-requirements)
  - [Types of Activation](#types-of-activation)
- [Device join type](#device-join-type)
- [Bitlocker](#bitlocker)
- [Scope Tags](#scope-tags)
- [Cloud Policy Service](#cloud-policy-service)
- [Applications](#applications)
  - [App Control for Business](#app-control-for-business)
  - [Win32 App](#win32-app)
  - [Enterprise App Catalog](#enterprise-app-catalog)
  - [Installation behavior : User vs System](#installation-behavior--user-vs-system)
- [Device Configuration Profile](#device-configuration-profile)
  - [Settings Catalog](#settings-catalog)
  - [Templates](#templates)
- [Policies](#policies)
  - [Application Protection Policy](#application-protection-policy)
  - [Application Configuration Policies](#application-configuration-policies)
  - [Managed apps policy](#managed-apps-policy)
  - [Quiet time Policies](#quiet-time-policies)
  - [Driver update policy](#driver-update-policy)
  - [Cloud policy vs Cloud Updates](#cloud-policy-vs-cloud-updates)
- [Intune Advanced Analytics](#intune-advanced-analytics)
- [Cloud Public Key Infrastructure (PKI)](#cloud-public-key-infrastructure-pki)
  - [Simple Certificate Enrollment Protocol (SCEP)](#simple-certificate-enrollment-protocol-scep)
- [Error Codes](#error-codes)
  - [0x800705B4 Time out Error](#0x800705b4-time-out-error)
- [Administrative Templates](#administrative-templates)
- [Break Glass Accounts](#break-glass-accounts)
- [Windows Hello for Business](#windows-hello-for-business)
  - [Cloud Deployment](#cloud-deployment)
  - [Hybrid Deployment](#hybrid-deployment)
- [Autopilot](#autopilot)
  - [Modes of Autopilot](#modes-of-autopilot)
  - [Device Preparation](#device-preparation)
  - [Device name Templates](#device-name-templates)
  - [Autopilot M365 Apps rollout](#autopilot-m365-apps-rollout)
- [Intune Enrollment Restrictions](#intune-enrollment-restrictions)
  - [Device Platform restrictions](#device-platform-restrictions)
- [Delivery Optimization](#delivery-optimization)
  - [Delivery Optimization Profile](#delivery-optimization-profile)
  - [NAT peering](#nat-peering)
  - [Device limit restrictions](#device-limit-restrictions)
- [Windows Configuration Designer (WCD)](#windows-configuration-designer-wcd)
  - [Bulk enrollment using Provisioning Packages](#bulk-enrollment-using-provisioning-packages)
- [Office Customization Tool](#office-customization-tool)
- [Windows Defender for Endpoint](#windows-defender-for-endpoint)
  - [Devices settings](#devices-settings)
  - [Antivirus Policy](#antivirus-policy)
  - [Endpoint security disk encryption policy](#endpoint-security-disk-encryption-policy)
  - [Cloud Protection with sample submission](#cloud-protection-with-sample-submission)
- [Security Baseline](#security-baseline)
  - [Per-setting status report](#per-setting-status-report)
- [Security Copilot](#security-copilot)
- [Virtual Machines](#virtual-machines)
  - [Multi-session session hosts](#multi-session-session-hosts)
- [KQL Queries](#kql-queries)
- [Diagnostic upload endpoint](#diagnostic-upload-endpoint)
- [Update Rings](#update-rings)
- [Microsoft Tunnel Gateway](#microsoft-tunnel-gateway)
  - [MAM tunnel](#mam-tunnel)
- [Multi-admin approval](#multi-admin-approval)
- [Microsoft Graph](#microsoft-graph)
- [Local Administrators Password Solution (LAPS)](#local-administrators-password-solution-laps)
- [Enterprise App Catalog](#enterprise-app-catalog-1)
- [Remote Help](#remote-help)
- [FIDO2 Keys](#fido2-keys)
- [Attack Surface Reduction (ASR)](#attack-surface-reduction-asr)
- [Azure Monitor Workbook](#azure-monitor-workbook)
- [Cloud PKI(Public Key Infrastructure) for Microsoft Intune](#cloud-pkipublic-key-infrastructure-for-microsoft-intune)
- [Android or Google Related](#android-or-google-related)
  - [Android compliance policy](#android-compliance-policy)
  - [Teams Rooms on Android devices](#teams-rooms-on-android-devices)
  - [Android Open Source Project (AOSP) management](#android-open-source-project-aosp-management)
  - [Firmware over the air (FOTA) deployment](#firmware-over-the-air-fota-deployment)
  - [Android Dedicated Enrollment](#android-dedicated-enrollment)
  - [Device restrictions](#device-restrictions)
- [Apple or iOS related](#apple-or-ios-related)
  - [.mobileconfig](#mobileconfig)
  - [Apple Business Manager (ABM)](#apple-business-manager-abm)
  - [Apple User Enrollment](#apple-user-enrollment)
  - [Automated Device Enrollment (ADE) via Apple Business Manager](#automated-device-enrollment-ade-via-apple-business-manager)
  - [Web based Device Enrollment](#web-based-device-enrollment)
  - [Apple Configurator for iOS](#apple-configurator-for-ios)
  - [Apple Configurator for Mac](#apple-configurator-for-mac)
  - [Apple Volume Purchase Program (VPP)](#apple-volume-purchase-program-vpp)
  - [Device features template](#device-features-template)
  - [Userless MacOS Devices](#userless-macos-devices)
  - [Apple Device Management](#apple-device-management)
  - [Setting Catalog](#setting-catalog)
  - [Preference file Template](#preference-file-template)
  - [Endpoint Security](#endpoint-security)
    - [macOS FileVault policy](#macos-filevault-policy)
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

  - Entra Joined is necessary for device name template to apply during enrollment

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

- User need to be signed in and has a valid license for the policies to be applied successfully

- Device does not need to be enrolled, policy settings for M365 Apps can be applied and enforced on unmanaged devices.

# Applications
## App Control for Business
- A windows security feature that controls which applications is allowed for the device.

## Win32 App
- Traditional Windows Desktop Application, typically with extensions of .msi or .exe
- Correct choice for deploying large desktop application to windows devices during Autopilot enrollment
- Allows you to package and deploy Win32 applications with multiple files, silent installation, detection rules.
- If the app is from Microsoft Store, you may need to repackage it as a Win32 app if you need to add a dependency chain and supersedence for prerequisite runtimes.

## Enterprise App Catalog
- These are applications that are pre packaged by Microsoft with install commands, requirements and detection rules
- Provides a simpler way to move to newer cataloged versions without constantly rebuilding the entire deployment approach
  - Uses the supersedence relationship when a newer version is available

## Installation behavior : User vs System
| Installation behvaior | System                           | User                              |
| --------------------- | -------------------------------- | --------------------------------- |
| Runs under            | Local SYSTEM account             | Signed in User account            |
| Installation Timing   | Can install before user signs in | Requires user sign in             |
| Installation scope    | Device wide                      | User profile                      |
| Available to          | All users on device              | Targeted user                     |
| Admin rights          | Not needed                       | Depends on installer requirements |

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

## Managed apps policy
- Allows admin to apply app configuration settings to apps on both enrolled and unenrolled devices
  - To ensure that the same general app configuration settings reach all devices regardless of enrollment status

## Quiet time Policies
- Quiet time policies are a dedicated policy type to mute Microsoft Outlook and Teams notifications at certain time period (E.g 6PM to 7AM) on iOS and Android.

## Driver update policy
- Let admins review, approve and control the rollout of driver updates distributed via Windows Update for Business

## Cloud policy vs Cloud Updates
- Cloud policy is used to enforce policies and settings for cloud based services in M365
  - Can be used to manage M365 Apps updates

- Cloud updates manages the update settings like custom rollout waves, exclusion windows

# Intune Advanced Analytics
- Provides advanced insights into endpoint performance
- Allows admins to identify trends, prioritize remediation and reduce support effort
  - Helps pinpoint the root causes of slow startup times and poor performance across different hardware and regions

# Cloud Public Key Infrastructure (PKI)
- A cloud based service that allows an organization to create, issue, renew and revoke digital certificates for managed devices and users
  - Without maintaining its own on-premise certificate authroity (CA)

## Simple Certificate Enrollment Protocol (SCEP)
- Used to automatically request and install digital certificates on managed devices

# Error Codes
## 0x800705B4 Time out Error
- Commonly associated with unsupported virtual machines during self deploying mode
- Normally caused by VM not having TPM 2.0 capability

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
    - Supports both Microsoft Entra and Microsoft Entra Hybrid joined

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

## Autopilot M365 Apps rollout
- Office Customization Tool (OCT) creates and exports configuration files that are used with Office Deployment Tools (ODT)
- Win32 apps in Intune are deployed using the Intune Management Extension

# Intune Enrollment Restrictions
## Device Platform restrictions
- Controls which platforms and ownership types can enroll
  - Allows or block Windows, macOS, iOS and Android
  - Block BYOD for supported platforms

# Delivery Optimization
## Delivery Optimization Profile
- A dedicated profile type that provides settings such as Download mode, which controls whether devices use peer to peer, group or internet only downloads, directl addressing the bandwidth reduction requirement.

## NAT peering
- Protocol for peer sharing across NAT boundaries
  - Port TCP 7680 Delivery Optimization peer to peer content sharing
  - Port UDP 3544 Teredo NAT traversal, helping peers connect across NATs
  - Port TCP 80 / 443 Donwload from Delivery Optimization cloud services 

## Device limit restrictions
- Controls how many devices a user can enroll

# Windows Configuration Designer (WCD)
- Microsoft tool used to create provisioning packages (.ppkg) that can configure Windows devices without requiring a full traditional imaging process

- Allows admins to apply standard WIFI profiles, device naming patterns and base settings to Windows before they connect to the internet.

- You should NOT apply PPKG to the same rollout as Windows Autopilot
  - This can lead to conflicting settings and configurations

## Bulk enrollment using Provisioning Packages
- For Windows bulk enrollment using Provisioning package, we need to retrieve a bulk token in WCD before applying the provisioning package to the device.

# Office Customization Tool
- Tool to build the deployment configuration for M365 Apps during Autopilot
- Allows customization of various settings such as 64 bit Apps, Montly Enterprise Channel and more
- Can be done without the need for manual XML editing

# Windows Defender for Endpoint

## Devices settings
- Connect Windows devices setting when enabled allow enrolled Windows devices to use Defender risk in compliance evaluation
  - This setting ensures that devices can communicate and integrade with Microsoft Defender for Endpoint
  - Enabling this setting is crucial for proper functioning of the service to service connection between Intune and Defender 

## Antivirus Policy
- Purpose built for antivirus management and allows admins to configure settings related to Microsoft Defender Antivirus

- Designed to avoid unrelated device setings and focus solely on antivirus management

## Endpoint security disk encryption policy
- Policy that is specifically designed to deploy BitLocker settings and encryption controls to devices manged by Intune.

## Cloud Protection with sample submission
- Allows Windows Defender to leverage cloud based threat intelligence and analysis to quickly identify and block newly encountered suspicious files

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

## Per-setting status report
- Provide detailed information on each individual setting within the security baseline profile
  - This allows admins to identify the specific setting that is failing or conflicting

- Report will help to pinpoint the exact issue before making any baseline design

# Security Copilot
- Security Copilot agent in Intune surfaces recommendations across 3 primary catergories:
  - Device compliance issues (Devices that are out of compliance)
  - Configuration drift (Managed devices whose settings have deviated from their assigned policies)
  - Vulnerability Remediation (guidance on addressing software vulnerabilities)

# Virtual Machines
## Multi-session session hosts
- Refers to virtual machines that allow multiple users to sign in and use the same Windows OS simultaneously.

# KQL Queries
- On demand device query is gated by the dedicated `Managed devices > Query` RBAC permission
  - Role need to have this permission in order for them to run Queries

- Single device query device requirements is that, the device must be managed by Intune and marked as corporate owned
  
- Device must be Entra joined or Entra Hybrid joined
  
- For multiple device queries, a Windows properties catalog policy is required

# Diagnostic upload endpoint
- Used for uploading diagnostic collections (logs) from device to Microsoft for troubleshooting.

- Can only be done via Intune admin center
  - You cannot use Microsoft Graph for this operation.

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

## MAM tunnel
- Tunnel for MAM on android does not support Always on VPN
  - When Always on VPN is enabled, the Tunnel connection fails

- When security requirement to block network access whenever MAM tunnel cannot connect, Admins should use Strict Tunnel Mode through the Microsoft Edge managed app configuration policy

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

- Maintenace window can be set to install updates during the window

## Android compliance policy
- To create Android compliance policy correctly, admins need to select Android Enterprise profile type.

## Teams Rooms on Android devices
- Dedicated `meeting room systems` that run Microsoft Teams

## Android Open Source Project (AOSP) management
- AOSP is the device management platform for Android devices to Enroll into Intune.

## Firmware over the air (FOTA) deployment
- Lets Intune schedule and control delivery of full OS firmware updates to supported managed Android devices

## Android Dedicated Enrollment
- Enrollment method for company owned devices that are intended for a specific purpose rather than general employee use.
- Commonly used for kiosk devices like warehouse scanner, signage and shared purpose devices.

## Device restrictions
- Device restrictions in Intune allow you to control various settings and features on devices
  - This includes the ability to manage when OS and app updates are installed and define freeze periods.

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
- Default All Users enrollment must aloow the iOS/iPadOS platform
  - Block the platform will cause ADE to fail with Invalid Profile result.

## Web based Device Enrollment
- Supports personal devices running iOS/iPadOS 15 or later
- Uses Safari and does not require Company Portal app

## Apple Configurator for iOS
- Bulk device management tool specifically designed for configuration, deployment and management of multiple Apple devices
- Add iPhones, iPads and Apple TVs to Apple Business Manager or Apple School Manager

## Apple Configurator for Mac
- Prepare, configure, supervise and restore Apple devices, including iPhones, iPads and Apple TVs.

## Apple Volume Purchase Program (VPP)
- VPP app licenses can be revoked by administrators in Intune directly from Intune Portal.
- This Action can be performed regardless of whether the device is still enrolled.

## Device features template
- Specifically for iOS or mac devices.
- Allows for configuration of device settings, including AirPrint or Apple SSO for internal web apps
- Template can be used to push specific settings and configruations to the Apple devices without the need to import custom file.

## Userless MacOS Devices
- For devices that are setup to be shared without being assigned to a specific user
  - E.g. macs in meeting rooms

- Intune compliance evaluation is not supported for userless macOS

## Apple Device Management
- Supervision state gives an organization greater control over the device

## Setting Catalog
- Settings catalog is a common place to configure settings
- The settings depends on OS and platform, meaning Windows and Mac each have its own setting catalog

## Preference file Template
- For preconfiguring line of business macOS app by deploying its .plist settings file
- Allows you to define and deploy custom preferences and settings for macOS apps

## Endpoint Security
### macOS FileVault policy
- For managing startup disk encryption on company owned MacBookthrough Apple Business Manage.
- Policy allows admins to enforce FileVault disk ecryption settings, manage recovery information and ensure complianace

----

# Linux related
