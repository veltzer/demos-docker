#!/bin/sh
# if [ ! -f gradle-bin.zip ]
# then
# 	wget "https://services.gradle.org/distributions/gradle-6.8.3-bin.zip" -O gradle-bin.zip
# fi
docker build --tag hello_gradle:latest .
