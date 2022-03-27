#!/bin/sh
javac HelloWorld.java
image_name=$(basename $PWD)
docker build --tag "${image_name}:latest" .
