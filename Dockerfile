FROM python:3.9.2-slim-buster
FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

RUN mkdir /app
RUN chmod 777 /app
WORKDIR /app

RUN apt -qq update
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata
RUN apt update && apt upgrade -y && apt install --no-install-recommends -y \
        debian-keyring \
        debian-archive-keyring \
        bash \
        curl \
        git \
        util-linux \
        libffi-dev \
        libjpeg-dev \
        liblzma-dev\
        libjpeg62-turbo-dev \
        libwebp-dev \
        linux-headers-amd64 \
        musl-dev \
        musl \
        neofetch \
        python3-lxml \
        postgresql \
        postgresql-client \
        libpq-dev \
        libcurl4-openssl-dev \
        libxml2-dev \
        libxslt1-dev \
        openssl \
        pv \
        jq \
        wget \
        python3-dev \
        libreadline-dev \
        libyaml-dev \
        zlib1g \
        ffmpeg \
        libssl-dev \
        libgconf-2-4 \
        libxi6 \
        zlib1g-dev \
        xvfb \
        unzip \
        make \
        libopus0 \
        libopus-dev \
        gcc
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i ./google-chrome-stable_current_amd64.deb; apt -fqqy install && \
    rm ./google-chrome-stable_current_amd64.deb
RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
    unzip chromedriver.zip chromedriver -d /usr/bin/ && \
    rm chromedriver.zip
COPY omk.py .
COPY Zsetup.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r Zsetup.txt
Aur ye jo omk.py hai 
Iska jagha directly path de do System ka

CMD["python3", "System"]
