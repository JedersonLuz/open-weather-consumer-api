# OpenWeather Consumer API
 
API that consume data from OpenWeather API

## Requirements

To run the application you will need to install Python3 and Docker.

## How to run

With Docker installed run the following commands to setup the environment.

To setup and execute database run:

```console
docker run -d --name postgres-container -e TZ=UTC -p 30432:5432 -e POSTGRES_PASSWORD=<your-database-password> ubuntu/postgres:14-22.04_beta
docker exec -i postgres-container /bin/bash -c "PGPASSWORD=<your-database-password> psql --username postgres postgres" < dump.sql
docker run --hostname=65737bc08514 \
    --mac-address=02:42:ac:11:00:02 \
    --env=TZ=UTC \
    --env=POSTGRES_PASSWORD=<your-database-password> \
    --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin \
    --env=DEBIAN_FRONTEND=noninteractive \
    --env=LANG=en_US.utf8 \
    --env=PG_MAJOR=14 \
    --env=PGDATA=/var/lib/postgresql/data \
    --volume=/var/lib/postgresql/data \
    -p 30432:5432 --restart=no --runtime=runc -d ubuntu/postgres:14-22.04_beta
```

To build and execute the API run:

```console
docker build -t open-weather-consumer-api .
docker run --hostname=ec6089a3f40a \
    --env=API_KEY=<your-open-weather-api-key> \
    --env=DB_HOST=<database-address> \
    --env=DB_PORT=<database-port> \
    --env=DB_USER=<database-username> \
    --env=DB_PASS=<database-password> \
    --env=DB_NAME=<database-name> \
    --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    --workdir=/app -p 8000:8000 \
    --runtime=runc -d open-weather-consumer-api:latest
```

## How to test

To execute the tests you need to install the pytest package. To install the package run:

```console
pip install pytest
```

To execute the tests just run:

```console
pytest
```
