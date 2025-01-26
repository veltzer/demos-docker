#!/bin/bash -e
if [ -x ./before_build.sh ]
then
	./before_build.sh
fi
image_name=$(basename "${PWD}")
docker buildx build --load --tag "${image_name}" .
