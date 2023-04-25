#!/bin/bash -e
# this is with docker
docker run --detach --publish 8000:8000 micro_services_basic ./app.py 8000 8001 app1 app2
docker run --detach --publish 8001:8001 micro_services_basic ./app.py 8001 8000 app2 app1
# this will run both apps without docker directly on my linux box
# ./app.py 8000 8001 app1 app2
# ./app.py 8001 8000 app2 app1
