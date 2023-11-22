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

## Install SystemD

```bash
curl -L -O "https://raw.githubusercontent.com/nullpo-head/wsl-distrod/main/install.sh"
chmod +x install.sh
sudo ./install.sh install
/opt/distrod/bin/distrod enable
```

Restart distribution:

```pwsh
wsl --terminate Ubuntu
```

After restart, check the init system:

```bash
ps -o comm 1
```

## Enable LXD

Install LXD:

```bash
snap info lxd
sudo snap install lxd
sudo lxd init
```

Check available containers:

```bash
sudo lxc ls
```

List available images:

```bash
sudo lxc image list ubuntu: 22.04 architecture=x86_64
```

Create container:

```bash
sudo lxc launch images:ubuntu/22.04
sudo lxc exec closing-gazelle -- su --login ubuntu
```

List local images:

```bash
sudo lxc image list
```

Delete container:

```bash
sudo lxc stop closing-gazelle
sudo lxc delete closing-gazelle
```

Delete image:

```bash
sudo lxc image list
sudo lxc image delete a3e17f0f0cbc
```

Create containers with names:

```bash
lxc launch images:centos/7 haproxy
lxc launch ubuntu:18.04 controller-0 --profile k8s
lxc launch ubuntu:18.04 controller-1 --profile k8s
lxc launch ubuntu:18.04 controller-2 --profile k8s
lxc launch ubuntu:18.04 worker-0 --profile k8s
lxc launch ubuntu:18.04 worker-1 --profile k8s
lxc launch ubuntu:18.04 worker-2 --profile k8s
lxc list
```