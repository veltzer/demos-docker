# Post Mortem

* create a docker image with python and an app inside it.
* the app should be a loop writing to a file with a delay.
* let the app run for several cycles and kill (CTRL+C)

## post mortem methods
* show that your container is listed in the deceased list:
    `$ docker container ps -a`
    or
    `$ docker ps -a`
* show how to extract the file written by the python app from the
    corpse of the deceased container.
    hint: use `docker cp`
* extract all the files from your container using the `docker export`
    command.

## Advanced
* create a new image from your deceased container using the `docker commit`
    command and explore it with `docker run` and bash.
