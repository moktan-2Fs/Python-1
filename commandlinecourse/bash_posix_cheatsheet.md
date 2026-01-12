BASH & POSIX COMMAND CHEAT SHEET

---

# 1. File & Directory Commands
ls -> List files/directories
Example: ls -l

cd -> Change directory
Example: cd /var/log

pwd -> Print working directory
Example: pwd

mkdir -> Create directory
Example: mkdir projects

rmdir -> Remove empty directory
Example: rmdir old_folder

rm -> Remove file/folder
Example: rm file.txt
Example: rm -r folder

cp -> Copy file/folder
Example: cp file1.txt file2.txt
Example: cp -r folder1 folder2

mv -> Move/rename file/folder
Example: mv old.txt new.txt
Example: mv file.txt /tmp/

touch -> Create empty file
Example: touch newfile.txt

file -> Determine file type
Example: file script.sh

stat -> Show file details
Example: stat file.txt

---

# 2. Viewing Files
cat -> Display file
Example: cat file.txt

less -> Scrollable view
Example: less file.txt

more -> Page view
Example: more file.txt

head -> First n lines
Example: head -n 5 file.txt

tail -> Last n lines
Example: tail -n 10 file.txt

tail -f -> Real-time log monitoring
Example: tail -f /var/log/syslog

echo -> Print text
Example: echo "Hello"

printf -> Formatted output
Example: printf "%-10s %-5d\n" Name 25

nano/vim -> Edit files
Example: nano file.txt
Example: vim file.txt

---

# 3. Text Processing
grep -> Search text
Example: grep "error" file.log

awk -> Process columns
Example: awk '{print $1,$3}' file.txt

sed -> Replace text
Example: sed 's/old/new/g' file.txt

cut -> Extract column
Example: cut -d',' -f2 file.csv

tr -> Translate/remove characters
Example: tr 'a-z' 'A-Z' < file.txt

sort -> Sort lines
Example: sort file.txt

uniq -> Remove duplicates
Example: sort file.txt | uniq

wc -> Count words/lines
Example: wc -l file.txt

---

# 4. Permissions & Ownership
chmod -> Change permissions
Example: chmod 755 script.sh

chown -> Change owner/group
Example: chown user:group file.txt

umask -> Default permissions
Example: umask 022

ls -l -> View permissions
Example: ls -l

---

# 5. Processes & System
ps -> Show processes
Example: ps aux

top -> Real-time monitoring
Example: top

htop -> Interactive process viewer
Example: htop

kill -> Kill PID
Example: kill 1234

killall -> Kill by name
Example: killall nginx

jobs -> List background jobs
Example: jobs

fg -> Bring job to foreground
Example: fg %1

bg -> Send job to background
Example: bg %1

uptime -> Show system uptime
Example: uptime

free -> Memory usage
Example: free -h

vmstat -> System performance stats
Example: vmstat 5

uname -> System info
Example: uname -a

who -> Logged in users
Example: who

w -> Users & activity
Example: w

last -> Login history
Example: last

---

# 6. Networking
ping -> Test connectivity
Example: ping google.com

traceroute -> Trace path to host
Example: traceroute google.com

curl -> HTTP/API request
Example: curl https://api.github.com

wget -> Download file
Example: wget https://example.com/file.zip

ifconfig -> Show network interfaces
Example: ifconfig

ip addr -> Show IP addresses
Example: ip addr

netstat -> Open ports/connections
Example: netstat -tuln

ss -> Modern netstat
Example: ss -tuln

dig -> DNS lookup
Example: dig example.com

nslookup -> DNS query
Example: nslookup example.com

scp -> Copy over SSH
Example: scp file.txt user@server:/path/

rsync -> Sync files
Example: rsync -avz folder/ user@server:/backup/

ssh -> Remote login
Example: ssh user@server

ftp/sftp -> File transfer
Example: sftp user@server

---

# 7. Pipes & Redirection
> -> Redirect output (overwrite)
Example: echo "Hello" > file.txt

>> -> Append output
Example: echo "World" >> file.txt

< -> Input from file
Example: sort < file.txt

| -> Pipe output
Example: cat file.txt | grep error

2> -> Redirect stderr
Example: command 2> error.log

&> -> Redirect stdout & stderr
Example: command &> output.log

xargs -> Execute commands from input
Example: find . -name "*.log" | xargs rm

---

# 8. Archiving & Compression
tar -> Archive files/folders
Example: tar -czvf archive.tar.gz folder/
gzip -> Compress file
Example: gzip file.txt
gunzip -> Decompress file
Example: gunzip file.txt.gz
zip -> Zip files
Example: zip archive.zip file1 file2
unzip -> Extract zip
Example: unzip archive.zip
bzip2 -> Compress with bzip2
Example: bzip2 file.txt
bunzip2 -> Decompress bzip2
Example: bunzip2 file.txt.bz2

---

# 9. Bash Scripting Basics
#!/bin/bash -> Bash interpreter
var=value -> Variable assignment
$var -> Print variable
$() -> Command substitution
Example script:
#!/bin/bash
mkdir -p /backup/logs
tar -czf /backup/logs_$(date +%F).tar.gz /var/log/nginx
echo "Backup done for $(date)" >> /var/log/backup.log

---

# 10. Advanced Utilities
cron -> Schedule tasks
Example: crontab -e

screen -> Persistent session
Example: screen -S session_name
tmux -> Terminal multiplexer
Example: tmux new -s session_name

find -> Search files/folders
Example: find /var/log -name "*.log"
watch -> Repeat command at intervals
Example: watch -n 5 'df -h'
df -> Disk space usage
Example: df -h
du -> Disk usage folder
Example: du -sh folder/
hostname -> Show hostname
Example: hostname
mount -> Mounted filesystems
Example: mount | column -t
umount -> Unmount filesystem
Example: umount /dev/sdb1

---

# 11. Package Managers
Debian/Ubuntu -> apt update | apt install packagename
Fedora/RedHat/CentOS -> dnf install packagename | yum install packagename
Arch -> pacman -S packagename
macOS -> brew install packagename

---

# Tips & Best Practices
- Test scripts in safe directories first
- Use POSIX commands for cross-distro scripts
- Combine commands with pipes for one-liners
- Use cron for automation
- Keep logs using >> or &>
- Check permissions before editing system files
- Learn networking commands for server debugging

---
End of Bash & POSIX Cheat Sheet

