# Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Tip for Infrastructure as Code (IaC) with Ansible](#tip-for-infrastructure-as-code-iac-with-ansible)
- [Final Objective](#final-objective)

## Overview

Prometheus is an open-source systems monitoring and alerting toolkit. Initially developed at SoundCloud, Prometheus has since become a part of the Cloud Native Computing Foundation and is widely adopted for monitoring and managing cloud-native applications.

## Key Features

- **Time Series Data Storage**: Prometheus stores all data as time series, which are identified by a metric name and key-value pairs.
- **Multi-dimensional Data Model**: It allows flexible querying of metrics by these key-value pairs.
- **Powerful Query Language**: Prometheus uses its own query language, PromQL, designed for efficient and flexible data retrieval.
- **Service Discovery**: Prometheus dynamically discovers targets to monitor through service discovery or static configurations.
- **Alerting**: Integrated alerting capabilities with the ability to define complex alert rules and notifications.
- **Pull-based Monitoring**: Prometheus scrapes targets at regular intervals, pulling the metric data instead of pushing it from the source.
- **Visualization**: Prometheus includes basic built-in visualization and integrates with other tools like Grafana for advanced dashboards.

## Architecture

Prometheus consists of multiple components that work together to monitor systems:

- **Prometheus Server**: The core component that scrapes and stores time series data.
- **Exporters**: Tools to expose metrics from applications or system components to Prometheus.
- **Alertmanager**: Manages alerts generated by Prometheus and handles routing, silencing, and grouping.
- **Pushgateway**: Used for short-lived jobs to push metrics to Prometheus.
- **Client Libraries**: Instrumentation libraries in various languages (Go, Java, Python, etc.) for custom application metrics.

## Use Cases

- **Infrastructure Monitoring**: Track system-level metrics such as CPU, memory usage, and disk I/O.
- **Application Performance Monitoring**: Monitor application health, response times, and custom business metrics.
- **Alerting**: Create alerts for system failures, performance bottlenecks, or any other conditions based on defined thresholds.
- **Microservices Monitoring**: Prometheus is particularly suited for monitoring cloud-native, microservices-based architectures.

## Installation
This would be the traditional way of installing Prometheus.

1. Download the latest version from [Prometheus Releases](https://prometheus.io/download/).
2. Unpack the tarball and run the Prometheus binary.
3. Configure the `prometheus.yml` file with the list of targets to monitor.
4. Start Prometheus.

./prometheus --config.file=prometheus.yml

But this is the way to install it within the minickube cluster. First let create a yaml file with the steps above:

- **Namespace Creation**:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: monitoring #A separate namespace will be created within the cluster to install all the monitoring tools
```

- **Configurations of the Prometheus**:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config #The name of the ConfigMap. Here, it is prometheus-config.
  namespace: monitoring # Specifies the namespace where the ConfigMap is located. It is set to monitoring.
  labels:
    app: prometheus #Provides metadata for organizing and selecting the ConfigMap. Here, it labels the ConfigMap with app: prometheus.
data:
  prometheus.yml: | #Contains the Prometheus configuration. It sets a global scrape interval of 15 seconds and defines a scrape job for Prometheus itself.
    global:
      scrape_interval: 15s

    scrape_configs:
      - job_name: 'prometheus'
        static_configs:
          - targets: ['localhost:9090']
```

- **Prometheus installation**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus-deployment
  namespace: monitoring
  labels:
    app: prometheus
spec:
  replicas: 1 #Specifies the number of replica Pods. Here, it is set to 1.
  selector:
    matchLabels:
      app: prometheus #Defines a label selector to identify the Pods managed by this Deployment. Here, it matches Pods with the label app: prometheus.
  template:
    metadata:
      labels:
        app: prometheus # Labels applied to Pods created by the Deployment. Here, it is labeled with app: prometheus.
    spec:
      containers:
        - name: prometheus #The name of the container. Here, it is prometheus.
          image: prom/prometheus:latest #The Docker image to use for the container. Here, it is prom/prometheus:latest.
          args:
            - "--config.file=/etc/prometheus/prometheus.yml" #Command-line arguments for the container. It specifies the path to the Prometheus configuration file.

          ports:
            - containerPort: 9090 #The port on which the container will listen. Here, it is set to 9090.
          volumeMounts:
            - name: prometheus-config-volume #The name of the volume to mount. Here, it is prometheus-config-volume.
              mountPath: /etc/prometheus/ #he path inside the container where the volume will be mounted. Here, it is /etc/prometheus/.
      volumes:
        - name: prometheus-config-volume #The name of the volume. Here, it is prometheus-config-volume.
          configMap:
            name: prometheus-config #The name of the ConfigMap to use for the volume. Here, it is prometheus-config.
```
- **Prometherus service**:
Finally a lets expose Prometheus from the minikube cluster
```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus-service
  namespace: monitoring
  labels:
    app: prometheus
spec:
  selector:
    app: prometheus
  ports:
    - protocol: TCP
      port: 9090
      targetPort: 9090
  type: NodePort
```

- **Run it together**:
Let´s run all together using these commands
```yaml
 kubectl apply -f prometheus.yaml 
 minikube service prometheus-service -n monitoring
```
---
# Tip for Infrastructure as Code (IaC) with Ansible

> [!TIP]
> A more efficient **Infrastructure as Code (IaC)** approach can be implemented with Ansible to apply the Prometheus configuration and start its service in Minikube. Below is an example of how to structure a YAML playbook to achieve this:
> 1. **Create a YAML Playbook**
> ```yaml
> ---
> - name: Apply Prometheus configuration and start service in Minikube
>   hosts: all
>   become: yes  # Optional, if sudo permissions are required
>   tasks:
>     - name: Apply Prometheus configuration
>       command: kubectl apply -f prometheus.yaml
>       args:
>         chdir: ./  #  directory where the command should be executed
> ```
> 2. **Run the Playbook**
> ```bash
> ansible-playbook -i ../exercise4.1/ansible_quickstart/inventory.ini infra.yaml
> minikube service prometheus-service -n monitoring
> ```
---
# Final Objective
At the end of this document, you should accomplished this:
> [!IMPORTANT]
> In the input field try to look for words like "memory", "cpu" or "kubernetes", then click in one of the results at the autocomplete overlay, then click > **Execute** and the resutls will be displayed in the table format, then change to grapgh format.
> 
> As promotheus was recently installed there are no too much information to display.
> 
> ![prometheus_table](prometheus_table.png)