import streamlit as st
import requests

st.title("Tip Prediction App")
st.write("Enter the details to get tip amount")

# input data
total_bill = st.number_input("Total Bill Amount", min_value=0.0)
sex = st.selectbox("Sex", options=["Male", "Female"])
smoker = st.selectbox("Smoker", options=["Yes", "No"])
day = st.selectbox("Day of the Week", options=["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox("Time of the Day", options=["Lunch", "Dinner"])
size = st.number_input("Size of the Party", min_value=1, max_value=10)

# DEFINE INPUT DATA HERE ✅
input_data = {
    "total_bill": total_bill,
    "sex": sex,
    "smoker": smoker,
    "day": day,
    "time": time,
    "size": size
}

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json=input_data
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Tip: {result['prediction']}")
    else:
        st.error("Error connecting to backend API")

