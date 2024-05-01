from app import db
from app.models.player import Player
from flask import jsonify
import logging

class PlayerService:
    @staticmethod
    def create_player(request):
        try:
            request_data = request.json
            player_name = request_data.get('player_name')

            # Check if player name is provided in the request
            if not player_name:
                raise Exception("Player name is required")

            new_player = Player(name=player_name)
            db.session.add(new_player)
            db.session.commit()
            logging.info(f"Player '{new_player.id}' created successfully")
            return {"data": new_player, "status_code": 200}
        except Exception as e:
            logging.error(f"Error creating player: {str(e)}")
            return {"error": str(e), "status_code": 500}
