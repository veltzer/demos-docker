FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install requests
RUN mkdir app
COPY app.py /app
WORKDIR app
CMD ["./app.py"]
