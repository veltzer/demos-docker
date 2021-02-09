#!/bin/sh
image_name=$(basename $PWD)
docker run --detach "${image_name}"
