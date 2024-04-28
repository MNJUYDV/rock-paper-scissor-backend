from flask import request, jsonify, Blueprint
from app.services.leaderboard_service import LeaderBoardService
from app.services.game_service import GameService
from app.services.game_player_service import GamePlayerService

bp = Blueprint('leaderboard_bp', __name__)

@bp.route('/api/v1/leaderboard', methods=['GET'])
def get_leaderboard():
    response_data = LeaderBoardService.get_leaderboard()
    return jsonify({"leaderboard_stats": response_data})


@bp.route('/api/v1/leaderboard', methods=['POST'])
def create_leaderboard_entry():
    LeaderBoardService.create_leaderboard_entry(request)
    return jsonify({'message': 'Leaderboard entry created successfully'}), 201


@bp.route('/api/v1/start-game', methods=['POST'])
def start_game():
    GameService.start_game(request)
    return jsonify({'message': 'Game entry created successfully'}), 201

@bp.route('/api/v1/game-players', methods=['GET'])
def get_game_play():
    result = GamePlayerService.get_game_play()
    return jsonify({'message': result}), 201