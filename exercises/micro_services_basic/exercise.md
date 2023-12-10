# Micro Services Basic

Create two dockers that together work to create a full application.

both of the dockers listen to web requests.
Docker1 prodcues a page with a link to a page by docker2.
Docker2 produces a page with a link to a page by docker1.

The idea is that every single docker is a "micro service"

* remember that in order to bring both containers up, you must
differnetiate from each other by the port they listen to.

* bonus: do the exercise with just one docker image. hint: check out the -E flag to docker run or checkout command line parameters to docker containers.
