# Podman compose

Podman Compose picks the services defined inside the `docker-compose.yaml` file and creates a container for each service.
Podman Compose adds the containers to a single pod for the whole project, and all the containers share the same network.

## Install

```sh
pip3 install https://github.com/containers/podman-compose/archive/devel.tar.gz
```

## Running

What happens when you run `podman-compose up` in the project directory:

- a pod is created and named after the directory
- named volumes defined in the YAML file are created if they do not exist
- one container is created for each service listed in the YAML file and added to the pod
- localhost aliases are added to each named container

Containers can resolve each other by name, although they are not on a bridge network.
To do this, use the option `–add-host`, ex: `–add-host web:localhost`.

Run:

```sh
podman-compose up
podman ps
podman-compose down

podman pod stop {podname}
podman pod rm {podname}
```

## Samples

Wordpress:

```yaml
version: "3.8"
services: 
  web:
    image: wordpress
    restart: always
    volumes:
      - wordpress:/var/www/html
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_TABLE_PREFIX: cz
      WORDPRESS_DEBUG: 0
    depends_on:
      - db
    networks:
      - wpnet
  db:
    image: mariadb:10.5
    restart: always
    ports:
      - 6603:3306

    volumes:
      - wpdbvol:/var/lib/mysql

    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
      MYSQL_ROOT_PASSWORD: wordpress
    networks:
      - wpnet
volumes:
  wordpress: {}
  wpdbvol: {}

networks:
  wpnet: {}
```

Access: `http://localhost:8080`

