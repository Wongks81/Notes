<h2>Web App Services</h2>

Azure App Services consist of the following:
- Web Apps
- Mobile Apps
- Logic Apps
- API Apps

---

<h4>Web Apps</h4>

- Formerly known as "Websites"
- Host and build apps with various programming language
- Auto-scalable
- Highly-available
- Devops features to automate deployments

---

<h4>Mobile Apps</h4>

- Build mobile device backend
  - Give developers mobile friendly enviroment
- Highly scalable and Highly available
- Allows building native apps for iOS, Android, Windows and cross platform apps
- Share same App Service deployment to reduce run rates

---

<h4>Logic Apps</h4>

- Automate business processes and workflows
- Use the orchestration engine to build a solution

>Every time app calls the API to do some task

<h4>API Apps</h4>

- Allows us to easily create, consume and call APIs
- Option to use APIs that are created
- Could also be from external API services

---

<h4>Security Features</h4>

- Any App Services will be run on isolated Virtual Machines
  
- Meets all the ISO standards like ISO, SOC and PCI compliant
  
- Fully Intergrated with Azure AD for authentication measures (Including social logins)
  
- Service Identity allows app to easily access other Azure AD protected services like Azure Key Vault

- Support custom domains, SSL/TLS, including custom certificates using wildcard or subject alt name

- Supports multiple authentication protocols:
  - OAuth
  - OpenID
  - Microsoft Active Directory

- Intergrates with Web Application Firewall (WAF) service

---

<h4>DevOps features</h4>

- CI/CD support is available through git, GitHub, Bitbucket, Docker Hub and VSTS

- Integrate with popular IDE tools such as Visual Studio

- Supports deployment from external folder sources such as OneDrive or Dropbox

- Have deployment Slots that allows us to stage environment:
  - Stage environment are pre-production environment
  - Normally used to test anything and everything before turning it into a production environment

---

<h4>App Service Environment (ASEs)</h4>

- Fully isolated environment

- For High-performing apps 
  - High CPU and/or memory

- Able to use individual or multiple service plans
  
- Can be deployed internal or external
  - Internal : deployed with internal IP via internal load balancer
  - External : when you want ASE to be access over the internet

- Created in a subnet of a VNet, which achieves isolation

- Note: May take a few hours to spin up.