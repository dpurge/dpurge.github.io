# Kubernetes on Azure

## Deployment to cluster

Connect to Azure container registry:

```sh
az account set --subscription $SubscriptionID
az aks get-credentials --resource-group ResGrp-Name001 --name acrname001
```

Create namespace YAML:

```sh
kubectl create namespace my-namespace-name -o yaml --dry-run=client
```

Create deployment YAML:

```sh
kubectl create deployment image-name --image=acrname001.azurecr.io/image_name:1.0.0 -o yaml --dry-run=client
```

Apply namespace YAML:

```sh
kubectl apply -f namespace.yaml
kubectl get namespaces
```

Apply deployment YAML:

```sh
kubectl apply -f image-name-deployment.yaml
kubectl logs -f deployment/image-name --namespace my-namespace-name
```

Check deployments:

```sh
kubectl get deployments --all-namespaces=true
kubectl get deployments --namespace $CurrentNamespace
kubectl describe deployment $CurrentDeployment --namespace $CurrentNamespace
kubectl logs -l $LabelKey=$LabelValue
```

List pods:

```sh
kubectl get pods --namespace my-namespace-name
```

Execute command on a pod:

```sh
kubectl exec image-name-xxxxxxxxxx-xxxxx --namespace my-namespace-name -- python --version
```

Run interactive shell on a pod:

```sh
kubectl exec --stdin --tty image-name-xxxxxxxxxx-xxxxx --namespace my-namespace-name -- bash
```
