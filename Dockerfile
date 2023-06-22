FROM ubuntu:22.04
COPY . /work
WORKDIR /work
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list &&\
sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list &&\
apt-get update &&\
apt-get install -yq sudo python3-full gfortran python3-scipy python3-dev python3-pip python-is-python3 subversion&&\
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN  /bin/bash -c "./install_tts.sh"

WORKDIR /work/vits

EXPOSE 8765

CMD [ "python server.py" ]
