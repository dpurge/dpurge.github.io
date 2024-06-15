# Ubuntu

Get network configuration:

```sh
ip a s
ifconfig -a
```

Static IP in `/etc/netplan/10-hostname.yaml`:

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      dhcp6: false
      dhcp-identifier: mac
      addresses:
        - 192.168.0.11/24
      routes:
        - to: default
          via: 192.168.0.1
      nameservers:
        addresses:
          - 192.168.0.1
```

Check disk size:

```sh
lsblk --scsi
sudo fdisk -l /dev/sda
sudo parted -l
df -h
```

Check memory:

```sh
free
```

Resize logical volume to all disk:

```sh
vgdisplay
lvdisplay
lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

## Generalize cloud image

```sh
sudo cloud-init clean
sudo rm -rf /var/lib/cloud/instances
sudo truncate -s 0 /etc/machine-id
sudo rm /var/lib/dbus/machine-id
sudo ln -s /etc/machine-id /var/lib/dbus/machine-id
sudo poweroff
```

## LXC server setup

Add user and install basic software:

```sh
adduser david
usermod -aG sudo david
sudo apt update
sudo apt dist-upgrade
sudo apt install curl wget git neovim mc tmux python3 jq golang sqlite3 autofs ca-certificates net-tools

sudo wget https://github.com/mikefarah/yq/releases/download/v4.44.1/yq_linux_amd64 -O /usr/local/bin/yq
sudo chmod +x /usr/local/bin/yq

wget https://github.com/google/go-jsonnet/releases/download/v0.20.0/jsonnet-go_0.20.0_linux_amd64.deb -O /tmp/jsonnet.deb
sudo apt install /tmp/jsonnet.deb
rm /tmp/jsonnet.deb

curl --fail --location --progress-bar --output /tmp/deno.zip https://github.com/denoland/deno/releases/download/v1.44.1/deno-x86_64-unknown-linux-gnu.zip
sudo unzip -d /usr/local/bin -o /tmp/deno.zip
rm /tmp/deno.zip

wget https://github.com/go-task/task/releases/download/v3.37.2/task_linux_amd64.deb -O /tmp/task.deb
sudo apt install /tmp/task.deb
rm /tmp/task.deb
```

Generalize image:

```sh
sudo apt clean
sudo apt autoremove
sudo rm /etc/ssh/ssh_host_*
sudo truncate -s 0 /etc/machine-id
sudo poweroff
```

Prepare container after creation from image:

```sh
sudo dpkg-reconfigure openssh-server

```

Install K3s in Proxmox LXC container:

In Proxmox host, change `/etc/sysctl.conf`:

```sh
net.ipv4.ip_forward=1
vm.swapiness=0
```

Disable swap in `/etc/fstab` and on command line: `swapoff -a`

Edit container confirguration in `/etc/pve/lxc/$ContainerID.conf`:

```sh
features: nesting=1
swap: 0
lxc.apparmor.profile: unconfined
lxc.cgroup2.devices.allow: a
lxc.cap.drop:
lxc.mount.auto: "proc:rw sys:rw"
```

Create `/etc/rc.local`:

```sh
#!/bin/sh -e
if [ ! -e /dev/kmsg ]; then
  ln -s /dev/console /dev/kmsg
fi
mount --make-rshared /
```

Make it executable nad run it:

```sh
chmod +x /etc/rc.local
/etc/rc.local
```

Install K3s: `curl -sfL https://get.k3s.io | sh -`
