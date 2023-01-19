#!/bin/bash -e
docker run --detach --network=host app_a /app_a.py localhost
docker run --detach --network=host app_b
