#!/bin/bash -e

# In this example we will create a bridge, then run both container a and container b
# and then connect them to the bridge so they could communicate
docker network rm br1
docker network create --driver=bridge br1
docker run --name app_a --detach -p 8080:8080 --network br1 app_a
docker run --name app_b --detach --network br1 app_b
