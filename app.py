import streamlit as st
import joblib

# Load the model
model = joblib.load('fraud_detection_model.pkl')

st.title("Credit Card Fraud Detection")

v1 = st.number_input("V1:")
v2 = st.number_input("V2:")
v3 = st.number_input("V3:")
amount = st.number_input("Amount:")

if st.button("Predict"):
    input_data = [[v1, v2, v3, amount]]
    prediction = model.predict(input_data)
    result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
    st.success(f"Prediction: {result}")
