# Linux Useful commands
- search for sshable computers on the local network
```
ifconfig
 . inet 172.30.1.39 netmask 0xffffff00 broadcast 172.30.1.255
sudo nmap -sS -p 22 172.30.1.0/24
```

- ssh yhong@192.168.0.105
- super user
 `sudo -i` 
- Resource Management
``` bash
### Ram/CPU/GPU
free -m
ps ax
htop
nvidia-smi
#Disk space
df -h --total
du
#Disk Drives / mount
fdisk -l
mount /dev/sd** /media/usb
ls -lh
unmount -l /media/usb
### Kill -9 is quite dangerous
killall -9 python


```
- Environment
```
which python3
```

- Mounting Drives

```
### Mount with permission
sudo mkdir -p /media/sec
sudo mount -t ext4 -o rw /dev/sdc1 /media/sec
sudo chown -R yhong:yhong /media/sec

sudo nano /etc/fstab
/dev/sdb1    /media/foo    ext4    rw,user,exec,umask=000 0 0
```
- Util
``` bash
###Delete Files with regular expression
ls | grep -P "^NAME.*[0-9]{2}$" | xargs -d"\n" rm
[bash - Delete files with regular expression - Super User](https://superuser.com/questions/392872/delete-files-with-regular-expression)
### Copy files
scp yhong@192.168.0.101:file.txt /destination/dir
scp file.txt yhong@192.168.0.101:/remote/directory/

### Runs a command every 5 seconds
watch -n 5 command
### Saves the output into a scrollview
command | less
### Saves the output to a file
command > test.txt
### Parse command output and finds text
command | grep python
### Cuts columns 1-5 of an output
command | cut -c1-5
### Changes output to a single string
$(command)
### Move and Remove
mv source dest 
rm file
rm -r directory

```

```
###Format Drives
sudo parted /dev/sdb
2) Create a new GPT disklabel (aka partition table):

(parted) mklabel gpt
3) Set the default unit to TB:

(parted) unit TB
4) Create one partition occupying all the space on the drive. For a 4TB drive:

(parted) mkpart
Partition name?  []? primary
File system type?  [ext2]? ext4
Start? 0
End? 4
5) Check that the results are correct:

(parted) print
There should be one partition occupying the entire drive.

(parted) quit
sudo mkfs -t ext4 /dev/sdb1
```

- Add hard drive
- [How do I increase console-mode resolution? - Ask Ubuntu](https://askubuntu.com/questions/18444/how-do-i-increase-console-mode-resolution)
