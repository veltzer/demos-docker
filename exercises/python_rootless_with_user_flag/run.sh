#!/bin/sh
image_name=$(basename $PWD)
docker run -it --user 1200:1200 "${image_name}"
