from app import create_app, db
from app.models.player import Player

def insert_initial_values():
    computer_player = Player.query.filter_by(name="Computer", id=1).first()
    if not computer_player:
        computer_player = Player(name="Computer")
        db.session.add(computer_player)
        db.session.commit()

if __name__ == '__main__':
    # Create database tables
    app = create_app()
    with app.app_context():
        db.create_all()
        insert_initial_values()
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
