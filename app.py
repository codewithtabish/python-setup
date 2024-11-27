from dotenv import load_dotenv
from config import DB_URL, DEBUG, PORT
from routes.all_routes import routes  # Import the routes blueprint
from models import db  # Import db from the models package
from models.user_model import User
import os
from config import app



# Load environment variables from .env file
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
    

        





if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
# cost_analyzer\Scripts\activate