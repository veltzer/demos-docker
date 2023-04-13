#!/bin/bash -e
docker kill app_a app_b || true
docker rm app_a app_b || true
