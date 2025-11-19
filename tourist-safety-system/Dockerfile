# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONPATH=/app/backend

# Expose port
EXPOSE 5000

# Change to backend directory and run the application via Gunicorn for production
WORKDIR /app/backend

# Default command using gunicorn directly (simpler approach)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "1", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-"]