# syntax=docker/dockerfile:1
FROM python:3.7-alpine
ADD . /app
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 6789
ENTRYPOINT python_i2cat.py 
