# Ensure AMD64 compatibility
FROM --platform=linux/amd64 python:3.10-slim

# Avoid buffering issues with print statements
ENV PYTHONUNBUFFERED=1

# Work in /app
WORKDIR /app

# Copy requirements first (for caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app contents
COPY app/ /app/

# Create input/output dirs if missing
RUN mkdir -p input output

# Run your script
CMD ["python", "main.py"]
