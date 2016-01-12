FROM python:2.7-slim

ADD elastic.gpg /

RUN apt-key add elastic.gpg
RUN touch /etc/apt/sources.list.d/curator.list && \
    echo "deb http://packages.elastic.co/curator/3/debian stable main" > /etc/apt/sources.list.d/curator.list

RUN apt-get update && apt-get install -y python-elasticsearch-curator
