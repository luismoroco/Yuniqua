#!bin/bash 


# sudo kind load docker-image flasktest:latest --name yuniqua-cluster

# docker exec -it demo-control-plane crictl images

# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' yuniqua-cluster-control-plane