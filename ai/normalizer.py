def normalize_skills(skills: list[str]) -> list[str]:
    """
    Normalize skill names:
    - Lowercase
    - Remove extra spaces
    - Remove duplicates
    """
    normalized = set()

    for skill in skills:
        cleaned = skill.strip().lower()
        normalized.add(cleaned)

    return list(normalized)
