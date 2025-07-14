# ATS-AI

An AI-powered Applicant Tracking System (ATS) backend that parses, embeds, and ranks resumes using NLP and vector search.

## Features

- **Resume Parsing:** Extracts name, skills, and summary from uploaded resumes (PDF).
- **Embedding:** Uses Sentence Transformers to embed resume summaries and job descriptions.
- **Vector Store:** Stores embeddings and metadata in a persistent ChromaDB vector store.
- **Resume Ranking:** Ranks resumes for a given job description using vector similarity.

## Tech Stack

- Python 3.11+
- FastAPI
- spaCy (`en_core_web_sm`)
- pdfplumber
- sentence-transformers
- chromadb

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ats-ai
   ```

2. **Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. **Run the backend:**
   ```bash
   uvicorn backend.app.main:app --reload
   ```

4. **Data Storage:**
   - Vector store data is saved in `/data/vector_store/` (excluded from git).

## API Usage Examples

### Upload a Resume

```bash
curl -X POST "http://127.0.0.1:8000/resumes/upload" \
  -F "file=@/path/to/your_resume.pdf"
```

### Add a Job Description

```bash
curl -X POST "http://127.0.0.1:8000/jobs/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Software Developer", "description": "Looking for an experienced Software Developer with experience of Python and Javascript."}'
```

### Rank Resumes for a Job

```bash
curl "http://127.0.0.1:8000/jobs/<job_id>/rank"
```
Replace `<job_id>` with the ID returned from the previous job creation step.

## API Overview

- **Upload Resume:**  
  `POST /resumes/upload`  
  Upload a PDF resume, extract metadata, and store embedding.

- **Add Job Description:**  
  `POST /jobs/`  
  Add a job description and store its embedding.

- **Rank Resumes:**  
  `GET /jobs/{job_id}/rank`  
  Retrieve top matching resumes for a job.

## Notes

- Only PDF resumes are supported.
- Make sure `/data/` is writable and not tracked by git.
- All vector data is stored in a single ChromaDB collection.

## License

MIT License

<img width="1480" height="685" alt="image" src="https://github.com/user-attachments/assets/2b5e91e3-0f75-4f4f-b251-26202fb9b3b5" />

