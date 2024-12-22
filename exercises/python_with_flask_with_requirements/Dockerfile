FROM python:3-alpine

# upgrade pip to latest version and configure it to shut up
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip

# install requirement
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

# install your app
RUN mkdir /app
COPY app.py /app
WORKDIR /app
CMD ["./app.py"]
