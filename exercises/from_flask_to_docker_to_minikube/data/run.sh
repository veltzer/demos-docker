#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename $PWD)
docker run --user $UID:$GID --detach --volume $PWD/data:/data --network host "${image_name}"
