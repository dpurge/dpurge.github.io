# Pod

A `pod` is a collection of containers that share network and storage.
Containers within a pod can talk to each other on `localhost` and can access the same volumes.
Pods are ephemeral.
Kubernetes assigns a unique IP address to a pod.
Containers within a pod can listen on different ports.

When the pod restarts, it gets a different IP address.
A `service` is an abstraction that gets a stable IP address and DNS name and acts as a load balancer for pods.

All containers within a pod will get scaled together - a pod is the unit of scale.
You cannot scale individual containers within the pod.

## Creating pods

You should not create pods directly.
One of the reasons is that if the pod crashes or is deleted, it will not be restarted.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-pod
  labels:
    app.kubernetes.io/name: hello
spec:
  containers:
    - name: hello-container
      image: busybox
      command: ["sh", "-c", "echo Hello World && sleep 3600"]
```

```sh
kubectl apply -f hello-pod.yaml
kubectl get pods
kubectl logs hello-pod
lubectl describe pod hello-pod
kubectl delete pod hello-pod
```
