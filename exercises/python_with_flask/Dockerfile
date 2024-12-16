FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install flask
RUN mkdir app
WORKDIR app
COPY app.py .
CMD ["./app.py"]
