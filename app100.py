import streamlit as st
import pickle
import numpy as np

# Load saved model
with open("simple_linear_regression.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("Diabetes Progression Prediction App")

st.write("Simple Linear Regression Model")

# User input
bmi = st.number_input("Enter BMI Value")

# Predict button
if st.button("Predict"):

    input_data = np.array([[bmi]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Disease Progression: {prediction[0]:.2f}")