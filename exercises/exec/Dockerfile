# FROM python:3-slim
FROM ubuntu:latest
COPY app.py /
RUN apt-get update -y
RUN apt-get install -y python3
CMD ["/app.py"]
