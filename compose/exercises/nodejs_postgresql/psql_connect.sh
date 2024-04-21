#!/bin/bash -e
source .env
psql --host="${env_db_host}" --username="${env_db_user}" --port="${env_db_port}" "${env_db_name}"
