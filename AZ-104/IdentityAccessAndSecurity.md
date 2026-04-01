<h2>Identity Access and Security</h2>

Core Identity Services:
1. Microsoft Entra ID (Azure AD)
2. Aceive directory Domain Services (ADDS)
3. Entra Domain Services (Azure AD Domain Services)

<h3> Microsoft Entra ID </h3>
- Previously Known as Azure Active Directory (AAD)
- Is Azure cloud based identity and access management service

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