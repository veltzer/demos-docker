rm -rf data || true
mkdir data
RUN_ARGS="--user \"${UID}:${UID}\" --detach --volume \"${PWD}/data:/data\" --network host"
