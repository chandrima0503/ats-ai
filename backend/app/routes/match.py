from fastapi import APIRouter, Query
from app.services import embedder, gpt

router = APIRouter()

@router.get("/")
async def match(job_id: str = Query(...)):
    results = embedder.rank_resumes_for_job(job_id)
    return results

@router.get("/chat")
async def chat(resume_id: str, question: str):
    answer = gpt.resume_chat(resume_id, question)
    return {"answer": answer}