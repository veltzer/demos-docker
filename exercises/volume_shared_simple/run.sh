#!/bin/sh
UID=$(id -u)
GID=$(id -g)
image_name=$(basename $PWD)
if [ ! -d "data" ]
then
	mkdir data
fi
docker run --detach --user "${UID}:${GID}" --volume "${PWD}/data:/data" "${image_name}" /writer.py /data/file1.txt
docker run --detach --user "${UID}:${GID}" --volume "${PWD}/data:/data" "${image_name}" /writer.py /data/file2.txt
# docker run --detach --volume "${PWD}/data:/data" "${image_name}" /writer.py /data/file1.txt
# docker run --detach --volume "${PWD}/data:/data" "${image_name}" /writer.py /data/file2.txt
