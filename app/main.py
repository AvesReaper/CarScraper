from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/health")
def health_status():
    return {"status" : "HEALTHY"}