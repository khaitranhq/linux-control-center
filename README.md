# Control center
A simply control center to monitor connections such as WiFi, Bluetooth, etc. And Monitor brightness level and sound volume.

This repository is a fork of [comice-control-center](https://github.com/libredeb/comice-control-center)

## Screenshot
![Screenshot](https://raw.githubusercontent.com/libredeb/comice-control-center/main/screenshots/screenshot.png)


## Compilation

1. Install build dependencies:
```bash
# Fedora
sudo dnf install python3 python3-dbus util-linux gsettings-desktop-schemas wireless-tools iproute alsa-utils

# Arch
sudo pacman -S util-linux gsettings-desktop-schemas wireless_tools iproute alsa-utils dbus-python python-pip
```
2. Install python3 (pip) dependencies:
```bash
sudo pip3 install -r requirements.txt
```
3. Add command to run your network manager application and bluetooth manager application into `control-center.conf`. You can see example in `control-center.example.conf`
4. Run `control-center` standalone:
```bash
./control-center
```
