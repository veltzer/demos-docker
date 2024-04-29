#!/bin/bash -e
# shellcheck source=exercises/mysql_reconfigured/.auto.enter.sh
source .env
mysql --host="127.0.0.1" --user="${env_db_user}" "${env_db_name}"
