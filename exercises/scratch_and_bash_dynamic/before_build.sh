#!/bin/sh
cp /bin/bash .
\rm -rf libs
mkdir libs
for x in $(ldd /bin/bash | tr -s " " | cut -f 3 -d " " | grep -v "^$")
do
	cp "${x}" libs
done
cp /lib64/ld-linux-x86-64.so.2 .
