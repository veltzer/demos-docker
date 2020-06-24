#!/bin/sh
docker build --tag hello_docker:latest --file Dockerfile .
# everything is built, take a look
docker images
