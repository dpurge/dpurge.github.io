# Setup

## Boot in text mode

Change the `grub` configuration file (`/etc/default/grub`):

```ini
# GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX="text"
GRUB_TERMINAL=console
```

```sh
sudo update-grub
sudo systemctl set-default multi-user.target
shutdown -r now
```

## SSH

```sh
sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
sudo ufw allow ssh
```

Check network configuration:

```sh
sudo apt install net-tools
ifconfig
```

## Docker

```sh
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

## Git

```sh

```