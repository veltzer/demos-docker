#!/bin/sh
UID=`getent passwd mark | cut -d ":" -f 3`
GID=`getent passwd mark | cut -d ":" -f 4`
docker run --detach --user $UID:$GID --volume /home/mark/tmp:/data data_volume
# everything is running, take a look
docker ps
