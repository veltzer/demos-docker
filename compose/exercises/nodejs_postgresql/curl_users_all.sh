#!/bin/bash -e
source .env
curl "http://${env_app_access}:${env_app_port}/users"
