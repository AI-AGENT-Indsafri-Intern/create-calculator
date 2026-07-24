from pathlib import Path

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Starter App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")


class LoginRequest(BaseModel):
    id_token: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@api_router.post("/login")
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


# Register API routes FIRST
app.include_router(api_router)

# Mount the frontend LAST
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"

app.mount(
    "/",
    StaticFiles(directory=frontend_dir, html=True),
    name="frontend"
)