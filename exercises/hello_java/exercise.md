# Hello Java

* Write a `hello world` app in java
    (you can find many on the internet)
    Call the file HelloWorld.java

* Install a java compiler `javac`.
    Most likely you need the package `openjdk-17-jdk` in order to compile your code
    `$ sudo apt install openjdk-17-jdk`

* Compile your `HelloWorld.java` into `HelloWorld.class`
    using a java compiler

    `$ javac HelloWorld.java`

    a `HelloWorld.class` file will be created.

* Run your app just to see that it is OK.
    run it using:
    `$ java HelloWorld`

* Write a file called `Dockerfile` with a FROM statement based
    on some docker image you find in docker hub which has a java
    runtime environment (JRE). For instance `eclipse-temurin:19-jre-ubi9-minimal`

* Put the class file inside the docker image using the COPY docker command

* Add a docker `CMD` command to run your application.

* Build you container with:
    `$ docker build --tag java_app:latest .`

* See you container with:
    `$ docker images`

$ Run your container with:
    `$ docker run java_app:latest`
