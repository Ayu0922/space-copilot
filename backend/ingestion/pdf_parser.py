import fitz
import re


def clean_text(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\x00", "", text)
    return text.strip()


def extract_pages_from_pdf(file_bytes: bytes) -> list[dict]:
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    pages = []

    for page_number, page in enumerate(doc, start=1):
        text = clean_text(page.get_text("text"))

        if len(text) > 50:
            pages.append({
                "page": page_number,
                "text": text
            })

    doc.close()

    return pages