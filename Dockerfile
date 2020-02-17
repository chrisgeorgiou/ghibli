FROM python:3.9-rc
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install Django==3.0.2
RUN pip install djangorestframework==3.11.0
RUN python -m django --version

RUN mkdir /ghibli
WORKDIR /ghibli

COPY requirements.txt /ghibli
RUN pip install -r requirements.txt
COPY . /ghibli
