FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY test/*.csproj .
RUN dotnet restore -r linux-musl-x64

# copy and publish app and libraries
COPY test/ .
RUN dotnet publish -c release -o /app -r linux-musl-x64 --no-restore /p:PublishTrimmed=true /p:TrimMode=Link

# final stage/image
FROM mcr.microsoft.com/dotnet/runtime-deps:8.0-alpine
WORKDIR /app
COPY --from=build /app .

ENTRYPOINT ["./test"]

EXPOSE 8080
