#!/bin/sh
image_name=$(basename $PWD)
# this will succeed
# docker run --interactive "${image_name}"
# this will fail
# docker run "${image_name}"
# this will also fail
# docker run --detach "${image_name}"
docker run --interactive --tty --detach "${image_name}"
