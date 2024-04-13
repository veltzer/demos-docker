#!/bin/bash -e
image=$(basename "${PWD}")
version="latest"
username="veltzer"
# site="docker.io"
site="ghcr.io"
docker tag "${image}:latest" "${site}/${username}/${image}:${version}"
docker push "${site}/${username}/${image}:${version}"
