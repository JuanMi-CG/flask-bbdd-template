# Dockerfile for Flask Backend
FROM python:3.10-slim

WORKDIR /app

# Install system tools, including netcat-openbsd
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-openbsd \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set the entrypoint script
CMD ["python", "run.py"]
