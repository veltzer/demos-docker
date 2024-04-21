#!/bin/bash -e
name=$1
email=$2
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"${name}\",\"email\":\"${email}\"}" http://localhost:3000/users
