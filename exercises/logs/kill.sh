#!/bin/sh
image_name=$(basename "${PWD}")
docker kill "${image_name}"
docker rm "${image_name}"
