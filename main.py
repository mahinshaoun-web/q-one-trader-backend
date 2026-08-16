from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Q-One Trader backend is running"
    }

@app.get("/status")
def status():
    return {
        "connected": True,
        "mode": "demo"
    }
