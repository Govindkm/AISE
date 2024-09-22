from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routers import validation, privacy

load_dotenv()

app = FastAPI(
    title="AI Powered Adaptive Input Sanitization Engine (AISE)",
    description="Provides API endpoints for security checks on input fields using GPT models.",
    version="1.0.0"
)


app.include_router(validation.router, prefix="/api", tags=["Validation"])
app.include_router(privacy.router, prefix="/api", tags=["Privacy"])

@app.get("/")
def read_root():
    return {"message": "AI Powered Adaptive Input Sanitization Engine (AISE) is running."}

