Production Grade MLOps Pipeline
End-to-End Text Classification System
AWS • Docker • Kubernetes • DVC • MLflow • CI/CD • Monitoring
Beautiful Badges
![Python](https://img.shields.io/badge/Python-3.10-blue)

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes)

![AWS](https://img.shields.io/badge/AWS-orange?logo=amazonaws)

![MLflow](https://img.shields.io/badge/MLflow-0194E2)

![DVC](https://img.shields.io/badge/DVC-purple)

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF)

![Prometheus](https://img.shields.io/badge/Prometheus-orange)

![Grafana](https://img.shields.io/badge/Grafana-F46800)

![Flask](https://img.shields.io/badge/Flask-black)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E)

![License](https://img.shields.io/badge/License-MIT-green)
Project Overview
An enterprise-ready end-to-end Machine Learning Operations (MLOps) project for Text Classification that automates the complete ML lifecycle—from data ingestion and preprocessing to model training, experiment tracking, versioning, deployment, monitoring, and continuous delivery using modern DevOps and cloud technologies.

This project demonstrates production-level ML engineering practices including DVC pipelines, MLflow experiment tracking, Docker containerization, AWS ECR/EKS deployment, GitHub Actions CI/CD, and monitoring with Prometheus and Grafana.
Features
✅ Automated Data Ingestion

✅ Data Preprocessing Pipeline

✅ Feature Engineering

✅ Model Training

✅ Model Evaluation

✅ MLflow Experiment Tracking

✅ DVC Data Versioning

✅ DVC Pipeline Automation

✅ Model Registry

✅ Flask REST API

✅ Docker Containerization

✅ GitHub Actions CI/CD

✅ AWS ECR Image Registry

✅ AWS EKS Deployment

✅ Kubernetes Orchestration

✅ Prometheus Monitoring

✅ Grafana Dashboard

✅ Cloud Deployment

✅ Production-ready Architecture
Tech Stack
Category	Technologies
Programming	Python
ML	Scikit-Learn
API	Flask
Experiment Tracking	MLflow + DagsHub
Data Versioning	DVC
Cloud	AWS
Storage	Amazon S3
Container	Docker
Registry	Amazon ECR
Orchestration	Kubernetes (EKS)
CI/CD	GitHub Actions
Monitoring	Prometheus
Visualization	Grafana
Version Control	Git & GitHub
Architecture Diagram
                GitHub Repository
                       │
                       ▼
              GitHub Actions CI
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
      Run Tests               Build Docker Image
         │                           │
         └─────────────┬─────────────┘
                       ▼
              Push Image to AWS ECR
                       │
                       ▼
                Deploy to AWS EKS
                       │
          Kubernetes Cluster
                       │
               Flask Application
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
     Prometheus               MLflow + DVC
          │
          ▼
      Grafana Dashboard
ML Pipeline
Raw Dataset

↓

Data Ingestion

↓

Data Preprocessing

↓

Feature Engineering

↓

Model Training

↓

Model Evaluation

↓

Model Registration

↓

Deployment
MLOps Workflow
Developer

↓

GitHub Push

↓

GitHub Actions

↓

Unit Tests

↓

DVC Pipeline

↓

MLflow Logging

↓

Docker Build

↓

Push Image → AWS ECR

↓

Deploy → AWS EKS

↓

Application Live

↓

Prometheus Monitoring

↓

Grafana Dashboard
AWS Services Used
Amazon EC2

Amazon S3

Amazon ECR

Amazon EKS

IAM

Load Balancer

Cloud Networking
Monitoring Stack
Application

↓

Prometheus

↓

Grafana

↓

Real-time Dashboards

↓

Performance Metrics
Project Structure
.
├── src
│   ├── logger
│   ├── data_ingestion
│   ├── data_preprocessing
│   ├── feature_engineering
│   ├── model_building
│   ├── model_evaluation
│   └── register_model
│
├── tests
├── scripts
├── flask_app
├── .github/workflows
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
CI/CD Pipeline
Developer Push

↓

GitHub Actions

↓

Install Dependencies

↓

Run Tests

↓

Run DVC Pipeline

↓

Build Docker Image

↓

Push Image to ECR

↓

Deploy to Kubernetes

↓

Application Updated
Recruiter Highlights
✔ Production-grade MLOps

✔ Cloud Native Deployment

✔ Kubernetes Orchestration

✔ Dockerized Application

✔ Complete CI/CD Pipeline

✔ Automated ML Workflow

✔ Data Versioning

✔ Experiment Tracking

✔ Monitoring & Alerting

✔ Scalable Deployment

✔ Infrastructure as Code Ready
Future Improvements
- Terraform Infrastructure
- Helm Charts
- ArgoCD GitOps
- Model Drift Detection
- Airflow Scheduling
- FastAPI Migration
- Canary Deployment
- Blue-Green Deployment
GitHub Stats Section
![Stars](https://img.shields.io/github/stars/USERNAME/REPO)

![Forks](https://img.shields.io/github/forks/USERNAME/REPO)

![Issues](https://img.shields.io/github/issues/USERNAME/REPO)

![Last Commit](https://img.shields.io/github/last-commit/USERNAME/REPO)
