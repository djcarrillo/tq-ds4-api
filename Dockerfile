# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-buster

# 0. Install essential packages
RUN apt-get update --allow-releaseinfo-change
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        freetds-dev \
        freetds-bin

WORKDIR $APP_HOME
COPY . ./

# 5. Install production dependencies.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt