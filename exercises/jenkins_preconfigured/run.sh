#!/bin/bash -e
docker rm jenkins_preconfigured || true 
docker run --name jenkins_preconfigured -it -p 8080:8080 jenkins_preconfigured
