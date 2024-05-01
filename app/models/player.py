from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)

    def __init__(self, name):
        self.name = name
