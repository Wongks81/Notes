<h2>Azure Storage </h2>

<h4>Types of storage</h4>

- Structured Data (E.g. SQL)
  - Adheres to a schema 
  - All the data has the same field or properties
  - Stored in a database table with rows and columns
  - Relies on keys (<b>E.g.Primary Keys</b>) to indicate how one row in a table relates to data in another row of another table
  - Referred to as "Relational Data"

- Semi Structured Data
  - Does not fit neatly into tables, rows and columns
  - Uses tags or keys to organize and provide a hierarchy for the data
  - Often referred to as NoSQL or non-relational data

- Unstructured Data
  - No designated structure
  - no restrictions on the kinds of data it can hold
  - E.g. Blob can hold JPEG, PNG, PDF, VID etc..

---

<h3>Benefits of Azure storage</h3>

- Durable and Highly Available
  - Redundancy ensures data is safe in the event of transient hardware failure


  - Gives an option to replicate data across datacenters or regions

- Secure
  - All data written to Azure storage is encrypted by the service
  - Fine grained control over data access

- Scalable
  - Massively scalable to meet storage and performance needs of taodays applications

- Managed
  - Azure handles hardware maintenance, updates and critical issues

- Accessible
  - Accessible from anywhere in the world over HTTP or HTTPS
  - Accessible via provided client libraries supporting a variety of programming languages

---

<h3> Azure Storage Data Services </h3>

- Azure Blobs
  - Massively scalable object store for text and binary data

  - Includes support for big data analytics through Data Lake Storage Gen 2

- Azure Files
  - Managed file shares for cloud or on-premise deployments

- Azure Queues
  - Messaging store for reliable messaging between application components

- Azure Tables
  - A NoSQL store for schemaless storage of structured data

- Azure Managed Disks
  - Block level storage volumes for Azure VMs

---

<h3>Replication Options</h3>

- Locally Replicated Storage (LRS)
  - Replicated 3 times within a storage scale unit.
  > E.g. You have 3 sets of same data in a storage rack

  - Hosted in a datacenter in the same region as where the storage account is created

- Zone Replicated Storage (ZRS)
  - Replicated 3 times across one or two datacenters in addition to storing 3 replicas
  > You have 3 sets of same data in 3 different rooms in the company( Zone ) <br> 

  - ZRS can recover data even in the event that the primary datacenter is unavaiable or unrecoverable
    - Data will be recovered from the other 2 datacenters
  
  > So even if one room caught fire or power trip, the other 2 will take over and reduplicate the data once the room recovers.

- Geographically Replicated Storage (GRS)
  - Replicates your data to a second regoin that is hundreds of km away from the primary region.

  > Data is duplicated to another office in another location / building / country.

  - Data is recoverable even if the whole region(zone) has an outage.

  > Even if the main office suffers from natural disasters or power trip, you can recover data from the other office.

- Read only Grographically Replicated Storage (RA_GRS)

  - Same replication as GRS

  - Data is live as it is constantly updated from primary region with a time lag in seconds to minutes.

  - Secondary region can only do a read on the data

---

<h3>Azure Blob Storage </h3>

- Object storage solution for massive amounts of <b>unstructed</b> data

- Stores files of any type including images, videos

- Use cases:
  - Streaming video and images direct to user
  - Backup of data
  - Archiving

<h4> Storage account types </h4>

- General Purpose Version 2
  - For normal usage, this is the default selection
  - Supports LRS, GRS, ZRS and RA-GRS

- Premium Block Blobs
  - For accounts that have high transactions rates
  
  - Or require low storage latency 

  > E.g. Applications like instagram where millions of people are uploading and downloading pictures every second

  - Supports LRS and ZRS

- Premium File Shares
  - Premium storage account for only file shares

  - Recommended for enterprise or high performance scale operations

  - Supports LRS and ZRS

- Premium Page Blobs
  - Premium storage account for only Page Blobs

  - Recommended when you need high paging activity read write operations

  ![](images/2026-04-04-16-54-14.png)

---

<h3>Storage Tiers based on Access Requirements</h3>

- Hot Tier ( Frequently accessed data )
  - Higher storage cost
  - Lower access cost

- Cool & Cold Tier
  - Lower storage cost
  - Higher access cost
  - Intended for data that will remain:
    - Cool for 30 days ( Data that are not oftenly used but when you need it, it will load fast )

    - Cold for 90 days ( Data that are almost not used and optimized to save cost )

- Archive
  - Lowest storage costs
  - Highest retrieval costs
  - Designed for rarely accessed data of 180 days or more.

---

<h3>Azure Table Storage</h3>

- A NoSQL key-value store
- Schemaless design
- Structured or Unstructed data
- Access using Odata protocol, LINQ queries, WCF Data Service or .NET Libraries

---

<h3>Azure Queue Storage</h3>

- Provides a reliable mechanism for storage and delivering messages for applications
- Single queue message can be up to 64KB in size 
- Queue can contain millions of messages

---

