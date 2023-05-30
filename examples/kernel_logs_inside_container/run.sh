#!/bin/sh
image_name=$(basename "${PWD}")
# removing the --cap-add CAP_SYSLOG in the next line will break this example
docker run -it --memory=4G --cap-add CAP_SYSLOG "${image_name}"
