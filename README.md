# turbine_status_prediction
This repository contains a Streamlit-based dashboard for predicting the operational status (Active or Inactive) of wind turbines and calculating their power generation in kilowatts based on various input parameters. The model leverages machine learning for prediction and includes a simulation of turbine status over time.

Features:
Predict Turbine Status: Classifies the turbine as Active or Inactive based on input parameters such as wind speed, rotor RPM, and ambient temperature.
Calculate Power Generation: Computes power output in kilowatts (kW) for active turbines.
Real-Time Data Simulation: Visualizes turbine status over time using simulated data.
Interactive Dashboard: User-friendly interface for inputting turbine parameters and viewing predictions.

Example Outputs
Predicted Status:
Active or Inactive based on input parameters.
Generated Power:
Displays power output in kilowatts for active turbines.
Simulated Chart:
A time-series chart showing turbine status over simulated time intervals.

Steps for execution:

Here are the detailed steps for executing the Wind Turbine Status Prediction Dashboard on your local machine:

Steps for Execution
1. Clone the Repository
Download the project files from the GitHub repository to your local machine.
in your bash terminal run:
git clone https://github.com/your-username/wind-turbine-dashboard.git
cd wind-turbine-dashboard
2. This installs all necessary libraries, including:
streamlit: For the interactive dashboard.
pandas: For data manipulation.
numpy: For numerical calculations.
scikit-learn: For the machine learning model.
joblib: For loading the pre-trained model and scaler.
