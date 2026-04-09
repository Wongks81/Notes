<h2> Virtual Machines </h2>

> Note: When creating new Virtual Machines, you can select the "Models"(VM Size) of the VMs

![](images/2026-04-08-05-18-01.png)

> VMs have their own lifecycle so you will need to move to a new VM "Model" when you receive a notification on it.

https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/retirement/retired-sizes-list

---

<h4> VM Availability Sets </h4>

- To group 2 or more machines in a set

- Seperated based on Fault Domains and Update Domains

- This is to prevent any unexpected issues when the following occurs:
  - Planned Maintenance
  - Unplanned hardware maintenance
  - Unexpected downtime

---

Fault Domains
- Think of it similar to LRS but in 1 datacenter

  ![](images/image2.png)

-  By group the machines into availability sets, the machines will be spread out across different servers in 1 datacenter.
   -  So when 1 of the machines goes down, the other machines in the group will continue to work.

Update Domains

- Groups that are rebooted at different times

- If you have 5 virtual machines and set 5 update domains, each machine will belong to 1 update domain. So it will reboot one at a time.

- Azure gurantees only 1 update zone is updated at a time, the rest are all running.
