#  TravelOps AI

> **An AI-powered Travel Analytics Platform that predicts flight prices, predicts customer gender, and recommends personalized hotels using Machine Learning.**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST_API-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![License](https://img.shields.io/badge/License-MIT-green)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4-38BDF8?logo=tailwindcss)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?logo=kubernetes)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2)
![Swagger](https://img.shields.io/badge/Swagger-API_Docs-85EA2D?logo=swagger)
![Vercel](https://img.shields.io/badge/Vercel-Frontend-black?logo=vercel)

---

#  Overview

TravelOps AI is a full-stack AI-powered travel analytics platform that integrates multiple machine learning models into a modern web application.

The project demonstrates an end-to-end MLOps workflow, including data preprocessing, model training, experiment tracking with MLflow, REST API development using Flask, Docker containerization, Kubernetes deployment, and a responsive React dashboard.

Users can:

-  Predict Flight Prices
-  Predict Customer Gender
-  Receive Personalized Hotel Recommendations
- 📊Interact through a modern React Dashboard

The project demonstrates the complete Machine Learning lifecycle from data preprocessing to deployment.

---

#  Features

##  Flight Price Prediction

Predicts the expected flight ticket price based on travel information.

### Input

- Source
- Destination
- Flight Type
- Agency
- Distance
- Travel Time
- Travel Date

### Model

- Extra Trees Regressor

---

## Gender Prediction

Predicts customer gender using demographic information.

### Input

- Company
- Age

### Model

- Logistic Regression

---

##  Hotel Recommendation System

Recommends similar hotels using content-based recommendation.

### Algorithm

- Nearest Neighbors
- Cosine Similarity

Returns

- Hotel Name
- Location
- Hotel Price
- Flight Type
- Similarity Score

---
# ⚙️ MLOps Pipeline

This project follows a basic MLOps workflow for deploying machine learning models as production-ready REST APIs.

### Pipeline

```
Data Collection
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
        ▼
Model Serialization (.pkl)
        │
        ▼
Flask REST APIs
        │
        ▼
API Testing (Thunder Client)
        │
        ▼
Frontend Integration (React)
        │
        ▼
Deployment (Render + Vercel)
```

### MLOps Components

- Model Serialization using Joblib
- Modular Flask Backend
- REST API Development
- Input Validation
- Error Handling
- Model Loading at Startup
- API Testing using Thunder Client
- Git Version Control
- Cloud Deployment (Render & Vercel)


#  Machine Learning Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Data Preprocessing
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Flask REST APIs
      │
      ▼
React Frontend
```

---

#  Tech Stack

## Programming

- Python
- JavaScript

## Backend

- Flask
- Flask-CORS

## Frontend

- React
- Axios

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

## Recommendation System

- Nearest Neighbors
- Cosine Similarity

## Deployment

- Render (Backend)
- Vercel (Frontend)

---

# 🚀 Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backend:
   ```bash
   python run.py
   ```
3. Access the API locally at:
   ```text
   http://127.0.0.1:5000
   ```

Available endpoints include flight price prediction, gender prediction, and hotel recommendation.

---

#  Project Structure

```
TravelOps_AI
│
├── app
│   ├── config.py
│   ├── main.py
│   ├── routes.py
│   └── utils.py
│
├── models
│   ├── flight_price_model.pkl
│   ├── flight_preprocessor.pkl
│   ├── gender_model.pkl
│   ├── gender_scaler.pkl
│   ├── gender_label_encoder.pkl
│   ├── recommendation_model.pkl
│   ├── recommendation_preprocessor.pkl
│   └── recommendation_dataset.pkl
│
├── notebooks
│
├── reports
│
├── run.py
├── requirements.txt
└── README.md
```

---

#  REST API Endpoints

## Home

```
GET /
```

---

## Health Check

```
GET /health
```

---

## Flight Price Prediction

```
POST /predict-flight-price
```

### Sample Request

```json
{
  "from": "Brasilia (DF)",
  "to": "Rio de Janeiro (RJ)",
  "flightType": "firstClass",
  "agency": "FlyingDrops",
  "distance": 830,
  "time": 2.5,
  "year": 2021,
  "month": 5,
  "day": 10,
  "day_of_week": "Monday"
}
```

---

## Gender Prediction

```
POST /predict-gender
```

```json
{
  "company": "4You",
  "age": 25
}
```

---

## Hotel Recommendation

```
POST /recommend-hotels
```

```json
{
  "userCode": 25
}
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/TravelOps_AI.git
```

Move into project directory

```bash
cd TravelOps_AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python run.py
```

---

#  API Testing

The APIs can be tested using

- Thunder Client
- Postman
- cURL

---
## 🐳 Docker

Build Image

```bash
docker build -t travelops-ai .
```

Run Container

```bash
docker run -p 5000:5000 travelops-ai
```

#### Docker Hub Repository:

https://hub.docker.com/r/vedantd400/travelops-ai

# Kubernetes

Deploy

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
#  Machine Learning Models

| Module | Algorithm |
|---------|-----------|
| Flight Price Prediction | Extra Trees Regressor |
| Gender Prediction | Logistic Regression |
| Hotel Recommendation | Nearest Neighbors |

---
# Screenshots

## Dashboard
<img width="2856" height="1324" alt="image" src="https://github.com/user-attachments/assets/4253e86a-0b6f-4eee-8f32-a6e7f0bea4ae" />



## Flight Prediction
<img width="2854" height="1325" alt="image" src="https://github.com/user-attachments/assets/3c3bcbf7-0657-49de-bb9f-0b417596ac7e" />


## Gender Prediction
<img width="2849" height="1291" alt="image" src="https://github.com/user-attachments/assets/7038a4b6-f35d-4d9e-a2e9-b558dcb05ab5" />


## Hotel Recommendation
<img width="2855" height="1313" alt="image" src="https://github.com/user-attachments/assets/cc89fcbd-ce3d-44bb-901a-e6e63ccfa2c8" />


## Swagger
<img width="2856" height="1456" alt="image" src="https://github.com/user-attachments/assets/5917f86d-eeaf-453f-aa07-a6262c4aa7d9" />



## MLflow
<img width="2851" height="1473" alt="image" src="https://github.com/user-attachments/assets/29a63717-f70c-4429-bed2-beb755313445" />




#  Future Improvements

- Authentication
- User Accounts
- Booking Integration
- Dynamic Flight Dropdowns
- Live Flight APIs
- Payment Gateway
- CI/CD using GitHub Actions
- Monitoring with Prometheus & Grafana
- Cloud Deployment on AWS/Azure/GCP

---

#  Author

**Vedant P. Deshmukh**

B.Tech CSE (Artificial Intelligence & Machine Learning)

VIT Bhopal University

GitHub: https://github.com/VedantDgit

LinkedIn: https://linkedin.com/in/vedant-deshmukh-9713a2212

---

# ⭐ If you found this project useful, don't forget to star the repository.
