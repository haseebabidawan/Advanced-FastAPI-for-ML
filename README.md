# 🚀 Advanced FastAPI for ML — Car Price Prediction System

## 🧠 Overview
This project demonstrates a **production-grade Machine Learning system** built using **FastAPI**, **Streamlit**, and modern backend technologies.

The goal is to predict **car prices** based on multiple input features such as company, year, engine capacity, mileage, and more — wrapped in a **secure, scalable, and monitored architecture**.

It showcases advanced FastAPI concepts, including:
- 🔐 JWT Authentication for secure access  
- ⚡ Redis caching for faster prediction performance  
- 📈 Prometheus metrics for system monitoring  
- 🐳 Dockerized microservices (backend, frontend, Redis, Prometheus)  
- 🎨 Streamlit UI for user-friendly interaction with the model  

---

## 🏗️ System Architecture

+----------------+ +--------------------+ +----------------+
| Streamlit UI | <---> | FastAPI Backend | <---> | Redis Cache |
| (Frontend) | | (Model + Auth) | | (Prediction) |
+----------------+ +--------------------+ +----------------+
| |
| v
| +-------------+
| | Prometheus |
| | Monitoring |
| +-------------+



---

## 🔑 Key Features

### 1. JWT Authentication
- Secure token-based login via FastAPI and PyJWT  
- Access control for prediction endpoints  
- Tokens validated on every API call  

### 2. Redis Caching
- Stores previously computed prediction results  
- Reduces redundant computation and improves latency  
- TTL automatically expires old cache entries  

### 3. Prometheus Monitoring
- Tracks request rate, error rate, and latency  
- Integrated via `prometheus_fastapi_instrumentator`  
- `/metrics` endpoint exposes data for visualization  

### 4. Streamlit Frontend
- Clean, interactive UI  
- Login page (JWT-based)  
- Prediction form with live inputs and API integration  

### 5. Dockerized Microservices
- Frontend, backend, Redis, and Prometheus run as separate containers  
- Unified orchestration via Docker Compose  
- Easy local or cloud deployment  

---

## ⚙️ Setup and Installation

### 🧩 Prerequisites
Make sure you have installed:
- Python 3.9+
- Docker & Docker Compose

---

### 🧰 Step 1: Clone the repository
```bash
git clone https://github.com/<your-username>/Advanced-FastAPI-for-ML.git
cd Advanced-FastAPI-for-ML
