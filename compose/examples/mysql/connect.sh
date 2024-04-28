#!/bin/bash -e
# shellcheck source=compose/examples/mysql/.auto.enter.sh
source ".auto.enter.sh"
mysql --host="127.0.0.1" --user="${env_db_user}" --password="${env_db_password}" mysql
