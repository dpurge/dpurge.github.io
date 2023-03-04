# Sealed secrets

## Install `kubeseal`

Command line:

```sh
curl -sSL https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.19.3/kubeseal-0.19.3-linux-amd64.tar.gz -o kubeseal-linux-amd64.tar.gz
tar -xf kubeseal-linux-amd64.tar.gz kubeseal
mv kubeseal /usr/local/bin/
kubeseal --version
```

Controller:

```sh
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.19.3/controller.yaml
kubectl get pods -n kube-system | grep sealed-secrets-controller
kubectl logs sealed-secrets-controller-xxx-xxx -n kube-system
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml
```