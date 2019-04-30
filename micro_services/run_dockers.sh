#!/bin/sh
docker run -d --expose=8000 -p 8000:8000 dapp1
docker run -d --expose=8001 -p 8001:8001 dapp2
# everything is running, take a look
#docker ps
