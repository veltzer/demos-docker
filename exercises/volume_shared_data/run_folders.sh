#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename $PWD)
docker run -d --user $UID:$GID --volume "${PWD}/data:/data" "${image_name}" python app.py app1 2
docker run -d --user $UID:$GID --volume "${PWD}/data:/data" "${image_name}" python app.py app2 7
