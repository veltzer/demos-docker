#!/bin/sh
javac HelloWorld.java
docker build --tag hello_java:latest .
