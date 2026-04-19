<h2> Networking </h2>

<h4>Hub Virtual Network</h4>

- Something like a shared services for your network
- Normally has a gateway subnet to connect to On Premise Network via ExpressRoute or gateway services
- Can be connected to Spoke network via virtual network peering
  > Spoke is a Virtual network that holds specific applications / VMs <br><br>
  > So connecting to Spoke is something like remoting in from Azure machines

<h4>Virtual Network Capabilities</h4>

- Basically Isolated networks
- Provide Internet Access
- Allow Azure Resource Connectivity
- Allow On Premises connectivity through ExpressRoute or gateway services
- Traffic Filter (Network Security Group), filter traffic like a firewall.
  - Restrict communication between services
- Offers Routing where we can route where the traffic goes
- With Virutal network peering, can connect virtual networks together

---

<h4>Network Securty Overview</h4>

- Network Access Control
- Firewall
- Secure remote access and cross premises connectivity
- Availability
- Name Resolution
- Global Traffic Routing
- DDoS
- Monitoring and Threat Detection
- Logging and Auditing

---

<h4>Network Access Control</h4>

- Network Layer Control
  - Secure Deployments through Network Security Groups(NSG), Application Security Group,Azure Security Center(ASC) and service endpoints
    - NSG can limit communications between VMs or subnets
    - Application Security Group can control the access of particular service or application
    - ASC have Just In Time VM access where somebody can request access for a VM for a period of time
    - Service Endpoints can restrict access 
      > E.g. Remove public access to blob storage

- Resource Control and Forced Tunneling
  - Control routing behavior on VNets with custom behavior and shuts down devices initiating connections to the internet via Forced Tunneling

- Virtual Network Security Appliances (E.g. Firewalls)
  - Enable security level higher than network for extra protection

- Azure Firewall
  - Cloud based network security service to protect Azure Virtual Network resources

---

<h4>Secure Remote and Cross-Premises Connectivity</h4>

- Connect individual workstations to a VNET
  - Using a service called point to site VPN connection

- Connect on premises network to a VNET with a VPN
  - Using a service called site to site VPN connection

- Connect on premises network to a VNET with a dedicated WAN link
  - Using a service called ExpressRoute

---

<h4>Availablity (making services available 24/7)</h4>

- HTTP Load Balancing (App Gateway)
  - Ensure availability of services

- Network Load Balancing (Azure Load Balancer)

- Global Load Balancing (Traffic Manager)

--

<h4>Other Network Security Factors</h4>

- DNS
  - Making sure the DNS is the <b>CORRECT</b> DNS server that you should be using

- Global Traffic Routing (Front Door)
  - Allows more efficient routing of your global traffic

- Monitoring and Threat Detection

- Logging and auditing of traffic

---

<h4> Network Security Groups (NSG)</h4>

- Is a Network Traffic Filter
- Used to allow or restrict traffic to resources in Azure network
- Has 2 types of rules, Inbound and Outbound
- Can be associated to subnet or NIC

- NSG Properties to configure
  - Protocol, E.g. TCP/UDP
  - Source and Destination Port Range
  - Source and Destination Address prefix
  - Direction of flow, Inbound or Outbound
  - Priority of rules, which should be validated first
  - Allow or Deny Access

- NSG Rule Priority
  - Rules are enforced based on priority
  - Ranges from 100 to 4096
  - Lower numbers have higher priority
  - Can use NSG default tags for easier identification on the service you need.
    - E.g. Use Azure Load Balancer tag instead of sourcing for its IP address.

---

<h4>Azure Firewall </h4>

- Cloud based network security service to protect Azure Virtual Network resources

- Fully stateful firewall service

- Key Features of of Firewall

  - Has built in High Availability
    - No need for load balancers

  - Availability Zone Support
    - Can span across availability zones

  - FQDN Filtering Rules
    - Limit outbound traffic to a specified list of fully qualified domain names

  - Network Traffic Filtering Rules
    - Centrally create allow / deny network filtering rules by source and desination IP, port and protocol

  - FQDN Tags
    - Allow well known traffic through firewall (e.g. Windows Update tag)
    - Create the App rule and include the tag

  - Service Tags
    - Microsoft managed groupings of services

  - Threat Intelligence
    - Filter traffic based on Microsoft Threat intelligence feed

  - SNAT / DNAT Support
    - SNAT : Source Network Address Translation
    - DNAT : Destination Network Address Translation

---

<h4> Azure Load Balancer Technologies </h4>

Load Balancing Services includes
  - Load Balancer (Basic & Standard Tier)
  - Application Gateway
  - Traffic Manager
---
Key features of Basic Load Balancer
  
  - OSI model layer 4
  - Supports up to 100 instances
  - Service monitoring
    - Probes to monitor health of instances
  - Automated reconfiguration
    - Auto configure itself when for example scaling up or down VMs
  - Hash based distribution
    - Contain 5 tuples hash which contains :
      - source IP address
      - source port
      - destination IP address
      - destination port
      - IP protocol number
  
  - Internal and public options
    - Can be attached to public IP address
    - Balance internal services

---
Key features of a Standard Load Balancer

- OSI model Layer 4
- Supports up to 1000 instances
- Any virtual machines in a single VNET
- Supports HTTPS
- Availability Zone support
- Secure by default

---

>Key point
>- Basic Load balancer is scoped to availability set
>- Standard Load balancer is scoped to the entire virtual network

---

Key Features of Load Balancing: App Gateway

- OSI Model layer 7
- Cookie based session affinity
- SSL offload
  - Can help with encrypting 
- Supports End to End SSL
- Web applications firewalls
- URL based content routing
- Requires its own subnet
- HA supports availability zones

![](images/2026-04-17-05-35-24.png)

>URL based Routing
![](images/2026-04-17-05-36-15.png)

---

<h4> Routing and Peering </h4>

System Routes
- Every subnet has a route table that contains the following minimium routes:

| Route       | Description                                                                               |
| ----------- | ----------------------------------------------------------------------------------------- |
| Local Vnet  | Route for local addresses <br><br> No next hop value                                      |
| On-Premises | Route for defined on premises address space <br><br> VNet gateway is the next hop address |
| Internet    | Route for all traffic destined to the internet <br><br> Internet gateway is the next hop address |
---

Default Routing in a Subnet

![](images/2026-04-20-06-13-04.png)

- If address is within th VNet address prefix : Route to local VNet
  
- If address is withing the on premises address prefixes or BGP published routes (BGP or Local Site Network for S2S) : Route to gateway

- If the address is not part of the VNet, BGP or LSN (Local Site Network) routes :  Route to internet via NAT

- If destination is an Azure datacenter address and ExpressRoute peering is enabled : Route to gateway
  - Microsoft advertised its thousands of IPs for router to pick up

  - Routers will know to use ExpressRoute if traffic is going to the listed IPs
  
  - Connects to Microsoft Services in the cloud

- If the destination is Azure datacenter with S2S or ExpressRoute without public peering enabled : Routed to Host NAT for internet but next leaves datacenter
  - ExpressRoute connect on premise and Azure via a dedicated line.

  - Can consider Azure to be an extension of the on premise network, which is why we route via gateway

  - Any traffic going to Azure services like Blob or SQL will go through standard ISP network instead of ER

  - Connects to your private network


---


