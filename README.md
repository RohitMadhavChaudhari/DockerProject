🐳 Flask + Redis Visitor Counter (Docker Project)
📖 Overview

This is a simple Python Flask web application that uses Redis as a backend to count and display the number of visitors.
Both services run inside Docker containers, managed with Docker Compose — a great example of a multi-container setup for beginners learning DevOps and containerization.

🏗️ Project Architecture
+-----------------+         +----------------+
|  Flask Web App  | <-----> |     Redis DB   |
| (Python + Flask)|         |  (Key-Value DB)|
+-----------------+         +----------------+
         ↑
   Managed via Docker Compose

⚙️ Technologies Used

Python 3

Flask (Web Framework)

Redis (In-memory Database)

Docker (Containerization)

Docker Compose (Orchestration)

📂 Project Structure
dockerProject/
│
├── app/
│   ├── app.py                # Flask application
│   ├── Dockerfile            # Builds custom Flask image
│   ├── requirements.txt      # Python dependencies
│   └── docker-compose.yml    # Multi-container configuration

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/flask-redis-docker.git
cd flask-redis-docker

2️⃣ Build and Run Containers
docker compose up -d

3️⃣ Access the Application

Open your browser and go to 👉 http://localhost:5000

You’ll see the visitor count increase every time you refresh the page!

🧩 How It Works

The Flask app connects to Redis using an environment variable (REDIS_HOST).

Every time a user visits the page, the Flask app:

Increments the visitor counter stored in Redis

Fetches and displays the updated count

Both services are networked via Docker Compose.

🧠 Key Learnings

Building custom Docker images for applications

Managing multiple containers with Docker Compose

Setting up inter-container networking

Using environment variables and persistent volumes

📸 Project Demo

(You can add your LinkedIn image or screenshot here)

🏁 Future Enhancements

Add Nginx as a reverse proxy

Add persistent Redis data storage

Deploy to AWS using ECS or EC2

🙌 Author

Made with ❤️ while learning Docker and DevOps concepts.
