FROM gcc:14 AS build
WORKDIR /app
COPY hello_world.c ./
RUN gcc -static hello_world.c -o hello_world

FROM scratch
COPY --from=build /app/hello_world /
CMD ["/hello_world"]
