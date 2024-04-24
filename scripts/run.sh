#!/bin/bash -e
RUN_ARGS="-it"
if [ -f "source.sh" ]
then
	source source.sh
fi
image_name=$(basename "${PWD}")
docker run ${RUN_ARGS} "${image_name}"
