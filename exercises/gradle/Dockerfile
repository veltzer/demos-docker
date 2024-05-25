FROM gradle
# RUN mkdir /project
COPY src /project/src
COPY build.gradle /project
WORKDIR /project
CMD ["gradle", "build"]
