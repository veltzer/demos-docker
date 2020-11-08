#!/bin/sh
image_name=$(basename $PWD)
cp /bin/bash .
cp `ldd /bin/bash | tr -s " " | cut -f 3 -d " " | grep -v "^$"` .
cp /lib64/ld-linux-x86-64.so.2 .
docker build --tag "${image_name}:latest" .
