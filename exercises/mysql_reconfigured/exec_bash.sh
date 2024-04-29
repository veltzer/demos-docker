#!/bin/bash -e
image_name=$(basename "${PWD}")
docker exec -it "${image_name}" bash
