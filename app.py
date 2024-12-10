from dotenv import load_dotenv
from config import DB_URL, DEBUG, PORT
from routes.all_routes import routes  # Import the routes blueprint
from models import db  # Import db from the models package
from models.user_model import User
import os
from config import app
from flask import render_template
from flask_cors import CORS







# Load environment variables from .env file

CORS(app)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')



# Initialize SQLAlchemy with the db instance from models
db.init_app(app)


# Access your configurations
print(f"Database URL: {DB_URL}")
print(f"Running in Debug mode: {DEBUG}")
print(f"App will run on port: {PORT}")

# Register the blueprint from routes
app.register_blueprint(routes,url_prefix="/api/v1")




    
def setup_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        print("Database connected and tables created.")

# Call the setup function when the app starts
setup_database()
    

        

@app.route('/')
def home():
    return "this is the home page"


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=9000)

# cost_analyzer\Scripts\activate
        # download_dir = r"C:\Users\Mark 1\Downloads"
# 

# docker run -it --rm redis:latest redis-cli -h singapore-redis.render.com -p 6379 -a DqU0IsGdKRsbo2CxYYPz2ETiUYkWKvzu --tls
