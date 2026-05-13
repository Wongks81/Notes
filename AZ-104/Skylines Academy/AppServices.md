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

---

<h4>Management Tools</h4>

- Azure Management Portal
- Kudu (System Control Manager)
- Visual Studio
- Powershell
- CLI

<h4>App Service Plan Metrics</h4>

| Component         | Description                                                                                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPU Percentage    | Average CPU used across all instances of the plan                                                                                                                                               |
| Memory Percentage | Average memory used across all instance of the plan                                                                                                                                             |
| Data In           | Average incoming bandwidth used across all instances of the plan                                                                                                                                |
| Data Out          | Average outgoing bandwidth used across all instances of the plan                                                                                                                                |
| Disk Queue Length | Average number of both read and write requests that were queued on storage <br><br> High disk queue length is an indication that an application might be slowing down due to excessive disk I/O |
| HTTP Queue Length | Average number of HTTP requests that had to sit on the queue before being fulfilled <br><br>HIgh or increasing HTTP Queue length is a symption of plan under heavy load  |

---

<h4>Free and Shared App Quotas</h4>

| Component   | Description                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| CPU (Short) | Amount of CPU allowed for this application in a 5 minute interval<br><br>Quota resets every 5 minutes                       |
| CPU (Day)   | Total amount of CPU allowed for this application in a day<br><br>Quota resets every 24 hrs at midnight UTC                  |
| Memory      | Total memory allowed for this application                                                                                   |
| Bandwidth   | Total amount of outgoing bandwidth allowed for this application in a day<br><br>Quota resets every 24 hours at midnight UTC |
| Filesystem  | Total amount of storage allowed |

---

<h4>Results of exceeding Quotas</h4>

| Component   | Description                                                                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPU         | Exceeding either CPU (short) or CPU (day) will result in the application being stopped until the quota resets.<br><br>During this time, all incoming requests will results in HTTP403 |
| Memory      | The Application is restarted                                                                                                                                                          |
| Bandwidth   | Application is stopped until the quota resets<br><br> During this time, all incoming requests will results in HTTP403                                                                 |
| Filesystems | Write operation including writes to logs will fail |

---

<h4>Azure Web Appl Diagnostic Logs</h4>

- Application Logs
  - Errror
  - Warning
  - Information
  - Verbose

- Web Server Logs
  - Web Server Logging
    - Information about HTTP Transactions
    - E.g. 
      - How many request from a specific IP
      - Number of requests handled

  - Detailed Error Message
    - Detailed error information for HTTP status codes that indicate failure

  - Failed request tracing
    - Detailed information on failed requests
    - Including the trace of IIS components that were used to process the request

---

<h4>Diagnostic Logs and Locations </h4>

| Type                  | Location - /LogFiles/ |
| --------------------- | --------------------- |
| Application Logs      | Application/          |
| Failed Request Traces | W3SVC#########/<br><b>*The # are numbers</b>       |
| Detailed Error Logs   | DetailedErrors/       |
| Web Server Logs       | http/RawLogs          |
| Deployment Logs       | /Git |

---

<h4>Deployment Slots</h4>

- Mainly used for testing changes as it is running live before changing it to production

- Allows you to deploy in non-produdction slots

- Applies to Web Apps on Windows and Linux, API and Mobile Apps

- Reduces risk and increases speed

- Apps deployed in the staging slots are live running applications

- Staging slot can seamlessly be swapped to and fro production and staging

<h4>Swapped vs Non Swapped Settings</h4>

- Swapped
  - General settings:
    - framework version
    - 32/64 bits
    - web sockets

  - App settings
    - Can be configured to stick to a slot

  - Connection strings
    - Can be configured to stick to a slot
    - Like the staging slot can be connected to dummy data instead of production

  - Handler Mappings

  - Monitoring and diagnostic settings

  - Webjobs content

- Not Swapped
  - Publishing endpoints
    - URLs and credentials used to deploy apps

  - Custom Domain names
  - SSL certs and binding
  - Scales
  - WebJobs Schedulers