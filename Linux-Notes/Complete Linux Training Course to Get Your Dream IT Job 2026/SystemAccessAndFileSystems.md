- [Important Things to Remember in Linux](#important-things-to-remember-in-linux)
- [Changing Password](#changing-password)
- [Introduction to File System](#introduction-to-file-system)
- [Linux File and Directory Properties](#linux-file-and-directory-properties)

# Important Things to Remember in Linux

- Linux has a super user account name "Root"
  - Most powerful account that can do anything in the system

- Linux is is **case-sensitive**
  - ABC is **NOT** same as abc
 
- Avoid using spaces when creating files and directories



# Changing Password

- To change a password for a user:
  - Command to use: ` passwd <userid>`

# Introduction to File System

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

# Linux File and Directory Properties

![](images/2026-02-08-18-42-51.png)




