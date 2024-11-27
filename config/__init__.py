import os
from dotenv import load_dotenv
from flask_mail import Mail
from flask import Flask
import redis

# Load environment variables from a .env file
load_dotenv()


app = Flask(__name__)




# General configurations
DB_URL = os.getenv("DB_URL")
DEBUG = os.getenv("DEBUG", "True") == "True"  # Default to True if not set
PORT = int(os.getenv("PORT"))  # Default to port 3000 if not set
REDIS_URL = str(os.getenv("REDIS_URL"))
print("REDIS_URL:", REDIS_URL)

# Initialize Redis connection using the Redis URL
redis_client = redis.from_url(REDIS_URL)

