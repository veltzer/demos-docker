#!/bin/sh
docker build --tag data_volume:latest --file Dockerfile .
# everything is built, take a look
docker images
