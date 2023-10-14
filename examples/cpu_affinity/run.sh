#!/bin/sh
image_name=$(basename "${PWD}")
docker run --detach --cpuset-cpus=6 --cpus=0.5 "${image_name}"
