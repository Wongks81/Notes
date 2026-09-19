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

> To setup devices to be deployed via deployment profiles, we need to setup a security group with dynamic devices setting. <br><br> 
> For the query to be entered, refer to https://learn.microsoft.com/en-us/autopilot/enrollment-autopilot for reads <br><br>
> But for standard deployment will be `(device.devicePhysicalIDs -any (_ -startsWith "[ZTDid]"))`

![](images/2026-09-13-09-51-42.png)

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

---

<h2>Choosing which Autopilot deployment modes</h2>

1. User Driven Deployment Mode
   - Designed for standard corporate devices that are assigned to a specific end user

   - Process
     - User unboxes the device
     - Connects to network
     - Enters corporate email
     - Autopilot joins device to Entra or Hybrid AD and completes Intune enrollment

    - User Experience
      - Highly interactive
      - User goes through the whole OOBE experience

    - Primary User
      - User who signs in become the primary user

    - Best for
      - Knowledge workers
      - Remote employees
      - Standard business laptops

2. Pre-Provisioning Deployment Mode (White Glove)
   - Splits the setup between IT (or OEM) and end user

   - Process 
     - IT Staff setup the device up to account creation page and trigger provisioning
     - Device is sealed so when the user receives it and signs in, provisioning resumes and completes

    - User Experience
      - Minimal steps for end user
      - They only sign in and skip most setup
  
    - Primary User
      - The first user to sign in after provisioning becomes the primary user

    - Best for
      - Organizations that need to pre load apps, configurations or perform tasks before the device reaches the user

3. Self-Deploying Deployment Mode
   - Fully Automated setup with no user interaction during provisioning

   - The Process
     - Device powers on
     - Connects to the internet
     - Completes Autopilot setup automatically
     - No user account is required during setup
     - Device is ready for use immediately or at a shared kiosk

    - User Experience
      - No OOBE prompts
      - Device goes directly to the desktop or assigned kiosk mode

    - Primary User
      - No Primary User is assigned

    - Requirements
      - Windows 11 with TPM 2.0 and automatic logon configuration

    - Best for
      - Shared devices
      - Dedicated kiosks
      - Digital signage
      - Task workers

  ![](images/2026-09-13-05-29-24.png)

---

<h2>Configuration Profiles</h2>

- Microsoft Intune includes settings and features you can enable or disable on different devices within your organization

- It is something like a cloud equivalent of a GPO and can affect other OS like android and Mac.

- These settings and features are added to "Configuration Profiles"
  - You can create profiles for different devices and different platforms

  - Then use Intune to apply or assign the profiles to the devices

- Usage examples of configuration profiles
  - Allow or prevent access to bluetooth on the device
  - Create a WIfi or VPN profile that gives different devices access to corporate network

- Main Options when creating a Profile
  - Device profiles allows you to add and configure settings and push these settings to devices in your organization

  - Administrative templates
    - On Windows devices, these templates are ADMX settings 

  - Baselines
    - There should be a baseline of configuration before the device should be used in the environment

    - Baselines include preconfigured security settings on Windows devices.

  - Settings catalog
    - Catalog to see all the available settings in one location

  - Templates
    - Predefined groups of alot of settings

    - Include a logical grouping of settings that configure a feature or concept
    ![](images/2026-09-14-05-41-04.png)

  - Properties Catalog
    - <b>Not for changing configuration</b>
    - It is mainly used for gathering data for inventory and reports.
    ![](images/2026-09-14-05-39-59.png)

> If there is a conflict between configuration profiles and Group policies, Group policies will overwrite what is deployed in Intue Configuration Profiles.

---

<h2>Microsoft Tunnel for Intune</h2>

- Microsoft Tunnel is a VPN gateway solution for Intune that runs in a container on Linux and allows access to on-premises resources from iOS/iPadOS and Android Enterprise devices using modern authentication and Conditional Access.

- Setup Process
  - Microsoft Tunnel Gateway installs onto a container that runs on Linux server
  - Linux server can be a physical box or virtual machine.
  - You can deploy Microsoft Defender for Endpoint as Tunnel client app and intune VPN profiles enable iOS and Android devices to use the tunnel to connect to corporate resources.
  - If the tunnel is hosted on the cloud, you will need to use solutions like Azure ExpressRoute to extend your on-premise network to the cloud.

  - Through the Microsoft Intune admin center:
    - Download the Microsoft Tunnel Installation script that you will run on Linux servers
    - Configure aspects of Microsoft Tunnel Gateway like IP addresses, DNS servers and ports
    - Deploy VPN profiles to devices to direct them to use the tunnel.

    ![](images/2026-09-16-05-33-08.png)

---

<h2>Actions in the device sub menu</h2>

![](images/2026-09-16-05-40-09.png)

- Retire
  - When device is connect to intune, a container is created to store all company data, apps and settings
  - Retire instructs machine to remove all company data, apps or settings from the machine
  - Device is not wipe and personnel data will not be deleted.
  - Remove device from intune

- Wipe
  - Factory reset the device to default settings
  ![](images/2026-09-16-05-44-49.png)

- Delete
  - Mainly used for stale device, devices that is no longer in intune. 
  - E.g. old laptops that are decommissioned

- Sync
  - Send a signal to device to tell them to check if there are jobs for them to run.

- Restart
  - Remote restart the machine / device

---

<h2>Security Baselines in Intune</h2>

- Security baselines is a concept in cybersecurity where the device should at least have a certain base level of security on it before it is allowed to operate in the environment.

- To access security baselines, goto 
  - Endpoint security > security baselines 
  ![](images/2026-09-18-05-13-54.png)

- Do take note before when creating a profile for security baselines. The settings might be set to enable on default.

- Settings that is set in the policy after executed in the device will disallow user from changing the state.

---

<h2> Microsoft Defender for Endpoint </h2>

- Is a enterprise grade endpoint security platform designed to help enterprise networks prevent, detect, investigate and respond to advanced threats

- Capabilities
  - Endpoint Behavioral sensors
    - Embedded in Windows, sensors collect and process behavioral siggnals from OS and send this sensor data to private, isolated, cloud instance of Endpoint.

  - Cloud security analytics
    - Behavioral signals are translated into insigghts, detectionss and recommended resposes to adavanced threats.

  - Threat intelligence
    - Enables Defender to identify attacker tools, techniques and procedures and generate alerts when they are observed in collected sensor data.

  - Threat and Vulnerability Management
    - Uses a game changing risk based approach to the discovery, prioritization and remediation of endpoint vulnerabilities and misconfigurations

  - Attack surface reduction
    - Provides the first line of defense by ensuring configuration settings are properly set and exploit mitigations techniques are applied.
    - Capabilities also covers network protection and web protection, which regulate access to malicious IP addresses, domains and URLs.

  - Next generation protection
    - Uses next generation protection designed to catch all types of emeerging threats

  - Endpoint detection and response
    - Endpoint detection and response are put in place to detect, investigate and respond to advanced threats that may have made it past the first 2 security pillars

    - Advanced hunting provides a query based threat hunting tool that lets you proactively find breaches and create custom detections

    - Automated investigation and remediation
      - Defender offers automatic investigation and remediation capabilities that help reduce the volume of alerts in minutes at scale

    - Microsoft secure score for devices
      - Defender includes Microsoft secure score for devices to help dynamically assess security state of Enterprise network, identify unprotected systems and take recommended actions to imptove the overall security of your organization.

    - Microsoft Threat Experts
      - New managed threat hunting service which provides proactive hunting, prioritization and additional context and insights that further empower Security operation centers to identify and respond to threats quickly and accurately.

---

<h2>Managed Device Updates</h2>

- Windows Servicing Model
  - Feature Update : updates that contains new features
  - Quality Update : Monthly updates that happens on patch Tuesday (2nd Tuesday of each month)

- Update Channels
  - Windows Insider
    - Receive feature updates months before they go public
    - Has to be turned on in Windows Settings
    - Mostly to be used on test lab / pilot computers

  - General Availability
    - Receive feature updates when they go live or a few months later
    - Mostly used by the majority of production computers

  - Long Term Servicing Channel (LTSC)
    - Mostly used for critical workstation that feature updates could cause problem for
    - Must install LTSC version of Windows in order to have this option.

- Windows Update Rings
  - Something like a timeframe
  - Tie to servicing channels as follows
    - Preview
      - E.g. Preview Ring might contain a group of test computers that will install Windows Insider updates as soon as it is out.

    - Limited
      - Machines in this group might hold off the updates till further testing as it might be connected or installed with sensitive machines that might not be happy with the updates

    - Broad
      - The general group where all the machines will be updated.

- Delivery Optimization
  - Peer to Peer option that allows Windows computers to download updates and share them with neighboring computers on the same network or sometimes even internet

