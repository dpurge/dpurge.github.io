# Service

Pods are ephemeral, so we cannot rely on pod IP addresses.

Example deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-frontend
  labels:
    app.kubernetes.io/name: web-frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: web-frontend
  template:
    metadata:
      labels:
        app.kubernetes.io/name: web-frontend
    spec:
      containers:
        - name: web-frontend-container
          image: projectid/helloworld:0.1.0
          ports:
            - containerPort: 3000
```

```sh
kubectl apply -f web-frontend.yaml
kubectl get po -o wide
kubectl run curl --image=radial/busyboxplus:curl -i --tty
curl 172.17.0.6:3000
```

Pod's IP is available only from within the cluster.

Kubernetes `service` is an abstraction which gives us access to pod's IP in a reliable way.
Service controller maintains a list of pod endpoints/IP addresses.
It uses selectors and labels to find its pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-frontend
  labels:
    app.kubernetes.io/name: web-frontend
spec:
  selector:
    app.kubernetes.io/name: web-frontend
  ports:
    - port: 80
      name: http
      targetPort: 3000
```

```sh
kubectl apply -f web-frontend-service.yaml
kubectl get service
kubectl attach curl -c curl -i -t
curl 10.109.203.211 # Cluster IP
curl web-frontend.default.svc.cluster.local # DNS name with namespace, kind and cluster name specified
curl web-frontend # same namespace
curl web-frontend.default # namespace specified
```

You can use proxy to access the API server from local computer:

```sh
kubectl proxy --port=8080
curl localhost:8080/api/v1/pods
curl localhost:8080/api/v1/namespaces
curl -v -L localhost:8080/api/v1/namespaces/default/services/web-frontend:80/proxy
```

Getting information about service:

```sh
kubectl describe svc web-frontend
kubectl get endpoints
```

Service types `kubectl describe svc web-frontend`:

- `ClusterIP` - cluster internal IP address; default; used for applications running inside the cluster
- `NodePort` - a specific port opened on every node in the cluster, forwards traffic to the service and pods
- `LoadBalancer` - expose kubernetes services to external traffic
- `ExternalName` - 

Node port should be between 30000 and 32767, and can optionally be set as `nodePort` property under `ports`.
However, the best practice is to leave it out and let Kubernetes choose the port number.
You can access them on the node IP: `kubectl describe node | grep InternalIP`

```yaml
kind: Service
spec:
  type: NodePort
  ports:
    - port: 80
      name: http
      targetPort: 3000
      nodePort: 32767 # optional; best practice is to leave it out
```

In the cloud, load balancer service will be exposed by the cloud implementation of the load balancer.
Locally, even if external IP is pending, load balancer service will be available on localhost address.
On Minikube, `minikube tunnel` will assingn a public IP to any service  with type LoadBalancer.

```yaml
kind: Service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      name: http
      targetPort: 3000
```

ExternalName service type does not use selectors; instead it uses DNS names to route traffic to the application that lives outside of the cluster.
You can use it to map a Kubernetes service to the external DNS name; eg. when you are migrating an application to Kubernetes.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-database
spec:
  type: ExternalName
  externalName: db.example.com
```
