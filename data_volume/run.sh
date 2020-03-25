#!/bin/sh
docker run --detach=true --user 1000:1000 --volume /home/mark/tmp:/data data_volume
# everything is running, take a look
docker ps
