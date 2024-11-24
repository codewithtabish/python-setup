from flask import Flask
from config import DB_URL, DEBUG, PORT
from routes.all_routes import routes  # Import the routes blueprint

app = Flask(__name__)

# Access your configurations
print(f"Database URL: {DB_URL}")
print(f"Running in Debug mode: {DEBUG}")
print(f"App will run on port: {PORT}")

# Register the blueprint from routes
app.register_blueprint(routes,url_prefix="/api/v1")




if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
