from app import db

class LeaderBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    player1_score = db.Column(db.Integer, nullable = False)
    player2_score = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.Date, nullable=False)
    
    # Define relationships
    game = db.relationship('Game', backref='leaderboard_entries')

    def __repr__(self):
        return f"<LeaderBoard(id={self.id}, game_id={self.game_id}, player1_score={self.player1_score}, player2_score={self.player2_score}, created_at={self.created_at})>"
