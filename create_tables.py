from app import app, db

# Use app.app_context() to set up the application context
with app.app_context():
    db.create_all()
