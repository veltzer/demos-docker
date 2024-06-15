FROM gradle:8.5-jdk17 AS build
WORKDIR /app
COPY build.gradle settings.gradle ./
COPY src ./src
RUN gradle uberJar --no-daemon
FROM openjdk:17-slim
WORKDIR /app
COPY --from=build /app/build/libs/*-uber.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
