#!/bin/sh
# docker run --network=host -it hello_python_with_flask
# docker run -p 8080:8080 -it hello_python_with_flask
docker run -p 8080:8080 -it hello_python_with_flask
# this DOES NOT work
# docker run -p 8080 -it hello_python_with_flask
