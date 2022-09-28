- create a docker python app with a loop that prints something like:
	hello 1
	hello 2
	hello 3
- run your applicaton with the -d/--detach flag
	This means that you will NOT be able to see the output of your
	application.
- look at the logs of your application while it is running using the
	`docker logs` command
- kill your container with the command:
	$ docker kill [docker container name]
- see that your applciation is listed as dead using the:
	$ docker ps -a
	command
- show the logs of your dead application using the `docker logs` command
