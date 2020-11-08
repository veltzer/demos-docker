#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename $PWD)
docker run -it --user $UID:$GID --volume /home/mark/tmp:/data "${image_name}"
