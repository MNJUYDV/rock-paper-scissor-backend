import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

import unittest
from app import create_app, db
from app.config import TestingConfig
from unittest.mock import patch, MagicMock
from app.services.game_service import GameService


class TestGameAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    @patch('app.services.game_service.PlayerService.create_player')
    @patch('app.services.game_service.GameService.create_game')
    @patch('app.services.game_service.GamePlayerService.create_game_player')
    def test_start_game_success(self, mock_create_game_player, mock_create_game, mock_create_player):
        # Mocking responses
        mock_player_response = {"data": MagicMock(id=1)}
        mock_create_player.return_value = mock_player_response

        mock_game_response = {"data": MagicMock(id=1)}
        mock_create_game.return_value = mock_game_response

        mock_game_player_response = {"data": MagicMock(id=1, game_id=1, player1_id=1)}
        mock_create_game_player.return_value = mock_game_player_response

        # Call the method
        result = GameService.start_game({})

        # Assertions
        self.assertIn("game_player_id", result)
        self.assertIn("game_id", result)
        self.assertIn("player1_id", result)
        self.assertEqual(result["game_id"], 1)
        self.assertEqual(result["player1_id"], 1)
        
        
    @patch('app.services.game_service.PlayerService.create_player')
    @patch('app.services.game_service.GameService.create_game')
    @patch('app.services.game_service.GamePlayerService.create_game_player')
    def test_start_game_player_creation_failure(self, mock_create_game_player, mock_create_game, mock_create_player):
        # Mocking response for player creation failure
        mock_player_response = {"error": "Player creation failed"}
        mock_create_player.return_value = mock_player_response

        # Call the method
        result = GameService.start_game({})

        # Assertions
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Player creation failed")

    @patch('app.services.game_service.PlayerService.create_player')
    @patch('app.services.game_service.GameService.create_game')
    def test_start_game_game_creation_failure(self, mock_create_game, mock_create_player):
        # Mocking response for game creation failure
        mock_game_response = {"error": "Game creation failed"}
        mock_create_game.return_value = mock_game_response

        # Call the method
        result = GameService.start_game({})

        # Assertions
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Game creation failed")

    @patch('app.services.game_service.PlayerService.create_player')
    @patch('app.services.game_service.GameService.create_game')
    @patch('app.services.game_service.GamePlayerService.create_game_player')
    def test_start_game_game_player_creation_failure(self, mock_create_game_player, mock_create_game, mock_create_player):
        # Mocking response for game player creation failure
        mock_game_player_response = {"error": "Game player creation failed"}
        mock_create_game_player.return_value = mock_game_player_response

        # Call the method
        result = GameService.start_game({})

        # Assertions
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Game player creation failed")
    
if __name__ == '__main__':
    unittest.main()