# Programs and 
* tmux, neovim
* i3

# disable monitor on boot
/etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="<default paramaters> video=LVDS-1:d"
update-grub
# lower brightness of disabled monitor
setpci -v -H1 -s 00:01.00 BRIDGE_CONTROL=0
echo 200 > /sys/class/backlight/gmux_backlight/brightness
