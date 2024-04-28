from app import db
from app.models.player import Player

class PlayerService:
    @staticmethod
    def create_player(request):
        request_data = request.json
        player_name = request_data.get('player_name')
        new_player = Player(name=player_name)
        db.session.add(new_player)
        db.session.commit()
        return new_player