# Docker compose

## PostgreSQL

Todo ...

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
