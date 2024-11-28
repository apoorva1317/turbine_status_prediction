import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from datetime import datetime

# Load the trained logistic regression model and scaler
model = load("turbine_model1.pkl")
scaler = load("scaler.pkl")

# Air density (kg/m³) at sea level
rho = 1.225  # Typical air density at sea level in kg/m³

# Streamlit App Title
st.title("Turbine Status Prediction Dashboard")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
wind_speed = st.sidebar.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
ambient_temp = st.sidebar.number_input("Ambient Temperature (°C)", min_value=-50.0, max_value=50.0, value=20.0, step=0.1)
rotor_rpm = st.sidebar.number_input("Rotor RPM", min_value=0.0, max_value=200.0, value=30.0, step=0.1)
blade_length = st.sidebar.number_input("Blade Length (m)", min_value=0.0, max_value=100.0, value=3.5, step=0.1)
blade_temp = st.sidebar.number_input("Blade Temperature (°C)", min_value=-50.0, max_value=100.0, value=25.0, step=0.1)

# Function to predict turbine status
def predict_status(wind_speed, ambient_temp, rotor_rpm, blade_length, blade_temp):
    # Prepare input features
    input_data = np.array([[wind_speed, ambient_temp, rotor_rpm, blade_length, blade_temp]])
    
    # Scale the input using the saved scaler
    scaled_input = scaler.transform(input_data)
    
    # Predict turbine status
    prediction = model.predict(scaled_input)[0]  # 1 = Active, 0 = Inactive
    return "Active" if prediction == 1 else "Inactive"

# Function to calculate power in kilowatts (if turbine is active)
def calculate_power_kw(wind_speed, blade_length, ambient_temp, blade_temp, efficiency, turbine_status):
    # If the turbine is inactive, return 0 power
    if turbine_status == "Inactive":
        return 0.0
    
    # Swept area (m²) of the turbine blades (assuming a circular area)
    A = np.pi * (blade_length ** 2)

    # Power formula (in kilowatts)
    power_kw = 0.5 * rho * A * (wind_speed ** 3) * efficiency / 1000  # Dividing by 1000 to convert to kW
    return power_kw

# Display prediction
predicted_status = predict_status(wind_speed, ambient_temp, rotor_rpm, blade_length, blade_temp)

# Assuming an efficiency range between 0.25 and 0.45 for Cp (Coefficient of performance)
efficiency = np.random.uniform(0.25, 0.45)

# Calculate power generation in kilowatts, but only if the turbine is active
generated_power_kw = calculate_power_kw(wind_speed, blade_length, ambient_temp, blade_temp, efficiency, predicted_status)

# Main display area
st.write(f"### Predicted Turbine Status: {predicted_status}")
st.write("Based on the input values, the turbine is predicted to be **{}**.".format(predicted_status))

# Display the generated power in kilowatts
if predicted_status == "Active":
    st.write(f"### Power Generated: {generated_power_kw:.2f} kW")
else:
    st.write("### Power Generated: 0.00 kW (Turbine is inactive)")

# Real-time data table
st.write("### Input Data Summary")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
input_summary = pd.DataFrame({
    "Timestamp": [current_time],
    "Wind Speed (m/s)": [wind_speed],
    "Ambient Temperature (°C)": [ambient_temp],
    "Rotor RPM": [rotor_rpm],
    "Blade Length (m)": [blade_length],
    "Blade Temperature (°C)": [blade_temp],
    "Turbine Status": [predicted_status],
    "Generated Power (kW)": [generated_power_kw]
})

st.dataframe(input_summary)

# Optional: Simulated chart for turbine predictions over time
st.write("### Simulated Turbine Status Over Time")
chart_data = pd.DataFrame({
    "Timestamp": pd.date_range(start=current_time, periods=10, freq='T'),
    "Predicted Status": ["Active" if np.random.rand() > 0.5 else "Inactive" for _ in range(10)]
})

st.line_chart(chart_data.set_index("Timestamp"))
