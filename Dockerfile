FROM ubuntu
RUN apt-get update && apt-get install -y python-pip

FROM python:3.6.5
RUN pip install psutil
COPY metrics.py /metrics.py
ENTRYPOINT ["python", "/metrics.py"]