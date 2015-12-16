#!/bin/sh

# provision elasticsearch user
adduser elasticsearch sudo
chsh -s /bin/bash elasticsearch
chown -R elasticsearch /usr/share/elasticsearch/
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# set environment
export CLUSTER_NAME=${CLUSTER_NAME:-"elasticsearch"}
export NODE_MASTER=${NODE_MASTER:-true}
export NODE_DATA=${NODE_DATA:-true}
export HTTP_ENABLE=${HTTP_ENABLE:-true}
export MULTICAST=${MULTICAST:-true}

# Kubernetes stuff
export KUBERNETES_NAMESPACE=${KUBERNETES_NAMESPACE:-default}
export SERVICE=${SERVICE:-elasticsearch-discovery}

# allow for memlock
# ulimit -l unlimited

# run
exec su elasticsearch -c "/usr/share/elasticsearch/bin/elasticsearch"
