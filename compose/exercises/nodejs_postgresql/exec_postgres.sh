#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
docker exec -it nodejs_postgresql_postgres_1 bash
