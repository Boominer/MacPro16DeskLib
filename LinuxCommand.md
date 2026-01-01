1. pwd - print working directory
2. ls - list files
3. Clear / Ctr + l
4. cd  - cd - / cd ~
5. mkdir - create directory
6. which - find program executable
7. whereis - find program executable and man page
8. man - F/B/J/K/Page Down/Page Up - navigation in man pages
   / - search within man page
   q - quit man page
9. touch - create empty file
10. echo - print text
    > to write to file
    >> to append to file
11. cat - display file contents
12. less - view file contents pager-style
13. cp - copy files
14. mv - move/rename files
15. rm - remove files rmdir - remove empty directories
16. cmp - compare files by bytes
17. diff - show differences between files
18. whoami 
19. sudo - execute command as superuser
20. grep - search for patterns in files
    example: ls | grep pattern
21. chmod +x filename 
22. echo $PATH  - display PATH environment variable
23. wget / curl - download files from URL
    example: wget https://example.com/file.txt
24. awk - process text files
    example: ls -lh | grep file | awk '{print $5}'
25. sed - stream editor for filtering and transforming text
    example: echo "hello world" | sed 's/hello/hi/'
26. zip - compress files
    example: zip archive.zip file1 file2
27. unzip - decompress zip files
    example: unzip archive.zip
28. find - search for files and directories
    example: find . -name "*.txt"
29. ip - show network configuration
    example: ip addr show
30. ping - test network connectivity
    example: ping google.com
31. free - show memory usage
    example: free -h
32. df -H - show disk space usage
    example: df -H
33. ps - show running processes
    example: ps aux
34. kill - terminate process
    example: kill PID
35. top / htop - interactive process viewer
36. history - show command history
