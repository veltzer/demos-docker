#!/bin/bash -e
docker-compose down
docker volume rm postgres_data
