#!/bin/bash -e
docker build --tag app_a --file a.dockerfile .
docker build --tag app_b --file b.dockerfile .
