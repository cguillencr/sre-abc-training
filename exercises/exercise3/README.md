# Pushing a Python Application to Docker Hub with Podman

## Table of Contents
- [Introduction to Docker Hub](#introduction-to-docker-hub)
- [Creating a Docker Hub Account](#creating-a-docker-hub-account)
- [Creating a Docker Repository](#creating-a-docker-repository)
- [Pushing the Image to Docker Hub](#pushing-the-image-to-docker-hub)
  - [Verify the Local Image](#verify-the-local-image)
  - [Tag the Local Image](#tag-the-local-image)
  - [Push the Image to Docker Hub](#push-the-image-to-docker-hub)
- [Running Remote Images](#running-remote-images)
- [Final Objective](#final-objective)

---

## Introduction to Docker Hub

Docker Hub is a cloud-based registry service where container images can be stored, shared, and managed. It simplifies the process of distributing containerized applications, making it easier for developers to collaborate and share resources.

### Key Features:
- **Image Repositories:** Store and share container images publicly or privately.
- **Automated Builds:** Automatically build images from source repositories.
- **Webhooks:** Trigger actions on image updates.
- **Teams and Organizations:** Manage team permissions for repositories.
- **Official Images:** Access Docker-maintained, verified container images.

In this exercise, we will push the containerized Python application created in **Exercise #2** to Docker Hub for distribution.

---

## Navigate to the Application Directory

To begin, navigate to the directory for Exercise 3:

```bash
cd sre-abc-training/exercises/exercise3
```

This directory contains the necessary files for the exercise, including the `Dockerfile` and application code.

---

## Creating a Docker Hub Account

To use Docker Hub, you need an account. Follow these steps to create one:

1. **Visit Docker Hub:**
   Navigate to [Docker Hub](https://hub.docker.com/).

2. **Sign Up:**
   - Click "Sign Up" at the top right.
   - Enter your username, email, and password.
   - Verify your email address by following the link sent to your inbox.

3. **Log In:**
   - Use your credentials to access your Docker Hub account.

---

## Creating a Docker Repository

A Docker repository is where your container images will be stored. Here's how to create one:

1. **Log In to Docker Hub:**
   - Go to [Docker Hub](https://hub.docker.com/) and log in.

2. **Create a New Repository:**
   - Navigate to the "Repositories" tab and click "Create Repository."

3. **Provide Repository Details:**
   - **Name:** Provide a unique, descriptive name (e.g., `my-python-app`).
   - **Visibility:** Choose **Public** (anyone can pull) or **Private** (restricted access).
   - **Description (optional):** Briefly describe the repository's purpose.

4. **Create the Repository:**
   - Click "Create" to finalize.

---

## Pushing the Image to Docker Hub

### Verify the Local Image

Before tagging and pushing the image, confirm that the image exists locally:

1. Run the following command:
   ```bash
   podman images
   ```

   You should see an image named `localhost/python-flask-app` with the tag `latest`. This is the image built in **Exercise #2**.

### Tag the Local Image

We will tag the local image with your Docker Hub username and repository name.

1. Use the `podman tag` command to associate the local image with your Docker Hub repository:
   ```bash
   podman tag localhost/python-flask-app:latest username/my-python-app:latest
   ```

   Replace:
   - `username` with your Docker Hub username.
   - `my-python-app` with the name of your Docker Hub repository.

2. Example:
   ```bash
   podman tag localhost/python-flask-app:latest shesho/python-flask-app:latest
   ```

This step ensures the local image is correctly associated with your Docker Hub repository.

### Push the Image to Docker Hub

1. Log in to Docker Hub:
   ```bash
   podman login docker.io
   ```

2. Push the tagged image to your Docker Hub repository:
   ```bash
   podman push username/my-python-app:latest
   ```

3. Example:
   ```bash
   podman push shesho/python-flask-app:latest
   ```

---

## Running Remote Images

After pushing the image to Docker Hub, you can pull and run it from any machine with Podman installed:

1. **Run the Container:**
   ```bash
   podman run --rm -it -p 5000:5000 username/my-python-app:latest
   ```

2. **Access the Application:**
   Open a web browser and go to:
   ```bash
   http://127.0.0.1:5000/
   ```

---

## Final Objective

At the end of this exercise, you should accomplish the following:

> **[!IMPORTANT]**
> Once the container is running, open your web browser and go to `http://127.0.0.1:5000/`. You should see the text **"Hello, World!"** displayed.
>
> ![app](app.png)

---