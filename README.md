# ATS-AI

An AI-powered Applicant Tracking System (ATS) that parses, embeds, stores, and ranks resumes using NLP and vector search.

<img width="1480" height="685" alt="image" src="https://github.com/user-attachments/assets/2b5e91e3-0f75-4f4f-b251-26202fb9b3b5" />

## Features

- **Resume Parsing:** Extracts name, skills, and summary from uploaded resumes (PDF/DOCX).
- **Embedding:** Uses Sentence Transformers to embed resume summaries and job descriptions.
- **Vector Store:** Stores embeddings and metadata in a persistent ChromaDB vector store.
- **Resume Ranking:** Ranks resumes for a given job description using vector similarity.
- **Frontend:** Vue 3 + PrimeVue UI for uploading, ranking, and browsing resumes and jobs.
- **Metadata Listing:** List all resumes and their metadata.
- **Clear Functionality:** Clear rankings and navigate back to the index page from the frontend.

## Tech Stack

- Python 3.11+
- FastAPI
- spaCy (`en_core_web_sm`)
- pdfplumber
- python-docx
- sentence-transformers
- chromadb
- Vue 3 + PrimeVue

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ats-ai
   ```

2. **Build and run the backend with Docker:**
   ```bash
   cd backend
   docker build -t ats-ai-backend .
   docker run -p 8000:8000 ats-ai-backend
   ```

3. **Run the frontend:**
   Open a new terminal and run:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

   - Access the UI at [http://localhost:5173](http://localhost:5173) (or the port shown in your terminal).

4. **Data Storage:**
   - Vector store data is saved in `/data/vector_store/` (excluded from git).

## API Usage Examples

### Upload a Resume

```bash
curl -X POST "http://127.0.0.1:8000/resumes/" \
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

### List All Resumes

```bash
curl "http://127.0.0.1:8000/resumes/"
```

## API Overview

- **Upload Resume:**  
  `POST /resumes/`  
  Upload a PDF or DOCX resume, extract metadata, and store embedding.

- **List Resumes:**  
  `GET /resumes/`  
  List all stored resumes and their metadata.

- **Add Job Description:**  
  `POST /jobs/`  
  Add a job description and store its embedding.

- **Rank Resumes:**  
  `GET /jobs/{job_id}/rank`  
  Retrieve top matching resumes for a job (returns full metadata for each match).


## Notes

- Only PDF and DOCX resumes are supported.
- Make sure `/data/` is writable and not tracked by git.
- All vector data is stored in a single ChromaDB collection.
- If you see `ModuleNotFoundError: No module named 'app'`, ensure you run `uvicorn` from the project root.
- If you see font loading errors in the frontend, ensure `primeicons` is installed and imported as described in the frontend setup.

## License

MIT License



