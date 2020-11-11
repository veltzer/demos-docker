#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename $PWD)
docker run -it --user $UID:$GID --volume "${PWD}/data:/data" -e SLEEP_TIME -e INCREMENT "${image_name}" /app.py
