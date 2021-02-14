#!/bin/bash -e
docker build --tag app1:latest --file Dockerfile1 .
docker build --tag app2:latest --file Dockerfile2 .
