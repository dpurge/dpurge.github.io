# KubeCtl configuration

## Configuration files

Default file:

- `~/.kube/config`
- `%USERPROFILE%\.kube\config`

Multiple files defined in environment variable:

```cmd
set KUBECONFIG=%USERPROFILE%\.kube\config;%USERPROFILE%\.kube\jdpnas02.yaml
```

```sh
KUBECONFIG=~/.kube/config:~/.kube/jdpnas02.yaml
```

Display configured contexts:

```sh
kubectl config get-contexts
```

Display merged configs:

```sh
kubectl config view
```

Show current context:

```sh
kubectl config current-context
```

Set default context:

```sh
kubectl config use-context jdpnas02
```
