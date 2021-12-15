#!/bin/sh
gcc main.c -o main
cp -L /lib/x86_64-linux-gnu/libc.so.6 .
cp -L /lib64/ld-linux-x86-64.so.2 .
