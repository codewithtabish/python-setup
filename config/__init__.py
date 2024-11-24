import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# General configurations
DB_URL = os.getenv("DB_URL")
DEBUG = os.getenv("DEBUG", "True") == "True"  # Default to True if not set
PORT = int(os.getenv("PORT"))  # Default to port 3000 if not set

# Other app-specific configurations can go here, such as email settings, etc.
