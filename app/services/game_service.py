from app import db
from app.models.game import Game
from app.services.player_service import PlayerService
from app.services.game_player_service import GamePlayerService

class GameService:
    
    @staticmethod
    def create_game():
        try:
            new_game = Game(name="game1")
            db.session.add(new_game)
            db.session.commit()
            return {"data": new_game}
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def start_game(request):
        try:
            player_response = PlayerService.create_player(request)
            if "error" in player_response:
                raise Exception(player_response["error"])
            game_response = GameService.create_game()
            if "error" in game_response:
                raise Exception(game_response["error"])
            game_player = GamePlayerService.create_game_player(game_response["data"].id, player_response["data"].id)
            return {"game_player_id": game_player.id, "game_id": game_player.game_id, "player1_id": game_player.player1_id}
        except Exception as e:
            return {"error": str(e)}
