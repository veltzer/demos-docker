#!/bin/sh
image_name=$(basename $PWD)
docker run -it "${image_name}"
