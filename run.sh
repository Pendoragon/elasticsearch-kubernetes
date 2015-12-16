#!/bin/sh

# provision elasticsearch user
addgroup sudo
adduser -D -g '' elasticsearch
adduser elasticsearch sudo
chown -R elasticsearch /elasticsearch /data
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
sudo -E -u elasticsearch elasticsearch
