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

Examples:

```sh
az account set --subscription xxxxxxxxxxx
az aks get-credentials --resource-group ResGrp-xxx-K8s --name xxxx
kubectl config current-context

kubectl get all --namespace xxx
kubectl get cronjob --namespace xxx
kubectl describe cronjob --namespace xxx
kubectl get pods --namespace xxx
kubectl logs --namespace xxx integration-sync-28023457-cbg4j
kubectl delete job --namespace xxx integration-sync-28023332
kubectl delete cronjob integration-sync --namespace xxx

kubectl exec --stdin --tty xxx-867d77f465-tkcdk --namespace xxx -- /bin/bash
curl -X POST 127.0.0.1/sync --data '{"time_to_sync": 240}' --header "Content-Type: application/json"
```
