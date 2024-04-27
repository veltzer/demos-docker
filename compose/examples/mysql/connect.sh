#!/bin/bash -e
mysql --host="127.0.0.1" --user="${env_db_user}" --password="${env_db_password}" mysql
