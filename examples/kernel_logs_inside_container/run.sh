#!/bin/sh
image_name=$(basename "${PWD}")
docker run -it --memory=4G --cap-add CAP_SYSLOG "${image_name}"
