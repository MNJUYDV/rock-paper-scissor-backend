from flask import request, jsonify, Blueprint
from app.services.leaderboard_service import LeaderBoardService
from app.services.game_service import GameService
from app.services.game_player_service import GamePlayerService

bp = Blueprint('leaderboard_bp', __name__)

@bp.route('/api/v1/players-stats', methods=['GET'])
def get_players_stats():
    try:
        response_data = LeaderBoardService.get_players_stats()
        return jsonify({"leaderboard_stats": response_data}), 200
    except Exception as e:
        return jsonify({'error': f'Error getting players stats: {str(e)}'}), 500

@bp.route('/api/v1/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        response_data = LeaderBoardService.get_leaderboard()
        return jsonify({"leaderboard_stats": response_data}), 200
    except Exception as e:
        return jsonify({'error': f'Error getting leaderboard: {str(e)}'}), 500

@bp.route('/api/v1/leaderboard', methods=['POST'])
def create_leaderboard_entry():
    try:
        response = LeaderBoardService.create_leaderboard_entry(request)
        if "error" in response:
            raise Exception(response["error"])
        return jsonify({'data': response, 'message': 'leaderboard entry created successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Error creating leaderboard entry: {str(e)}'}), 500

@bp.route('/api/v1/start-game', methods=['POST'])
def start_game():
    try:
        response = GameService.start_game(request)
        if "error" in response:
            raise Exception(response["error"])
        return jsonify({'data': response, 'message': 'Game entry created successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Error starting game: {str(e)}'}), 500

@bp.route('/api/v1/game-players', methods=['GET'])
def get_game_play():
    try:
        result = GamePlayerService.get_game_play()
        return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': f'Error getting game players: {str(e)}'}), 500
