from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config
from sqlalchemy.engine.reflection import Inspector
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from app.routes import player_bp, leaderboard_bp
app.register_blueprint(player_bp)
app.register_blueprint(leaderboard_bp)