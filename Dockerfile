# Specify the platform to ensure amd64 compatibility
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy application code and dependencies
COPY app /app

# Install dependencies
RUN pip install --no-cache-dir pymupdf

# Create input and output directories inside container
RUN mkdir -p /app/input /app/output

# Set entrypoint to run the processing script automatically
ENTRYPOINT ["python", "main.py"]
