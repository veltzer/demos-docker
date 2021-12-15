#!/bin/bash -e
docker run --detach --network=host app1
docker run --detach --network=host app2
