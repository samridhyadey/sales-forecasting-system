from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Forecast API Running"}

@app.get("/predict")
def predict():
    forecast = [100,120,130,150,170,160,180,200]
    return {"forecast_8_weeks": forecast}