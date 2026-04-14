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


