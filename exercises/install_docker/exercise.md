# Install Docker

Install docker in Ubuntu:
* You need to have an ubuntu virtual machine.
* Install the following packages:
    `docker.io`
    `containerd`
    `docker-buildx`
    with:
    `$ sudo apt install docker.io containerd docker-buildx`
* After the installation you can see them running with:
    `$ ps -ef | grep dockerd`
    `$ ps -ef | grep containerd`

Adding yourself to the docker group:
* Check if you are in the docker group using the command:
    `$ groups`
* If you are in the docker group go to the next phase of the exercise
* If you are not in the docker group then:
    * add yourself to the docker group using the command:
        `$ sudo /usr/sbin/adduser [your_user_name] docker`
    * logout and re-login (in windows virtualization you may need to restart the vm guest)
    * after re-login or re-start run:
        `$ groups`
    and check that now you are in the "docker" group.

Lets run some containers...
Make sure you don't have anything listening on port 80:
    `$ netstat -lp | grep http`
    `$ docker run --network host nginx`
and now check that you can talk to the nginx that you just installed by pointing
you browser to:
    localhost:80

* if you dont have `netstat` then install the `net-tools` package.