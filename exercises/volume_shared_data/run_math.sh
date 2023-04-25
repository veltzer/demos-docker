#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename "${PWD}")
docker run -d --user "${UID}:${GID}" --volume "${PWD}/data:/data" -e SLEEP_TIME=5 -e INCREMENT=1 "${image_name}"
docker run -d --user "${UID}:${GID}" --volume "${PWD}/data:/data" -e SLEEP_TIME=3 -e INCREMENT=5 "${image_name}"
