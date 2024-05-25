#!/bin/bash -e
image_name=$(basename "${PWD}")
docker kill "${image_name}" || true
sleep 5
docker rm "${image_name}" || true
