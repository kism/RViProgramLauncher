# VI Program Launcher

## Install Prerequisites 

```bash
sudo apt-get install newsbeuter links mplayer calibre alpine python-pip
sudo pip install psutil python-uinput
```

You will also need the kernel headers for the kernel that you are running. For example if you are running 3.18 which is currently on Debian Wheezy.

```bash
sudo apt-get install linux-headers-3.18*
```

## Other Prerequisites  

### Enabeling uinput

viinputdaemon.py requires the kernel module 'uinput' to be activated.

To enable uinput temporarly

```bash
sudo modprobe uinput
```

To enable uinput on boot

```bash
sudo bash -c "echo 'uinput' >> /etc/modules"
```

### 'Fixing' sudo

Due to the fact it is difficult to run a program as root and then run programs as other users the program will run the appropiate commands as sudo, this means that if sudo asks for a password the program will not be able to run. If you are running Raspbian Wheezy on a Raspberry Pi this is the default.

To change sudo to not ask for a password use visudo to edit, the entry you need to change will probably need to make will probably be at the end of the file.

```bash
sudo visudo
<your username> ALL = NOPASSWD : ALL
```
