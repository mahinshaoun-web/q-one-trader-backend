from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Q-One Trader API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # production-এ নির্দিষ্ট frontend domain দিন
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Q-One Trader Backend"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/pairs")
def pairs():
    return {
        "pairs": [
            "EURUSD",
            "GBPUSD",
            "USDJPY",
            "AUDUSD"
        ]
    }


@app.get("/api/market/status")
def market_status():
    return {
        "status": "available"
    }
