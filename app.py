from app import app, db

from app.models.player import Player

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
