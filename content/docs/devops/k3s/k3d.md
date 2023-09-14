# K3d

K3d is a wrapper of K3s.
K3d deploys docker based k3s clusters.

## Installation

K3d CLI binaries:

- <https://github.com/k3d-io/k3d/releases/download/v5.4.8/k3d-windows-amd64.exe>
- <https://github.com/k3d-io/k3d/releases/download/v5.4.8/k3d-linux-amd64>

## Test

```sh
k3d cluster create mycluster
kubectl cluster-info
kubectl get all
k3d cluster delete mycluster
```
