from app import db
from app.models.game import Game
from app.services.player_service import PlayerService
from app.services.game_player_service import GamePlayerService


class GameService:
    
    @staticmethod
    def create_game():
        new_game = Game(name="game1")
        db.session.add(new_game)
        db.session.commit()
        return new_game
    
    @staticmethod
    def start_game(request):
        player = PlayerService.create_player(request)
        game = GameService.create_game()
        game_player = GamePlayerService.create_game_player(game.id, player.id)
        return game_player