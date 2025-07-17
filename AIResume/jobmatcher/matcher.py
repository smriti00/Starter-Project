# matcher.py

from sentence_transformers import SentenceTransformer, util
import torch

# Load model once at startup (recommended: all-MiniLM-L6-v2 for speed + quality)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, job_description):
    try:
        # Encode both inputs
        embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
        return float(similarity_score)
    except Exception as e:
        print(f"Error in similarity calculation: {e}")
        return 0.0

def rank_resumes(resumes, job_description):
    """
    resumes: list of {'name': ..., 'text': ...}
    job_description: string
    returns: list sorted by similarity
    """
    ranked = []
    for res in resumes:
        score = calculate_similarity(res['text'], job_description)
        ranked.append({**res, 'score': round(score, 4)})
    
    # Sort by score descending
    return sorted(ranked, key=lambda x: x['score'], reverse=True)

