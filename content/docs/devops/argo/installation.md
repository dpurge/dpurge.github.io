# Installation

Install ArgoCD:

```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

```sh
helm repo add argo https://argoproj.github.io/argo-helm
```

Forward port:

```sh
kubectl get all -n argocd
kubectl port-forward service/argocd-server -n argocd 8080:443
```

Extract credential:

```sh
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Login from CLI:

```sh
kubectl port-forward svc/argocd-server -n argocd 8080:443
argocd login 127.0.0.1:8080
```

Install application:

```sh
argocd app create nginx-prod \
  --repo https://github.com/dpurge/argo-config.git \
  --path nginx/overlays/prod \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace prod
```

Cheatsheet:

```sh
argocd app create             # Create a new Argo CD application.
argocd app list               # List all applications in Argo CD.
argocd app logs <appname>     # Get the application’s log output.
argocd app get <appname>      # Get information about an Argo CD application.
argocd app diff <appname>     # Compare the application’s configuration to its source repository.
argocd app sync <appname>     # Synchronize the application with its source repository.
argocd app history <appname>  # Get information about an Argo CD application.
argocd app rollback <appname> # Rollback to a previous version
argocd app set <appname>      # Set the application’s configuration.
argocd app delete <appname>   # Delete an Argo CD application.
```

Cleanup:

```sh
kubectl delete CustomResourceDefinition applications.argoproj.io
kubectl delete CustomResourceDefinition applicationsets.argoproj.io
kubectl delete CustomResourceDefinition appprojects.argoproj.io
```

Examples:

```sh
helm template infra-cluster001/ | kubectl apply -f -

argocd app create argo-cd   --repo https://xxx/homelab.git   --path environments/dev/argo-cd   --dest-server https://kubernetes.default.svc   --dest-namespace argocd
argocd proj create infra --description 'Infrastructure' --dest '*,*' --src '*' --allow-cluster-resource '*/*'
argocd repocreds add https://xxx/_git/infrastructure-helm-charts --username infrastructure-helm-charts --password xxxxxxxxxxxx
argocd app create root --repo https://xxx/_git/infrastructure-helm-charts --path infra-cluster001 --dest-namespace default --dest-server https://kubernetes.default.svc
```
