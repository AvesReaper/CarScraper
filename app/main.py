from fastapi import FastAPI
from app.db.database import Base, engine
import app.db.models 
from app.api.router import router as car_router
from contextlib import asynccontextmanager

Base.metadata.create_all(bind=engine)



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/health")
def health_status():
    return {"status" : "HEALTHY"}



app.include_router(car_router)