FROM maven:3.8.7-openjdk-18 AS build
# FROM maven:latest AS build
WORKDIR /app
# Notice the two stages to utilize the cache better assuming pom.xml
# did not change
COPY pom.xml /app
RUN mvn dependency:go-offline
RUN mvn dependency:copy-dependencies -DoutputDirectory=target/dependencies
RUN mvn dependency:resolve-plugins
# Next line does not work
# RUN mvn dependency:resolve-plugin-dependencies

COPY src /app/src
RUN mvn package -DskipTests

FROM openjdk:18-jdk-slim
WORKDIR /app
COPY --from=build /app/target/app-1.0.jar /app/target/dependencies /app
CMD ["java", "-cp", "./*", "com.company.HelloWorld"]
