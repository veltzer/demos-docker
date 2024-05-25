# test

This project is based on [GenHTTP](https://github.com/Kaliumhexacyanoferrat/GenHTTP)

## Development

To build this project from source, checkout this repository and execute
the following commands in your terminal. This requires the
[.NET SDK](https://dotnet.microsoft.com/download) to be installed.

```bash
cd test
dotnet run
```

This will make the website available at [link](http://localhost:8080/).

## Deployment

To run this project with [Docker](https://www.docker.com/), run the
following commands in your terminal (and adjust the first line
depending on your platform).

```bash
docker build -f Dockerfile.linux-x64 -t test .

docker run -p 8080:8080 test
```

## About

This project uses the [GenHTTP webserver](https://genhttp.org/) to
implement it's functionality.
