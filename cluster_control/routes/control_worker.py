from flask import Blueprint, request, jsonify
from redis_client import r

bp = Blueprint("control", __name__)

CHANNEL_NAME = "worker-control"

@bp.route('/control', methods=['POST'])
def control_worker():
    data = request.get_json()
    node = data.get("node")
    action = data.get("action")  # should be "pause" or "resume"

    if node is None or action not in ("pause", "resume"):
        return jsonify({"error": "Invalid input"}), 400

    message = {
        "node": node,
        "action": action
    }
    control_channel = f"{CHANNEL_NAME}:{node}"
    r.publish(control_channel, str(message))
    return jsonify({"status": "ok", "message": message}), 200
