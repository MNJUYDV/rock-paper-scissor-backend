import unittest
from app import create_app, db
from app.models import Player

class TestPlayerModel(unittest.TestCase):

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

    def tearDown(self):
        # Clean up test data
        db.session.rollback()

    def test_player_creation(self):
        # Add the player to the database
        db.session.add(self.player)
        db.session.commit()

        # Retrieve the player from the database
        retrieved_player = Player.query.filter_by(id=self.player.id).first()

        # Check if the retrieved player matches the original one
        self.assertIsNotNone(retrieved_player)
        self.assertEqual(retrieved_player.name, 'Test Player')

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
