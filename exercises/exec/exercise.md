# Exec

Create a python image with your own app that runs forever.
Use "docker exec" to enter the container AT RUNTIME and investigate.

Use python:3-slim as your base image, as it already has bash and some
command line utilities.

Advanced:
Repeat the exercise with python:3-alpine which is a slimmer docker image with python.
In this case you will not have debugging (bash, ls, ...) in the container and you
will have to add them yourself.

try injecting static packages into your container like:
    `bash-static` `busybox-static`
