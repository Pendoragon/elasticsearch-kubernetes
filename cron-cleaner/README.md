# Cron cleaner

This is a rather simple cron job like cleaner for elasticsearch on k8s cluster. Since elasticsearch does not
shrink data for you as it grows (or I just didn't find it). There IS a way to do this which requires ttl to be
set for indices and it adds more workload to elasticsearch (so I've heard).

Basically what this container does is, it runs in the same pod as ES. It has a small python script which acts
like a cron job and uses [curator](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/index.html) to manage indices.
