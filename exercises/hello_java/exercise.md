* first phase: write a "hello world" app in java
	(you can find many on the internet)
	Call the file HelloWorld.java

* second phase: compile your HelloWorld.java into HelloWorld.class
	using a java compiler
	(you need to install one, it is called javac)

* third phase: run your app just to see that it is ok.
	run it using:
	java -classpath . HelloWorld

* Write a file called 'Dockerfile' with a FROM statement based
	on some docker image you find in docker hub which has a java
	virtual machine.

* Put the class file inside the docker image using the COPY docker command

* Add a docker "CMD" command to run your application.

* Build you container with:
	$ docker build --tag java_app:latest .

* See you container with:
	$ docker images

$ Run your container with:
	$ docker run -it java_app:latest 
