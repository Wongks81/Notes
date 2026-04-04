<h2>Role Based Access Control (RBAC)</h2>

![](images/2026-04-04-03-50-20.png)

- Main function is to control access and permissions given to users, apps or user groups.

- Roles includes various actions that defines what type of operations you can perform on a given resource type
  - Write enables PUT,POST,PATCH and DELETE operations

  - Read only enables you to perform GET operations

<h3>General Built in Roles in RBAC:</h3>
- Owner 
  - Full access to all resources, including the right to delegate access to others

- Contributor
  - Can create and manage all types of Azure resources but cannot grant access to others

- Reader
  - Can view existing Azure resources but cannot perform any other actions

> There are many other roles created by Microsoft, refer to website for it.

<h3>Custom roles</h3>

- To allow users to create a customize role if the build in roles are unable to sufficently fit user needs

- Able to assign "Actions" and "NotActions" to the roles

- Can be assigned to:
  - Subscriptions
  - Resource Groups
  - Individual Resources

  
