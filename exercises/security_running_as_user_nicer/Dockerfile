FROM ubuntu:latest
RUN useradd mark
RUN mkdir /home/mark
COPY app.sh /home/mark
RUN chown -R mark:mark /home/mark
USER mark
WORKDIR /home/mark
CMD ["./app.sh"]
