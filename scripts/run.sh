#!/bin/bash -e
RUN_ARGS="-it"
if [ -f "source.sh" ]
then
	# shellcheck source=/dev/null
	source source.sh
fi
image_name=$(basename "${PWD}")
docker rm "${image_name}" || true
docker run ${RUN_ARGS} --name "${image_name}" "${image_name}"
