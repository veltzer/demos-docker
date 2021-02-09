FROM ubuntu:latest
RUN apt-get -qy update
RUN apt-get -qy dist-upgrade
RUN apt-get install -qy python3
COPY app.py /app.py
CMD ["/app.py"]
