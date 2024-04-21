#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
xdg-open "http://${env_app_access}:${env_app_port}"
