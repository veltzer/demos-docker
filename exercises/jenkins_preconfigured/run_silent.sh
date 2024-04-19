#!/bin/bash -e
docker rm jenkins_preconfigured || true 
docker run --name jenkins_preconfigured -p 8080:8080 --detach jenkins_preconfigured
