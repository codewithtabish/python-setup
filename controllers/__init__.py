from flask import jsonify ,render_template,request,send_file
from constants.index import product_list, mobile_listResponse
import re 
import bcrypt
from models import db
from models.user_model import User
from utils.send_email import send_email
from config import redis_client  # Import redis_client from config
from utils.tags_extractor import get_video_tags
from utils.qr_generator import generate_qr_code





# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


def home():
    return "Welcome to your first Flask app!"

def about():
    return "This is the about route"

def products():
    response = {
        "status": True,
        "message": "All products are here",
        "products": product_list,
    }
    return jsonify(response), 200

def mobile_list():
    return jsonify(mobile_listResponse)

def service():
    return render_template("services.html")


def mood_checker():
    return "you are now in a good mood 💞💞💞💞"

def live_score():
    return "This team will make 400 scores!!"


def kotlin_func():
    
    return "This is the kotlin function from controller 💞💞💞"

def all_courses():
    return "This is the all courses routes from controller 💞💞💞"


def signup():
    data=request.json
    name=data.get('name')
    email=data['email']
    password=data.get('password')
    if not name or not email or not password :
        return jsonify({"message":"All fields are required"}),400
    if len(password)<6:
        return jsonify({"message":"Password must be at least 6 characters"}),400
    if not re.match(EMAIL_REGEX,email):
        return jsonify({"message":"Invalid email format"}),400
    
    salt=bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    user=User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message":"Email already exists"}),400
       # Add the user to the database
    
    # Create a new User instance
    new_user = User(name=name, email=email, password=hashed_password)   
    db.session.add(new_user)
    db.session.commit()  # Save the changes to the database

    send_email(name,email)
        # Delete the 'users' list from Redis
    redis_client.delete('users')  # This deletes the cached users from Redis

    return jsonify({"message": "User created successfully!"}), 201


def get_all_users():
    try:
        # Check if 'users' key exists in Redis
        if redis_client.exists('users'):
            # Fetch users from Redis
            users_data = redis_client.get('users')
            # Decode the byte string and convert it back to a list of dictionaries
            users_data = users_data.decode('utf-8')  # Decode from bytes to string
            users_data = eval(users_data)  # Convert the string back to a list of dictionaries

            return jsonify({"users": users_data}), 200
        else:
            # If not found in Redis, fetch users from the database
            users = User.query.all()
            # Prepare a list of dictionaries with the details you need
            users_data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

            # Save users to Redis for future access (as a string representation of the list of dictionaries)
            redis_client.set('users', str(users_data))

            return jsonify({"users": users_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



def tags_extractor():
    data=request.json
    url=data['url']
    # Check if 'url' is in the request payload
    if not data or 'url' not in data:
        return jsonify({"error": "A valid 'url' must be provided"}), 400
    url = data['url']

    # Validate the URL
    if not url or not isinstance(url, str):
        return jsonify({"error": "Invalid URL format"}), 400

    tags = get_video_tags(url)

    # Handle case where tags cannot be extracted (invalid URL or other issues)
    if tags is None:
        return jsonify({"error": "Failed to extract tags. Ensure the URL is valid."}), 400

    return jsonify({"tags": tags}), 200

    
    
    
    
def generate_qr_method():
     data = request.json
     

    # Validate input
     if not data or 'text' not in data:
        return jsonify({"error": "The 'text' field must be provided"}), 400

     text = data['text']

    # Generate the QR code
     qr_stream = generate_qr_code(text)

    # Return the QR code image as a response
     return send_file(qr_stream, mimetype="image/png", as_attachment=True, download_name="qr_code.png")
    
    



