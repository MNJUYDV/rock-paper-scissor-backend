from app import db
from sqlalchemy import Index

class GamePlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False, unique=True)
    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    
    # Define relationships
    player1 = db.relationship('Player', foreign_keys=[player1_id])
    player2 = db.relationship('Player', foreign_keys=[player2_id])
    game = db.relationship('Game', backref='gameplayer_entries')

    # Define index
    __table_args__ = (
        Index('idx_gameplayer_player1_game', 'player1_id', 'game_id'),
    )

    def __repr__(self):
        return f"GamePlayer(id={self.id}, game_id={self.game_id}, player1_id={self.player1_id}, player2_id={self.player2_id}, created_at={self.created_at})"
