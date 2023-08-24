#!/bin/bash -e
docker-compose --file compose_folder/docker-compose.yml --project-directory $PWD build
