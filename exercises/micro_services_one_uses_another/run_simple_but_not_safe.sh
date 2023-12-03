#!/bin/bash -e
docker run --detach --network=host --name app_b app_b
docker run --detach --network=host --name app_a app_a /app_a.py localhost
