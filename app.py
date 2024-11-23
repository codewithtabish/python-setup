from flask import Flask,jsonify
from constants.index import product_list
from constants.index import mobile_listResponse
import os
from dotenv import load_dotenv



# Load the .env file
load_dotenv()

print("The DB URL IS ",os.getenv("DB_URL"))

app=Flask(__name__)

@app.route("/")

def home():
        return "Welcome to your first Flask app!"  # Display this message in the browser
    
@app.route("/about")

def about():
    return "This is the about route" # Display this message in the browser   

@app.route("/products")
def products():
   
     # Return a response with the correct format
    response = {
        "status": True,
        "message": "All products are here",
        "products": product_list,
    }
  
    
    return jsonify(response),200
    

@app.route('/mobiles')
def mobile_list():
    return jsonify(mobile_listResponse)
  
  
@app.route('/service')
def service():
    response = {
        "status": True,
        "message": "All services are here"
    }
    return response
    

@app.route("/mood_checker")
def mood_checker():
    return "you are now in good mood 💞💞💞💞"

@app.route("/live_score")
def live_score():
    return "This team will make 400 score !! "
        

    
if __name__=="__main__":
    app.run(debug=True,port=3000)    





