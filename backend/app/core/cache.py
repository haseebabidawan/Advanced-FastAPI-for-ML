import redis
import json
from app.core.config import setting

redis_client = redis.Redis.from_url(setting.REDIS_URL)


def get_cached_data(key:str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def add_cached_data(key:str, value:dict, expiry:int = 3600):
    redis_client.setex(key,expiry, json.dumps(value))