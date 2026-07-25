import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./space_copilot.db")
CHROMA_PATH = os.getenv("CHROMA_PATH", "../data/chroma_store")
COLLECTION_NAME = "space_docs"
EMBED_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 5