from fastapi import APIRouter, Body, HTTPException
from app.services import embedder
from pydantic import BaseModel

router = APIRouter()

class JobIn(BaseModel):
    title: str
    description: str

@router.post("/")
async def add_job(job: JobIn):
    vector = embedder.embed_text(job.description)
    job_id = embedder.add_job_vector(vector, job.description, metadata={"title": job.title, "description": job.description})
    return {"job_id": job_id}

@router.get("/{job_id}/rank")
def rank_resumes(job_id: str):
    try:
        results = embedder.rank_resumes_for_job(job_id)
        print(f"Ranking results for job {job_id}: {results}")
        return results
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))