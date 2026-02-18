from ai.semantic_matcher import compute_semantic_similarity

from typing import List
from ai.normalizer import normalize_skills


def calculate_match_score(resume_skills: List[str],
                          job_skills: List[str]) -> dict:

    # Normalize skills
    resume_skills = normalize_skills(resume_skills)
    job_skills = normalize_skills(job_skills)

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)

    # ---------- Rule-based score ----------
    if not job_set:
        rule_score = 0.0
    else:
        rule_score = len(matched) / len(job_set)

    # ---------- Semantic score ----------
    resume_text = " ".join(resume_skills)
    job_text = " ".join(job_skills)

    semantic_score = compute_semantic_similarity(resume_text, job_text)

    # ---------- Hybrid score ----------
    final_score = (0.6 * rule_score) + (0.4 * semantic_score)

    return {
        "matched_skills": list(matched),
        "rule_score": round(rule_score, 3),
        "semantic_score": round(semantic_score, 3),
        "final_score": round(final_score, 3)
    }

