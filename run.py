from app import app, db

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
