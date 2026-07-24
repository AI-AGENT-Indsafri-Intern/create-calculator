from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="Starter App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginRequest(BaseModel):
    id_token: str


@app.get("/", response_class=HTMLResponse)
async def home():
    html_path = Path(__file__).resolve().parent.parent / "FrontEnd" / "index.html"
    return html_path.read_text(encoding="utf-8")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/login")
async def login(payload: LoginRequest):
    if not payload.id_token:
        raise HTTPException(
            status_code=400,
            detail="Google ID token is required"
        )

    return {
        "message": "Login successful",
        "authenticated": True
    }