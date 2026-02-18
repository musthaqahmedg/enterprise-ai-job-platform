from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(text1: str, text2: str) -> float:
    """
    Compute cosine similarity between two text inputs using embeddings.
    Returns a similarity score between 0 and 1.
    """

    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)
