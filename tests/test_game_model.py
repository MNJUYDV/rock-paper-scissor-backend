# tests/test_game_model.py

import unittest
from app import create_app, db
from app.models import Game

class TestGameModel(unittest.TestCase):

    def setUp(self):
        # Create a Flask test app
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create the database and tables
        db.create_all()

    def tearDown(self):
        # Remove the database and tables
        db.session.remove()
        db.drop_all()

        # Pop the app context
        self.app_context.pop()

    def test_game_creation(self):
        # Create a new Game instance
        game = Game(name='Test Game')

        # Add the game to the session and commit to the database
        with self.app.app_context():
            db.session.add(game)
            db.session.commit()

            # Retrieve the game from the database
            retrieved_game = Game.query.filter_by(name='Test Game').first()

            # Assert that the retrieved game is not None
            self.assertIsNotNone(retrieved_game)

            # Assert that the attributes of the retrieved game match the original values
            self.assertEqual(retrieved_game.name)

if __name__ == '__main__':
    unittest.main()
