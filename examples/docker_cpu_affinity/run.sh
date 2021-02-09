#!/bin/sh
image_name=$(basename $PWD)
docker run -it --cpuset-cpus=5 "${image_name}"
