#!/bin/bash -e
source .env
name=$1
email=$2
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"${name}\",\"email\":\"${email}\"}"\
	"http://${env_app_access}:${env_app_port}/users"
