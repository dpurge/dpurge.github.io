# Ubuntu 22.04

Update the system:

```bash
sudo apt update
sudo apt -y upgrade
```

## RDP connections

Install xrdp and xwindows:

```bash
sudo apt install -y xrdp
sudo apt install -y xfce4 xfce4-goodies
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/max_bpp=32/max_bpp=128/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/xserverbpp=24/xserverbpp=128/g' /etc/xrdp/xrdp.ini
echo xfce4-session > ~/.xsession
```

Comment out and add line in `/etc/xrdp/startwm.sh`:

```bash
# test -x /etc/X11/Xsession && exec /etc/X11/Xsession
# exec /bin/sh /etc/X11/Xsession

startxfce4
```

Start XRDP:

```bash
sudo /etc/init.d/xrdp start
```

Connect in RDP to `localhost:3390`.
