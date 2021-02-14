#!/bin/bash -e

# THIS SOLUTION DOES NOT WORK

# In this version of the run script we do not use "--network host"
# which is a security hazard. We will try another configuration which is safer...
id=$(docker run -d app1)
docker run -d -p 8080:8080 --link $id app2
