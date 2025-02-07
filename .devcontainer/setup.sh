#!/bin/bash

echo "Setting up the environment..."

# Ensure Minikube is configured correctly
minikube start --driver=docker

# Verify installation
kubectl version --client
helm version
docker --version

echo "Environment setup complete!"
