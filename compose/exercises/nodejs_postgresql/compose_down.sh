#!/bin/bash -e
source .env
docker-compose down
docker volume rm nodejs_postgresql_postgres_data
