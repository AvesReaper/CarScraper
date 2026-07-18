from fastapi import FastAPI
from database import Base, engine
import models  
from api.router import router as car_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/health")
def health_status():
    return {"status" : "HEALTHY"}



app.include_router(car_router)