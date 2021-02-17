#!/bin/sh
image_name=$(basename $PWD)
docker run -it --cpuset-cpus=6 --cpus=0.5 "${image_name}"
