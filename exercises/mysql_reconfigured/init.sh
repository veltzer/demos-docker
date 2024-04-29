#!/bin/bash

# Pipe the general log to stdout
exec tail -F /var/log/mysql/general.log &

# Run the command from the parent image
exec "$@"
