#!/bin/sh
# docker run --network=host -it hello_python_and_flask
# docker run -p 8080:8080 -it hello_python_and_flask
docker run -p 8080:8080 -d hello_python_and_flask
# this DOES NOT work
# docker run -p 8080 -it hello_python_and_flask
