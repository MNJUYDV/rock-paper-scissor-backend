from app import db
from app.models.player import Player
from app.models.game import Game

class LeaderBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    player_score = db.Column(db.Integer)
    computer_score = db.Column(db.Integer)
    created_at = db.Column(db.Date, nullable=False)
    
    # Define relationships
    player = db.relationship('Player', backref='leaderboard_entries')
    game = db.relationship('Game', backref='leaderboard_entries')

    def __repr__(self):
        return f"<LeaderBoard(id={self.id}, player_id={self.player_id}, game_id={self.game_id}, player_score={self.player_score}, computer_score={self.computer_score}, created_at={self.created_at})>"
