FROM python:3-slim
RUN mkdir /app
COPY app.py /
COPY data.txt /app
RUN chown -R 1200:1200 /app
WORKDIR /app
CMD ["/app.py"]
