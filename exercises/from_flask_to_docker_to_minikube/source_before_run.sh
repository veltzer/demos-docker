rm -rf data || true
mkdir data
# shellcheck disable=SC2034
RUN_ARGS="--user \"${UID}:${UID}\" --detach --volume \"${PWD}/data:/data\" --network host"
