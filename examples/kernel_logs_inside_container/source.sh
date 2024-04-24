# removing the --cap-add CAP_SYSLOG in the next line will break this example
# shellcheck disable=SC2034
RUN_ARGS="-it --memory=4G --cap-add CAP_SYSLOG"
