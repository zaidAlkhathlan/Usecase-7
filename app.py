import streamlit as st
import numpy as np
import requests

# Streamlit App Title
st.title("Player Clustering Prediction")

# User Input Fields
appearance = st.number_input("Appearance", min_value=0, max_value=200, value=50)
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=20000, value=4000)
award = st.number_input("Awards Won", min_value=0, max_value=100, value=5)
highest_value = st.number_input("Highest Market Value", min_value=0, max_value=500000000, value=10000000)

# API URL
API_URL = "https://detest-bsd7.onrender.com/predict"

# Predict Button
if st.button("Predict Cluster"):
    # Prepare Input Data
    input_data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "award": award,
        "highest_value": highest_value
    }
    
    # Send Data to API
    response = requests.post(API_URL, json=input_data)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction", "Unknown")
        
        # Ensure prediction is an integer
        if isinstance(prediction, list) and len(prediction) > 0:
            prediction = prediction[0]  # Extract first element if it's a list
        
        if isinstance(prediction, int):
            # Display Prediction
            st.success(f"This player belongs to Cluster: {prediction}")
            
            # Cluster Characteristics
            cluster_desc = {
                0: "Mid-tier players with moderate playtime and decent market value.",
                1: "Low-tier players with minimal playtime and lower value.",
                2: "Elite players with high experience, many awards, and high market value."
            }
            
            st.write("**Cluster Description:**")
            st.info(cluster_desc.get(prediction, "Unknown Cluster"))
        else:
            st.error("Invalid response format from API.")
    else:
        st.error("Failed to get prediction. Please try again later.")

# Run using: streamlit run app.py
