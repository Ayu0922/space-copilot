from config import CHUNK_SIZE, CHUNK_OVERLAP
import re


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP
) -> list[str]:

    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        if len(current_chunk.split()) + len(paragraph.split()) <= chunk_size:
            current_chunk += "\n\n" + paragraph if current_chunk else paragraph

        else:
            if current_chunk:
                chunks.append(current_chunk.strip())

            words = paragraph.split()

            while len(words) > chunk_size:

                chunk = " ".join(words[:chunk_size])

                chunks.append(chunk)

                words = words[chunk_size - overlap:]

            current_chunk = " ".join(words)

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks