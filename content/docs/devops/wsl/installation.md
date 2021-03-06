# Installation of WSL

## WSL2

```pwsh
Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName Microsoft-Windows-Subsystem-Linux
Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName VirtualMachinePlatform
Invoke-WebRequest https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile c:\wsl_update_x64.msi -UseBasicParsing
```

Reboot and install `c:\wsl_update_x64.msi`.

Set WSL2 as default: `wsl --set-default-version 2`

## Ubuntu 20.04

```pwsh
Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile c:\ubuntu2004.appx -UseBasicParsing 
Add-AppxPackage c:\ubuntu2004.appx
# DISM.EXE /Online /Add-ProvisionedAppxPackage /PackagePath:c:\\ubuntu2004.appx /SkipLicense --AllUsers
```

Start Ubuntu 20.04 console to install the base system, and then run:

```bash
sudo apt update
sudo apt upgrade
```

## Docker in Ubuntu 20.04

```bash
sudo apt install --no-install-recommends apt-transport-https ca-certificates curl gnupg2 net-tools
source /etc/os-release
curl -fsSL https://download.docker.com/linux/${ID}/gpg | sudo apt-key add -
echo "deb [arch=amd64] https://download.docker.com/linux/${ID} ${VERSION_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose
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
