#!/bin/bash -eu
# docker volume rm shared_volume
docker volume prune -f
docker volume create shared_volume
