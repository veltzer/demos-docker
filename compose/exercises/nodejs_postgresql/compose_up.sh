#!/bin/bash -e
source .env
# docker-compose build
docker-compose up --detach --remove-orphans
