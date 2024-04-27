from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))

    def __init__(self, name, type):
        self.name = name
        self.type = type