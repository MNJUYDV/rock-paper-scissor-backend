from flask import Flask

app = Flask(__name__)

# Import routes after creating the Flask app instance to avoid circular imports
from app import routes
