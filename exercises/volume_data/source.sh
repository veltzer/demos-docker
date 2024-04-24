UID=$(id -u)
GID=$(id -g)
# shellcheck disable=SC2034
RUN_ARGS="--detach --user "${UID}:${GID}" --volume \"${PWD}/data:/data\""
