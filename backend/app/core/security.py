from jose import jwt, JWTError
from core.config import setting
from datetime import datetime, timedelta, timezone



def create_token(data:dict, expiry_time:int=30):
    load = data.copy()
    exp = datetime.now(timezone.utc)+ timedelta(minutes=expiry_time)
    load.update({'exp':exp})
    return jwt.encode(load, setting.JWT_SECRET_KEY, setting.JWT_ALGO)



def decode_token(token:str):
    try:
        payload = jwt.decode(token=token, key=setting.JWT_SECRET_KEY, algorithms=setting.JWT_ALGO)
        return payload
    except JWTError:
        return None