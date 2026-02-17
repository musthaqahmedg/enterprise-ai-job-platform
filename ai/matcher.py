from typing import List
from ai.normalizer import normalize_skills


def calculate_match_score(resume_skills: List[str], job_skills: List[str]) -> dict:

    # Normalize skills before matching
    resume_skills = normalize_skills(resume_skills)
    job_skills = normalize_skills(job_skills)

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)

    if not job_set:
        score = 0.0
    else:
        score = len(matched) / len(job_set)

    return {
        "matched_skills": list(matched),
        "match_score": round(score, 2)
    }
