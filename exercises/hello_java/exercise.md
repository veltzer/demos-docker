
Run a java hello world program inside a docker container.

* first check that docker is already running on your system.
	$ ps -ef | grep container

* If docker is not running on your system install it with:
	$ sudo apt install docker.io

* second, check that you are in the 'docker' group:
	$ groups

* If you are not, then add yourself to the 'docker' group with:
	$ sudo adduser $USER docker
	and relogin for that to take effect

* Write a file called 'Dockerfile' with a FROM statement based
	on some docker image you find in docker hub.

* Write a small java app (hello world like).

* Compile the app

* Put the app inside the docker image using the COPY docker command

* Build you container with:
	$ docker build --tag java_app:latest .

* See you container with:
	$ docker images

$ Run your container with:
	$ docker run -it java_app:latest 
