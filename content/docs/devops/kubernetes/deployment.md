# Deployment

`Deployment` is a wrapper around replica set, which allows to do controlled updates to pods.
When we update the pod template in the deployment, it will update the pods.

```yaml
apiVersion: apps/v1
kind: Deployment
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
          command: ['sh', '-c', 'echo Hello from deployment! && sleep 3600']
```

```sh
kubectl apply -f deployment.yaml --record
kubectl get deployment
kubectl get rs
kubectl get pod
kubectl scale deployment hello --replicas=5
kubectl get po --watch
kubectl scale deploy hello --replicas=3
kubectl set image deploy hello hello-container=busybox:1.31.1 --record
kubectl rollout history deploy hello
kubectl rollout undo deploy hello
```

Deployment strategies:

- `Recreate` - deletes all pods and starts new ones
- `RollingUpdate` - you optionally define maximum unavailable and maximum surge numbers (default is 25%), new pods are created before old pods are deleted

```yaml
spec:
  strategy:
    type: Recreate
```

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 40%
      maxSurge: 40%
```
