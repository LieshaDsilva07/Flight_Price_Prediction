# flight_app.py

import streamlit as st
import pandas as pd
import joblib
import json
from datetime import datetime
import os

# --- Load model and schema ---
model_path = os.path.join("model", "flight_price_model.pkl")
columns_path = os.path.join("model", "model_columns.json")

model = joblib.load(model_path)
with open(columns_path, "r") as f:
    model_columns = json.load(f)

# --- Streamlit UI ---
st.title("✈️ Flight Price Prediction App")
st.write("Enter flight details below to get a price prediction.")

# --- User Inputs ---
airline = st.selectbox("Airline", 
    ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
     'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
     'Trujet', 'Vistara', 'Vistara Premium economy'])

departure = st.selectbox("Departure City", ['Chennai', 'Delhi', 'Kolkata', 'Mumbai'])
arrival = st.selectbox("Arrival City", ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'])
date = st.date_input("Journey Date", min_value=datetime.today())
stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

# Dummy time values (simplified for demo)
dep_hour, dep_min = 10, 15
arr_hour, arr_min = 13, 30
duration_hours = arr_hour - dep_hour
duration_mins = arr_min - dep_min

# --- Prepare Input Row ---
row = {
    "stops": stops,
    "Journey_Day": date.day,
    "Journey_Month": date.month,
    "dep_hour": dep_hour,
    "dep_min": dep_min,
    "arr_hour": arr_hour,
    "arr_min": arr_min,
    "Duration_hours": duration_hours,
    "Duration_mins": duration_mins,
}

# One-hot encoding for cities
for loc in ["Chennai", "Delhi", "Kolkata", "Mumbai"]:
    row[f"departure_loc_{loc}"] = 1 if departure == loc else 0
for loc in ["Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"]:
    row[f"arrival_loc_{loc}"] = 1 if arrival == loc else 0

# One-hot encoding for airlines
for a in ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
          'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
          'Trujet', 'Vistara', 'Vistara Premium economy']:
    row[a] = 1 if a == airline else 0

# Convert to DataFrame and align with model schema
input_df = pd.DataFrame([row])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# --- Prediction ---
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Ticket Price: ₹{int(prediction)}")
