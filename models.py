from app import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    votes1 = db.Column(db.Integer, default=0)
    votes2 = db.Column(db.Integer, default=0)
