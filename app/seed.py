from app import create_app, db
from app.models.player import Player

def seed_initial_values():
    if not Player.query.all():
        computer_player = Player(name="Computer")
        db.session.add(computer_player)
        db.session.commit()
        print("Initial values seeded successfully.")
    else:
        print("Player table is not empty. Skipping seeding.")