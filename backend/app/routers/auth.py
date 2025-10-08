from fastapi import APIRouter , HTTPException, status
from app.core.security import create_token

router = APIRouter()

user = {"admin":"admin"}

@router.post("/login")
def login(username:str, password:str):
    if username not in user and user[username] != password:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid Credentials")
    token = create_token({"sub":username})
    return {"access_token":token, "token_type":"bearer"}