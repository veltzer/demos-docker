#!/bin/sh
image_name=$(basename $PWD)
cp /bin/bash-static .
docker build --tag "${image_name}:latest" .
