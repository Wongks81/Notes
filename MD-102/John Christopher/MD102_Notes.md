- Implementing Device Groups
  - When dealing with large number of devices, it is best to create groups in Azure to segregate them accordingly
    
  - Group types

    - When creating a new group in Azure, for devices, group type can only be <b>Security</b>

      ![](images/2026-09-06-08-30-34.png)

      > Microsoft 365 groups are more geared towards users.
      > <br><br>A special group when created, the users in the group will share a workshop with functions that are available across the team. 
      > <br><br>Like Shared calendar, onenote etc...

  - Membership types

    - There are mainly <b>2 options</b> for devices. Assigned and Dynamic Device.

        > Dynamic User is more for M365 group
    
        ![](images/2026-09-06-08-44-05.png)

    - Assigned :
      - The manual way of adding devices to the group
      - Admins add the devices themselves to the group

    - Dynamic Device :
      - The "Scripted" way to add devices by comparing parameters in the device

      - You will need to add a dynamic query for it to work
        ![](images/2026-09-06-08-45-03.png)

      - Example of query: Device have a parameter with "deviceOSType" = "Windows"
        ![](images/2026-09-06-08-47-07.png)

---

- Enrolling device into Intune 
  - Place to enroll devices in Azure :
    - Intune Admin Center > Devices > Device Enrollment > Enroll Devices

    ![](images/2026-09-06-10-32-22.png)

  - Windows device enrollment will mainly be either done automatically when :
    - You setup a new machine and registering the machine to a 'Work or School Account' during setup

    - After logging in to the device, search for settings > accounts > Access work or school > Connect 

    ![](images/2026-09-06-10-40-22.png)

---

  - For Apple device, before we can do anything, we need to have a `Apple MDM Push Certificate`

    ![](images/2026-09-06-10-44-09.png)

    1. After click on the Push certificate card, you will have to check the box to grant Microsoft permission to send both user and device information to Apple. 
      ![](images/2026-09-06-10-45-49.png)

    2. Download the certificate signing request 
      ![](images/2026-09-06-10-47-22.png)
    
    3. Click on create MDM push Certificate
      ![](images/2026-09-06-10-46-22.png)

    4. After clicking, it will bring you to apple website and prompt you to logon

    5. After logon, you will see the `Apple Push Certificates Portal`, click on "Create a Certificate"
      ![](images/2026-09-06-10-49-53.png)

    6. Agree to the terms and when you see the "Create a New Push Certificate" page, upload the csr file that you have downloaded in (2) and click upload.
      ![](images/2026-09-06-10-51-31.png)
     
    7. It will prompt you to sign in again, after signing in, you can download the certificate.

      ![](images/2026-09-06-10-52-41.png)

    8. Go back to Intune and enter the Apple ID that is used to create the certificate

      ![](images/2026-09-06-10-54-23.png)

    9. Upload the certificate you have downloaded in (7)

---

  - For Android devices : 

    1. Click on "Managed Google Play" card.
    ![](images/2026-09-06-10-56-19.png)

    2. Agree to terms and click on "Launch Google to connect now"
    ![](images/2026-09-06-11-02-40.png)

    3. It will bring you to Google's page, Click  on "Get Started" and enter what is needed.
    ![](images/2026-09-06-11-04-49.png)

    4. Enter the data needed for the remaining of the registration.

    5. Once done, it should show that Google Play successfully configured with tenant
    ![](images/2026-09-06-11-06-15.png)

---

- Enrollment device limit restrictions
  - Default device limit is 5
  ![](images/2026-09-06-11-08-13.png)

  - This setting sets how many devices 1 user which has the intune license can enroll or linked to intune.

- Enrollment device platform restrictions
  - This settings allow what `Type of devices` people can enroll
  ![](images/2026-09-06-13-36-30.png)

  - Can be scope down to groups and only allow users in groups to enroll using the correct devices

  - E.g.
    ![](images/2026-09-06-13-40-31.png)

  - We can also block personnel devices if need but turning on the block state.
  ![](images/2026-09-06-13-42-00.png)

---

- Corporate device identifiers
  - A way for intune to identify if the device enrolled belongs to the company.
    - More details please google

- Device Enrollment Manager
  - A way for people to enroll on behalf of someone else.
  ![](images/2026-09-06-13-48-07.png)

---

- Bulk Enroll devices
  - Windows 
    - Make sure Automatic Enrollment for Windows is turned on.
    ![](images/2026-09-06-14-33-07.png)

    - Can use Group Policy to enroll Intune device
    ![](images/2026-09-06-14-35-58.png)

      - Can be set to use User Credential or Device Credential for enrollment.

      - Difference between the 2 of them can be simply describe as:
        - User Credential : "KS is enrolling into Intune"
        - Device Credential : This laptop is enrolling into Intune

      - Device Credential is mainly used by devices that are shared by a group of people.

  - Apple
    - Need to have a `Apple MDM Push Certificate` registered before you can do anything

    - Cick on `Apple Configurator`
    ![](images/2026-09-06-16-10-05.png)

    - Devices can be Added via a csv that can be uploaded to Intune
    
    - Click on "Profiles" and create an enrollment profile.
    ![](images/2026-09-06-16-12-59.png)

      - Go to "Create Enrollment Profile" > "Settings"
        ![](images/2026-09-06-16-18-03.png)

      - Under "User affinity" :
        - Enroll with User affinity means to associate that device with the user, mainly for used with users having company devices assigned to them.

        - Enroll without User affinity means to enroll device without any users linked to it, mainly for shared devices that are accessible by more than 1 user.

    - Under "Select where users must authenticate" :
      - Company Portal will require the device to be installed with company portal app to be registered

      - Setup Assistant is more for new devices so that it can get registered on when new setup is required to configure the device

    - Enrollment program tokens
      - Apple Business Management `(ABM)` and Apple School Management `(ASM)`

        - These are Apple Cloud Service for organizations to centrally manage Apple Devices, Apps, users and automated enrollment
        > ABM knows that these Apple devices belong to your organization. <br><br> Intune Manages them

      1. Click "+ Add" to add enrollment token

      2. Agree to grant Microsoft to send data to Apple and click to "Download public key"
      ![](images/2026-09-06-16-32-04.png)

      3. Click on "Create a token via Apple Business Manager"
      ![](images/2026-09-06-16-32-56.png)

      4. It will bring you to Apple website for you to login to your Apple account.

      5. Go through the steps in Apple and download the token.

      6. Enter your Apple ID and upload the token that you have downloaded in (5)
      ![](images/2026-09-06-16-34-33.png)

  - Android
    - Make sure Managed Google Play is linked / registered

    - Zero touch Enrollment
    ![](images/2026-09-06-16-37-55.png)

      - This enrollment is all configured in cloud so that employees can even receive an unopened device. 

      ![](images/2026-09-06-16-42-49.png)
      
---

<h2>Understanding Roles in Azure and Entra ID</h2>

Roles
- Roles define what users can do within Microsoft Services
- Based on the principle of least privilege
- Central to Role Based Access Control `(RBAC)`
- Used in Azure, M365 and Entra ID to control Access

Azure RBAC Roles
- Role Based access control permissions that manage
  - Who can access Azure resources
  - What they can do
  - What scope. Management, subscription, resource group or resource

- Key Role Types:
  - Owner       : Full access including assigning roles
  - Contributor : Create and manage resources (Excluding RBAC)
  - Reader      : View only access
  - Custom Role : Define specific permissions

- Scope Levels :
  - Management Group > Subscription > Resource Group > Resource

Entra ID Roles
- Predefined sets of permissions that control access to identity and directory resources across M365 and Azure environments
- Roles can be assigned to users, groups or service principles

- Roles Examples :
  - Global Administrator  : Full control across Entra ID
  - User Administrator    : Manage users and groups
  - Security Reader       : View security settings
 
Microsoft 365 Roles
- Built in administrative roles that grant users specific permissions to manage services and compliance features within the Microsoft 365 ecosystem

- Key Built in Roles:
  - Global Admin      : Full access
  - Exchange Admin    : Manage Mailboxes, transport rules
  - SharePoint Admin  : Site collections and settings
  - Teams Admin       : Manage Teams policies and configuration
  - Compliance Admin  : Access Purview features

Principle of Least Privilege
- Give out the least amount of rights, just enough to do their jobs
  
- Mixed with Privileged Identity Management `(PIM)`, we can achieve "Just In Time" `(JIT)` administration using roles.
  
- Example of JIT : IT admin is on leave for the next 2 weeks, give someone a role like User administrator, for that 2 weeks to cover for the IT admin.

Summary 
- Roles = Permissions
- Entra ID is identity focused
- Azure is Resource focused
- M365 is App focused

Best Practices
- Assign roles to groups not individuals
- Follow least privilege
- Regularly review role assignments

---

<h2>Scope Tags</h2>

- Scope Tags seeks out tags that are in the devices enrolled in intune
- We can limit the amount of devices an admin can see by using scope tags.
  - Example would be region tags, US can only see US devices, APAC can only see APAC devices.
- We can also easily add devices to the scope tags by creating a group, e.g."US-DEVICE-GROUP", and assign the scope tag to the group instead of each individual devices

![](images/2026-09-08-04-08-22.png)
- Example on the above where we have 2 region device admins and 2 scope tags, US and UK
- When for example, a US admin that is linked to "US-Devices" scope tag logs in, he can only see devices that are tagged with US-Devices

![](images/2026-09-08-04-11-50.png)
  1. Scope is created
  2. Role Permissions is assigned to the scope
  3. Add / Associate members to the scope
  4. Objects that are tagged to the scope
  5. Members can only work with those objects

- Scope tags can be created under
  - Intune Admin Center > Tenant administration > Roles > Scope tags
    ![](images/2026-09-08-04-20-34.png)
    ![](images/2026-09-08-04-23-40.png)

- When creating roles and permissions, you can add scope tags.
  ![](images/2026-09-08-04-32-37.png)

- You can check if the devices are tagged with scope tags by looking at the properties of the device.
  ![](images/2026-09-08-04-36-33.png)

---

<h2>Compliance Policies</h2>

- Compliance policies help create rules and settings that users and devices must meet to be compliant
- Can be applied to devices or users
- When Combined with Conditional Access, administrators can block users and devices that don't meet the rules.

- When Compliance Policies `with` Conditional Access in place:
  - If Device don't comply, they do not get access to organizational resources

- When Compliance Policies `without` Conditional Access in place:
  - If devices don't comply they don't get restricted but reports are generated for monitoring

- Main criteria for Compliant settings::
  - PIN or password configuration
  - Device encryption
  - Jailbroken or rooted device
  - Email profile
  - Minimum OS version
  - Maximum OS version
  - Windows health attestation

- Outcome of Non-Compliance
  - Remediated
    - Device OS enforces compliance 
    - E.g. User forced to set a PIN or update the OS

  - Quarantined
    - Device operating system doesn't enforce compliance. E.g. Android
      - If conditional access policy applies to user, the device is blocked
      - Company portal app notifies the user about any compliance problems

---

<h2>Conditional Access</h2>

- Conditional Access can be found in 
  - Azure > Entra ID > Security > Conditional Access
  ![](images/2026-09-10-05-03-38.png)

  - Entra portal > Protection > Conditional Access
  ![](images/2026-09-10-05-06-31.png)

- Conditional Access is a tool in Azure that brings signals together for access decision making

- Signals help in decision making on whether to allow access or enforce certain policies

- Common Signals that are used:
  
  - Identities 
    - Microsoft Entra ID 
    - Microsoft Defender for Identity 

  - Applications 
    - Microsoft Defender for cloud

  - Endpoints 
    - Microsoft Defender
    - Microsoft Endpoint Manager

  - Data
    - Microsoft Information Protection

  - Infrastructure
    - Microsoft Cloud App Security

  - Network

- Zero Trust Policy enforcement
  - Every time a connection connects in, it should be checked and rechecked 

  - Nothing is seen as trustworthy just because a user logged in 5 mins ago from the same device

- Signals Example
  - User or Group membership
    - Policies can be targeted to specific users and groups giving administrators fine grained control over access

  - IP Location information
    - Organizations can create trusted IP address ranges that can be used when making policy decisions
    - Administrators can specify entire countries / regions IP ranges to block or allow traffic from.

- Device
  - Users with devices of specific platforms or marked with a specific state
    - E.g. Certain patches to cover major exploits are not patched for devices
  
- Application
  - Users attempting to access specific applications can trigger different Conditional Access policies

- Real time and calculated risk Detection
  - Signals integration with Microsoft Entra ID Protection allows Conditional Access policies to identify and remediate risky users and sign in behavior

- Microsoft Defender for Cloud Apps
  - Enables user application access and sessions to be monitored and controlled in real time

---

<h2>Autopilot Deployment Profiles</h2>

- Autopilot deployment profiles allows the organization to automate the setup and provisioning of Windows devices

- Helps organization to predefine the Out Of Box Experience (OOBE)

- Can automatically join deivces to Entra ID or Hybrid Environments 

- Allows you to customize your naming conventions and cofigure user experiences during the setup

- Allows organization to standadize device deployments

- Allows organizations to deliver a consistent, secure and scalable deployment experience while reducing the time required to prepare these new devices.

<br>
<h2>Autopilot Device Preparation Polices</h2>

- Newer Strategy trying to simplify the approach of deploying Windows devices through Microsoft Intune.

- More for <b>cloud only based deployment</b>

- Does not need hardware hashes or traditional Autopilot registration processes

- Processes are streamlined for deployment for cloud native environments

<br>
<h2>Autopilot Deployment Profiles vs Device Preparation Policies</h2>

- When to use Autopilot Deployment Profiles 
  - Advanced deployment scenarios
  - Hyrbrid join environments
  - When pre-provisioning is required
  - When on premise AD is invovled

- When to use Device Preparation Policies
  - For faster, cloud native deployments
  - Deploying to devices that only joint to Entra ID. 
  - When organization is cloud only, no physical hardware

