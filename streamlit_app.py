import streamlit as st
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 Delhi House Price Prediction")

user_input = {}

st.subheader("Enter Property Details")

for col in columns:
    user_input[col] = st.number_input(
        col,
        value=0.0,
        step=1.0
    )

if st.button("Predict Price"):
    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)

    st.success(f"Estimated House Price: ₹{prediction[0]:,.2f}")