from fastapi import FastAPI
from app.database import engine
from app import models

app = FastAPI(
    title="Fitness Tracker API",
    description="API for tracking users, exercises and workouts",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Fitness Tracker API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "details": str(e)}
    
models.Base.metadata.create_all(bind=engine)
