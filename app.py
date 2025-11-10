from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def home():
    count = r.incr('visitor_count')
    return f"<h1>Welcome to Dockerized Flask App!</h1><p>Visitor count: {count}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

