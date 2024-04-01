# K3s

K3s deploys a virtual machine-based Kubernetes cluster.

## Installation

```sh
curl -Lo /usr/local/bin/k3s https://github.com/k3s-io/k3s/releases/download/v1.27.5%2Bk3s1/k3s
chmod a+x /usr/local/bin/k3s
```

```sh
curl -Lo /usr/local/bin/kubectl "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod a+x /usr/local/bin/kubectl
```

## Maintenance

```sh
sudo k3s crictl images
sudo k3s crictl rmi --prune
```

## Test

Start server:

```sh
K3S_KUBECONFIG_MODE="644" k3s server --flannel-backend none
```

Access server:

```sh
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
kubectl get pods --all-namespaces
helm ls --all-namespaces
```

Install in LXD container:

```sh
sudo su -
cd /tmp
curl https://get.k3s.io/ -o k3s.sh
chmod +x k3s.sh
./k3s.sh
systemctl status k3s
k3s check-config
```

Troubleshooting:

```sh
cat /etc/os-release
ip a s
tail /var/log/syslog
journalctl -u k3s.service
/usr/local/bin/k3s-uninstall.sh
```
