#!/bin/sh
image_name=$(basename $PWD)
docker run -p 3000:3000 "${image_name}"
