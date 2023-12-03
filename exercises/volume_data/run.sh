#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename "${PWD}")
docker run --detach --user "${UID}:${GID}" --volume "${PWD}/data:/data" "${image_name}"
