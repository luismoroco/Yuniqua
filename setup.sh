#!bin/bash

if [ "$1" != "--mode" ]; then
    echo "Use: $0 --mode <local|cluster>"
    exit 1
fi

mode="$2"

function local_env() {
    docker-compose up --build
}

function cluster_env() {
    kind create cluster --name yuniqua-cluster --config ./deployment/cluster/kind-config.yaml
}

if [ "$mode" == "local" ]; then
    echo "Setup mode: LOCAL"
    local_env
    exit 1
elif [ "$mode" == "cluster" ]; then
    echo "Setup mode: CLUSTER"
    cluster_env
    exit
else
    echo "Use: $0 --mode <local|cluster>"
    exit 1
fi


# Kind


# sudo kind load docker-image flasktest:latest --name yuniqua-cluster

# docker exec -it demo-control-plane crictl images

# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' yuniqua-cluster-control-plane