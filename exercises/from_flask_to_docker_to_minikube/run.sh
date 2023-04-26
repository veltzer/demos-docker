#!/bin/bash -e
image_name=$(basename "${PWD}")
rm -rf data
mkdir data
docker run --user "${UID}:${UID}" --detach --volume "${PWD}/data:/data" --network host "${image_name}"
