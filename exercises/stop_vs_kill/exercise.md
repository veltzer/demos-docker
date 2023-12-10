Write a python app which does some cleanup when receiving a SIGTERM signal.
Demostrate the app actually does the cleanup when you use:
	$ docker stop [containerid]
Demonstrate that this does not happen when you use:
	$ docker kill [containerid]

References:
- https://www.baeldung.com/ops/docker-stop-vs-kill
