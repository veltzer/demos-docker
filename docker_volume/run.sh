#!/bin/sh
docker run --detach=true --mount source=shared_volume,target=/data docker_volume python writer.py /data/d1.txt
docker run --detach=true --mount source=shared_volume,target=/data docker_volume python writer.py /data/d2.txt
# everything is running, take a look
docker ps
