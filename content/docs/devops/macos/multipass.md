# Multipass

Install with package from `https://multipass.run/install`.

The command is installed in `/usr/local/bin/multipass`.

Logs are in `/Library/Logs/Multipass/multipassd.log`.

Usage:

```sh
multipass networks
multipass set local.bridged-network=en0
multipass launch docker --name jdp --cpus 2 --memory 6G --disk 50G --bridged
multipass info jdp
multipass shell jdp
multipass start jdp
multipass restart jdp
multipass stop jdp
multipass delete jdp

multipass launch docker --cpus 2 --memory 6G --disk 50G
multipass list
multipass info --all
multipass purge
```

## Config

Add to `~/.zprofile`:

```sh
PATH="${PATH}:/Users/david/Library/Application Support/multipass/bin"
```

Applications to install:

- KubeCtl
- [K3D](https://github.com/k3d-io/k3d/releases/)

Inside Ubuntu, install additional tools:

```sh
# kubectl
curl -LO https://dl.k8s.io/release/v1.28.3/bin/linux/arm64/kubectl
sudo chmod +x kubectl
sudo mv kubectl /usr/local/bin

# K3D
sudo curl -sfL https://github.com/k3d-io/k3d/releases/download/v5.6.0/k3d-linux-arm64 --output k3d
sudo chmod +x k3d
sudo mv k3d /usr/local/bin
```

In MacOS terminal:

```sh
multipass mount $HOME jdp
multipass mount /opt/jdp/src jdp
multipass alias docker:kubectl kubectl
multipass alias docker:k3d k3d
```

MacOS firewall [has problems](https://github.com/canonical/multipass/issues/2387).

On unmanaged Mac:

```sh
/usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/libexec/bootpd
/usr/libexec/ApplicationFirewall/socketfilterfw --unblock /usr/libexec/bootpd
```
