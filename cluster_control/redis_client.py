import redis
import yaml

with open("config.yaml") as f:
    cfg = yaml.safe_load(f)

r = redis.Redis(host=cfg["redis_host"], port=cfg["redis_port"], db=0)
QUEUE_NAME = cfg.get("redis_queue", "tasks")
