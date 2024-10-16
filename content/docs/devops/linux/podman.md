# Podman

- container management tool
- does not require a daemon
- each container is run in its own process
- supports rootless containers
- created by RedHat
- is open source

## Podman vs Docker

Differences:

- Podman has deamonless architecture and runs containers as processes.
  Docker utilizes a client-server architecture, docker daemon runs as a background process.
- Podman supports rootless containers.
  Docker generally requires administrative privileges to run containers.
- Podman is considered more secure because it does not require a deamon and can run containers as non-root.
  Docker raises security concerns because of a daemon running with root privileges.
- Podman supports multiple image formats.
  Docker uses docker image format.
- Podman leverages the host system networking directly.
  Docker manages networking through its own implementation.

Similarities:

- similar command line interface
- container formats are compatible

## Installation

MacOS:

```sh
export PATH="/opt/homebrew/bin:$PATH"
brew install podman
podman --version
```

## Podman machine

Manages lightweight, virtualized environments for running containers.

```sh
podman machine init podman1
podman machine start podman1
podman machine list
podman machine info
podman machine inspect podman1
podman machine stop podman1
podman machine rm podman1
```

## Images

- blueprints for containers
- contain necessary configurations and components

```sh
podman pull alpine:latest
podman info # check registries.search
podman images
```

## Containers

Container lifecycle:

- created: defined and configured, but not yet started
- up: running the application or service
- paused: halted temporarily, its processes frozen; can be resumed maintaining its state
- stopped: its processes halted; does not consume resources; can be restarted
- exited: completed its execution

```sh
podman run hello-world
podman ps -a

podman run -d -it --name alp1 docker.io/library/alpine:latest /bin/sh
podman ps
podman exec -it alp1 /bin/sh
podman stop alp1
podman start alp1
podman rm alp1
```

## Custom container

```py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == "main":
    app.run(host ='0.0.0.0', port = 80)
```

```dockerfile
FROM alpine:latest
LABEL maintainer="me@example.com"
WORKDIR /app
COPY . /app
RUN apk add --no-cache python3
EXPOSE 80
CMD ["python3", "./app.py"]
```

```sh
podman build -t my-flask:latest .
podman images
```

## Webserver

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World from Flask</title>
    </head>
    <body> 
        <h1>Hello, world!!!</h1>   
        <p>Welcome to the web server...</p>
    </body>
</html>
```

```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html
```

```sh
podman build -t webserver .
podman images
podman run -d --name webserver -p 9090:80 webserver
podman ps
```
