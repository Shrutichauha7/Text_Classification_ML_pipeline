#  End-to-End MLOps Pipeline for Text Classification

> A production-ready MLOps pipeline for Text Classification built with **Python, Scikit-learn, DVC, MLflow, Docker, AWS, Kubernetes, GitHub Actions, Prometheus, and Grafana**.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes)
![AWS](https://img.shields.io/badge/AWS-FF9900?logo=amazonaws)
![MLflow](https://img.shields.io/badge/MLflow-0194E2)
![DVC](https://img.shields.io/badge/DVC-945DD6)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana)

---

## 📌 Overview

This project demonstrates a complete **Machine Learning Operations (MLOps)** workflow for a Text Classification application. It automates the ML lifecycle—from data ingestion and preprocessing to model training, experiment tracking, versioning, deployment, and monitoring using modern cloud-native technologies.

---

## ✨ Key Features

- 📥 Automated Data Ingestion & Preprocessing
- 🧹 Feature Engineering Pipeline
- 🤖 Model Training & Evaluation
- 📊 MLflow Experiment Tracking
- 📦 DVC Data & Pipeline Versioning
- 🐳 Docker Containerization
- ☁️ AWS S3, ECR & EKS Integration
- 🚀 GitHub Actions CI/CD Pipeline
- ☸️ Kubernetes Deployment
- 📈 Prometheus & Grafana Monitoring
- 🌐 Flask REST API Deployment

---

## 🏗️ Architecture

```text
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ├────────► MLflow (Experiment Tracking)
   └────────► DVC (Data & Pipeline Versioning)
                    │
                    ▼
               Flask API
                    │
                    ▼
                 Docker
                    │
                    ▼
                Amazon ECR
                    │
                    ▼
             Kubernetes (EKS)
                    │
                    ▼
              Load Balancer
                    │
                    ▼
                 End Users
                    │
                    ▼
         Prometheus → Grafana
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python 3.10 |
| Machine Learning | Scikit-learn |
| Backend | Flask |
| Experiment Tracking | MLflow + DagsHub |
| Data Versioning | DVC |
| Cloud | AWS |
| Storage | Amazon S3 |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Amazon EKS (Kubernetes) |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus & Grafana |
| Version Control | Git & GitHub |

---

## ⚙️ Project Workflow

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Run Tests
   │
   ▼
DVC Pipeline
   │
   ▼
MLflow Tracking
   │
   ▼
Build Docker Image
   │
   ▼
Push to Amazon ECR
   │
   ▼
Deploy on Amazon EKS
   │
   ▼
Monitor with Prometheus & Grafana
```

---

## 📂 Project Structure

```text
├── src/
│   ├── data_ingestion/
│   ├── data_preprocessing/
│   ├── feature_engineering/
│   ├── model_building/
│   ├── model_evaluation/
│   └── register_model/
│
├── flask_app/
├── tests/
├── scripts/
├── .github/workflows/
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```

---

## 🚀 Technologies Demonstrated

- Machine Learning Pipeline
- Data Versioning with DVC
- MLflow Experiment Tracking
- Model Registry
- Docker Containerization
- AWS Cloud Deployment
- Kubernetes Orchestration
- CI/CD Automation
- Infrastructure Monitoring
- Production-Ready REST API

---

## 📸 Project Screenshots

Add screenshots here for:

- MLflow Dashboard
- GitHub Actions
- Docker Image
- Kubernetes Pods
- Prometheus
- Grafana Dashboard
- Application UI

---

## 🎯 Future Improvements

- Infrastructure as Code using Terraform
- GitOps with ArgoCD
- Helm Charts
- Model Drift Detection
- Canary & Blue-Green Deployments

---

## 👩‍💻 Author

**Shruti Chauhan**

- GitHub: https://github.com/Shrutichauha7
- LinkedIn: https://www.linkedin.com/in/shrutichauhan792004

---

⭐ **If you found this project helpful, consider giving it a star!**