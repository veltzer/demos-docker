#!/bin/sh
docker run --detach=true --mount source=shared_volume,target=/data docker_volume writer.py data prefix1
docker run --detach=true --mount source=shared_volume,target=/data docker_volume writer.py data prefix2
# everything is running, take a look
docker ps
