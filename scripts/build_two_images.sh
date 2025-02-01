#!/bin/bash -e
docker buildx build --load --tag app_a --file a.dockerfile .
docker buildx build --load --tag app_b --file b.dockerfile .
