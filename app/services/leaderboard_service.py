from app.models.leaderboard import LeaderBoard
from app.models.player import Player
from app.models.game_player import GamePlayer
from app import db
from datetime import date
from flask import jsonify

class LeaderBoardService:
    
    @staticmethod
    def get_leaderboard():
        # Get all players
        players = Player.query.all()

        # Dictionary to store aggregated stats for each player
        aggregated_stats_per_player = {}

        # Iterate over all players
        for player in players:
            player_id = player.id

            # Initialize aggregated stats for the player
            aggregated_stats = {
                "wins": 0,
                "losses": 0,
                "ties": 0
            }

            # Fetch all games where the player is player1
            games_for_player = GamePlayer.query.filter_by(player1_id=player_id).all()
            
            for game in games_for_player:
                # Fetch one leaderboard entry for the current game
                leaderboard = LeaderBoard.query.filter_by(game_id=game.game_id).first()

                # Calculate wins, losses, and ties for the player
                if leaderboard:
                    if leaderboard.player1_score > leaderboard.player2_score:
                        aggregated_stats["wins"] += 1
                    elif leaderboard.player1_score < leaderboard.player2_score:
                        aggregated_stats["losses"] += 1
                    else:
                        aggregated_stats["ties"] += 1

            # Store aggregated stats for the player
            aggregated_stats_per_player[player.name] = aggregated_stats

        return aggregated_stats_per_player

    
    @staticmethod
    def create_leaderboard_entry(request):
        # Get data from request body
        request_data = request.json
        game_id = request_data.get('game_id')
        player1_score = request_data.get('player1_score')
        player2_score = request_data.get('player2_score')

        # If game_id is not provided, return an error response
        if not game_id:
            return jsonify({'error': 'Game ID is required'}), 400

        # Set default player2_id to 1
        player2 = Player.query.get(1)  # Assuming player2_id=1 exists in the database

        # Create a new leaderboard entry
        leaderboard_entry = LeaderBoard(
            game_id=game_id,
            player1_score=player1_score,
            player2_score=player2_score,
            created_at=date.today()
        )
        db.session.add(leaderboard_entry)
        db.session.commit()

        return jsonify({'message': 'Leaderboard entry created successfully'}), 201
