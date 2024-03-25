# Docker compose

## CI/CD test environment

```yaml
version: 3.8

networks:
  pipeline:
    external: false

services:

  postgres:
    image: postgres
    container_name: postgres
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    networks:
      - pipeline
    ports:
      - 5432:5432
    volumes:
      - type: volume
        source: postgres
        target: /var/lib/postgresql/data
      - type: bind
        source: ./init.sql
        target: /docker-entrypoint-initdb.d/init.sql

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin
    environment:
      - PGADMIN_DEFAULT_EMAIL=jdp@example.com
      - PGADMIN_DEFAULT_PASSWORD=pgadmin
    networks:
      - pipeline
    ports:
      - 15433:80
    volumes:
      - type: volume
        source: pgadmin
        target: /var/lib/pgadmin
    depends_on:
      - postgres

  gitea:
    image: gitea/gitea
    container_name: gitea
    restart: always
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=postgres
      - GITEA__database__HOST=postgres:5432
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea
    networks:
      - pipeline
    ports:
      - 3000:3000
      - 222:22
    volumes:
      - type: volume
        source: gitea
        target: /data
    depends_on:
      - postgres

  jenkins:
    image: jenkins/jenkins
    container_name: jenkins
    pribileged: true
    user: root
    restart: always
    environment:
      - DOCKER_HOST=unix:///var/run/docker.sock
    networks:
      - pipeline
    ports:
      - 8080:8080
      - 50000:50000
    volumes:
      - type: bind
        source: /var/run/docker.sock
        target: /var/run/docker.sock
      - type: volume
        source: jenkins
        target: /var/jenkins_home

volumes:
  postgres:
  pgadmin:
  gitea:
  jenkins:
```

`.env` file:

```ini
COMPOSE_CONVERT_WINDOWS_PATHS=1
```

`init.sql` file:

```sql
CREATE ROLE gitea
  WITH ENCRYPTED PASSWORD 'gitea';

ALTER ROLE gitea
  WITH LOGIN;

CREATE DATABASE gitea;

GRANT ALL PRIVILEGES
  ON DATABASE gitea
  TO gitea;

\c gitea postgres
GRANT ALL
  ON SCHEMA public
  TO gitea;
```

## MSSQL Server

`./db/Dockerfile`:

```sh
FROM mcr.microsoft.com/mssql/server:2019-latest

WORKDIR /usr/src/app

COPY ./entrypoint.sh /usr/src/app

EXPOSE 1432
EXPOSE 1433

USER root
CMD /bin/bash ./entrypoint.sh
```

`./db/entrypoint.sh`:

```sh
/opt/mssql/bin/sqlservr
```

`./docker-compose.yaml`:

```yaml
version: "3"
services:
  db:
      restart: always      
      build:
        context: ./db
        dockerfile: ./Dockerfile      
      environment:
        SA_PASSWORD: p@ssw0rd
        ACCEPT_EULA: "Y"      
      ports:
        - "1433:1433"
```
