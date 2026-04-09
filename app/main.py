from fastapi import FastAPI
import numpy as np
from app.model import load_model
from app.schema import PatientData

app = FastAPI(title="Healthcare ML API")

model = load_model()

@app.get("/")
def home():
    return {"message": "Healthcare ML API is running"}

@app.post("/predict")
def predict(data: PatientData):
    features = np.array([[data.age, data.blood_pressure, data.cholesterol]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
