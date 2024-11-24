from flask import jsonify
from constants.index import product_list, mobile_listResponse

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
    response = {
        "status": True,
        "message": "All services are here"
    }
    return response

def mood_checker():
    return "you are now in a good mood 💞💞💞💞"

def live_score():
    return "This team will make 400 scores!!"


def kotlin_func():
    
    return "This is the kotlin function from controller 💞💞💞"

def all_courses():
    return "This is the all courses routes from controller 💞💞💞"