from flask import jsonify ,render_template,request
from constants.index import product_list, mobile_listResponse
import re 
import bcrypt
from models import db
from models.user_model import User




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

    return jsonify({"message": "User created successfully!"}), 201

