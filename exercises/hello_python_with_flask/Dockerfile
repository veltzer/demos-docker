FROM python:3-alpine
RUN pip install flask
RUN mkdir app
COPY app.py /app
WORKDIR app
CMD ["./app.py"]
