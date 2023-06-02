FROM python:3.9.16

ENV PYTHONUNBUFFERED 1

RUN mkdir /root/workspace
COPY requirements.txt /root/workspace/
WORKDIR /root/workspace

RUN pip install --upgrade pip\
    && pip install --upgrade setuptools\
    && pip install -r requirements.txt
