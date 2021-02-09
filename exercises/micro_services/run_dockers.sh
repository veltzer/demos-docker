#!/bin/sh
docker run -d -p 8000:8000 app1
docker run -d -p 8001:8001 app2
# everything is running, take a look
docker ps
