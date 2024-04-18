#!/bin/bash -e

if [[ "$#" -ne 1 ]]
then
	echo "error: you must pass a name of a container to this script..."
	exit 1
fi

name=$(docker inspect "$1" | jq -r ".[0].Mounts[].Name")
docker run --rm -v "${name}:/volume" -v /tmp/backup:/backup alpine tar czf /backup/backup.tar.gz -C /volume .
cp /tmp/backup/backup.tar.gz .
