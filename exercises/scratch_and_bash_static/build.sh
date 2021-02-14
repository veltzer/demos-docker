#!/bin/bash -e
image_name=$(basename $PWD)
cp /bin/bash-static bash
# cp /bin/bash .
docker build --tag "${image_name}:latest" .
