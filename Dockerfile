# Start from a Python base image
FROM python:3.9-slim

# Update and install system packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create directory for the app
WORKDIR /opt/app

# Install Python dependencies
RUN pip3 install virtualenv
RUN virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -U pip

# Copy the application code
COPY . .

# Install the application in editable mode
RUN . venv/bin/activate && \
    pip install --no-cache-dir -e .

# Set the entry point
ENTRYPOINT ["python3", "hello_world.py"]
