import unittest
from datetime import date
from app import create_app, db
from app.models import LeaderBoard, Player, Game

class TestLeaderBoardModel(unittest.TestCase):

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
        self.player = Player(name='Test Player')
        self.game = Game(name='Test Game')
        self.leaderboard_entry = LeaderBoard(player=self.player, game=self.game,
                                             player_score=10, computer_score=5,
                                             created_at=date.today())

    def tearDown(self):
        # Clean up test data
        db.session.rollback()

    def test_leaderboard_entry_creation(self):
        # Add the leaderboard entry to the database
        db.session.add(self.player)
        db.session.add(self.game)
        db.session.add(self.leaderboard_entry)
        db.session.commit()

        # Retrieve the leaderboard entry from the database
        retrieved_entry = LeaderBoard.query.filter_by(id=self.leaderboard_entry.id).first()

        # Check if the retrieved entry matches the original one
        self.assertIsNotNone(retrieved_entry)
        self.assertEqual(retrieved_entry.player_id, self.player.id)
        self.assertEqual(retrieved_entry.game_id, self.game.id)
        self.assertEqual(retrieved_entry.player_score, 10)
        self.assertEqual(retrieved_entry.computer_score, 5)
        self.assertEqual(retrieved_entry.created_at, date.today())

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
