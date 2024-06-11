FROM maven:3.8.6-openjdk-18 AS build
WORKDIR /app
COPY pom.xml src /app
RUN mvn package

FROM openjdk:18-jdk-slim
WORKDIR /app
COPY --from=build /app/target/app-1.0.jar /app/app-1.0.jar
ENTRYPOINT ["java", "-jar", "/app/app-1.0.jar"]
