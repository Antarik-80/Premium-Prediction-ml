# 🩺 Insurance Premium Predictor

A smart web application built using **Streamlit** that predicts an individual's health insurance premium based on demographic, lifestyle, and medical history attributes. The model assists insurers and users alike in understanding expected premium costs in real time.

---

## 🌐 Live Demo

**[🔗 Try it Live](https://premium-prediction-using-ml.streamlit.app/)** 


---

## 🛠 Features

- 🔥 Clean dark-themed and emoji-enhanced UI powered by **Streamlit**
- 📊 Predicts health insurance premiums based on:
  - Age, BMI, Income, Dependants, Smoking habits, etc.
- 🧠 Utilizes a pre-trained regression model with scaled & encoded inputs
- 💡 Fast, lightweight and real-time predictions
- 🚀 Easily deployable on Streamlit, HuggingFace Spaces, or local system

---

## 📂 Project Structure
Insurance_Premium_Predictor/
│
├── artifacts/
│ └── model.joblib # Trained regression model and encoders
│
├── main.py # Main Streamlit app logic
├── prediction_helper.py # Input transformation and prediction
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## 🚀 How to Run Locally

### ✅ Prerequisites:
- Python 3.8 or higher

### 📦 Installation:
```bash
git clone https://github.com/Antarik-80/Premium-Prediction-ml.git
cd Insurance-Premium-Predictor
pip install -r requirements.txt

▶️ Launch App:
streamlit run main.py

🧠 How It Works
🎯 User Inputs:
Age, Gender, Region, Income (in Lakhs)

Smoking status, Medical history

Employment status, Insurance plan

BMI category, Number of dependants

Genetical risk score (0–5)

⚙️ Prediction Pipeline:
Inputs are encoded/scaled using pre-fitted transformers

The model predicts expected premium using regression

Result is instantly displayed on the Streamlit UI

📘 License
Licensed under the Apache License 2.0
