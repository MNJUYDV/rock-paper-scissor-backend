from flask import request, jsonify, Blueprint
from app import app, db
from app.models.player import Player
from app.models.game import Game
from app.models.leaderboard import LeaderBoard
from datetime import date


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
    
    # Initialize dictionaries to store win, loss, and tie counts for each player
    win_count = {}
    loss_count = {}
    tie_count = {}
    
    # Count wins, losses, and ties for each player
    for entry in leaderboard:
        player_name = Player.query.get(entry.player_id).name
        
        # Initialize counts if player_name is not already present in the dictionaries
        if player_name not in win_count:
            win_count[player_name] = 0
            loss_count[player_name] = 0
            tie_count[player_name] = 0
        
        # Determine win, loss, or tie based on player_score and computer_score
        if entry.player_score > entry.computer_score:
            win_count[player_name] += 1
        elif entry.player_score < entry.computer_score:
            loss_count[player_name] += 1
        else:
            tie_count[player_name] += 1
    
    # Prepare response data
    response_data = []
    for player_name in win_count.keys():
        response_data.append({
            "player_name": player_name,
            "wins": win_count[player_name],
            "losses": loss_count[player_name],
            "ties": tie_count[player_name]
        })
    
    return jsonify({"leaderboard_stats": response_data})


@leaderboard_bp.route('/leaderboard', methods=['POST'])
def create_leaderboard_entry():
    # Get data from request body
    request_data = request.json
    player_name = request_data.get('player_name')
    player_score = request_data.get('player_score')
    game_score = request_data.get('game_score')
    
    # If player_name is not provided, return an error response
    if not player_name:
        return jsonify({'error': 'Player name is required'}), 400

    # Create a new player
    player = Player(name=player_name)
    db.session.add(player)
    db.session.commit()

    # Create a new game (default name and type)
    game = Game(name='game1', type='human vs computer')
    db.session.add(game)
    db.session.commit()

    # Create a new leaderboard entry
    leaderboard_entry = LeaderBoard(
        player_id=player.id,
        game_id=game.id,
        player_score=player_score,
        computer_score=game_score,
        created_at=date.today()
    )
    db.session.add(leaderboard_entry)
    db.session.commit()

    return jsonify({'message': 'Leaderboard entry created successfully'}), 201