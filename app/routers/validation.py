# app/routers/validation.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.langchain_service import LangChainService

router = APIRouter()

# Define request and response models
class ValidationRequest(BaseModel):
    input_text: str
    validation_type: List[str]

class ValidationResponse(BaseModel):
    validation_result: dict
    message: str

# Create a LangChainService instance
langchain_service = LangChainService(model_type="openai")  # Or "huggingface"

@router.post("/validate-input", response_model=ValidationResponse)
def validate_input(request: ValidationRequest):
    validation_result = {}
    for v_type in request.validation_type:
        validation_result[v_type] = langchain_service.validate_input(request.input_text, v_type)
    
    return ValidationResponse(
        validation_result=validation_result,
        message="Validation completed"
    )
