from flask import Blueprint, render_template_string
from redis_client import r, QUEUE_NAME
import json

bp = Blueprint("view_queue", __name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Queue Viewer</title>
  <style>
    body { font-family: sans-serif; padding: 1em; }
    pre { background: #f0f0f0; padding: 1em; }
  </style>
</head>
<body>
  <h1>Current Task Queue</h1>
  <ul>
    {% for job in jobs %}
      <li><pre>{{ job | tojson(indent=2) }}</pre></li>
    {% endfor %}
  </ul>
</body>
</html>
"""

@bp.route("/queue")
def view_queue():
    jobs = [json.loads(j) for j in r.lrange(QUEUE_NAME, 0, -1)]
    return render_template_string(TEMPLATE, jobs=jobs)
