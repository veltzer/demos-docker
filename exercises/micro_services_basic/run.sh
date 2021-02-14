#!/bin/bash -e
docker run -d -p 8000:8000 app ./app.py 8000
docker run -d -p 8001:8001 app ./app.py 8001
