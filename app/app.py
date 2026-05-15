import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("../models/credit_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

# Title
st.set_page_config(
    page_title="CreditLens",
    layout="centered"
)

st.title("💳 CreditLens")
st.subheader("AI-Powered Credit Risk Prediction System")

st.write("""
This application predicts whether a customer is likely to default on a loan
using Machine Learning models trained on financial history data.
""")

st.write("Predict whether a person is creditworthy or not.")

# User Inputs
person_age = st.number_input("Age", min_value=18, max_value=100, value=25)

person_income = st.number_input("Annual Income", min_value=0)

person_emp_length = st.number_input(
    "Employment Length (Years)",
    min_value=0.0
)

loan_amnt = st.number_input("Loan Amount", min_value=0)

loan_int_rate = st.number_input(
    "Interest Rate",
    min_value=0.0
)

loan_percent_income = st.number_input(
    "Loan Percent Income",
    min_value=0.0
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    min_value=0
)

# Encoded categorical inputs
person_home_ownership = st.selectbox(
    "Home Ownership",
    [0,1,2,3]
)

loan_intent = st.selectbox(
    "Loan Intent",
    [0,1,2,3,4,5]
)

loan_grade = st.selectbox(
    "Loan Grade",
    [0,1,2,3,4,5,6]
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    [0,1]
)

# Prediction Button
if st.button("Predict Credit Risk"):

    features = np.array([[
        person_age,
        person_income,
        person_home_ownership,
        person_emp_length,
        loan_intent,
        loan_grade,
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        cb_person_default_on_file,
        cb_person_cred_hist_length
    ]])

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)

    probability = model.predict_proba(features_scaled)

    risk_score = probability[0][1]

    st.write(f"### Risk Probability: {risk_score:.2f}")

    if prediction[0] == 1:
        st.error("⚠ High Credit Risk / Possible Default")
    else:
        st.success("✅ Low Credit Risk / Creditworthy")

    # Scale data
    features_scaled = scaler.transform(features)

    # Prediction
    prediction = model.predict(features_scaled)

    # Result
    if prediction[0] == 1:
        st.error("High Credit Risk / Possible Default")
    else:
        st.success("Low Credit Risk / Creditworthy")