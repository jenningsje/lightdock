# Start from a Python base image
FROM python:3.9-slim

# Update and install system packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs

# Create directory for the app
WORKDIR /opt/app

# Copy the application code from lightdock directory
COPY lightdock/. .

# Install Python dependencies
RUN pip3 install virtualenv
RUN virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -U pip

# Install the application dependencies in editable mode
RUN . venv/bin/activate && \
    pip install --no-cache-dir -e . && \
    pip install gemmi && \
    pip install requests && \
    pip install pandas

# Set the entry point
ENTRYPOINT ["python3", "./hello_world.py"]