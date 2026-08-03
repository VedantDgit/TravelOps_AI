# ✈️ TravelOps AI

> **An AI-powered Travel Analytics Platform that predicts flight prices, predicts customer gender, and recommends personalized hotels using Machine Learning.**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST_API-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

TravelOps AI is an end-to-end Machine Learning application that provides intelligent travel analytics using historical travel data.

The application consists of a Flask REST API backend and a React frontend, allowing users to:

- ✈️ Predict Flight Prices
- 👤 Predict Customer Gender
- 🏨 Get Personalized Hotel Recommendations

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

#  Machine Learning Models

| Module | Algorithm |
|---------|-----------|
| Flight Price Prediction | Extra Trees Regressor |
| Gender Prediction | Logistic Regression |
| Hotel Recommendation | Nearest Neighbors |

---

#  Future Improvements

- JWT Authentication
- User Login
- Hotel Booking Integration
- Flight Booking Integration
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- Cloud Database Integration

---

#  Author

**Vedant P. Deshmukh**

B.Tech CSE (Artificial Intelligence & Machine Learning)

VIT Bhopal University

GitHub: https://github.com/VedantDgit

LinkedIn: https://linkedin.com/in/vedant-deshmukh-9713a2212

---

# ⭐ If you found this project useful, don't forget to star the repository.