# shellcheck disable=SC2034
RUN_ARGS="--detach -e MYSQL_ROOT_PASSWORD=${env_db_password} -p 3306:3306 --rm"
