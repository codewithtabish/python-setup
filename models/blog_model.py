from models import db  # Import db from your models package
import uuid  # Import the UUID module
from datetime import datetime  # Import datetime for timestamping

class Blog(db.Model):
    __tablename__ = 'blogs'  # Optional: specify the table name

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # UUID v4
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)  # Ensure slugs are unique
    blog_content = db.Column(db.Text, nullable=False, unique=True)
    blog_keywords = db.Column(db.ARRAY(db.String), nullable=False)  # List of keywords
    blog_main_image = db.Column(db.Text, nullable=False)  # URL or path to the main image
    category = db.Column(db.String(100), nullable=False)  # Category of the blog
    is_published = db.Column(db.Boolean, default=False, nullable=False)  # Publish status
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp for creation
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # Timestamp for updates

    def __repr__(self):
        return f"<Blog {self.title}, Category: {self.category}>"
