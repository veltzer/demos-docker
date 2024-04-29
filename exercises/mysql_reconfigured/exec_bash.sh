#!/bin/bash -e
image_name=$(basename "${PWD}")
docker exec -it mysql_reconfigured /bin/bash
