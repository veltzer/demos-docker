# Logs

* create a docker python app with a loop that prints something like:
    =======8<========
    hello output 1
    hello error 1
    hello output 2
    hello error 2
    hello output 3
    hello error 3
    =======8<========
    to standard output and standard error respectively.
    Just use the python 'print' function and the 'file' parameter to it.
* run your application with the -d/--detach flag
    This means that you will NOT be able to see the output of your
    application on the command line.
* look at the logs of your application while it is running using the
    `docker logs` command
    Notice that you cannot see the outputs.
    But you can see the errors.
    Strange right?
    That's OK. Lets continue.
* kill your container with the command:
    $ docker kill [docker container name]
* see that your application is listed as dead using the command:
    $ docker ps -a
* show the logs of your dead application using the `docker logs` command
    Now can you see the output logs?
* add:
    import sys
  and
    sys.stdout.flush()
  between prints
* now can you see the output logs while the container is running?
* what about if you run the container with the "-it" flags?
* Answer the following questions:
    How can you see only outputs?
    How can you see only errors?
    How can you redirect only outputs to a file? (don't mind what is on the console)
    How can you redirect only errors to a file? (don't mind what is on the console)
    How can you redirect both outputs and errors to a file?
    How can you pipe both outputs and errors to another program? (say "wc -l")
