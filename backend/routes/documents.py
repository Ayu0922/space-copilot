from fastapi import APIRouter
from pathlib import Path
import fitz  # PyMuPDF

router = APIRouter()

DOCUMENTS_FOLDER = Path("../documents")


@router.get("/documents")
def get_documents():

    docs = []

    if DOCUMENTS_FOLDER.exists():

        for pdf in DOCUMENTS_FOLDER.glob("*.pdf"):

            try:

                document = fitz.open(pdf)

                pages = len(document)

                document.close()

            except:

                pages = 0

            docs.append({

                "name": pdf.stem,

                "filename": pdf.name,

                "pages": pages

            })

    return {

        "documents": docs

    }