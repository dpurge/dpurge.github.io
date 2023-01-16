# Installation

# Linux

```sh
export PACKER_VERSION=1.7.10
curl \
    -sSL https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
    -o /tmp/packer_linux_amd64.zip
cd /usr/local/bin
unzip /tmp/packer_linux_amd64.zip
rm /tmp/packer_linux_amd64.zip
```
