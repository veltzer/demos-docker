#!/bin/sh
gcc main.c -static -o main
docker build --tag hello_scratch_bash:latest --file Dockerfile .
