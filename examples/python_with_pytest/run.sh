#!/bin/sh
image_name=$(basename "${PWD}")
docker run "${image_name}"
