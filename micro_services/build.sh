#!/bin/sh
docker build --tag dapp1:latest --file Dockerfile1 .
docker build --tag dapp2:latest --file Dockerfile2 .
# everything is build, take a loot
docker images
