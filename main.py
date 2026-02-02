from fastapi import FastAPI, Header, HTTPException
from typing import Optional, Dict, Any

app = FastAPI()

VALID_API_KEY = "my_secret_key_123"

@app.post("/honeypot")
def honeypot(
    payload: Dict[str, Any],
    x_api_key: Optional[str] = Header(None)
):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "active",
        "honeypot_ready": True,
        "message": "Honeypot endpoint is operational"
    }
