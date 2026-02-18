import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi import UploadFile, File
from pypdf import PdfReader
from ai.skill_extractor import extract_skills
from ai.llm_skill_extractor import extract_skills_llm
from ai.pdf_parser import extract_text_from_pdf
from typing import List
from pydantic import BaseModel
from ai.matcher import calculate_match_score


app = FastAPI(
    title="Enterprise AI Job Platform",
    description=(
        "AI-powered backend service for extracting structured skills from "
        "unstructured resume text. Supports rule-based and LLM-based extraction "
        "with safe production fallback."
    ),
    version="1.1.0"
)

# ------------------------
# Request Models
# ------------------------

class TextRequest(BaseModel):
    text: str


class MatchRequest(BaseModel):
    resume_text: str
    job_description_text: str


class MatchV2Request(BaseModel):
    resume_text: str
    required_skills: list[str]
    optional_skills: list[str] = []

class MatchRequest(BaseModel):
    resume_skills: List[str]
    job_skills: List[str]




# ------------------------
# Basic Routes
# ------------------------

@app.get("/")
def root():
    return {"message": "API is running ✅"}


@app.get("/health")
def health():
    return {"status": "ok"}


# ------------------------
# Text Skill Extraction
# ------------------------

@app.post("/predict")
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


# ------------------------
# PDF Skill Extraction
# ------------------------

@app.post("/predict-pdf")
async def predict_pdf(file: UploadFile = File(...)):

    try:
        # ✅ Use file.file (NOT file.read())
        reader = PdfReader(file.file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text.lower()

        skills_list = [
            "python", "machine learning", "deep learning",
            "nlp", "llm", "rag", "aws", "azure",
            "pandas", "numpy", "scikit-learn"
        ]

        skills_found = []

        for skill in skills_list:
            if skill in text:
                skills_found.append(skill)

        return {
            "skills_found": skills_found,
            "skills_count": len(skills_found),
            "extraction_source": "pdf_rule_based"
        }

    except Exception as e:
        return {"error": str(e)}

# ------------------------
# Basic Match (V1)
# ------------------------

@app.post("/match")
def match(req: MatchRequest):

    result = calculate_match_score(
        resume_skills=req.resume_skills,
        job_skills=req.job_skills
    )

    return result





# ------------------------
# Advanced Match (V2 - Weighted)
# ------------------------

@app.post("/match-v2")
def match_v2(req: MatchV2Request):

    resume_skills = extract_skills(req.resume_text)

    required = set([skill.lower() for skill in req.required_skills])
    optional = set([skill.lower() for skill in req.optional_skills])
    resume_set = set(resume_skills)

    matched_required = required.intersection(resume_set)
    matched_optional = optional.intersection(resume_set)

    required_score = (
        len(matched_required) / len(required)
        if len(required) > 0 else 0
    )

    optional_score = (
        len(matched_optional) / len(optional)
        if len(optional) > 0 else 0
    )

    final_score = round((required_score * 0.7) + (optional_score * 0.3), 2)

    return {
        "resume_skills": resume_skills,
        "matched_required_skills": list(matched_required),
        "matched_optional_skills": list(matched_optional),
        "missing_required_skills": list(required - resume_set),
        "final_match_score": final_score
    }
