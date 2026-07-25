# 🚀 Space Copilot
### AI Powered Mission Intelligence Platform for ISRO Documents

Space Copilot is a Retrieval Augmented Generation (RAG) based AI assistant that enables users to interact with ISRO mission documents using natural language. It combines semantic search, vector embeddings, large language models, and session memory to provide accurate, context aware answers from uploaded technical documents.

---

## Project Overview

Space Copilot allows engineers, researchers, and students to query ISRO mission documentation as if they were conversing with an expert assistant.

Instead of manually searching through hundreds of pages, users can simply ask questions such as:

- How does PSLV work?
- Explain the objectives of Aditya L1.
- Compare LVM3 and PSLV.
- Which document discusses cryogenic engines?

The assistant retrieves the most relevant document chunks from a vector database and generates an accurate response using Groq LLM.

---

## Features

### AI Mission Assistant

- Natural language question answering
- Context aware conversations
- Multi turn chat support
- Session memory using unique session IDs

### Retrieval Augmented Generation (RAG)

- Semantic document retrieval
- Vector similarity search
- Context injection before generation
- Source citation support

### Document Management

- Upload PDF mission documents
- Automatic document parsing
- Document indexing
- Download and preview PDFs

### News Module

- Latest ISRO space news
- Dynamic news cards
- External article links

### Dashboard

- Indexed document statistics
- Mission coverage
- Knowledge base status
- AI engine information

---

## Supported Mission Documents

- Aditya L1
- Chandrayaan 3
- PSLV
- LVM3
- Gaganyaan
- Mars Orbiter Mission

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

### Backend

- FastAPI
- Python

### AI Stack

- Groq LLM
- Sentence Transformers
- ChromaDB
- Retrieval Augmented Generation (RAG)

### Database

- PostgreSQL
- ChromaDB Vector Database

### PDF Processing

- PyMuPDF
- LangChain Text Splitter

---

## Project Architecture

```
                 User
                   │
                   ▼
             Frontend (HTML/CSS/JS)
                   │
                   ▼
              FastAPI Backend
                   │
      ┌────────────┼─────────────┐
      │            │             │
      ▼            ▼             ▼
 PDF Parser    ChromaDB      PostgreSQL
      │            │
      └──────► Embeddings
                   │
                   ▼
             Relevant Chunks
                   │
                   ▼
               Groq LLM
                   │
                   ▼
              Final Response
```

---

## Folder Structure

```
space-copilot/

│
├── backend/
│   ├── ingestion/
│   ├── rag/
│   ├── routes/
│   ├── db/
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── assets/
│   │    └── images/
│   ├── css/
│   ├── js/
│   ├── index.html
│   ├── upload.html
│   ├── documents.html
│   └── news.html
│
├── documents/
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/space-copilot.git

cd space-copilot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside the backend directory.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

DATABASE_URL=YOUR_POSTGRES_CONNECTION_STRING
```

---

### Run Backend

```bash
cd backend

python -m uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

### Open Frontend

Simply open

```
frontend/index.html
```

or serve using

```bash
python -m http.server
```

---

## API Endpoints

### Chat

```
POST /api/chat
```

Ask questions from uploaded mission documents.

---

### Upload

```
POST /api/upload
```

Upload PDF documents.

---

### Documents

```
GET /api/documents
```

Returns indexed document information.

---

### News

```
GET /api/news
```

Returns latest ISRO related news.

---

## Sample Questions

```
Explain the objectives of Chandrayaan-3.

How does PSLV work?

Compare PSLV and LVM3.

Summarize Aditya L1 mission.

Which document discusses cryogenic engines?

Describe the launch sequence of PSLV.

Explain Mars Orbiter Mission.

What are the objectives of Gaganyaan?
```

---

## Key Features Demonstrated

- Retrieval Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Context Aware AI
- Session Memory
- Source Attribution
- PDF Processing
- FastAPI REST APIs
- Responsive User Interface

---

## Future Enhancements

- Voice Assistant
- OCR Support
- Multilingual Queries
- Image Based Question Answering
- Mission Timeline Visualization
- Authentication
- User Profiles
- Cloud Deployment
- Document Annotation
- Advanced Analytics Dashboard

---

## Developed By

**Space Copilot Team**

AI Powered Mission Intelligence Platform

Built using FastAPI, ChromaDB, Sentence Transformers, Groq LLM, and Retrieval Augmented Generation (RAG).

---

## License

This project is developed for educational and research purposes.
../venv\Scripts\activate
python -m uvicorn main:app --reload
