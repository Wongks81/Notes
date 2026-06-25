<h1>Microsoft 365</h1>

# 1. Core objects of M365 Services

## 1.1 Licence types affect access to M365

- M365 licenses are going to control what services a user can access
- Features that you can access depends on licenses that you have purchased
- You will have to purchase and assign a license to a user before they can do anything
  - Would reccomend to assign licenses to groups instead of users
  - In the event of internal transfer, the user will change his license accordingly

> Note: If a user belongs to 2 groups, it might consume the licenses of both groups. 
> 
> Even if for example one group has E5 and the other is E3. Although the E5 covers all of E3, it will still consume 2 licenses.

## 1.2 Organisation Configurations

- Access it via M365 Admin center > settings > Org Settings

    ![](images/2026-06-25-07-28-56.png)

- We can setup a Domain Name for the subscription by going to the Domain section under settings
- But for the domain name to be recognized, we need to first buy the domain name from a domain name provider like GoDaddy.
    - You can also buy the domain name directly in this page

    ![](images/2026-06-25-07-44-07.png)
    ![](images/2026-06-25-07-47-44.png)

- You can also buy domain name from other companys but you will have to manually add them yourself by using the "Add Domain" button

    ![](images/2026-06-25-07-50-09.png)

## 1.3 Exchange Online Objects

- Any users that have an exchange online license can have a mailbox created for them

![](images/2026-06-25-08-17-53.png)

- To manage email for users we have to access the Exchange Admin center which is accessible via the left menu from M365 Admin center
  - You might need to click "Show All" for it to appear

  ![](images/2026-06-25-08-20-02.png)

### 1.3.1 Exchange 365 Groups

- Access via Exchange Admin Center > Recipents > Groups

- When a group is created, it will also create the following:
  - Email address for the group
    - Any email sent to this address, all users in groups will recieve it
    - Not to be confused with shared mailbox
    - Shared mailbox creates a mailbox container to store mails that was sent to them and allows the group members to drag and drop the emails from the mailbox to their personnel email.
    - Emails that are sent to groups email address appear in the group folder in each user Outlook.

  - SharePoint linked to the group
  - Teams linked to the group
  - Shared Calendar

### 1.3.2 Exchange Distribution List

- Just a group that have an email address and nothing else
- Sending to that email address will automatically send to all users in the group
- Mainly for applications to send status of the server (error notifications) to inform a particular group or for announcements that can span over a wide range of users
- There are 2 different types of Distribution List
  ![](images/2026-06-25-08-39-37.png)

- For Static, you will have to add the users in manually.
- For Dynamic, you can set some conditions for it to be added automatically
    ![](images/2026-06-25-08-41-10.png)

    > When users belong to a department called support, it will automatically be added to this distribution list.

    - Dynamic do not stores the group members in a static location / list, it evaluate the rules instead.
    
### 1.3.3 Exchange Email Enabled Security

- This group gets an email address and it can gives permission
- Basically it is a security group that can receive emails.

### 1.3.4 Exchange Recipents Contacts

- Allows you to add external users as a contact to show up in the global address list.

## 1.4 Sharepoint Administration Objects

- Sharepoint is Microsoft cloud based platform for creating, storing, organizing and sharing content across organization
  
- Can be access via M365 Admin center > menu on the left > Sharepoint

  ![alt text](image.png)

- Engine behind collaboration in M365
- Everytime you create a new M365 group or teams, sharepoint will provide a site where files, lists, pages and other shared resources can live.
- You can also build sites according to your needs

  ![alt text](image-1.png)

### 1.4.1 Roles and Permissions involving Sharepoint sites

- Sharepoint sites have the following Memberships

  ![](images/2026-06-25-15-26-54.png)

- Owners
  - Refers to the M365 Group Owners that the site connected to.
  
    >E.g. When the group is created, the Owner of the group is the owner of this site
  
- Site Owners
  - Refers to the SharePoint specific owners.
  - They are only owners of the site and can makes changes only to the site.
  - No additional permissions are given out of the site

- Members
  - Users who belong to the group and automatically have access to the site.

- Site Members
  - To grant access to the sites and not everything the M365 group is offering
  - Something like just allowing users outside of the group to access the site resources like files and folders
  - Site Members have the <b>EDIT</b> permissions

- Site admins
  - Assist the site owners to manage the sites
  - They have elevated capabilities such as configuring the site features and help maintaining the site

- Site Visitors
  - Only have read access to the sites
  
## 1.4 Microsoft Teams Administration

- Can be access via M365 Admin center > menu on the left > Teams

  ![](images/2026-06-25-16-09-30.png)

- When you create a new M365 Group, the system will automatically create a Team for you

- The new Team will show up in the Teams app

  ![](images/2026-06-25-16-14-29.png)

- You can add Channels in the team to show difference chats
  
  ![](images/2026-06-25-16-16-23.png)


