#!/bin/bash -e
DB_HOST="localhost"
DB_USER="postgres"
DB_PORT="5432"
DB_NAME="postgres"
psql --host="${DB_HOST}" --username="${DB_USER}" --port="${DB_PORT}" "${DB_NAME}"
