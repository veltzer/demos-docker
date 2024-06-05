#!/bin/bash -e

# This script logs in to your container registry

site="docker.io"
# site="ghcr.io"
username="veltzer"

# get password
password=$(pass show "passwords/${site}/${username}")
# debug
# echo "username is ${username}"
# echo "password is ${password}"
# echo "site is ${site}"

# login
echo "${password}" | docker login --username "${username}" --password-stdin "${site}"
