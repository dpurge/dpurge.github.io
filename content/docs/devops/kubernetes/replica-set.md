# Replica set

`Replica set` maintains a stamble number of pod copies (replicas).

Replica set controller guarantees that a specified nymber of identical pods are running at all times.
It uses the selector field and pod labels to find pods that it owns.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: hello
  labels:
   app.kubernetes.io/name: hello
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: hello
  template:
    metadata:
      labels:
        app.kubernetes.io/name: hello
    spec:
      containers:
      - name: hello-container
        image: busybox
        command: ["sh", "-c", "echo Hello from replica set! && sleep 3600"]
```

```sh
kubectl apply -f replicaset.yaml
kubectl get replicaset
kubectl get pods -l app.kubernetes.io/name=hello
kubectl get pods hello-xxxxx -o yaml | grep -A5 ownerReferences
kubectl delete po hello-xxxxx
kubectl edit rs hello
kubectl get po hello-xxxxx  | grep Image
kubectl delete rs hello
```

Replica set can be managed by a `deployment`, which can update pods managed by this replica set in a controlled, zero-downtime manner.
