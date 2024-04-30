FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install flask requests
RUN mkdir app
COPY *.py /app
WORKDIR app
CMD ["./app.py"]

HEALTHCHECK --interval=3s --timeout=3s CMD /app/curl.py http://localhost:8080/
