from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Use the configuration class

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from app.routes import bp
app.register_blueprint(bp)