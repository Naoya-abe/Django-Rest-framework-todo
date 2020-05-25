
FROM python:3.7-alpine

LABEL architecture="Naoya Abe"

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /todo-api

WORKDIR /todo-api

COPY ./todo-api /todo-api

RUN adduser -D user

USER user