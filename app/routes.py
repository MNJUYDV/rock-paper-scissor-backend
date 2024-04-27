from flask import request, jsonify, Blueprint
from app.services.leaderboard_service import LeaderBoardService

leaderboard_bp = Blueprint('leaderboard_bp', __name__)

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    response_data = LeaderBoardService.get_leaderboard()
    return jsonify({"leaderboard_stats": response_data})


@leaderboard_bp.route('/leaderboard', methods=['POST'])
def create_leaderboard_entry():
    LeaderBoardService.create_leaderboard_entry(request)
    return jsonify({'message': 'Leaderboard entry created successfully'}), 201