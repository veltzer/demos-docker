#!/bin/sh
image_name=$(basename "${PWD}")
# --log-driver json-file is the default
docker run --detach --name "${image_name}" "${image_name}"
