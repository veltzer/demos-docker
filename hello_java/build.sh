#!/bin/sh
docker build --tag hello_java:latest --file Dockerfile .
# everything is built, take a look
docker images
