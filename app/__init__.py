from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from .config import DevelopmentConfig, TestingConfig
import os
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)  
    db.init_app(app)
    CORS(app)

    from app.routes import bp
    app.register_blueprint(bp)
    configure_logging(app)

    
    from .seed import seed_initial_values
    with app.app_context():
        db.create_all()
        seed_initial_values()
        
    return app

def configure_logging(app):
    log_level = app.config.get('LOG_LEVEL', 'INFO')
    log_file = app.config.get('LOG_FILE')

    # Set the log level
    logging.basicConfig(level=log_level)

    # Add file handler if log file is specified
    if log_file:
        file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=10)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        app.logger.addHandler(file_handler)
