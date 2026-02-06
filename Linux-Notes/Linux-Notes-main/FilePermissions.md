>File Permissions can be listed by using `ls -l` to view them

![](Images/2025-11-20-15-14-20.png)

Taking `drwxr-xr-x`for example, specfically the table column for <strong>Type</string>:
| Position | Description                                                                            | Remarks                                                                      |
| :------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1        | `d` indicate this object is a folder <br> `l` indicate this object is a link <-> `-` indicate object is a file |                                                                              |
| 2 - 4 (`u`)   | `r` refers to read <br> `w` refers to write <br> `x` refers to execute <br> `-`  no permission                | These 3 bits in position 2-4 specify the permissions for `user` of the file |
| 5-7 (`g`)     | `r` refers to read <br> `w` refers to write <br> `x` refers to execute  <br> `-`  no permission               | These 3 bits in position 2-4 specify the permissions for `group` of the file |                                                                                 
| 8-10 (`o`)    | `r` refers to read <br> `w` refers to write <br> `x` refers to execute <br> `-`  no permission                | These 3 bits in position 2-4 specify the permissions for `other` of the file 

&nbsp;

>chmod - command to change the permission of the file

To change permission to the file we will use the + sign to add and - sign to remove.

There are are a couple of ways to do it:

    Example 1:
    chmod g-rw file.txt
    *Change permission (chmod) for group (g), remove read and write permission (-w) for file.txt

    Example 2: Using bits and Umask
    

>File Ownership

There are 2 owners of a file or directory, user and group.

Command to change file ownership:
- chown : changes user ownership of the file
- chgrp : change group ownership of the file

        E.g. chgrp [new owner] [ file/folder ]

>Using recursive ownership change option (-R)

This arguement is mainly used for directories.<br>
It allows user to change all the files and folders inside the directory

    E.g.
    chgrp -R [ new group ] [ directory]

