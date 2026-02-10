import re
from typing import List

# Canonical skill dictionary (industry-focused, expandable)
SKILL_KEYWORDS = [
    "python", "java", "sql", "pyspark", "spark", "docker", "kubernetes",
    "aws", "azure", "gcp", "fastapi", "flask",
    "machine learning", "deep learning", "nlp", "computer vision",
    "llm", "transformers", "rag", "faiss",
    "pandas", "numpy", "scikit-learn",
    "airflow", "mlops", "ci/cd"
]

def extract_skills(text: str) -> List[str]:
    """
    Extract technical skills from free-form text.
    This function is API-safe, Docker-safe, and LLM-upgradable.
    """
    if not text:
        return []

    text = text.lower()

    found_skills = set()

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)
