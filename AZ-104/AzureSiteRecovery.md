<h2>Azure Site Recovery (ASR) Overview</h2>

On-Premises to Azure Recovery
- On-Premises to Azure Recovery Tool / Migration Tool
  - Take VMware or Hyper V workloads and replicate them to Azure for recovery / migration

Azure to Azure Recovery
- Recover workloads from Primary in a Secondary target region
- Secondary region as a backup in the event of an event failure in the primary region

Automation and Orchestration
- Setup recovery plans to customize the order in which services are restored and subsequent scripts that need to be run
- Rich integration into Azure Automation for additional automation requirements

Recovery Time Objectives (RTO) and Recovery Point Objective (RPO) targets
- Continuous replication for Azure, VMware and Hyper V

Azure Site Recovery Frequency
- Data or resources can be replicated in the interval of :
  - 30 seconds
  - 5 minutes
  - 15 minutes

VMware to Azure Recovery, the ASR process
- Converts VM to VHD
- Uploads to Azure
- Migration completed from recovery vault

VMware Migration Process
1. Prepare Azure
   - Verify Account permissions
     - Able to create a VM in the resource group?
     - Able to create a VM in the selected network?
     - Able to write to selected storage account?

    - Create Storage account

    - Create Recovery Services Vault
    
    - Setup Azure network
 
2. Prepare VMware
    - VMware permissions
        - https://docs.microsoft.com/en-us/azure/site-recovery/vmware-azure-tutorial-prepare-on-premises

        ![](images/2026-04-27-05-55-55.png)

    - Prepare an account for Mobility service installation

    - Verify Compatibility

      - VMware Support Matrix

      - Linux VMs, Check system requirements

      - Verify Network and Storage

      - Check post failover configuration support

      - Validate Azure VM requirements

    - Prepare connectivity to Azure VMs
      - Check if VMs can be access from required users / services    

3. Setup Recovery

---

Azure Backup
- Backup solution purpose built for Cloud

- Unlimited Scaling

- Unlimited Data Transfer

- Multiple Storage Options

- Long Term Retention

- Application Consistent Backups

- Data Encryption
