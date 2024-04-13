#!/bin/bash -e

# This script logs in to your container registry

# site="docker.io"
site="ghcr.io"

# get user and password
username=$(jq -r ".[\"${site}\"][\"user\"]" ~/.passwords.json)
password=$(jq -r ".[\"${site}\"][\"password\"]" ~/.passwords.json)
# debug
# echo "username is ${username}"
# echo "password is ${password}"
# echo "site is ${site}"

# login
echo "${password}" | docker login --username "${username}" --password-stdin "${site}"
