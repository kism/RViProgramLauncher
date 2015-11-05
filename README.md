# VI Program Launcher

## Install Dependencies  

```bash
sudo apt-get install newsbeuter links mplayer python-pip python-dev libudev-dev zsh alpine newsbeuter links frotz calibre
sudo pip install psutil python-uinput
```

You will also need the kernel headers for the kernel that you are running. For example if you are running 3.18 which is currently on Debian Wheezy. Also make sure if you do an apt-get command with wildcards you use bash.

```bash
sudo apt-get install linux-headers-3.18.0-trunk-*
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

## Simulating the serial input device

The serial connection will need to be 115200 baud, No Parity, 8 Data Bits, 1 Stop Bit, No Flow control. On the device running the daemon /dev/ttyUSB0 will be used.

Over serial send values 129 - 136 to trigger the macros, see [SERIAL.md](https://github.com/kism/RViProgramLauncher/blob/master/SERIAL.md) for documentation of the serial input standard.

You can use any program to test out viinputdaemon.py that can output the correct bits.

On windows you can use [Realterm](http://realterm.sourceforge.net/index.html#downloads_Download)

On linux you can use Minicom

## Installing the man page

```bash
sudo mkdir /usr/local/man/man1
sudo cp viui.1 /usr/local/man/man1
```

## Function key functionality list

| Program    | F1          | F2         | F3         | F4         | F5      | F6              | F7              | F8                     |
|------------|-------------|------------|------------|------------|---------|-----------------|-----------------|------------------------|
| viui       | help menu   | nano       | alpine     | newsbeuter | links   | irssi           | zsh             | option & shutdown menu |
| nano       | help        | open file  | save file  | cancel     | cut     | uncut           | find            | quit                   |
| alpine     | help        | open index | compose    | back       | journal |                 | setup           | quit                   |
| newsbeuter | help        | open entry | save story |            | reload  | next unread     | open in browser | quit                   |
| links      | help        | go to url  | menu       | cancel     |         |                 | find in page    | quit                   |
| irssi      | help        | /connect   | /join      | /part      | /query  | previous window | next window     | quit                   |
| zsh        | home folder | play       |            | ^c         |         |                 |                 | quit                   |

# Running ViUi

ViUi can be run by entering the command

```bash
python viui.py
```
