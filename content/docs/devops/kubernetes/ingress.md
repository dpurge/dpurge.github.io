# Ingress

`Ingress` resource exposes multiple services to the outside of the cluster and manages access.
It is a collection of rules and paths but needs something to apply these rules the `Ingress controller`.
Ingress controller acts as a gateway and routes external traffic to services based on the Ingress resource and its rules.

Ingress controller is a collection of:

- kubernetes deployment, with pods running containers with a gateway or proxy server, eg. nginx, ambassador
- kubernetes service that exposes ingress controller pods
- supporting resources: configuration maps, secrets etc.

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-example
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /blog
            backend:
              serviceName: blogservice
              servicePort: 80
          - path: /music
            backend:
              serviceName: musicservice
              servicePort: 8080
```

Ingress controller will have annotations that depend on the type of Ingress Controller you are using (Traeffik. Nginx, HAProxy, Ambassador, ...)

Example with Ambassador gateway:

```sh
kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-crds.yaml
kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-rbac.yaml
kubectl get deploy
kubectl get po
kubectl get svc
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ambassador
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    service: ambassador
  ports:
    - port: 80
      targetPort: 8080
```

```sh
kubectl apply -f ambassador-lb.yaml
minikube service ambassador # opens browser to the service address; diagnostics: /ambassador/v0/diag/
```

Ingress without rules:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: ambassador
  name: my-ingress
spec:
  defaultBackend:
    service:
      name: hello-world
      port:
        number: 3000
```

```sh
kubectl apply -f simple-ing.haml
kubectl get ing
minikube service ambassador
```

Example with path-based routing:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: ambassador
  name: my-ingress
spec:
  rules:
    - http:
        paths:
          - path: /hello
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 3000
          - path: /dog
            pathType: Prefix
            backend:
              service:
                name: dog-service
                port:
                  number: 3000
```

```sh
kubectl apply -f path-ing.haml
kubectl describe ing my-ingress
minikube ip
# access:
# http://.../hello
# http://.../dog
```

Hostname based access:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: ambassador
  name: my-ingress
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /hello
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 3000
          - path: /dog
            pathType: Prefix
            backend:
              service:
                name: dog-service
                port:
                  number: 3000
```

```sh
kubectl apply -f hostname-ing.yaml
kubectl describe ing my-ingress
# add DNS record to your domain registrar and access: http://example.com/hello
```

Some ingress controllers will automatically set up default backend service.
In Ambassador you can combine `defaultBackend` and `rules`.

Subdomain ingress:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: ambassador
  name: my-ingress
spec:
  defaultBackend:
    service:
      name: hello-world
      port:
        number: 3000
  rules:
    - host: example.com
      http:
        paths:
          - path: /hello
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 3000
    - host: dog.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: dog-service
                port:
                  number: 3000
```

```sh
kubectl apply -f subdomain-ing.yaml
kubectl describe ing my-ingress
# http://example.com/hello
# http://dog.example.com/
```
