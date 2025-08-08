import uuid
from datetime import datetime

def enrich_job(job):
    job["id"] = str(uuid.uuid4())
    job["submitted_at"] = datetime.utcnow().isoformat() + "Z"
    job["status"] = "queued"
    return job
