# app/routers/privacy.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.langchain_service import LangChainService

router = APIRouter()

# Define request and response models
class PrivacyCheckRequest(BaseModel):
    input_text: str
    check_type: str  # "PII" or "sensitive_data"

class PrivacyCheckResponse(BaseModel):
    result: str
    message: str

# Create a LangChainService instance
langchain_service = LangChainService(model_type="openai")  # Or "huggingface"

@router.post("/check-privacy", response_model=PrivacyCheckResponse)
def check_privacy(request: PrivacyCheckRequest):
    result = langchain_service.check_privacy(request.input_text, request.check_type)
    
    return PrivacyCheckResponse(
        result=result,
        message="Privacy check completed"
    )
