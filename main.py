from fastapi import FastAPI, Header, HTTPException, Request
from typing import Optional

app = FastAPI()

VALID_API_KEY = "my_secret_key_123"


# Optional root endpoint (helps Render & browsers, GUVI doesn't care)
@app.get("/")
def root():
    return {"status": "service running"}


@app.api_route("/honeypot", methods=["GET", "POST"], include_in_schema=True)
async def honeypot(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    # API key validation
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Read body SAFELY (no validation, no 422)
    payload = None
    try:
        body_bytes = await request.body()
        if body_bytes:
            try:
                payload = await request.json()
            except:
                payload = body_bytes.decode(errors="ignore")
    except:
        payload = None

    return {
        "status": "active",
        "honeypot_ready": True,
        "message": "Honeypot endpoint is operational",
        "received_payload": payload
    }

