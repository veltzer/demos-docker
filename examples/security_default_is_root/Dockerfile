# FROM bash:latest
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y libcap2-bin systemd-sysv
COPY app.sh /
CMD ["/app.sh"]
