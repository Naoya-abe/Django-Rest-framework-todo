
FROM python:3.7-alpine

LABEL architecture="Naoya Abe"

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /restframework-todo

WORKDIR /restframework-todo

COPY ./restframework-todo /restframework-todo

RUN adduser -D user

USER user