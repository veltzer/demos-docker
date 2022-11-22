FROM python:3-alpine
RUN pip install flask
RUN mkdir /app
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["./app.py"]
