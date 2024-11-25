# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Create a global db instance here, so it's shared across models
db = SQLAlchemy()
