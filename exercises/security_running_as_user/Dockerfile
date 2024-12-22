FROM bash
# This is the simple example
# CMD ["/usr/bin/id"]
# This is the complex example
RUN mkdir /myapp
COPY app.sh /myapp
RUN chown -R 2020:2020 /myapp
WORKDIR /myapp
USER 2020:2020
CMD ["./app.sh"]
# CMD ["/myapp/app.sh"]
