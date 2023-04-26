FROM python:3-slim
COPY requirements.txt /
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY phase3_alone.py /phase3.py
CMD ["python3", "/phase3.py"]
