import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

import unittest
from flask import json
from app import create_app, db
from app.models.leaderboard import LeaderBoard
from app.models.game_player import GamePlayer
from app.models.game import Game
from app.models.player import Player
from app.services.leaderboard_service import LeaderBoardService
from app.config import TestingConfig
from datetime import date
from unittest.mock import patch, MagicMock
from flask import jsonify


class TestLeaderboardAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
        
    @patch('app.services.leaderboard_service.db')
    def test_get_players_stats_success(self, MockDB):
        # Mocking the query results
        mock_result1 = ('Player1', 3, 2, 1)
        mock_result2 = ('Player2', 2, 3, 0)

        # Set the return value of the mock query
        MockDB.session.query().join().join().group_by().order_by().limit().all.return_value = [mock_result1, mock_result2]

        # Call the method
        result = LeaderBoardService.get_players_stats()

        # Assertions
        expected_result = {
            'Player1': {'wins': 3, 'losses': 2, 'ties': 1},
            'Player2': {'wins': 2, 'losses': 3, 'ties': 0}
        }
        self.assertEqual(result, expected_result)
        
    @patch('app.services.leaderboard_service.db')
    def test_get_players_stats_failure(self, MockDB):
        # Mocking an exception
        MockDB.session.query().join().join().group_by().order_by().limit().all.side_effect = Exception("Database Error")

        # Call the method
        result = LeaderBoardService.get_players_stats()

        # Assertions
        expected_error = 'Error fetching players stats: Database Error'
        self.assertEqual(result, expected_error)
            
    @patch('app.services.leaderboard_service.LeaderBoard')
    def test_get_leaderboard_success(self, MockLeaderBoard):
        # Mocking the query results
        mock_leaderboard1 = MagicMock()
        mock_leaderboard1.game_id = 1
        mock_leaderboard1.player1_score = 3
        mock_leaderboard1.player2_score = 2

        mock_leaderboard2 = MagicMock()
        mock_leaderboard2.game_id = 2
        mock_leaderboard2.player1_score = 2
        mock_leaderboard2.player2_score = 1

        # Set the return value of the mock query
        MockLeaderBoard.query.all.return_value = [mock_leaderboard1, mock_leaderboard2]

        # Call the method
        result = LeaderBoardService.get_leaderboard()

        # Assertions
        expected_result = [
            {"game_id": 1, "player1_score": 3, "player2_score": 2},
            {"game_id": 2, "player1_score": 2, "player2_score": 1}
        ]
        self.assertEqual(result, expected_result)  
            

    @patch('app.services.leaderboard_service.LeaderBoardService.create_leaderboard_entry')
    @patch('app.models.game.Game')
    def test_create_leaderboard_entry(self, MockGame, mock_create_leaderboard_entry):
        mock_game = MagicMock()
        mock_game.id = 1
        MockGame.query.get.return_value = mock_game
        
        mock_create_leaderboard_entry.return_value = [{"game_id": 1, "player1_score": 1, "player2_score": 2}]
        data = LeaderBoardService.create_leaderboard_entry({'game_id': '1', "player1_score": 1, "player2_score": 2})
        self.assertEqual(data[0]["game_id"], 1)
        self.assertEqual(data[0]["player1_score"], 1)
        self.assertEqual(data[0]["player2_score"], 2)
    
if __name__ == '__main__':
    unittest.main()