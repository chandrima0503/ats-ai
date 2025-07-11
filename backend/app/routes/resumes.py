from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import parser, embedder

router = APIRouter()

@router.post("/")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX accepted")

    text = await parser.extract_text(file)
    meta = parser.extract_metadata(text)
    vector = embedder.embed_text(text)

    resume_id = embedder.add_to_vector_store(vector, meta)
    return {"resume_id": resume_id, "metadata": meta}