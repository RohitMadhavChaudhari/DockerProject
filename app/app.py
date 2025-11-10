from flask import Flask, render_template_string
from redis import Redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis = Redis(host=redis_host, port=6379)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Visitor Counter</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #007bff, #00c6ff);
            color: white;
            text-align: center;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .counter {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px 40px;
            border-radius: 15px;
            font-size: 3em;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.9em;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <h1>🌐 Welcome to My Dockerized Flask App!</h1>
    <div class="counter">
        👁️ Visitor Count: {{ count }}
    </div>
    <footer>Powered by Flask 🐍 + Redis 🟥 + Docker 🐳</footer>
</body>
</html>
"""

@app.route('/')
def home():
    count = redis.incr('visits')
    return render_template_string(HTML_TEMPLATE, count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

