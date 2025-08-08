from flask import Flask
from routes.enqueue import bp as enqueue_bp
from routes.view_queue import bp as view_queue_bp
from routes.control_worker import bp as control_worker_bp
import yaml

with open("config.yaml") as f:
    cfg = yaml.safe_load(f)

app = Flask(__name__)
app.register_blueprint(enqueue_bp)
app.register_blueprint(view_queue_bp)
app.register_blueprint(control_worker_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=cfg.get("http_port", 5042))
