<h2>Identity Access and Security</h2>

Core Identity Services:
1. Microsoft Entra ID (Azure AD)
2. Aceive directory Domain Services (ADDS)
3. Entra Domain Services (Azure AD Domain Services)

---
<h4>Core features:</h4>

- Authentication
  - Employee sign in to access resources
  
- Single sign on (SSO)
  - Ease of only a single sign in to access all resources
- Application Management
  - Tie identities to application 
- Business to Business (B2B)
  - Connect to another company to share resources or services 
- Business to Customer (B2C)identity services
  - Either using other identity services (Google, Facebook) for access management
  - Or using our identity access to login to other services provided by Customer
  - Device Management
    - Keep track of devices and use it for conditional access policies
---

<h3>Active Directory Domain Services (ADDS)</h3>

- Legacy Active Directory since Windows 2000
- Traditional Kerberos and LDAP functionality

<h3>Azure Active Directory Domain Services</h3>

- Replacement for ADDS in cloud form
- Provides managed domain services
- Allows you to be able to use domain services without the need to patch and maintain domain controllers on IaaS

- Supports all of the following:
  - Domain Join
  - Group Policy
  - LDAP
  - Kerberos
  - NTLM

- Can also be used to run legacy applications that can't use modern authentications standards in the cloud
- Can be configured to automatically sync from local ADDS using <b>Microsoft Entra Connect</b>

![](images/2026-04-02-06-13-47.png)

---

<h3> Microsoft Entra ID </h3>

- Previously Known as Azure Active Directory (AAD)
- Is Azure cloud based identity and access management service

![](images/2026-04-02-14-04-27.png)

- Enterprise Identity Solution
  - Creates a single identity for users and keep them in sync across the enterprise

- Single Sign On (SSO)
  - Provide Single Sign on access to applications and infrastructure services

- Multifactor Authentication (MFA)
  - Enhance security with additional factors of authentication

- Self Service
  - Empower users to complete password resets themselves 
  - Empower users to request access to specific apps and services

---

<h3>Azure B2B and B2C </h3>

Business to Customer (B2C) <br>
** Social IDs or User IDs **
- Securely authenticate customers using their preferred identity provider
  - E.g. Google, facebook
  
- Can captureCapture login, preference and conversion data for customers
  - Conversion data is the actions that the customer have taken while using the website
    - Making a purchase
    - Downloading apps
    - Adding items to cart
  
- Provides Branded (white-label) registration and login experiences
  - White label registration:
    - Giving a look that belongs to your company but the backend process might be proccess by other 3rd part vendors

Business to Business (B2B) <br>
** Partners and other business entities **
- Method for allowing other business entities to use their IDs

![](images/2026-04-03-04-50-55.png)

---

<h3>Azure Policies</h3>

- Used for enforcing governance to resources

- Ensure users can only access within the boundaries admin has set in the portal

- They are available:
  - Built in by Microsoft
  - Custom created by Admins
  - Downloadable from the community

- Can be sssigned to Subscriptions to affect everyone or to Resource Groups to affect only that group.

