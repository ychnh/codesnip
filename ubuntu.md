# Linux Philosophy
- let the program to do one thing and do it well (single responsibility principle)
- make it abstract enough to be agnostic of irrelevant details or data types
- compose separate individual programs using standard well-defined interfaces.

- https://unix.stackexchange.com/questions/159513/what-are-the-shells-control-and-redirection-operators
# Linux Useful commands


## keyremap
* ./xflux -z 90011 -k 2500
* xmodmap -e 'clear Lock' -e 'keycode 0x42 = Super_L'

## xrandr
* xrandr --output eDP --mode 1680x1050 --set 'scaling mode' Full
* xrandr --output HDMI-1-0 --auto --same-as eDP-1 --mode 2560x1440

## sudo
* run sudo with user's environment variables
* sudo -E

## Diff
```
diff --brief -x '*.py' A B
```

### Find Large Directories
* find . -name 'mystring*'
* du --max-depth=1 -h
* du -a /home | sort -n -r | head -n 5
* du -h -d1
```
## Network
# Find SSH Host

```
ifconfig
$ inet 172.30.1.39 netmask 0xffffff00 broadcast 172.30.1.255
sudo nmap -sS -p 22 172.30.1.0/24
```
- grep pattern -r --include='*.{cpp,h}' rootdir

## Clone File Directory Structure
- rsync -a --ignore-existing /local/directory/ host:/remote/directory/
- sudo sshfs -o allow_other sijin@xxx.xxx.xxx.xxx:/home/sijin /mnt/droplet
- sudo umount /mnt/droplet


- scp -P portnumb -r yhong@123.123.123.1.:/source /dest
- scp -P portnumb -r /source yhong@123.123.123.1.:/dest
- ssh yhong@192.168.0.105
- ssh -L localhost:8888:localhost:8887 yhong@cjy9306.iptime.org -p 13532
- super user
 `sudo -i` 
- Resource Management
``` bash
### Ram/CPU/GPU
lscpu
free -m
ps ax
top (press e to cycle btw readable values)
nvidia-smi
#Disk space
df -h --total
du -hs 
#Disk Drives / mount
fdisk -l
mount /dev/sd** /media/usb
ls -lh
unmount -l /media/usb
### Kill -9 is quite dangerous
killall -9 python

- Symbolic links
ln -s /media/files/tb-prod/files files (-s create -sf change)
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
1) List hardrives
sudo lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL



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


# Country Code and Setup 
- /etc/apt/sources.list
- deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted (Change us to kr)

# Update
apt-get update

# Edit and remove apt-get
apt-get remove pkg
apt-get autoremove
apt-get purge pkg

# MAC Slow SSH
May be you're not enthusiastic about hacking your SSH configuration files. Another solution is to add the IP addresses you're going to connect to (or which are going to connect to your mac) in /etc/hosts.

# Set/Read variables
````
pwd > /tmp/loc
cd "$(</tmp/loc)"
cd "`</tmp/loc`"
````
For more elab apporaches check [pass-variable-to-another-pane](https://superuser.com/questions/1067335/pass-variable-to-another-pane)

# Tar
````
tar -czf file.tar.gz directory 
tar -xvf
````

# ffmpeg
decompl/compl
````
ffmpeg -ss 00:00 -i in.avi -t 05:07 %05d.png
ffmpeg -r 20 -start_number 0 -i %05d.png -vcodec mpeg4 -qscale 0 -y ../out.mp4

ffmpeg -i raw/a1.avi -vf "select='between(t,2,59)+between(t,170,225)" an1-a1-2/%05d.png -vsync 0

ffmpeg -r 20 -i /media/sec/semi/results/R-B2-b1-0/%*.png -qscale 0 -vcodec mpeg4 -y test.mp4
````

# Timezone
* timedatectl
* timedatectl list-timezones
* sudo timedatectl set-timezone

