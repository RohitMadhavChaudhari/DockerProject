# Use official Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy all source code into the working directory
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

