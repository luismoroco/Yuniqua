#!bin/bash

if [ "$1" != "--mode" ]; then
    echo "Use: $0 --mode <local|cluster>"
    exit 1
fi

mode="$2"

function build_images() {
    docker rmi yuniqua-server:latest
    docker rmi yuniqua-db:latest

    docker build -t yuniqua-server:latest ./server/
    docker build -t yuniqua-db:latest ./server/database/
}

function load_images() {
    kind load docker-image yuniqua-server:latest --name yuniqua-cluster
    kind load docker-image yuniqua-db:latest --name yuniqua-cluster
}

function local_env() {
    docker-compose up --build
}

function cluster_env() {
    kind create cluster --name yuniqua-cluster --config ./deployment/cluster/kind-config.yaml
    build_images
    load_images
}

if [ "$mode" == "local" ]; then
    echo "Setup mode: LOCAL"
    local_env
    exit 1
elif [ "$mode" == "cluster" ]; then
    echo "Setup mode: CLUSTER"
    cluster_env
    docker exec -it yuniqua-cluster-control-plane  crictl images
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' yuniqua-cluster-control-plane
    exit
else
    echo "Use: $0 --mode <local|cluster>"
    exit 1
fi
