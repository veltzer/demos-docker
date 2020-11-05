#!/bin/sh
docker run --detach hello_bash
docker run -it hello_bash
# everything is running, take a look
docker ps
