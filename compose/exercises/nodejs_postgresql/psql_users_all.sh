#!/bin/bash -e
DB_HOST="localhost"
DB_USER="postgres"
DB_PORT="5432"
DB_NAME="postgres"
psql --command "SELECT * from users" --host="${DB_HOST}" --username="${DB_USER}" --port="${DB_PORT}" "${DB_NAME}"
