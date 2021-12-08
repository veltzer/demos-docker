* Write a file called 'Dockerfile' with a FROM statement based
	on some docker image you find in docker hub which has a java
	virtual machine.

* Write a small java app (hello world like).

* Compile the app and get a .class file

* Put the app inside the docker image using the COPY docker command

* Add a docker "CMD" command to run your application.

* Build you container with:
	$ docker build --tag java_app:latest .

* See you container with:
	$ docker images

$ Run your container with:
	$ docker run -it java_app:latest 
