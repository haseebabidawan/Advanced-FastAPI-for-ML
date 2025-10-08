from fastapi import APIRouter, status, HTTPException, Depends
from app.core.cache import get_cached_data, add_cached_data
import joblib
from app.core.security import decode_token
from app.core.config import setting
import pandas as pd
from pydantic import BaseModel

class CareFeatures(BaseModel):
    company:str
    year:int
    owner:str
    fuel:str
    seller_type:str
    transmission: str
    km_driven: float
    mileage_mpg:float
    engine_cc:float
    max_power_bhp:float
    torque_nm:float
    seats:float

router = APIRouter()

model = joblib.load(setting.MODEL_PATH)

@router.post("/")
def predict_price(data:CareFeatures, token = Depends(decode_token)):
    data_update = data.model_dump()
    cache_key = " ".join([str(val) for val in data_update.values()])
    cached = get_cached_data(cache_key)
    if cached:
        return cached
    input_data = pd.DataFrame([data_update])
    prediction = model.predict(input_data)[0]
    add_cached_data(cache_key,prediction)
    return {'Predicted_price': f'{prediction:,.2f}'}