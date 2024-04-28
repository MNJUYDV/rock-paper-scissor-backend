from app.models.leaderboard import LeaderBoard
from app.models.player import Player
from app.models.game_player import GamePlayer
from app import db
from datetime import date
from flask import jsonify
from sqlalchemy import func, case, desc

class LeaderBoardService:
    
    @staticmethod
    def get_players_stats():
        try:
            # Query to get aggregated stats for each player
            stats_query = db.session.query(
                Player.name,
                func.sum(
                    case(
                        (LeaderBoard.player1_score > LeaderBoard.player2_score, 1),
                        else_=0
                    )
                ).label("wins"),
                func.sum(
                    case(
                        (LeaderBoard.player1_score < LeaderBoard.player2_score, 1),
                        else_=0
                    )
                ).label("losses"),
                func.sum(
                    case(
                        (LeaderBoard.player1_score == LeaderBoard.player2_score, 1),
                        else_=0
                    )
                ).label("ties")
            ).join(GamePlayer, GamePlayer.player1_id == Player.id) \
            .join(LeaderBoard, LeaderBoard.game_id == GamePlayer.game_id) \
            .group_by(Player.id) \
            .order_by(desc(LeaderBoard.created_at)) \
            .limit(50)

            # Execute the query and fetch results
            results = stats_query.all()

            # Convert results to a dictionary
            aggregated_stats_per_player = {}
            for result in results:
                player_name, wins, losses, ties = result
                aggregated_stats_per_player[player_name] = {
                    "wins": wins or 0,
                    "losses": losses or 0,
                    "ties": ties or 0
                }

            return aggregated_stats_per_player
        except Exception as e:
            return f"Error fetching players stats: {str(e)}"
    
    @staticmethod
    def create_leaderboard_entry(request):
        try:
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

            return leaderboard_entry
        except Exception as e:
            return jsonify({'error': f'Error creating leaderboard entry: {str(e)}'}), 500
    
    @staticmethod
    def get_leaderboard():
        try:
            response = []
            leaderboard = LeaderBoard.query.all()
            for e in leaderboard:
                response.append({
                    "game_id": e.game_id,
                    "player1_score": e.player1_score,
                    "player2_score": e.player2_score
                })
            return response
        except Exception as e:
            return jsonify({'error': f'Error fetching leaderboard: {str(e)}'}), 500
