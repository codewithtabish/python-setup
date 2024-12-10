# Use a Python base image with a suitable version
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install pip dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the default command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "python_setup:app"]
