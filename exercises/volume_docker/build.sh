#!/bin/sh
echo "building the image..."
docker build --tag docker_volume:latest --file Dockerfile . 2> /dev/null > /dev/null
# everything is built, take a look
docker images | grep docker_volume
