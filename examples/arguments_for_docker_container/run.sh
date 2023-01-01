#!/bin/sh
image_name=$(basename $PWD)
docker run -it -e A=6 "${image_name}"
