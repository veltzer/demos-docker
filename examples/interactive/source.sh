# shellcheck disable=SC2034
RUN_ARGS="--interactive"
# this will fail:
# RUN_ARGS=""
# these will also fail:
# RUN_ARGS="--detach"
# RUN_ARGS="--interactive --tty --detach"
