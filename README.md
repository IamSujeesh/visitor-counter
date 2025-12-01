🚀 Visitor Counter – DevOps End-to-End Project

This project demonstrates a complete DevOps workflow starting from local development → Docker → Kubernetes (kubeadm cluster on AWS EC2).
It uses a Python Flask web app + Redis to track and display visitor counts.

🧰 Tools Used

VS Code

Python

Docker Desktop

Git / GitHub

AWS EC2

Kubernetes (kubeadm)

Redis

📌 Architecture Diagram (ASCII)
                     +---------------------------+
                     |        User Browser       |
                     |  http://EC2_PUBLIC_IP:31816
                     +-------------+-------------+
                                   |
                             NodePort Service
                                   |
      ---------------------------------------------------------
      |                        Kubernetes Cluster             |
      |                                                       |
      |  +------------------+        +------------------+     |
      |  | visitor-app Pod  |        | visitor-app Pod  |     |
      |  |  (Flask App)     |        |  (Flask App)     |     |
      |  +--------+---------+        +---------+--------+     |
      |           |                            |              |
      |           +-------------+--------------+              |
      |                         |                             |
      |                ClusterIP Service                      |
      |                   (redis)                             |
      |                         |                             |
      |               +---------+---------+                   |
      |               |   Redis Pod       |                   |
      |               +-------------------+                   |
      ---------------------------------------------------------




📁 Project Structure
visitor-counter/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
│── k8s/
    │── redis-deployment.yaml
    │── redis-service.yaml
    │── visitor-deployment.yaml
    │── visitor-service.yaml

📌 1. Project Setup on Local Machine

The project folder is located at:

C:\Users\Sujeesh\Desktop\visitor-counter

Git Initialization
git --version
git init
git add .
git commit -m "Initial project files"
git config --global --list
git remote add origin https://github.com/IamSujeesh/visitor-counter.git
git branch -M main
git push -u origin main

📌 2. Docker – Build, Run, Test Locally
Check Docker Version
docker --version

Build Image
docker build -t visitor-app:1.0 C:\Users\Sujeesh\Desktop\visitor-counter

Verify Image
docker images

Run App Container
docker run -d -p 5000:5000 --name visitor-container visitor-app:1.0

Check Running Containers
docker ps

📌 3. Redis Container Setup
docker run -d --name redis -p 6379:6379 redis
docker ps

📌 4. Link App with Redis
docker stop visitor-container
docker rm visitor-container
docker run -d --name visitor-app --link redis -p 5000:5000 visitor-app:1.0


Test app locally:

👉 http://localhost:5000

📌 5. Docker Hub – Login, Tag, Push
docker login
docker tag visitor-app:1.0 iamsujeesh/visitor-app:1.0
docker push iamsujeesh/visitor-app:1.0
docker pull iamsujeesh/visitor-app:1.0

📌 6. Kubernetes Setup on AWS EC2 (kubeadm Cluster)

For setting up Kubernetes, I followed this guide:
🔗 https://github.com/yeshwanthlm/Kubeadm-Installation-Guide

🔹 EC2 Setup

Create 2 instances:

Master Node

Worker Node

🔹 Install Kubernetes Components (both nodes)

kubeadm

kubelet

kubectl

(Installation steps are in the guide.)

📌 7. Deploy Application in Kubernetes
Clone Repository
git clone https://github.com/IamSujeesh/visitor-counter.git
cd visitor-counter

Apply Manifests
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/visitor-deployment.yaml
kubectl apply -f k8s/visitor-service.yaml

Verify
kubectl get pods
kubectl get svc

Access Application
http://<Worker Public IP>:<NodePort>

🖥 8. High-Level Architecture Overview

Developer Laptop
│
├── VS Code → Python Code
├── Git → GitHub
└── Docker → Build Image → Push to Docker Hub
│
▼
AWS EC2 – Kubernetes Cluster
│
├── Master Node → kubeadm init → deploy YAMLs
└── Worker Node → Redis Pod + Visitor App Pods

⭐ Flow Summary

Code → written in VS Code

Containerized → Docker

Image → pushed to Docker Hub

Repo + YAML → GitHub

Master node pulls repo → deploys

Pods run on worker

Redis + App communicate internally

User accesses via NodePort

✅ Project Demonstrates

Dockerization

Git version control

Manual CI workflow

Kubernetes cluster setup (kubeadm)

Multi-container app

Redis–App internal communication

NodePort exposure

Scaling with replicas

🎯 End of Documentation

This project showcases end-to-end DevOps workflow
from coding → containerization → orchestration → AWS deployment.
