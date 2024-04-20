#!/bin/bash -e
docker rm my-postgres
docker run -d --name my-postgres  -e POSTGRES_PASSWORD=db_password -p 5432:5432 postgres
