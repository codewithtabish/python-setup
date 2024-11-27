import os
from dotenv import load_dotenv
from flask_mail import Mail
from flask import Flask

# Load environment variables from a .env file
load_dotenv()


app = Flask(__name__)




# General configurations
DB_URL = os.getenv("DB_URL")
DEBUG = os.getenv("DEBUG", "True") == "True"  # Default to True if not set
PORT = int(os.getenv("PORT"))  # Default to port 3000 if not set

# Other app-specific configurations can go here, such as email settings, etc.
