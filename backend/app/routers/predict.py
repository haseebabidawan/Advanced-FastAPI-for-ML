from fastapi import APIRouter, status, HTTPException, Depends
from core.cache import get_cached_data, add_cached_data
import joblib
from core.security import decode_token
from core.config import setting
import pandas as pd
from utils.models_utils import predict_car_price 
from utils.data_preprocess import CareFeatures

router = APIRouter()

model = joblib.load(setting.MODEL_PATH)

@router.post("/")
def predict_price(data:CareFeatures, token:dict = Depends(decode_token)):
    price  = predict_car_price(data)
    return {'Predicted_price': round(price,2)}