#!/bin/bash -e
docker build --tag app_a:latest --file a.dockerfile .
docker build --tag app_b:latest --file b.dockerfile .
