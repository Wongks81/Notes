- [1. Important Things to Remember in Linux](#1-important-things-to-remember-in-linux)
- [2. Changing Password](#2-changing-password)
- [3. Introduction to File System](#3-introduction-to-file-system)
- [4. Linux File and Directory Properties](#4-linux-file-and-directory-properties)
  - [4.1. Type Column](#41-type-column)
  - [4.2. Number of Links (# of Links)](#42-number-of-links--of-links)
  - [4.3. Owner](#43-owner)
  - [4.4. Group](#44-group)
  - [4.5. Size](#45-size)
  - [4.6. Month, Day and Time](#46-month-day-and-time)
  - [4.7. Name](#47-name)
- [5. File System Paths](#5-file-system-paths)
- [6. Creating File and Directory](#6-creating-file-and-directory)
  - [6.1. Copying Directories](#61-copying-directories)
  - [6.2. Finding Files and Directories](#62-finding-files-and-directories)
  - [6.3. Difference between find and locate commands](#63-difference-between-find-and-locate-commands)
- [7. Wildcards](#7-wildcards)
  - [7.1. Special Note](#71-special-note)
- [8. Linux File Types](#8-linux-file-types)
- [9. Soft and Hard links](#9-soft-and-hard-links)

# 1. Important Things to Remember in Linux

- Linux has a super user account name "Root"
  - Most powerful account that can do anything in the system

- Linux is is **case-sensitive**
  - ABC is **NOT** same as abc
 
- Avoid using spaces when creating files and directories



# 2. Changing Password

- To change a password for a user:
  - Command to use: ` passwd <userid>`

# 3. Introduction to File System

 - Filesystem is a system used by an operating system to manage files

    ## File System Structure and Description

    | Folder name | Description                                                                                                                                        |
    | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
    | /boot       | Contains files that is used by the boot loader (grub.cfg)                                                                                          |
    | /root       | root user home directory. <br><br>It is **NOT** the same as /                                                                                      |
    | /dev        | For system devices (e.g. keyboard, USB, mouse etc) <br><br> Devices are created as each individual file for identification                         |
    | /etc        | Stores Configuration files <br><br> <span style="color:red"> **Make a backup BEFORE making changes to any of the files inside this folder**</span> |
    | /usr/bin    | Previous versions of linux is `/bin` <br><br> Stores common and frequent user commands that are used every session                                 |
    | usr/sbin    | Previous versions of linux is `/sbin` <br><br> Stores System / FileSystem commands                                                                 |
    | /opt        | Optional Add-On application <br><br> System files for 3rd party applications (e.g. SAP, Oracle)                                                    |
    | /proc       | Running processes use and create files in this folder. (Only those exist in memory)                                                                |
    | /usr/lib    | Previous versions of linux is `/lib`  <br><br> Stores C programming library files needed by commands and apps                                      |
    | /tmp        | Directory for temporary files                                                                                                                      |
    | /home       | Directory for user                                                                                                                                 |
    | /var        | For system Logs                                                                                                                                    |
    | /run        | Stores system daemons that start very early (e.g. systemd and udev) <br><br> Stores temporary runtime files like PID files                         |
    | /mnt        | To mount external filesystem                                                                                                                       |
    | /media      | For cdrom mounts |

# 4. Linux File and Directory Properties

![](images/2026-02-08-18-42-51.png)

|0|1|2|3|4|5|6|7|8|9|
|-|-|-|-|-|-|-|-|-|-|
|d|r|w|x|r|-|x|r|-|x|

## 4.1. Type Column
| Position | Description                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| 0        | d &emsp; Object is a directory <br> l &emsp; Object is a link(shortcut) <br> - (DASH) &emsp; Object is a regular file <br> Refer to [Section 8](#8-linux-file-types) |
| 1 to 3   | This groups sets the `Owner` permission of the object                                                        |
| 4-6      | This groups sets the `Group` permission of the object                                                        |
| 7-9      | This groups sets the `Others` permission of the object           |

**r - read. w - write, x - execute permissions**

## 4.2. Number of Links (# of Links)

For a regular file, this number refers to the number of hard links to the file

For a directory, this number is the number of immediate subdirectories it has plus the parent directory and itself.

## 4.3. Owner

Refers to who owns the file or directory.
Normally will display the person who create the file or directory

## 4.4. Group

Refers to which group owns the file or directory.
It normally refers to the primary group that the owner is part of

## 4.5. Size

Size of the file shown in bytes

## 4.6. Month, Day and Time

These 3 columns show the Date and Time the file is created.
(Year not shown)

## 4.7. Name

Name of the file
<br>
<br>

# 5. File System Paths

There are 2 paths to navigate to a filesystem
- Absolute path
  - Absolute path always begins with a " / "
  - " / " indicates that the path starts at root directory
  - E.g.: ```` cd /var/log ````

- Relative path
  - Does not begins with " / "
  - Identifies location relative to your current position
  - E.g.: <br> 
    >  admin@localhost:~$ cd Desktop 
    >  admin@localhost:~/Desktop$ 
  
  **~** is the home directory of the current user

  # 6. Creating File and Directory

  Creating files
  - touch : Creates an empty file
  - cp : Copying an existing file and create a new file with the same contents in the new location
  
  Creating directories
  - mkdir : creates a directory

## 6.1. Copying Directories
Copy command :`cp`
Optional Arguements : 
- `-R` : Option to copy from source, all the files and folders recursively

  > cp -R <source_folder><destination_folder>

## 6.2. Finding Files and Directories

2 Main commands are used to find files and directories
- find
  > find `.` -name "filename"

  Use `.` to find from current location downwards into its subdirectories

  > find `/home` -name "filename
  
  You can also use absolute directory name to search from that folder downwards

- locate
  > locate "filename"

  **If the command does not output any results then run command "updatedb" using `sudo` or as root account**

  If "updatedb" gives error:
  - Check if you have installed "mlocate" by
    > rpm -qa | grep mlocate
  - To install :
    > yum install mlocate

## 6.3. Difference between find and locate commands

- `locate` use a prebuilt database, which should be regulary updated
  - Faster but maybe inaccurate if database is not updated
    - Use `updatedb` if you need to update the database

- `find` iteratres over a filesystem to locate files
  - How slow it will be will depends on how big of the filesystem it needs to iterates. 

# 7. Wildcards

Wildcard is a character that can be used as a substitute for any of a class of characters in a search

\* (Asterisk) : represents 0 or more characters

\? : represents a single character

\[ \] : represent a range of characters. For searching only. Use `\{ \}`for creation.

\\ : escape character

\^ (caret) : the beginning of the line

\$ : end of the line

## 7.1. Special Note
- For creation a list of files in sequence:
  E.g. 
  > abc1.txt
  > abc2.txt
  > abc3.txt

  Instead of using \[ \], use braces instead.

  > touch abc[1..3].txt

# 8. Linux File Types

| File Symbol | Meaning                |
| ----------- | ---------------------- |
| -           | Regular File           |
| d           | Directory              |
| l           | Link                   |
| c           | Special or device file |
| s           | socket <br><br> Used for network communication between processes                |
| p           | Named Pipe <br><br> Also known as FIFO and used for interprocess communication. <br> Allows data to be pass to between processes in a `F`irst `I`n `F`irst `O` manner           |
| b           | Block device <br><br> Represents devices that handle data in blocks such as USB or hard drives         |
|             |                        |

# 9. Soft and Hard links

- `inode` is a Pointer or number of a file on the hard disk
  - Everytime a file is created, a number(inode) is generated to associate with the file.
  - When a command or process requires to read a file, it will pass the number(inode) to the filesystem to ask it to retreive the file for them.
  
- `Softlink` is a link when created will be remove if the source file is removed or renamed

- `Hardlink` is links the file to data blocks instead. So when deleting, moving or renaming the source file, it will not affect the link. 
  - The link will only disappear when all the links are removed

**You cannot create soft or hard link with the same name within the same directory.**

Command to create link:
- Hardlink
    >ln [source_file_path]

- Softlink
  > ln -s [source_file_path]

Command to check inode
> ls -ltri

