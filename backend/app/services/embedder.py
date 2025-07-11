import chromadb
from sentence_transformers import SentenceTransformer
import uuid

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data" / "vector_store"

chroma_client = chromadb.PersistentClient(path=str(DATA_DIR))

collection = chroma_client.get_or_create_collection("resumes")
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str):
    return model.encode([text])[0].tolist()

def _sanitize_metadata(metadata):
    sanitized = {}
    for k, v in metadata.items():
        if isinstance(v, list):
            sanitized[k] = ", ".join(str(item) for item in v)
        else:
            sanitized[k] = v
    return sanitized

def add_to_vector_store(vector, metadata):
    resume_id = str(uuid.uuid4())
    sanitized_metadata = _sanitize_metadata(metadata)
    collection.add(
        documents=[sanitized_metadata["summary"]],
        embeddings=[vector],
        ids=[resume_id],
        metadatas=[sanitized_metadata]
    )
    return resume_id

def add_job_vector(vector, description, metadata=None):
    job_id = str(uuid.uuid4())
    meta = metadata if metadata else {"type": "job"}
    collection.add(
        documents=[description],
        embeddings=[vector],
        ids=[job_id],
        metadatas=[meta]
    )
    # Debug: print what was just added
    print(f"Added job with id {job_id}, meta: {meta}")
    print("Get after add:", collection.get(ids=[job_id], include=["embeddings", "documents", "metadatas"]))
    print("All IDs in collection:", collection.get()["ids"])
    return job_id

def rank_resumes_for_job(job_id):
    job_doc = collection.get(ids=[job_id], include=["embeddings", "documents", "metadatas"])
    if (
        not job_doc
        or "embeddings" not in job_doc
        or job_doc["embeddings"] is None
        or len(job_doc["embeddings"]) == 0
    ):
        raise ValueError(f"Job with id {job_id} not found in vector store.")
    job_vector = job_doc["embeddings"][0]
    results = collection.query(query_embeddings=[job_vector], n_results=5)
    return results