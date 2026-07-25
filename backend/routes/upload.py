from fastapi import APIRouter, UploadFile, File, HTTPException
from ingestion.pdf_parser import extract_pages_from_pdf
from ingestion.chunker import chunk_text
from rag.embedder import embed_texts
from db.chroma_client import get_collection
import uuid

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are accepted"
        )

    # Read file
    file_bytes = await file.read()

    # Validate size (20 MB max)
    if len(file_bytes) > 20 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File too large. Max 20MB."
        )

    # Extract pages
    pages = extract_pages_from_pdf(file_bytes)

    if not pages:
        raise HTTPException(
            status_code=400,
            detail="Could not extract meaningful text from this PDF"
        )

    all_chunks = []
    all_metadata = []

    # Chunk page by page so page numbers are preserved
    for page in pages:
        page_chunks = chunk_text(page["text"])

        for chunk in page_chunks:
            all_chunks.append(chunk)

            all_metadata.append({
                "source": file.filename,
                "page": page["page"],
                "type": "research_paper"
            })

    if not all_chunks:
        raise HTTPException(
            status_code=400,
            detail="No valid text chunks generated from PDF"
        )

    # Generate embeddings
    embeddings = embed_texts(all_chunks)

    # Store in ChromaDB
    collection = get_collection()

    ids = [str(uuid.uuid4()) for _ in all_chunks]

    collection.add(
        documents=all_chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=all_metadata
    )

    return {
        "message": f"Successfully ingested {file.filename}",
        "chunks_stored": len(all_chunks),
        "pages_processed": len(pages),
        "filename": file.filename
    }