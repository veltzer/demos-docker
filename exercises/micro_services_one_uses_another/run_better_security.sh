#!/bin/bash -e

# In this version of the run script we do not use "--network host"
# which is a security hazard. We will try another configuration which is safer...
docker run -d --name app_b app_b
APP_B_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' app_b)
docker run -d --name app_a -p 8080:8080 --link app_b:app_b app_a ./app_a.py "$APP_B_IP"
