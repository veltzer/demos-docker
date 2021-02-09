#!/bin/sh
docker run -d --network=host app1
docker run -d --network=host app2
