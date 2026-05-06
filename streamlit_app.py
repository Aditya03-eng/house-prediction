import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)

trestbps = st.number_input("Resting Blood Pressure")

chol = st.number_input("Cholesterol Level")

thalach = st.number_input("Maximum Heart Rate")

# Prediction button
if st.button("Predict"):

    # Create input array
    input_data = np.array([[age, sex, cp, trestbps, chol, thalach]])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    if prediction[0] > 0.5:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")