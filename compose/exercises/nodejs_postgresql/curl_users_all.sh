#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
curl "http://${env_app_access}:${env_app_port}/users"
