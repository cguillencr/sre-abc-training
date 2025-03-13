#!/bin/bash

# Update package list and install dependencies
sudo apt-get update
sudo apt-get install -y \
    curl \
    wget \
    git \
    vim \
    build-essential \
    docker.io \
    kubectl

# Install Podman
. /etc/os-release
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_$VERSION_ID/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
curl -L "https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable/xUbuntu_$VERSION_ID/Release.key" | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install podman

# Install kind (Kubernetes in Docker)
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Install minikube
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/

# Start minikube with Podman
minikube start --driver=podman

# Print versions
echo "Installed versions:"
podman --version
kind --version
minikube version
kubectl version --client
