import os
from fastapi import FastAPI
from pydantic import BaseModel

from ai.skill_extractor import extract_skills
from ai.llm_skill_extractor import extract_skills_llm


app = FastAPI(
    title="Enterprise AI Job Platform",
    description=(
        "AI-powered backend service for extracting structured skills from "
        "unstructured resume text. Supports rule-based and LLM-based extraction "
        "with safe production fallback."
    ),
    version="1.0.0"
)


# ----------- Request Model -----------

class TextRequest(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": (
                    "Software Engineer with experience in Python, FastAPI, "
                    "Docker, AWS, and REST API development."
                )
            }
        }


# ----------- Response Model -----------

class PredictionResponse(BaseModel):
    input_text: str
    skills_found: list[str]
    skills_count: int
    extraction_source: str


# ----------- Routes -----------

@app.get("/")
def root():
    return {"message": "API is running ✅"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Extract skills from resume text",
    description=(
        "Extracts structured professional skills from unstructured resume text. "
        "Uses LLM-based extraction if enabled, otherwise falls back to rule-based logic."
    ),
)
def predict(req: TextRequest):
    use_llm = os.getenv("USE_LLM", "false").lower() == "true"

    if use_llm:
        try:
            skills_found = extract_skills_llm(req.text)
            source = "llm"
        except Exception:
            skills_found = extract_skills(req.text)
            source = "rule_based_fallback"
    else:
        skills_found = extract_skills(req.text)
        source = "rule_based"

    return {
        "input_text": req.text,
        "skills_found": skills_found,
        "skills_count": len(skills_found),
        "extraction_source": source,
    }
