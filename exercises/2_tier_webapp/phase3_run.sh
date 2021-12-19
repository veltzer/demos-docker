#!/bin/sh
image_name=$(basename $PWD)
docker run -d --network host "${image_name}"
