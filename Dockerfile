FROM elasticsearch:2.1.0

MAINTAINER tupachydralisk@gmail.com

# install plugins
RUN plugin install io.fabric8/elasticsearch-cloud-kubernetes/2.1.0 --verbose

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Copy run script
COPY run.sh /

CMD ["./run.sh"]
