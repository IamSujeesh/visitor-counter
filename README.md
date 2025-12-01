🚀 Visitor Counter – DevOps End-to-End Project

This project demonstrates a complete DevOps workflow starting from local development → Docker → Kubernetes (kubeadm cluster on AWS EC2).
It uses a Python Flask application + Redis to track visitor counts.

🧰 Tools Used

VS Code

Python

Docker Desktop

Git / GitHub

AWS EC2

Kubernetes (kubeadm)

Redis

📌 Architecture Diagram

(You should insert an actual image here — see instructions below)

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

📌 1. Local Project Setup

Project located at:

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

List Images
docker images

Run App Container
docker run -d -p 5000:5000 --name visitor-container visitor-app:1.0

View Running Containers
docker ps

📌 3. Run Redis Container
docker run -d --name redis -p 6379:6379 redis
docker ps

📌 4. Link App with Redis
docker stop visitor-container
docker rm visitor-container
docker run -d --name visitor-app --link redis -p 5000:5000 visitor-app:1.0

Verify in Browser

👉 http://localhost:5000

📌 5. Docker Hub – Login, Tag, Push
docker login
docker tag visitor-app:1.0 iamsujeesh/visitor-app:1.0
docker push iamsujeesh/visitor-app:1.0
docker pull iamsujeesh/visitor-app:1.0

📌 6. Kubernetes Setup on AWS EC2 (kubeadm)

Kubeadm guide reference:
👉 https://github.com/yeshwanthlm/Kubeadm-Installation-Guide

EC2 Setup

Master Node

Worker Node

Install Kubernetes Components

kubeadm

kubelet

kubectl

(Installed as per guide)

📌 7. Deploy Application on Kubernetes Cluster
Clone Repository
git clone https://github.com/IamSujeesh/visitor-counter.git
cd visitor-counter

Apply Kubernetes Manifests
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/visitor-deployment.yaml
kubectl apply -f k8s/visitor-service.yaml

Verify
kubectl get pods
kubectl get svc

Access Application
http://<Worker Public IP>:<NodePort>

🖥 8. High-Level Architecture Flow

Developer Laptop:

VS Code → Python Code

Git → Push to GitHub

Docker → Build Image → Push to Docker Hub

AWS EC2 Kubernetes Cluster:

Master Node

kubeadm init

Clone repo

Apply YAML files

Worker Node

Redis Pod

Visitor App Pods (3 replicas)

Exposed via NodePort

🎯 What This Project Demonstrates

Dockerization

Git version control

Manual CI workflow

Kubernetes setup (kubeadm)

Multi-container architecture

Redis + Flask communication

NodePort external access

Deployment & scaling

🏁 End of Documentation

This project showcases a complete DevOps workflow from coding → containerization → orchestration → cloud deployment.