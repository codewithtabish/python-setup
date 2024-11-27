# Use Python 3.10 alpine image for lightweight container
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (including Postgres client libraries and others if needed)
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    && rm -rf /var/cache/apk/*

# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 9000

# Run the Flask application
CMD ["python", "app.py"]
