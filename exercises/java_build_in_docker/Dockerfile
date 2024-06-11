FROM maven:3.8.6-openjdk-18 AS build
WORKDIR /app
COPY . /app
RUN mvn package

FROM openjdk:18-jdk-slim
WORKDIR /app
COPY --from=build /app/target/your-application.jar /app/your-application.jar
ENTRYPOINT ["java", "-jar", "/app/your-application.jar"]
