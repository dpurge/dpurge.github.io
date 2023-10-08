# Azure from docker

## Access to the storage account

Dockerfile:

```sh
FROM ubuntu:22.04

RUN apt-get update && apt install -y ca-certificates pkg-config libfuse-dev cmake libcurl4-gnutls-dev libgnutls28-dev uuid-dev libgcrypt20-dev wget

RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
	&& rm packages-microsoft-prod.deb
	
RUN apt-get update

RUN apt-get install -y blobfuse fuse
RUN mkdir /storage-container

COPY fuse_connection.cfg /fuse_connection.cfg
```

Contents of `fuse_connection.cfg`:

```sh
accountName mystgaccnt
accountKey xxxxxxxxxxxxxxxxxxxxxx
containerName test-data
```

Build and start the container:

```sh
docker build -t azure-data .
docker run -it --rm --cap-add SYS_ADMIN --device /dev/fuse azure-data bash
```

Create blob in `test-data` container:

```sh
blobfuse /storage-container --tmp-path=/mnt/resource/blobfusetmp  --config-file=/fuse_connection.cfg -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120
mkdir /storage-container/test
echo "hello world" > test/hello-blob.txt
```

In another instance, read that data:

```sh
blobfuse /storage-container --tmp-path=/mnt/resource/blobfusetmp  --config-file=/fuse_connection.cfg -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120
cat /storage-container/test/hello-blob.txt
```

Delete blob and the directory:

```sh
rm /storage-container/test/hello-blob.txt
rmdir /storage-container/test
```

Example:

```sh
az login
az account set --subscription "DEV environment"
az acr login -n devdockercr001
docker pull devdockercr001.azurecr.io/devops-tools

docker pull postgres
docker run  -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d -p 5432:5432 postgres
```
