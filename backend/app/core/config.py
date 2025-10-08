from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    PROJECt_NAME :str = "Advanced FastAPI with ML"
    API_KEY :str = os.getenv("API_KEY")
    JWT_SECRET_KEY:str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGO :str = "HS256"
    REDIS_URL :str = os.getenv("REDIS_URL")
    MODEL_PATH:str = 'models/model.joblib'


setting = Settings()