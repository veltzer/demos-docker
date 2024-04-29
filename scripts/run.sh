#!/bin/bash -e
if [ -f "source_before_run.sh" ]
then
	# shellcheck source=/dev/null
	source source_before_run.sh
else
	RUN_ARGS="-it"
fi
image_name=$(basename "${PWD}")
if docker ps -a --filter "name=${image_name}" --format '{{.Names}}' | grep -q "${image_name}"
then
	echo "Container [${image_name}] exists. Removing..."
	docker kill "${image_name}"
	sleep 5
fi
docker run ${RUN_ARGS} --name "${image_name}" "${image_name}"
