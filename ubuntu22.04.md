# dual boot
* https://adamtheautomator.com/install-ubuntu-on-a-partition/

# korean fcitx
* https://notes.harues.com/posts/hangul-input-using-fcitx/

# gnome-tweaks
* sudo apt-get install gnome-tweaks

# Find required packages workflow
```
$ sudo apt-get install apt-file
$ sudo apt-file update
$ apt-file search "X11/extensions/Xinerama.h"
libxinerama-dev: /usr/include/X11/extensions/Xinerama.h
$ sudoi apt-get install libxinerama-dev
```

# driver
* downgrade to nvidia-435 driver

# dwm
```
https://cannibalcandy.wordpress.com/2012/04/26/installing-and-configuring-dwm-under-ubuntu/

sudo apt-get update
sudo apt-get install build-essential libx11-dev libxinerama-dev sharutils suckless-tools
cd /usr/local/src
sudo wget https://dl.suckless.org/dwm/dwm-6.2.tar.gz
sudo tar xvzf dwm-6.0.tar.gz
chown -R `id -u`:`id -g` dwm-6.0
cd dwm-6.0
sudo make clean install

# add dwm to entry

sudo apt-get install dwm
sudo cp /usr/share/xsessions/dwm.desktop{,.bak}
sudo apt-get purge dwm
sudo mv /usr/share/xsessions/dwm.desktop{.bak,}
```

hotkeys
```
Alt+Shift+Enter
    Launch xterm
Alt+Shift+C
    Kill a client (a window, if you must insist)
Alt+t
    Switch to tile layout
Alt+m
    Switch to monocle layout
Alt+f
    Switch to floating layout
Alt+b
    Show/hide bar
Alt+p
    Launch dmenu
Alt+[num]
    Switch to tag [num]
Alt+Shift+Q
    Quit dwm
```

