from app import db
from app.models.game_player import GamePlayer
from datetime import date

class GamePlayerService:
    @staticmethod
    def create_game_player(game_id, player_id):
        game_player = GamePlayer(game_id = game_id, player1_id = player_id, player2_id=1,created_at=date.today())
        db.session.add(game_player)
        db.session.commit()
        return game_player
    
    def get_game_play():
        game_plays = GamePlayer.query.all()
        result = []
        for e in game_plays:
            result.append({"game_id": e.game_id, "player1_id": e.player1_id, "player2_id": e.player2_id})
        return result