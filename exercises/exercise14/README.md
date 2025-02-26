# **Installation and Configuration Using Helm Charts**

## **Table of Contents**
1. [Introduction to Helm](#introduction-to-helm)  
2. [Installing Helm](#installing-helm)  
3. [Creating the First Helm Chart](#creating-the-first-helm-chart)  
4. [Installing and Running the Helm Chart](#installing-and-running-the-helm-chart)  
5. [Expose Services](#expose-services)  
6. [Publishing a Helm Chart to a Public Repository](#publishing-a-helm-chart-to-a-public-repository)  
7. [Final Objective](#final-objective)  
8. [Cleanup](#cleanup) 

---

## **Introduction to Helm**
In previous exercises, we deployed our application components using Kubernetes manifests stored in YAML files. These manifests were applied in a strict order using a script (`cluster.sh`). However, this approach has some drawbacks:

- **Rigid installation order** – Components must be installed in a specific sequence, with no built-in rollback mechanism if something fails.
- **Code duplication** – The same values (e.g., resource limits, image names, environment variables) are repeated across multiple manifests.
- **Difficult updates** – Keeping track of changes across multiple YAML files is cumbersome.

### **What is Helm?**
**Helm** is a package manager for Kubernetes that allows you to define, install, and upgrade complex Kubernetes applications. It provides a way to package Kubernetes resources into **Helm Charts**, which are reusable, versioned, and easily deployable across environments.

### **Why Use Helm?**
Using **Helm charts** for Kubernetes deployments provides several benefits:

**Simplifies deployment** – A Helm chart encapsulates all necessary Kubernetes resources, eliminating the need to apply them individually.  
**Version control** – Helm keeps track of chart versions, making rollbacks and upgrades easier.  
**Reusable configurations** – Instead of duplicating values across multiple manifests, Helm allows you to define configurations in a centralized file (`values.yaml`).  
**Improved maintainability** – With Helm, you can manage deployments in a structured and modular way.  

In this exercise, we will transition from manually applying Kubernetes manifests to using **Helm charts** to deploy and manage our application.

---

## **Installing Helm**
Before creating our first Helm chart, we need to install Helm.

```bash
brew install helm
```

Once installed, verify the version:

```bash
helm version
```

---

## **Creating the First Helm Chart**
Before proceeding, **navigate to the correct directory**:

```bash
cd sre-abc-training/exercises/exercise14
```

Now, create the **Helm Chart**:

```bash
helm create my-sre-app-chart
```

This creates a new directory **`my-sre-app-chart`** with a default Helm structure. However, we need to remove the default templates:

```bash
rm -rf my-sre-app-chart/templates/*
```

> **[!NOTE]**  
> When executing the above command, **you may receive a confirmation prompt** like this:  
> ```
> zsh: sure you want to delete all the files in /Users/<your-user>/sre-abc-training/exercises/exercise14/my-sre-app-chart/templates [yn]?
> ```
> Just type Y. This is expected since Helm generates default templates that we don’t need.

### **Copying Necessary Manifests**
Next, copy the required manifests from previous exercises into our new **Helm Chart**:

```bash
cp ../exercise10/storage.yaml ../exercise10/deployment.yaml ../exercise10/otel-collector.yaml \
   ../exercise8/jaeger.yaml ../exercise9/prometheus.yaml ../exercise12/grafana-loki.yaml \
   ../exercise12/grafana.yaml my-sre-app-chart/templates/
```

---

## **Installing and Running the Helm Chart**
Once everything is set up, install the chart with:

```bash
helm install sre-app ./my-sre-app-chart
```

To verify the installation:

```bash
helm get manifest sre-app
kubectl get pods -A
```

> **[!IMPORTANT]**
> After installing the Helm Chart, it may take several minutes for all services to start.  
>  
> Run the following command to monitor their status:
> ```bash
> kubectl get pods -A -o wide
> ```
> Wait for all pods to reach Running status before continuing.

---

## **Expose Services**

### **Access the Application Service**
Run:
```bash
minikube service sre-abc-training-service -n application
```
- This will open the **application page** in your default web browser.
- **Keep the terminal open**—closing it will stop the service.

### **Access Grafana (New Terminal)**
1. **Open a new terminal session**.
2. Run:
   ```bash
   minikube service grafana-service -n monitoring
   ```
3. This will open **Grafana’s UI** in a browser.

---

## **Publishing a Helm Chart to a Public Repository**
This section covers **publishing the Helm chart** to a public repository.

### **1. Package the Helm Chart**
```bash
helm package ./my-sre-app-chart
```

This will create a `.tgz` file in the current directory.

### **2. Create an `index.yaml` File**
```bash
helm repo index . --url https://cguillencr.github.io/sre-abc-training/
```

This generates an **index file** required for Helm repositories.

### **3. Enable GitHub Pages**
- Navigate to your repository **on GitHub**.
- Go to **Settings > Pages**.
- Set the source to **main branch** and **docs directory**.
- Save the changes.

### **4. Push the Helm Chart Files to GitHub**
```bash
mkdir -p ../../docs/
mv my-sre-app-chart-0.1.0.tgz ../../docs/my-sre-app-chart-0.1.0.tgz
cd ../../docs
helm repo index ./ --url https://cguillencr.github.io/sre-abc-training

git add ./index.yaml
git add ./my-sre-app-chart-0.1.0.tgz
cd ../exercises/exercise14
git commit --amend -m "Helm configuration"
git push -u origin main -f
```

### **5. Add the Repository Locally**
```bash
helm repo add sre-abc-lab https://cguillencr.github.io/sre-abc-training/
helm repo update
helm repo list
helm search repo sre-abc-lab
```

### **6. Install the Application from the Repository**
```bash
helm install sre-app sre-abc-lab/my-sre-app-chart
```

---

## **Final Objective**
At the end of this exercise, you should accomplish the following:

> All cluster components should be installed using **Helm Charts**, replacing direct > Kubernetes manifests.  
> You should be able to **rollback** deployments in case of failure.  
> The **Helm Chart** should be **published to a repository** and **retrievable** via > Helm.  
> 
> To verify, run:
> 
> ```bash
> kubectl get pods -A
> ```
> 
> You should see output similar to:
> 
> ```
> application     sre-abc-training-app-fc68fcc89-dz9rk     1/1     Running
> monitoring      grafana-deployment-69c545d6-2ljnh        1/1     Running
> monitoring      prometheus-deployment-7b4f4dddbf-mdfbr   1/1     Running
> opentelemetry   jaeger-856888c4b4-zznjv                  1/1     Running
> opentelemetry   loki-86657bb9c-9f9zh                     1/1     Running
> opentelemetry   otel-collector-7fdd968cb5-jgnzn          1/1     Running
> ```

---

## **Cleanup**
To delete the Helm deployment and clean up resources, run:
```bash
helm uninstall sre-app
```

To verify that all resources are deleted:
```bash
kubectl get pods -A
```

---