# Ubuntu 20.04

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