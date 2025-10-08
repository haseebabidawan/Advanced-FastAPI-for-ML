from fastapi import APIRouter

router = APIRouter()

@router.get("/live")
def liveness_check():
    return {"status": "alive"}

@router.get("/ready")
def readiness_check():
    return {"status": "ready"}