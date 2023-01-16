# Docker volumes

Docker Desktop for Windows stores volumes in the WSL instance `docker-desktop-data`.
It is used by Docker Desktop backend to store images and volumes.

To export it:

```sh
wsl --export docker-desktop-data docker-desktop-data.tar
```

## Creating and removing volumes

```sh
docker volume create jdp_src
docker volume rm jdp_src
```

## Mounting volumes

Mounting simple volumes:

```sh
docker run -it --rm --volume jdp_src:/src alpine
docker run -it --rm --mount source=jdp_src,target=/src alpine
```

Mounting from WSL:

```sh
docker run -it --rm --volume "\\wsl$\Ubuntu\var\docker\volumes\alpine_persistent_data:/data" alpine
```
