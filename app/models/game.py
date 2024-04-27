from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    type = db.Column(db.String(100), unique=True)

    def __init__(self, name, type):
        self.name = name
        self.type = type