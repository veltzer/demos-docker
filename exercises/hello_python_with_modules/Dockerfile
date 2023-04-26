FROM python:3-slim
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN python -m pip install --upgrade pip
RUN pip install pyvardump
COPY app.py /
CMD ["/app.py"]
