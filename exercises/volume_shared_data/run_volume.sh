#!/bin/sh
VOLUME_NAME="my_volume"
docker volume rm "${VOLUME_NAME}"
docker volume create "${VOLUME_NAME}"
image_name=$(basename "${PWD}")
docker run -d --volume "${VOLUME_NAME}:/data" "${image_name}" python app.py app1 2
docker run -d --volume "${VOLUME_NAME}:/data" "${image_name}" python app.py app2 7
