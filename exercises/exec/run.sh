#!/bin/sh
image_name=$(basename $PWD)
docker run --detach "${image_name}"
# docker run -it "${image_name}"
