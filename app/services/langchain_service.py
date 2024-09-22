# app/services/langchain_service.py

from langchain.llms.openai import OpenAI
from langchain.llms.huggingface_hub import HuggingFaceHub
import os

class LangChainService:
    def __init__(self, model_type='openai'):
        if model_type == 'openai':
            self.model = OpenAI(model_name="text-davinci-003", api_key=os.getenv("OPENAI_API_KEY"))
        elif model_type == 'huggingface':
            self.model = HuggingFaceHub(repo_id="gpt2", model_kwargs={"temperature": 0.7})
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
    
    def validate_input(self, input_text: str, validation_type: str):
        prompt = self._generate_prompt(input_text, validation_type)
        response = self.model(prompt)
        return response['choices'][0]['text'] if 'choices' in response else response

    def _generate_prompt(self, input_text: str, validation_type: str) -> str:
        prompts = {
            "xss": f"Check the following input for XSS vulnerabilities: {input_text}",
            "csrf": f"Check the following input for CSRF vulnerabilities: {input_text}",
            "sqli": f"Check the following input for SQL Injection vulnerabilities: {input_text}",
        }
        return prompts.get(validation_type, f"Analyze this input for general security risks: {input_text}")

    def check_privacy(self, input_text: str, check_type: str):
        if check_type == "PII":
            prompt = f"Does the following text contain any Personally Identifiable Information (PII)? {input_text}"
        elif check_type == "sensitive_data":
            prompt = f"Does the following text contain sensitive company information? {input_text}"
        else:
            prompt = f"Analyze this text for any privacy-related risks: {input_text}"
        
        response = self.model(prompt)
        return response['choices'][0]['text'] if 'choices' in response else response
