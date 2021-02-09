FROM python:3-slim
COPY app.py /
RUN mkdir /user
COPY data.txt /user
RUN chown -R 1000:1000 /user
WORKDIR /user
USER 1000
CMD ["/app.py"]
