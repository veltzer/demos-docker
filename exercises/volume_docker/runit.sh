#!/bin/sh
docker run --detach=true --mount source=shared_volume,target=/data volume_docker python writer.py d1 /data/d1.txt
docker run --detach=true --mount source=shared_volume,target=/data volume_docker python writer.py d2 /data/d2.txt
# everything is running, take a look
docker ps
