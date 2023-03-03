# Installation

## Linux

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

## Packages

Find helm charts on https://artifacthub.io/

## Example usage

```sh
helm repo list
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install mysql bitnami/mysql
helm list
helm uninstall mysql
```
Find chart values:

```sh
helm show values bitnami/mysql > values.yaml
vim values.yaml
helm upgrade mysql bitnami/mysql --set section.name=value
helm upgrade mysql bitnami/mysql --values=values.yaml
```