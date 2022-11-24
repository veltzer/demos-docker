#!/bin/bash -e
docker run --detach --network=host app_a
docker run --detach --network=host app_b
