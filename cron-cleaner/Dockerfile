FROM alpine:3.2

RUN apk --update add python py-pip && \
    pip install elasticsearch-curator==3.4.0 schedule && \
    apk del py-pip && \
    rm -rf /var/cache/apk/*

ADD cron.py /

CMD ["python", "cron.py"]
