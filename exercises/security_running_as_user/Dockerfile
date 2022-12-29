FROM bash:latest
# This is the simple example
# CMD ["/usr/bin/id"]
# This is the complex example
RUN mkdir /home/foo
COPY app.sh /home/foo
RUN chown -R 2020:2020 /home/foo
WORKDIR /home/foo
USER 2020:2020
CMD ["./app.sh"]
# CMD ["/home/foo/app.sh"]
