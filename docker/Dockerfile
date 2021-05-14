# Pull base image.
FROM ubuntu:18.04

# Install
RUN \
  apt-get -y update  && \
  apt-get -y upgrade && \
  apt-get install -y python3-pip python3-dev locales git vim sudo

COPY requirements.txt /tmp/requirements.txt
COPY entrypoint.sh /tmp/entrypoint.sh

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

