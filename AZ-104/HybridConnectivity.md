<h2>Hybrid Connectivity Options</h2>

<h3>Gateway Reccomendations</h3>

![](images/2026-04-19-04-44-21.png)

---

<h4>Site to Site (S2S) VPN</h4>

- Connecting Data center over a vpn device to Azure

![](images/2026-04-19-04-35-29.png)

- S2S VPN gateway connection is a connection over <b>IPsec/IKE</b> (IKEv1 or IKEv2) VPN tunnel
- Requires a VPN device in enterprise datacenter that has a public IP address assigned to it
- Must not be located behind a NAT
- S2S connections can be used for cross premises and hybrid configurations

---
  
<h4>Point to Site (P2S) </h4>

- Connecting devices like laptops directly to virtual network
- Like VPN to office network

![](images/2026-04-19-04-39-39.png)

- Secure connection from individual computer
  - Great for remote worker situations
- No need for VPN device or public IP, can connect as long as there is internet
- Throughput up to 100Mbps 
- Does not scale easily

---

<h4>ExpressRoute</h4>

- Dedicated circuit for Azure
- For users who feel Azure is a permanent extension to their datacenters

![](images/2026-04-19-04-50-02.png)
>Partner's Edge is the devices that are provided by yourself or 3rd party vendors, that is connected directly physically to Microsoft Edge 


<h4>ExpressRoute Connectivity Models</h4>

![](images/2026-04-19-04-55-03.png)

<h4>Key Benefits of ExpressRoute</h4>

- Layer 3 Connectivity (Network Layer)
  - Allows resource sharing between on premise and Azure network

- Connectivity in all Regions
  - Connect to Microsoft Cloud services across all regions in the geopolitical region

- Global Connectivity (<b>Premium Add On</b>)
  - Premium add on allows you to have access to Microsoft services across all regions with no limit

- Dynamic Routing
  - Uses Border Gateway Protocol (BGP) for connection between your network and Microsoft

- Built In Redundancy
  - Redundancy for better reliability

---

<h4> Hybrid Connection </h4>

![](images/2026-04-20-06-40-45.png)

- Allows Web App to talk to the datacenter

- Hybrid Connection can be shared across Web Apps and Mobile Apps

- All Web App Frameworks supported 

- Example Scenarios:
  - .Net Framework Access to SQL Server
  - PHP Access to SQL server or MySQL
  - Java Access to SQL server
  - Java or .Net Framework access to HTTP/HTTS Services

- Hybrid Connection Manager can be installed on the following operating systems:
  - Windows Server 2008 R2 and requires :
    - .Net Framework 4.5+
    - Windows Management Framework 4.0+

- Windows Server 2012 and requires :
  - .Net Framework 4.0+

- Windows Server 2012 R2








