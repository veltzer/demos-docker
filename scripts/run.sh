#!/bin/bash -e
if [ -f "RUN_ARGS" ]
then
	read -r RUN_ARGS < RUN_ARGS
else
	RUN_ARGS="-it"
fi
image_name=$(basename "${PWD}")
docker run ${RUN_ARGS} "${image_name}"
