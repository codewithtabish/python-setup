import os
from dotenv import load_dotenv
from flask import Flask
import redis
from rq import Queue
import logging
from flask_cors import CORS


# Load environment variables from a .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)

# General configurations
DB_URL = os.getenv("DB_URL")
DEBUG = os.getenv("DEBUG", "True") == "True"  # Default to True if not set
PORT = int(os.getenv("PORT", 9000))  # Default to port 9000 if not set
REDIS_URL = os.getenv("REDIS_URL")

# Check if the required environment variables are present
if not REDIS_URL:
    raise ValueError("REDIS_URL is required but not set in the .env file.")
if not DB_URL:
    raise ValueError("DB_URL is required but not set in the .env file.")

# Initialize Redis connection using the Redis URL
try:
    redis_client = redis.from_url(REDIS_URL)
    logging.info("Successfully connected to Redis.")
except redis.exceptions.ConnectionError as e:
    logging.error(f"Failed to connect to Redis: {str(e)}")
    raise

# Initialize RQ Queue using Redis
queue = Queue(connection=redis_client)

logging.info("RQ Queue initialized.")



