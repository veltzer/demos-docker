FROM python:3-slim
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY phase3_alone.py /phase3.py
CMD ["python3", "/phase3.py"]
