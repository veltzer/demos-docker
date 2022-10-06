#!/bin/bash -e
docker build --tag app_a:latest --file Dockerfile.a .
docker build --tag app_b:latest --file Dockerfile.b .
