from fastapi import FastAPI, Header, HTTPException, Request
from typing import Optional

app = FastAPI()

VALID_API_KEY = "my_secret_key_123"

@app.get("/")
def health():
    return {"status": "alive"}

@app.post("/honeypot")
async def honeypot(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "active",
        "honeypot_ready": True,
        "message": "Honeypot endpoint is operational"
    }

