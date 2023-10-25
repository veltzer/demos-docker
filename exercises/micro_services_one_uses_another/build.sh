#!/bin/bash -e
docker buildx build --tag app_a --file a.dockerfile .
docker buildx build --tag app_b --file b.dockerfile .
