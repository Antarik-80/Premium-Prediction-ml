import streamlit as st
from prediction_helper import predict

# Page Config
st.set_page_config(page_title="🩺 Insurance Premium Predictor", page_icon="💡", layout="wide")

# --- Dark Theme Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #f0f0f0;
    }
    h1, h3 {
        color: #38bdf8;
    }
    hr {
        border: none;
        border-top: 2px solid #333333;
        margin: 10px 0 25px;
    }
    .stNumberInput input {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stSelectbox > div {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🩺 Insurance Premium Predictor</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Categorical Options ---
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# --- Input Layout ---
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# --- Inputs ---
with row1[0]:
    age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧 Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('💼 Income (in Lakhs)', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk (0–5)', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('📦 Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('🏢 Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('⚧️ Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('🗺️ Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🧾 Medical History', categorical_options['Medical History'])

# --- Input Dict ---
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# --- Predict and Display Results ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button('🔍 Predict'):
    prediction = predict(input_dict)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 💰 Predicted Premium")
    st.metric(label="🧾 Estimated Cost", value=f"₹ {prediction:,.2f}")
