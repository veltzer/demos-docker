#!/bin/sh
javac HelloWorld.java
docker build -f Dockerfile.folder --tag hello_java:latest .
