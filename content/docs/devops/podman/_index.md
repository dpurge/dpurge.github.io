---
title: Podman
bookCollapseSection: true
---

A Pod is a group of one or more containers,
with shared storage/network resources,
and a specification for how to run the containers.

Pods are a way of grouping containers together inside their own namespace, network, and security context.
You can even start and stop the whole pod at once.

Podman lets you:

- generate Kubernetes definitions from the existing pod with `podman generate kube` command
- run Kubernetes definitions using the `podman play kube` command

## Setup

```sh
sudo dnf install -y podman podman-docker docker-compose
sudo systemctl enable podman.socket
sudo systemctl start podman.socket
sudo systemctl status podman.socket

sudo curl -H "Content-Type: application/json" --unix-socket

flatpak install flathub io.podman_desktop.PodmanDesktop
```

Test:

```sh
podman pull hello-world 
podman run hello-world
podman ps -a
podman pod ls
```

Build and run image:

```sh
podman build .
podman images
podman run -p 8080:8080 {image-name}
podman stop {container_id}
podman rmi {image_id}
```

Run K3D:

```sh
XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR:-/run/user/$(id -u)}
export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock
k3d cluster create
```

K3D registry:

```sh
k3d registry create --default-network podman mycluster-registry
k3d cluster create --registry-use mycluster-registry mycluster
```

Using `docker-compose` in root-ful mode:

```sh
sudo docker-compose up
sudo docker-compose down
```

Using `docker-compose` with root-less podman:

```sh
systemctl --user enable podman.socket
systemctl --user start podman.socket
systemctl --user status podman.socket
export DOCKER_HOST=unix:///run/user/$UID/podman/podman.sock
```

## Pods

Create a pod:

```sh
sudo podman pod create --name wordpress -p 8080:80

sudo podman run \
-d --restart=always --pod=wordpress \
-e MYSQL_ROOT_PASSWORD="rootpass" \
-e MYSQL_DATABASE="wordpress" \
-e MYSQL_USER="wordpress" \
-e MYSQL_PASSWORD="wordpress" \
--name=wordpress-db mariadb

sudo podman run \
-d --restart=always --pod=wordpress \
-e WORDPRESS_DB_NAME="wordpress" \
-e WORDPRESS_DB_USER="wordpress" \
-e WORDPRESS_DB_PASSWORD="wordpress" \
-e WORDPRESS_DB_HOST="127.0.0.1" \
--name wordpress-web wordpress

sudo podman pod ls
sudo podman ps
```

Access: `http://localhost:8080/`

Generate `YAML`:

```sh
sudo podman generate kube wordpress >> wordpress.yaml
```

Output:

```yaml
apiVersion: v1
kind: Pod

metadata:
  labels:
    app: wordpress
  name: wordpress

spec:

  containers:

  - name: wordpress-web
    env:
    - name: WORDPRESS_DB_NAME
      value: wordpress
    - name: WORDPRESS_DB_HOST
      value: 127.0.0.1
    - name: WORDPRESS_DB_USER
      value: wordpress
    - name: WORDPRESS_DB_PASSWORD
      value: wordpress
    image: docker.io/library/wordpress:latest
    ports:
    - containerPort: 80
      hostPort: 8080
      protocol: TCP
    securityContext:
      allowPrivilegeEscalation: true
      privileged: false
      readOnlyRootFilesystem: false
    workingDir: /var/www/html

  - name: wordpress-db
    env:
    - name: MYSQL_ROOT_PASSWORD
      value: rootpass
    - name: MYSQL_USER
      value: wordpress
    - name: MYSQL_PASSWORD
      value: wordpress
    - name: MYSQL_DATABASE
      value: wordpress
    image: docker.io/library/mariadb:latest
    securityContext:
      allowPrivilegeEscalation: true
      privileged: false
      readOnlyRootFilesystem: false
    workingDir: /
```

Play:

```sh
sudo podman play kube ./wordpress.yaml
sudo podman pod ls
sudo podman ps
```
