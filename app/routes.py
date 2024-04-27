from flask import Blueprint, jsonify
from app.models.player import Player

player_bp = Blueprint('player_bp', __name__)

@player_bp.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    player_list = [{"id": player.id, "name": player.name} for player in players]
    return jsonify({"players": player_list})
