#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
psql --command "SELECT * from users" --host="${env_db_access}"\
	--username="${env_db_user}" --port="${env_db_port}" "${env_db_name}"
