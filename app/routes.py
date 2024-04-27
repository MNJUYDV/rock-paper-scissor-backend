from flask import Blueprint, jsonify
from app.models.player import Player
from app.models.leaderboard import LeaderBoard


player_bp = Blueprint('player_bp', __name__)
leaderboard_bp = Blueprint('leaderboard_bp', __name__)

@player_bp.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    player_list = [{"id": player.id, "name": player.name} for player in players]
    return jsonify({"players": player_list})


@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard = LeaderBoard.query.all()
    entry_list = [{"id": entry.id, "player_score": entry.player_score} for entry in leaderboard]
    return jsonify({"leaderboard": entry_list})