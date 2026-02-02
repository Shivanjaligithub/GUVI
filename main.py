from fastapi import FastAPI, Header, HTTPException, Request
from typing import Optional

app = FastAPI()

VALID_API_KEY = "my_secret_key_123"

@app.api_route("/honeypot", methods=["GET", "POST"])
async def honeypot(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Safely read body (even if empty or invalid)
    try:
        payload = await request.json()
    except:
        payload = None

    return {
        "status": "active",
        "honeypot_ready": True,
        "message": "Honeypot endpoint is operational",
        "received_payload": payload
    }

