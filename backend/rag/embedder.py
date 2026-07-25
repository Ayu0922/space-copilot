from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model

def embed_texts(texts: list[str]) -> list[list[float]]:
    model = get_model()
    return model.encode(texts, show_progress_bar=False).tolist()

def embed_query(query: str) -> list[float]:
    return embed_texts([query])[0]