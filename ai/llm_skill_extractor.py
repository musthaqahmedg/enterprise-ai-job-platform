import json
import os
from typing import List

from openai import OpenAI


def extract_skills_llm(resume_text: str) -> List[str]:
    """
    Extract skills from resume_text using an LLM.
    Returns a list of unique skills.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an AI that extracts professional skills from resume text.

Return ONLY valid JSON in this exact format:
{{
  "skills": ["Python", "FastAPI", "Docker"]
}}

Rules:
- skills must be short strings
- remove duplicates
- do not explain anything

Resume text:
{resume_text}
""".strip()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        input=prompt,
    )

    raw_text = response.output_text.strip()
    data = json.loads(raw_text)

    skills = data.get("skills", [])

    cleaned = []
    seen = set()
    for skill in skills:
        if isinstance(skill, str):
            s = skill.strip()
            if s and s.lower() not in seen:
                seen.add(s.lower())
                cleaned.append(s)

    return cleaned
