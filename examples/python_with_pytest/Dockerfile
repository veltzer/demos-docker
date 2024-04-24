FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install pytest
RUN mkdir myapp
COPY module /myapp/module
COPY tests /myapp/tests
WORKDIR myapp
CMD ["PYTHONPATH=.","python","-m","pytest"]
