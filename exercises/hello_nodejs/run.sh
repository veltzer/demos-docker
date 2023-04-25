#!/bin/sh
image_name=$(basename "${PWD}")
docker run -p 8000:8000 "${image_name}"
