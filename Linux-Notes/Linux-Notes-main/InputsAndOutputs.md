>Input and Output redirects
   
    E.g.
    $ ls -l >> ls.txt

>There are 3 redirects in Linux

| Name            | Command | File Descriptor |
| :-------------- | ------- | --------------- |
| Standard Input  | stdin   | 0               |
| Standard Output | stout   | 1               |
| Standard error  | stderr  | 2               |

- Input (stdin)
    - Input is used when feeding file contents to a file, `< symbol`
        - E.g. mail -s "Office memo" allusers@abc.com < memoletter

- Output(stdout)
    - Output of command can be routed to file using `> symbol`
        - E.g. ls -l result.txt
    
    - To add new lines or append to the output file, use `>> symbol`
        - E.g. echo "This is to add a new line" >> newfile.txt

- Error(stderr)
    - stderr only consider an error as and error when the error is display on the screen after command is executed
    - Used for redirecting errors to 
        - a log file for troubleshooting
        - `/dev/null` to ignore any errors that is produced. <br> `/dev/null` is a speical device that is considered a black hole or trash can for redirects

>Pipes ( | )

A pipe is used by the shell to connect the output of one command directly to the input of another command

Command Syntax is:

    command1 [args] | command2 [args]

E.g. To display ls result page by page, use more 

        $ ls -ltr | more

