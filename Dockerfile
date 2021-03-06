#Scheduler & Downloader
FROM python:3.9-slim-buster as etl

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN apt-get update -y && \
    apt-get install -y gcc g++ &&\
    pip install -U --no-cache-dir pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install https://github.com/mher/flower/zipball/master#egg=flower && \
    apt-get autoremove -y

EXPOSE 8080 18081


