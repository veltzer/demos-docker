#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
xdg-open "http://${env_postgrest_access}:${env_postgrest_port}"
