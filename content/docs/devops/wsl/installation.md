# Installation of WSL

Basic commands:

```pwsh
wsl --list --online
wsl --list
wsl --install -d <distro>
wsl -d <distro>
wsl --terminate <distro>
```

## WSL2

Enable Windows subsystem for Linux:

```pwsh
Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName Microsoft-Windows-Subsystem-Linux
Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName VirtualMachinePlatform
```

Enable version 2 of WSL:

```pwsh
Invoke-WebRequest https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile c:\wsl_update_x64.msi -UseBasicParsing
Invoke-WebRequest https://... -OutFile D:\dat\WSL\kernel\vmlinux -UseBasicParsing
start D:\dat\WSL\wsl_update_x64.msi
wsl --set-default-version 2
```

Configure non-default kernel in `%USERPROFILE%\.wslconfig`:

```
[wsl2]
kernel=D:\\dat\\WSL\\kernel\\vmlinux
```

## Import Ubuntu image from docker

- Download image: `Invoke-WebRequest https://raw.githubusercontent.com/tianon/docker-brew-ubuntu-core/fbca80af7960ffcca085d509c20f53ced1697ade/kinetic/ubuntu-kinetic-oci-amd64-root.tar.gz -OutFile C:\ubuntu-kinetic-oci-amd64-root.tar.gz -UseBasicParsing`
- Import image: `wsl --import jdp-ubuntu C:\dat\WSL\jdp-ubuntu C:\ubuntu-kinetic-oci-amd64-root.tar.gz`
- Update system: `apt-get update`

## Import Arch image from docker

- Download image: `Invoke-WebRequest https://gitlab.archlinux.org/archlinux/archlinux-docker/-/package_files/2816/download -OutFile C:\arch-base-20220704.0.66039.tar.zst -UseBasicParsing`
- Import image: `wsl --import jdp-arch C:\dat\WSL\jdp-arch C:\arch-base-20220704.0.66039.tar`
- Uncomment locale file: `/etc/locale.gen`
- Generate locale: `locale-gen`
- Initialize key: `pacman-key --init`
- Update system: `pacman -Syu`

## Mount host directory

Create directory in WSL: `mkdir /src`

Edit `/etc/fstab` and add line: `C:/src /src drvfs defaults 0 0`

Reload the fstab file: `sudo mount -a`

## Enable SystemD

Install store version of WSL: https://aka.ms/wslstorepage

Enable systemd inside distribution by editting `/etc/wsl.conf`:

```
[boot]
systemd=true
```

Reboot WSL and test:

```sh
systemctl list-units --type=service
systemctl list-unit-files --type=service
```
