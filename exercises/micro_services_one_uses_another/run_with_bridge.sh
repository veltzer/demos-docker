#!/bin/bash -e

# In this example we will create a bridge, then run both container a and container b
# and then connect them to the bridge so they could communicate
# we still need to call app_b "app_b" so that app_a will be able to find it.
docker network rm br1 || true
docker network create --driver=bridge br1
docker run --detach -p 8080:8080 --network br1 app_a
docker run --name app_b --detach --network br1 app_b
