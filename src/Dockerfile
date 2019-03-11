FROM python:3-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt
