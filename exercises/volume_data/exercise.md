# Volume Data

* Add a small python container that runs in a loop and writes some data to the data folder.
* Use data volumes to make sure that the application writes to a data volume which are
    simply folders on the host operating system.
    (data volumes are achieved using the --volume command line argument to "docker run")
* Run the docker container for 20 seconds.
* Kill the container.
* Check the data volume to see that you have data from 20 seconds of operation.
