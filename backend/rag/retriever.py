from db.chroma_client import get_collection
from rag.embedder import embed_query
from config import TOP_K_RESULTS

def retrieve(query: str, top_k: int = TOP_K_RESULTS) -> list[dict]:
    collection = get_collection()

    if collection.count() == 0:
        return []

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    chunks = []
    for i, doc in enumerate(results["documents"][0]):
        chunks.append({
            "text": doc,
            "metadata": results["metadatas"][0][i],
            "score": 1 - results["distances"][0][i]
        })

    return chunks