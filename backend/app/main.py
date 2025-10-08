from fastapi import FastAPI
from app.core.monitoring import setup_metrics
from app.core.middleware import loggingMiddle
from app.routers import auth,health,predict


app = FastAPI(
    title= "Advanced FastAPI Concept with ML", 
    version ="1.0.0",
    description="Advanced FastAPI ML backend with JWT, Redis, and Prometheus.")

app.add_middleware(loggingMiddle)


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(health.router, prefix="/health", tags=["Health"])


setup_metrics(app)

@app.get("/")
def root():
    return {"message": "Welcome to Advanced FastAPI Car Price Prediction API"}
