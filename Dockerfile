FROM ubuntu:22.04
COPY . /work
WORKDIR /work
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN \
apt-get update &&\
apt-get install -yq sudo python3-full wget gfortran python3-scipy python3-dev python3-pip python-is-python3 subversion

RUN  /bin/bash -c "./install_tts.sh"

WORKDIR /work/vits

EXPOSE 8765

CMD [ "python3 server.py" ]
