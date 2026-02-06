import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("random_forest_mortality_model.pkl")

st.set_page_config(page_title="Tobacco Mortality Predictor", layout="centered")

st.title("🚬 Tobacco Mortality Risk Predictor")
st.write("Enter smoking and economic indicators to estimate mortality risk.")

# User Inputs
Smoking_Prevalence = st.slider("Smoking Prevalence (%)", 0.0, 50.0, 20.0)
Tobacco_Affordability = st.slider("Tobacco Affordability Index", 0.0, 200.0, 80.0)
Smoking_Duration_Proxy = st.number_input("Smoking Duration Proxy", 0.0, 2000.0, 900.0)
Tobacco_Price_Relative = st.slider("Tobacco Price Relative Index", 0.0, 300.0, 230.0)
Total_Prescriptions = st.number_input("Total Prescriptions", 0.0, 10000.0, 2000.0)
Admission_per_Smoker = st.number_input("Admission per Smoker", 0.0, 15000.0, 6000.0)
Income_Impact = st.slider("Income Impact Index", 0.0, 20.0, 7.0)

if st.button("Predict Mortality Risk"):
    
    # --- Derived / default values ---
    Avg_Admission_Rate = 180000        # dataset average
    Prescription_Cost = 50000          # dataset average
    Disposable_Income = 190            # dataset average
    Smoking_Trend = -1.0               # slight downward trend
    Prescription_per_Smoker = Total_Prescriptions / max(Smoking_Prevalence, 1)
    Affordability_Impact = Tobacco_Affordability / Tobacco_Price_Relative

    # --- Feature array in EXACT training order ---
    features = np.array([[
        Smoking_Prevalence,
        Avg_Admission_Rate,
        Total_Prescriptions,
        Prescription_Cost,
        Tobacco_Price_Relative,
        Tobacco_Affordability,
        Disposable_Income,
        Smoking_Duration_Proxy,
        Smoking_Trend,
        Admission_per_Smoker,
        Prescription_per_Smoker,
        Affordability_Impact,
        Income_Impact
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("High Mortality Risk Predicted")
    else:
        st.success("Low Mortality Risk Predicted")

