from fastapi import FastAPI
import joblib
import numpy as np

# Load trained model
model = joblib.load("random_forest_mortality_model.pkl")

app = FastAPI(title="Tobacco Mortality Prediction API")

@app.get("/")
def home():
    return {"message": "Tobacco Mortality Prediction API is running"}

@app.post("/predict")
def predict(
    Smoking_Prevalence: float,
    Tobacco_Affordability: float,
    Smoking_Duration_Proxy: float,
    Tobacco_Price_Relative: float,
    Total_Prescriptions: float,
    Admission_per_Smoker: float,
    Income_Impact: float
):
    """
    Predicts whether the given indicators correspond to a High Mortality Risk year.
    """

    features = np.array([[
        Smoking_Prevalence,
        Tobacco_Affordability,
        Smoking_Duration_Proxy,
        Tobacco_Price_Relative,
        Total_Prescriptions,
        Admission_per_Smoker,
        Income_Impact
    ]])

    prediction = model.predict(features)[0]

    return {
        "High Mortality Risk": int(prediction),
        "Interpretation": "1 = High Risk, 0 = Low Risk"
    }
