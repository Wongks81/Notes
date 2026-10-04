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

---

To use subscription activation, deviecs must be Entra joined or hybrid joined.

---

>You created one required Microsoft 365 Apps deployment that installed Word, Excel, and PowerPoint. <br><br>
>Later, another admin assigned a second required Microsoft 365 Apps deployment to the same devices that included only Excel and PowerPoint.<br><br>
>Why did Word disappear from the devices?

- Later suite assignments overwrite the earlier one

---

- MAM (Mobile Application Management)
  - Manages the apps and corporate data

  - Control the corporate applications/data without necessarily controling the whole device

  - Edwards should be using MAM which ask you to install company portal in your personnel phone.

- MDM (Mobile Device Management)
  - Manages the entire device
  
  - Admins can managed things configurations for wifi, security, VPN etc...

  - Darwin is a good example to remember for MDM.

---

Intune Device limit restrictions 
  - Default limit a user can enroll is 15 (Normal user enrolling E.g. Laptop, phone, tablet etc.. assigned / belong to him/her)
  - Limit can be configured in `Devices > Enrollment > Device limit restrictions`

---

Automatic MDM enrollment enabels Windows devices to automatically enroll in Intune when they are joined to Entra

---

Device Configuration Profile in Intune enforces device settings 
  - Does not control access on compliance

Conditional Access policy in Entra ID can enforce device compliance so that only compliance devices can access M365 Services.

---

Windows Local Administrator Password Solution (LAPS)
- Windows feature that automatically manages and rotates password of a local administrator account on each device
- Password can be securely back up to Entra ID or Active Directory

---

Notification on compliance policy for non compliant can only be done on email

---

Windows Configuration Designer is used for creating provisioning packages
- One of the options is to remove preinstalled software.

---

Device Configuration profile with :
- Settings catalog
  - Settings that are similar to AD GPO settings
    - E.g. Configure Edge Homepage, Disable Control Panel or Configure Bitlocker options

- Templates
  - Pre-built profiles designed for a specific purpose, relevant settings are group together
    - E.g. Administrative Templates,VPN, Wifi 

---

- Dedicated device Profiles
  - For shared, task specific and intended for tightly controlled usage

- Corporate owned work profile
  - Supports both work and personel use with seperation between both sides.
  
---

- User driven Autopilot
  - Requires user to go through the setup process

- Autopilot reset workflow
  - Is used to reset a device to its original state

- Pre-provisioned Autopilot
  - Ensure employees first sign in experience is as short as possible

- Self deploying Autopilot
  - Designed for devices that can be setup without user interaction

---

- Entra allows Local Administrator Password to be retreive for troubleshooting purposes

---


