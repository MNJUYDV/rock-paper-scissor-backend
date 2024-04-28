from app import db
from app.models.player import Player
from flask import jsonify

class PlayerService:
    @staticmethod
    def create_player(request):
        try:
            request_data = request.json
            player_name = request_data.get('player_name')

            # Check if player name is provided in the request
            if not player_name:
                return jsonify({'error': 'Player name is required'}), 400

            new_player = Player(name=player_name)
            db.session.add(new_player)
            db.session.commit()
            return new_player
        except Exception as e:
            return jsonify({'error': f'Error creating player: {str(e)}'}), 500
