#!/bin/sh
image_name=$(basename "${PWD}")
id=$(docker run --detach --restart on-failure:3 "${image_name}")
echo "id is ${id}"
while true
do
	docker logs --follow "${id}"
done
# convert id to name, because only name remains constant across restarts
# name=$(docker ps --all --filter "id=${id}" --format "{{.Names}}")
# echo "name is ${name}"
# docker logs --follow "${name}"
