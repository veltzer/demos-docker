FROM python:3-alpine
# the next 4 commands are to enable the app to write
# to the disk at /app
RUN mkdir /app
RUN chown 1200:1200 /app
COPY app.py /
WORKDIR /app
USER 1200
# this will not work because there is no /etc/passwd inside the container
# which defines what "mark" means
# USER mark
CMD ["/app.py"]
