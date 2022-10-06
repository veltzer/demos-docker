FROM python:3-alpine
RUN pip install flask
COPY app_b.py /
CMD ["app_b.py"]
