# K3s

K3s deploys a virtual machine-based Kubernetes cluster.

## Installation

```sh
curl -Lo /usr/local/bin/k3s https://github.com/k3s-io/k3s/releases/download/v1.27.5%2Bk3s1/k3s
chmod a+x /usr/local/bin/k3s
```

## Test

```sh
K3S_KUBECONFIG_MODE="644" k3s server --flannel-backend none
```