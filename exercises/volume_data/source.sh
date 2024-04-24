UID=$(id -u)
GID=$(id -g)
RUN_ARGS="--detach --user "${UID}:${GID}" --volume \"${PWD}/data:/data\""
