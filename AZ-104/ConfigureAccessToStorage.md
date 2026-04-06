<h2>Configure Access to Storage</h2>

<h4>Manage Access</h4>

- Container Access
  - Public Access can be configured by the Access Policy in the settings

  - 3 policy can be selected:
    - Private   :   No Anonymous Access
    - Blob      :   Anonymous read access for blobs only
    - Container :   Anonymous read access for containers and blobs

![](images/2026-04-07-03-52-37.png)

- Shared Access Signature (SAS)
  - It is a query string that we add on to the URL of the storage resource

  - String informs Azure what access should be granted

  - Utlizes hash-based message authentication

  - Controlled by Stored Access Policies
    - Group shared access signatures
    - Provides additional restrictions
    - Can be used to change the start time, expiry time, permissions or revoke it after it has been issued
    - Only supports <b>Service SAS</b> on blobs, file shares, Queus and Tables

  - Account SAS Tokens
    - Granted at the account level to grant permissions to services within the account

  - Service SAS Tokens
    - Grants access to a specific service within a Storage account

![](images/2026-04-07-03-58-19.png)
![](images/2026-04-07-04-00-36.png)

Signed Service:
> b = blob, f = file, q = queue, t = table

Signed Resources Types
> s = service, c = container, o = object

Signed permissions
> rwd = read, write, delete <br>
> l = list, a = add, c = create, u = update, p = process

![](images/2026-04-07-04-10-49.png)

---

<h4> Encryption Keys and Key Vault</h4>

![](images/2026-04-07-04-20-34.png)

- Key Vault is a service in Azure that you can use to store secrets and keys

---

<h4>Custome Domain</h4>

- You can map custom domain name to your storage instead of using the default URL provided by Microsoft

- Create a CNAME record with DNS provider that points from
  - Your own domain:
    > E.g. www.abcdomain.com points to slsasdemo.blob.core.windows.net

    - Note: takes awhile for Azure to verify the domain registration

  - Using the Azure "asverify" subdomain
    > E.g. asverify.abcdomain.com to asverify.slsasdemo.blob.core.windows.net

    - After it completed, create a CNAME record that points to slsasdemo.blob.core.windows.net

    - So its sort of verify the domain name first before linking using the CNAME

    - Does not incur any downtime

    - To use this method, select "Use Indirect CNAME Validation" checkbox 