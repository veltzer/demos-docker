#!/bin/bash -e
if [ -f "source_before_run.sh" ]
then
	# shellcheck source=/dev/null
	source source_before_run.sh
else
	RUN_ARGS="-it --rm"
fi
image_name=$(basename "${PWD}")
if docker ps --filter "name=${image_name}" --format '{{.Names}}' | grep -q "${image_name}"
then
	echo "Container [${image_name}] is running. Killing..."
	docker kill "${image_name}" || true
	sleep 5
fi

if docker ps -a --filter "name=${image_name}" --format '{{.Names}}' | grep -q "${image_name}"
then
	echo "Container [${image_name}] is dead. Removing..."
	docker rm "${image_name}"
fi
# shellcheck disable=SC2086
docker run ${RUN_ARGS} --name "${image_name}" "${image_name}"
