# Stop vs Kill

Write a python app which does some cleanup when receiving a SIGTERM signal.
Demonstrate the app actually does the cleanup when you use:
    `$ docker stop [containerid]`
Demonstrate that this does not happen when you use:
    `$ docker kill [containerid]`

References:
* [stop-vs-kill](https://www.baeldung.com/ops/docker-stop-vs-kill)

Conclusions:
* `docker stop` sends `SIGTERM` with optional `SIGKILL` after a timeout.
* `docker kill` sends `SIGKILL` or any other signal you choose.
