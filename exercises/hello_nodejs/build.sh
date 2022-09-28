#!/bin/sh
image_name=$(basename $PWD)
docker build --network=host --tag "${image_name}:latest" .
