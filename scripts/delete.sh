#!/bin/bash -e
image_name=$(basename "${PWD}")
docker rm "${image_name}" || true
