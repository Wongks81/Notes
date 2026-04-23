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

