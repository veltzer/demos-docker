#!/bin/sh
image_name=$(basename "${PWD}")
docker run -it --memory=20m "${image_name}"
