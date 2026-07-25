from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Any
import uuid

from rag.retriever import retrieve
from rag.generator import generate_answer
from db.postgres import get_db, save_message, get_history
from config import GROQ_API_KEY
router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    session_id: str
    sources: list[dict[str, Any]]


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    session_id = request.session_id or str(uuid.uuid4())

    # Load previous conversation
    history_rows = get_history(db, session_id)
    history = [
        {
            "role": row.role,
            "content": row.content
        }
        for row in history_rows
    ]

    # Retrieve relevant chunks
    context_chunks = retrieve(request.query)

    # Generate answer
    answer = generate_answer(
        request.query,
        context_chunks,
        history
    )

    # Save conversation
    save_message(db, session_id, "user", request.query)
    save_message(db, session_id, "assistant", answer)

    # Build source list
    sources = []

    for chunk in context_chunks:
        metadata = chunk.get("metadata", {})

        sources.append(
            {
                "document": metadata.get("source", "Unknown"),
                "page": metadata.get("page", "?"),
                "score": round(chunk.get("score", 0), 3)
            }
        )

    return ChatResponse(
        answer=answer,
        session_id=session_id,
        sources=sources
    )

print("Groq key loaded:", bool(GROQ_API_KEY))
print("Groq key starts with:", GROQ_API_KEY[:8] if GROQ_API_KEY else "EMPTY")