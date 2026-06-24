<h2>Foundation Notes<h2>

![](images/2026-06-25-05-53-39.png)

# Notes on AD before Start

<h3> Some Notes to review before Start </h3>

DNS - Domain Name Server

- A server that associates Name and IP address for the domain.

- All machines in domain would register with DNS

  - This allows the centralization of name resolution

  - IP addresses and hostname will be paired and saved into the DNS database

- To find the IP address or the Hostname of a machine, user can query DNS to get the answer

GPO - Group Policy Objects

- An object that you can create that can change all the settings parameters, attributes of the machines that is managed by the domain.

<br>

# Notes on Remote Access Service (RAS)

- A service that is used by windows to support VPN
  - In today's concept it is referred to as RRAS (Routing and Remote Access Service) 

- Allows VPN tunnel to be created and communication using this tunnel is encrypted

<br>

# Notes on DMZ Zone (Perimeter Network)

- The zone is created when there is a need for 2 Firewalls, mainly for application or web servers that allows users from the internet to access them

  - The first firewall that is used on the edge of the internal network to protect the domain 

  - The 2nd firewall is used on the front end of the service which is connected to the internet.

  - The zone in between is called the DMZ zone.

![](images/2026-06-25-05-11-45.png)

- Internet ports 80/443 is only open on the 2nd firewall to allow users to access the web / application servers.

- Connections to domain network via first firewall are strictly contained so that none of the users from the internet can access it.

<br>

# Notes on Cloud Services

- IaaS : Infrastructure as a Service (Azure)

  - Cloud Service that the vendors (with Datacenters) host the Virtual Devices for consumers (Users)
  - Virtual Devices include Virtual Machines, Virtual Storage, Virtual Network etc...
  - Basically anything you can create in on premise network, the service is able to host for you.
  
- SaaS : Software as a Service

  - Fully functional app or application that is ready for you to start using 

- PaaS : Platform as a Service

  - Software platform that is available and ready to be used.
  - Difference to SaaS is that user will have to administer it and use it before it can do anything
  - Intra ID is an example
    - When you first access it, it only has an admin account. 
    - Therefor you need to go in to add users, create groups for it to work as needed.

<br>

# Notes on Azure and M365

- Azure mostly geared to IaaS 
- M365 have both PaaS and SaaS services in it
![](images/2026-06-25-05-45-03.png)
*Entra ID is shared between both Azure and M365

- For consumption and payment:
  - Azure : You are paying for CPU, RAM, Storage
  - M365 : You purchase subscription licenses in order to use the services provided

- Entra Connect : Server that is needed to
  - Sync the accounts between on premise AD and cloud Entra ID
  - Provide seamsless Single Sign On (SSO) where when user logins to the domain, it actually logins to both the on premise and the cloud service network.

  > Take note that you can only sync towards the cloud and not from cloud back to on premise



