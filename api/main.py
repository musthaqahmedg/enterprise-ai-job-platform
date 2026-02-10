from fastapi import FastAPI
from pydantic import BaseModel
from ai.skill_extractor import extract_skills

app = FastAPI(title="Enterprise AI Job Platform")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "API is running ✅"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: TextRequest):
    skills_found = extract_skills(req.text)

    return {
        "input_text": req.text,
        "skills_found": skills_found,
        "skills_count": len(skills_found)
    }
