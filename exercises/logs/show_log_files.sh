#!/bin/sh

# shows logs files for all running containers...
for x in $(docker ps --no-trunc -q)
do
	sudo ls -l "/var/lib/docker/containers/${x}/${x}-json.log"
	docker logs "$x"
done
