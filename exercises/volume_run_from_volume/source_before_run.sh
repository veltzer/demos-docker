# shellcheck disable=SC2034
GID=$(id -g)
RUN_ARGS="-it --user ${UID}:${GID} --volume ${PWD}/data:/data"
