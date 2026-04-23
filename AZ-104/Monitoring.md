<h2>Azure Monitoring</h2>

Overview
- Monitor and Visualize Metrics
- Query and Analyze Logs
- Setup Alerts and Actions

![](images/2026-04-21-04-55-25.png)

---

What does Azure Monitor Collect?

- Application Monitoring data
  - Data about the performance and functionality of the code

- Guest OS monitoring data
  - Data about the operating system on which your application is running
  - OS can be running in Azure, other cloud services or on premises

- Azure resource monitoring data
  - Data about the operation of an Azure resource

- Azure subscription data
  - Data about the operation and management of an Azure subscription
  - Health and operation of Azure itself

- Azure tenant data
  - Data about the operation of tenant level Azure services such as AAD (Azure Active Directory)

---

Diagnostic Logs

- Each Azure resource requires its own diagnostic setting, which defines the following:

  - Categories of logs and metric data sent to destinations defined in the setting

  - Available categories will vary for different resource types

- One or more destinations to send the logs

  - Current destinations include :
    - Log Analytics
    - Event Hubs
    - Azure Storage 

---

Key Monitoring Solutions

- Azure Monitor for Virtual Machines
  - Monitor the availablity, performance and usage of your windows and Linux VMs at scale

- Azure Monitor for Containers
  - Monitor the performance of container workloads deployed on Azure Kuberbetes Service

- App Insights
  - Monitor the availability, performance and usage of your web applications

---

Log Analytics 

- Central Role in Monitoring
  - Bring all the data that is monitored by other services together in one place

- Data Sources
  - Services or devices you can connect to
  - E.g. VM you want data on

  ![](images/2026-04-22-05-57-32.png)

- Other analytics Sources 
  - E.g. Security Center and App insights have their own Log Analytics

- Search Queries
  - Query the data to get what you needed

  - Search Query Fundamentals :
    - Start with the source table (e.g. Event)
    - Follow on with a series of operators
    - Separate out additional operations by using pipe | 
    - Join other tables and workspaces using "union"

- Output options
  - Alot of output options for us to select

![](images/2026-04-22-05-49-46.png)

![](images/2026-04-22-05-55-31.png)

