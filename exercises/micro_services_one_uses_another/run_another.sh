#!/bin/bash -e

# THIS SOLUTION DOES NOT WORK

# In this version of the run script we do not use "--network host"
# which is a security hazard. We will try another configuration which is safer...
docker network create mynetwork
docker run -d --network mynetwork --hostname adder -p 8081:8081 app1
docker run -d -p 8080:8080 --network mynetwork app2
