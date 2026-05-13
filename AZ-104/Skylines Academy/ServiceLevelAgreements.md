<h2>Service Level Agreements (SLA)</h2>

SLA is an agreement witht he business and application teams on the expected performance and availability of a specific service

General SLA Practices :
- Define SLA for each workload
- Dependency mapping
  - Make sure to include internal / external dependencies
- Identify single point of failure
  - E.g. Workload requires 99.99% but depends on a service that only has a 99.9% non failure rate.
  - So there is no chance to gurantee the SLA that is given at 99.99%

---

Key Terms
- Mean Time to Recovery (MTTR)
  - Average time to recover service from an outage

- Mean Time Between Failures (MTBF)
  - Average time between outages

- Recovery Point Objective (RPO)
  - Interval of time in which data could be lost during a recovery
  - E.g. 5 mins of RPO means up to 5 mins of data could be lost during recovery

- Recovery Time Objective (RTO)
  - Time requirement for recovery to be completed in before there is business impact

---

Composite SLAs
- Is a SLA that involves a service depending on another service to work
- We need to know how to calculate the service SLA

![](images/2026-04-24-05-25-22.png)

---

![](images/2026-04-24-05-26-32.png)

---

<h3>Business Continuity</h3>

Disaster Recovery Consideration

- Azure Regional Outage

  - When the whole region that your resources are in went offline due to this and that issue. 

  - Customers who do not have multi region backup will have their services affected

  ![](images/2026-04-25-04-38-34.png)

  - Region Pairs helps protect against regional outages
  
- Azure Service Outage
  
  - Considered single or multiple Azure service outage

  - E.g. Azure SQL service down for all regions

  - Considerations need to be taken on services that you are using in Azure, make sure there is another backup option that does not rely on Azure services (E.g. On Premise)

  - If unable to, you will need to accept the risk that comes with the SLA

- Azure wide Outage

  - Azure totally went offline

  - A consideration but very very rare chance it will happen

- Individual workload issue

  - E.g. VMs not configured properly for workload and users hitting the service in the VMs consistently causing degradated performance

---

<h3>Business Continuity Strategies</h3>

High Availability
- Parallel running multiple instances of apps to distribute workload and also to keep the app running in the event that one of the instances went down.

![](images/2026-04-25-04-47-35.png)

- Use Availability Sets or Zones to help setting up the service for better coverage.

![](images/2026-04-25-04-56-14.png)

Disaster Recovery
- Recovery from another datacenter in the event there are failures in the main datacenter 

![](images/2026-04-25-04-50-54.png)

- Use region pair to help with mitigating the risk of outage in a region

Backup
- Mainly for restoring files or data
- Keep another copy of the files or data in Blobs, tapes or another file server

![](images/2026-04-25-04-53-23.png)