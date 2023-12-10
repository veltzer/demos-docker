# From Flask to Docker to Minikube

## Phase 1
* create a flask application with the following UI:
    upload a file [_______________]V
     where the user can upload a file.
    This page will appear in `http://localhost/upload`
* make the "server" side of the application save the uploaded file to a predefined directory.
* add a page that lists all the files that you currently have in storage
    This page will appear in `http://localhost/list`
    When starting the list, of course, should be empty.

## Phase 2
* Wrap your application as docker image (prepare Dockerfile, build etc...)
* Run your application with a volume (--volume) and make your application write to that
    volume so that after you kill the app the files uploaded are still there.
* Upload some files, kill the docker container and see that the files are still there.
    (in order to demonstrate that your solution is fine...)

## Phase 3
* Install minikube on your linux machine.
    It must be a real linux machine with enough RAM (at least 4 gig but maybe more).
    It must not be a WSL type windows system.
    `https://phoenixnap.com/kb/install-minikube-on-ubuntu`
    `https://minikube.sigs.k8s.io/docs/start`
* Run minikube.
* Create a deployment file for your container (app.yaml) and deploy your newly created app.
    At first do it simply with no stateful storage.
    relicas = 1 in our case (we don't need replicas for this exercise)
* Second stage: add stateful storage to the k8s installation.
