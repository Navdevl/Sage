FROM ubuntu:latest
MAINTAINER naveen "naveen@skcript.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# RUN pip3 install sqlite3
RUN pip3 install discord

CMD 'mkdir -p /var/www/discord'
ADD . /var/www/discord

WORKDIR '/var/www/discord'
RUN pwd

CMD [ "python", "-u", "./main.py" ]



