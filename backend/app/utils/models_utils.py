import os
import joblib
import pandas as pd
from utils.data_preprocess import CareFeatures
from core.cache import get_cached_data, add_cached_data
from core.config import setting

MODEL_PATH = setting.MODEL_PATH

# Load model once on startup
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    with open(MODEL_PATH, "rb") as f:
        model = joblib.load(f)
    return model

model = load_model()

def predict_car_price(input_data: dict) -> float:
    """
    Main prediction pipeline: preprocess input, check cache, predict using model.
    """
    data_update = input_data.model_dump()
    cache_key = " ".join([str(val) for val in data_update.values()])
    cached = get_cached_data(cache_key)
    if cached:
        return cached
    input_data = pd.DataFrame([data_update])
    prediction = model.predict(input_data)[0]
    add_cached_data(cache_key,prediction)
    return {'Predicted_price': f'{prediction:,.2f}'}