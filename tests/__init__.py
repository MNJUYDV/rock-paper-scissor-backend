# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.config import DevelopmentConfig, TestingConfig  # Import both DevelopmentConfig and TestingConfig

# Initialize Flask extensions
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

# Create the Flask application factory function
def create_app(config_name='development'):
    app = Flask(__name__)

    # Choose the configuration based on the provided config_name
    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Initialize Flask extensions with the app
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # Import blueprints and register them
    from app.routes import leaderboard_bp
    app.register_blueprint(leaderboard_bp)

    return app
