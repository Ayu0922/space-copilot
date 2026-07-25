import httpx
from config import NASA_API_KEY
from ingestion.chunker import chunk_text
from rag.embedder import embed_texts
from db.chroma_client import get_collection
import uuid

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_NEOWS_URL = "https://api.nasa.gov/neo/rest/v1/feed"

async def load_nasa_apod(count: int = 10):
    async with httpx.AsyncClient() as client:
        resp = await client.get(NASA_APOD_URL, params={
            "api_key": NASA_API_KEY,
            "count": count
        })
        resp.raise_for_status()
        items = resp.json()

    docs = []
    for item in items:
        text = f"Title: {item.get('title', '')}\nDate: {item.get('date', '')}\n{item.get('explanation', '')}"
        docs.append({"text": text, "source": f"NASA APOD - {item.get('title', '')}", "type": "nasa_apod"})

    return docs

def ingest_documents(docs: list[dict]):
    collection = get_collection()
    all_chunks = []
    all_ids = []
    all_embeddings = []
    all_metadatas = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            all_chunks.append(chunk)
            all_ids.append(str(uuid.uuid4()))
            all_metadatas.append({"source": doc["source"], "type": doc.get("type", "document")})

    if all_chunks:
        all_embeddings = embed_texts(all_chunks)
        collection.add(
            documents=all_chunks,
            embeddings=all_embeddings,
            ids=all_ids,
            metadatas=all_metadatas
        )

    return len(all_chunks)