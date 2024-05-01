from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from .config import DevelopmentConfig, TestingConfig
import os

db = SQLAlchemy()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)  
    db.init_app(app)
    CORS(app)

    from app.routes import bp
    app.register_blueprint(bp)
    
    from .seed import seed_initial_values
    with app.app_context():
        db.create_all()
        seed_initial_values()
        
    return app
