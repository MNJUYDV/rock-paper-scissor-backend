import unittest
from unittest.mock import patch, MagicMock
from app.models.leaderboard import LeaderBoard
from app import db
from flask import jsonify
from app.services.leaderboard_service import LeaderBoardService  # Replace 'your_app' with the actual name of your application package
from app import create_app, db

class TestLeaderBoardService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Flask app for testing
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Clean up after testing
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        # Create test data
        self.request_data = {
            'player_name': 'Test Player',
            'player_score': 10,
            'computer_score': 5
        }

    def tearDown(self):
        # Clean up test data
        db.session.rollback()

    @patch('app.models.leaderboard.LeaderBoard.query')
    @patch('app.models.leaderboard.Player.query')
    def test_get_leaderboard(self, mock_player_query, mock_leaderboard_query):
        # Mock LeaderBoard and Player queries
        mock_leaderboard_query.all.return_value = [
            LeaderBoard(id=1, player_id=1, player_score=10, computer_score=5),
            LeaderBoard(id=2, player_id=2, player_score=5, computer_score=10)
        ]
        mock_player_query.get.side_effect = lambda player_id: MagicMock(name=f'Player{id}', name='Test Player')

        # Call the get_leaderboard method
        response_data = LeaderBoardService.get_leaderboard()

        # Check if the response data is as expected
        expected_data = [
            {'player_name': 'Test Player', 'wins': 1, 'losses': 1, 'ties': 0},
            {'player_name': 'Test Player', 'wins': 0, 'losses': 1, 'ties': 0}
        ]
        self.assertEqual(response_data, expected_data)

    @patch('app.models.leaderboard.Player')
    @patch('app.models.leaderboard.Game')
    def test_create_leaderboard_entry(self, mock_game, mock_player):
        # Mock Player and Game creation
        mock_player_instance = MagicMock(id=1)
        mock_player.return_value = mock_player_instance
        mock_game_instance = MagicMock(id=1)
        mock_game.return_value = mock_game_instance

        # Call the create_leaderboard_entry method
        response = LeaderBoardService.create_leaderboard_entry(MagicMock(json=lambda: self.request_data))

        # Check if the response is as expected
        expected_response = jsonify(success=True)
        self.assertEqual(response, expected_response)

        # Check if the player and game were added to the session
        self.assertIn(mock_player_instance, db.session.add.call_args_list)
        self.assertIn(mock_game_instance, db.session.add.call_args_list)

        # Check if the leaderboard entry was added to the session
        leaderboard_entry_args = db.session.add.call_args[0][0]
        self.assertEqual(leaderboard_entry_args.player_id, mock_player_instance.id)
        self.assertEqual(leaderboard_entry_args.game_id, mock_game_instance.id)
        self.assertEqual(leaderboard_entry_args.player_score, self.request_data['player_score'])
        self.assertEqual(leaderboard_entry_args.computer_score, self.request_data['computer_score'])

if __name__ == '__main__':
    unittest.main()
