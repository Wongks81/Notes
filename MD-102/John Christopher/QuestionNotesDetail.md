- [Licensing requirements](#licensing-requirements)
- [Bitlocker](#bitlocker)
- [Cloud Policy Service](#cloud-policy-service)
- [App Protection Policy](#app-protection-policy)
- [Administrative Templates](#administrative-templates)
- [Break Glass Accounts](#break-glass-accounts)
- [Autopilot](#autopilot)
  - [Modes of Autopilot](#modes-of-autopilot)
  - [Device Preparation](#device-preparation)
- [Security Copilot](#security-copilot)
- [KQL Queries](#kql-queries)
- [Update Rings](#update-rings)
- [Multi-admin approval](#multi-admin-approval)


# Licensing requirements
- Windows Autopatch requires a Enterprise E3 or E5 license per user or device

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

# App Protection Policy
> What can the user do with the data inside the app

- Data protection policy for the application

- Enforce specific Intune app protection policy set by the organization

- Device must be registered in Entra ID and a broker app like `Microsoft Company Portal` is required for sign in.
  - Broker apps helps identify the identity and Device relationship with Intune or Entra

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
    

## Device Preparation
![](images/2026-10-05-04-19-37.png)

  - Device Preparation trackes Intuen Management Extension installation
  - Device Setup tracks apps, certs and policies assigned to the device
  - Account Setup tracks apps, certs and policies assignend to the user


# Security Copilot

- Security Copilot agent in Intune surfaces recommendations across 3 primary catergories:
  - Device compliance issues (Devices that are out of compliance)
  - Configuration drift (Managed devices whose settings have deviated from their assigned policies)
  - Vulnerability Remediation (guidance on addressing software vulnerabilities)

# KQL Queries
- On demand device query is gated by the dedicated `Managed devices > Query` RBAC permission
  - Role need to have this permission in order for them to run Queries

# Update Rings
- Update deferral
  - Refers to when the devices will get the update

- Update Deadline
  - Ensures that the update is installed within the stated days of release

- Deadline Grace Period
  - The amount of days to allow users to postphone the required restart after the update.

# Multi-admin approval
- Multi-admin approval is a tenant level feature in Microsoft Inntune that is designed to add an additionnnnal layer of oversight by required a second administrator to approve certainnn high-impact changes.

- Multi-admin approval can be enabled by navigating to `Tenant administrationn > Multi-admin approval` in Microsoft Intune admin center.




