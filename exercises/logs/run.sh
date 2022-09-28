#!/bin/sh
image_name=$(basename $PWD)
docker run --log-driver json-file "${image_name}"
