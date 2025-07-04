from fastapi import FastAPI

app = FastAPI(title="TradeSense API")

@app.get("/health")
def health_check():
    return {"status": "ok"}