# Installation

# Linux

TODO

Install `Helm`:

```sh
export HELM_VERSION=3.9.2
cd /tmp
curl \
    -sSL https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    -o helm.tar.gz
tar xf helm.tar.gz linux-amd64/helm
mv linux-amd64/helm /usr/local/bin/helm
rmdir linux-amd64
rm helm.tar.gz
```
