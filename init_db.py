from app import app, db
from models import Poll

with app.app_context():
    db.create_all()

    # Optionally, add some initial data
    if Poll.query.count() == 0:
        poll1 = Poll(question="What's your favorite color?", option1="Red", option2="Blue")
        db.session.add(poll1)
        db.session.commit()
