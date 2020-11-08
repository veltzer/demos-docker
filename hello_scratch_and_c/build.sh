#!/bin/sh
gcc main.c -static -o main
docker build --tag hello_scratch_and_c:latest --file Dockerfile .
