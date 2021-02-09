FROM ubuntu:latest
RUN apt-get -yq update
RUN apt-get -yq dist-upgrade
COPY app.sh /
# now install anything you want
# RUN apt-get install -yq [package]
CMD ["/app.sh"]

