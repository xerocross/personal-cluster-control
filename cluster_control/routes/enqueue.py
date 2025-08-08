from flask import Blueprint, request, jsonify
from redis_client import r, QUEUE_NAME
from job_utils import enrich_job
import json

bp = Blueprint("enqueue", __name__)

@bp.route("/enqueue", methods=["POST"])
def enqueue():
    job = request.get_json()
    if not job or "job_type" not in job:
        return jsonify({"error": "Missing 'job_type'"}), 400

    job = enrich_job(job)
    r.rpush(QUEUE_NAME, json.dumps(job))
    return jsonify({"status": "queued", "id": job["id"]})
