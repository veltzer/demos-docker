#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
curl -I "http://${env_app_access}:${env_app_port}/users"
curl -I "http://${env_postgrest_access}:${env_postgrest_port}/users"
