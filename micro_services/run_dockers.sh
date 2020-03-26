#!/bin/sh
docker run -d -p 8000:8000 dapp1
docker run -d -p 8001:8001 dapp2
# everything is running, take a look
docker ps
