FROM python:3.11.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade setuptools

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .