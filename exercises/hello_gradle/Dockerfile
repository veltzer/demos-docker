FROM gradle:latest
RUN mkdir /project
COPY src /project/src
COPY build.gradle /project
WORKDIR /project
CMD gradle build
