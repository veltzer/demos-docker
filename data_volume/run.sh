#!/bin/sh
docker run --detach=true --volume /home/mark/tmp:/data data_volume
# everything is running, take a look
docker ps
