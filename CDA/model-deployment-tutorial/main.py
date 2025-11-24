from typing import List

import pandas as pd

from fastapi import FastAPI

from data_model import DataModel
from prediction_model import PredictionModel


app = FastAPI(title="Churn Prediction API Uniandes CDA")

@app.get("/")
def read_root():
    return { "message": "Hello world" }

@app.post("/predict")
def make_predictions(X: List[DataModel]):
    print(X)
    data = pd.DataFrame([x.dict() for x in X])
    predicion_model = PredictionModel()
    results = predicion_model.get_churn_probability(data=data)
    return results.tolist()
