#!/bin/bash -e

if systemctl is-active --quiet docker.service
then
	status="1"
else
	status="0"
fi
echo "${status}"
