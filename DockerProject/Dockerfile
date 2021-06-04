# syntax=docker/dockerfile:1
FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3-pip

RUN mkdir app

COPY requirements.txt /app/requirements.txt
COPY python_i2cat.py /app/python_i2cat.py

RUN pip install -r /app/requirements.txt

EXPOSE 6789
ENTRYPOINT ["/app/python_i2cat.py"]
