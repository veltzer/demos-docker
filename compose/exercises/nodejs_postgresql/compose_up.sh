#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
# docker-compose build
docker-compose up --detach --remove-orphans
