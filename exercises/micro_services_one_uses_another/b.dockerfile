FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install flask
COPY app_b.py /
CMD ["/app_b.py"]
