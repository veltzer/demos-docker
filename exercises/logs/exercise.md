- create a docker python app with a loop that prints something like:
	=======<8========
	hello 1
	hello 2
	hello 3
	=======<8========
	to standard output.
	Just use the python 'print' function
- run your applicaton with the -d/--detach flag
	This means that you will NOT be able to see the output of your
	application.
- look at the logs of your application while it is running using the
	`docker logs` command
	You don't see anything? That's ok.
- kill your container with the command:
	$ docker kill [docker container name]
- see that your applciation is listed as dead using the:
	$ docker ps -a
	command
- show the logs of your dead application using the `docker logs` command
	Now can you see the logs?
- add:
	import sys
  and
	sys.stdout.flush()
  between prints
- now can you see the logs while the container is running?
- what about if you run the container with the "-it" flags?
