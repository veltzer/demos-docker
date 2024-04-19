#!/bin/bash -e
docker-compose build
docker-compose up --detach --remove-orphans
