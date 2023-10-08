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
