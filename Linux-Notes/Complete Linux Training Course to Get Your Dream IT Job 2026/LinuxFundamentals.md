Linux Fundamentals
- [1. File Permissions](#1-file-permissions)
  - [Types of permission](#types-of-permission)
  - [Permission Controls](#permission-controls)
  - [Assigning Permissions (chmod)](#assigning-permissions-chmod)
    - [Assigning using letters](#assigning-using-letters)
  - [Assigning using numbers](#assigning-using-numbers)
- [File Ownership](#file-ownership)
  - [Command to change file ownership](#command-to-change-file-ownership)
- [Access Control List (ACL)](#access-control-list-acl)
  - [When would we use ACL?](#when-would-we-use-acl)
  - [Things to Note](#things-to-note)
- [Help Commands](#help-commands)

# 1. File Permissions

Permissions for a file or directory maybe restricted by types.

## Types of permission
3 types of permissions
- r - read
- w - write
- x - execute / run a program

## Permission Controls
Each permission can be controlled at 3 levels.
- u - user
- g - group or people in the same department / project
- o - other = everyone on the system

Permission can be displayed by running `ls -l` command

**Type Column**
![](images/2026-02-08-18-42-51.png)

[Explanation of letters](./SystemAccessAndFileSystems.md/#41-type-column)

## Assigning Permissions (chmod)

`chmod` is the command to assign permissions to files or directories

![](images/2026-02-12-09-03-56.png)

### Assigning using letters

[Refer to this table for letters explanation](./SystemAccessAndFileSystems.md/#41-type-column)

> chmod g+w fileadd.txt

This means to `add(+)` `write(w)` permissions `group(g)`.

> chmod u-x fileremove.txt

This means to `remove(-)` `executable(x)` permissions to `user(u)`

> chmod a+w fileaddall.txt

This means to `add(+)` `write(w)` permissions to `all(a)`, users, groups and others.

> chmod u+rw addtwo.txt

This means to `add(+)` `read and write(rw)` permissions to `user(u)`

## Assigning using numbers

Assigning via numbers is the same as using first 3 bit of the binary table.

| bit 2 | bit 1 | bit 0 |
| ----- | ----- | ----- |
| r     | w     | x     |
| 4     | 2     | 1     |
|       |       |       |

From the table above you can see that for `read` its value in numbers is `4`

So for example to add read permissions to all:
> chmod 444 file.txt

---

In order to change only 1 part of the permissions, you will need to know the permissions of the file you will be changing.

Example if the file have the following permissions:

>-rwxrw-r-x file.txt

To modify user permission to read and write and no execute:
> chmod 766 file.txt

- The first 7 (`user`) means read(`4`),write(`2`) and execute(`1`)
- Second 6 (`group`) means read(`4`) and write(`2`)
- Third 6 (`others`) means read(`4`) and write(`2`)

# File Ownership

There are 2 levels of ownership when a file or directory is created.
- User level
- Group level

Which means there are 2 owners to a file or directory:
- Normally it belongs to `user` on user level and the `PRIMARY GROUP` that the user belongs to.

## Command to change file ownership

![](images/2026-02-19-11-53-57.png)
> Who is the user owner (yellow) <br>
> Who is the group owner (blue)

- chwon and chgrp
  - `chown` changes the user ownership of a file
  - `chgrp` changes the group ownership of a file

- To change directories recursively, use the `-R` option.

# Access Control List (ACL)

- ACL provides an additional, more flexible permission mechanism for file systems.
  - Another layer of security on top of the previous permissions
  
- Allows admin to assign permissions `per user` or `per group`

## When would we use ACL?
- In a scenario where a particular user needs to access a certain subset of files but is not a member of group that have permissions for it.
  - ACL helps to solve this situation as it is able to give only certain permissions (read,write) to the user for accessing the files.
  - Its for situations where you do not want to give access to any of the other groups the user is in. <br>
  `( As this will allows other users of the group to have access also ) `
- Used to define more fine-grained discretionary access
- Commands to get the details of ACL of a file or directory is:
  > getfacl `filename/directory name`

  ![](images/2026-02-19-13-52-21.png)

- Commands to assign and remove ACL permissions are
  > setfacl
 

- Examples:
  - To add permission for user
    > setfacl -m u:userid:rwx /path/to/file

    - `-m` - refers to modify the affected user permissions
    - `u:userid` - state which user you want to modify
    - `rwx` - set which permissions you want to give 
  
  - To add permission for group
    > setfacl -m g:groupName:rw /path/to/file
  
    - `-m` - refers to modify the affected user permissions
    - `g:groupName` - state which group you want to modify
    - `rw` - set which permissions you want to give 
  
  - To allow all files or directories to inherit ACL entries from the directory it is within
    >setfacl -Rm "entry" /path/to/dir 

    - `Rm` - modify the directory recursively
    - `entry` - refers to user or group permissions you want to set.
      - E.g. `u:userid:rwx` or `g:groupName:rwx`
  
  - To remove a specific entry (specific user)
    >setfacl -x u:user /path/to/file

    - `-x` - Option to indicate remove

  - To remove all entries (all users)
    > setfacl -b path/to/file

    - `-b` - Option to indicate all users

## Things to Note
- Remove all entries as stated above
  - This option only removes additional entries added to the permissions, it does not affect the base permissions that is currently in effect. <br><br> Removes all ACL entries that are added.
  
- Files with ACL permissions have a `+` sign at the end of the permission.

  ![](images/2026-02-19-13-48-55.png)

- Setting `w` permission with ACL does not allow user to remove a file, only modify.
- 

# Help Commands

**Certain distributions might need you to do a `sudo mandb` first before you can use some of the commands**

- Commands that will help you get information
  - whatis [command]
    ![](images/2026-02-19-15-58-39.png)

  - [command] --help
  - man [command]