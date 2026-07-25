from fastapi import FastAPI
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import chat, upload, news, documents
from db.postgres import init_db

app = FastAPI(title="Space Research Copilot", version="1.0.0")
BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "documents"

app.mount(
    "/documents",
    StaticFiles(directory=DOCUMENTS_DIR),
    name="documents"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(news.router, prefix="/api")
app.include_router(documents.router, prefix="/api")
@app.on_event("startup")
async def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "Space Research Copilot API is running"}