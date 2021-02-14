#!/bin/bash -e

# In this version of the run script we do not use "--network host"
# which is a security hazard. We will try another configuration which is safer...
docker run -d --name app1 app1
APP1_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' app1)
echo $APP1_IP
docker run -d --name app2 -p 8080:8080 --link app1:app1 app2 ./app2.py $APP1_IP
