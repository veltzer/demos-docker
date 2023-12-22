# Hello Python

* Create a docker container which prints out messages in a loop.
* Use python as the language.
* Remember to write a "Dockerfile" to describe how to build your image.
* Remember to base your image on a python image from docker hub
    You can use any of the following already prepared python images:
    python:3-latest -> latest python with of the pythons features
        cons: too fat (around 1 gig)
    python:3-slim -> more slim version version of python
    python:3-alpine -> the slimmest version of python (around 50 megs)
    in the docker file the first line selects the image that you build on:
    FROM [image_name]
* Remember to put your application inside the image using the docker "COPY" command.
* Remember to change what the docker image runs using the "CMD" command.
* Remember to build your image using:
    `$ docker build --tag "[your_image_name]:[your_image_version]" .`
    "latest" is the default version if you do not supply any
* Run your image using:
    `$ docker run -it "[your_image_name]:[your_image_version]"`
    "latest" is the default version if you do not supply any
