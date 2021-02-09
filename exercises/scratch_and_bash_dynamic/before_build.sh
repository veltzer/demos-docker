#!/bin/sh
cp /bin/bash .
\rm -rf libs
mkdir libs
cp `ldd /bin/bash | tr -s " " | cut -f 3 -d " " | grep -v "^$"` libs
cp /lib64/ld-linux-x86-64.so.2 .
