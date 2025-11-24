from catboost import CatBoostClassifier
import pandas as pd
class PredictionModel:

    def __init__(self):
        model = CatBoostClassifier()
        MODEL_PATH = "model/catboost_model.cbm"  # Update with relative path in the Docker container
        self.model = model.load_model(MODEL_PATH)

    def get_churn_probability(self, data):
        churn_probability = self.model.predict_proba(data)[0][1]
        return churn_probability
