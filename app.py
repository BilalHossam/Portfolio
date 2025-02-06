from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    votes1 = db.Column(db.Integer, default=0)
    votes2 = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    polls = Poll.query.all()
    return render_template('index.html', polls=polls)

@app.route('/create_poll', methods=['GET', 'POST'])
def create_poll():
    if request.method == 'POST':
        question = request.form.get('question')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        if not question or not option1 or not option2:
            flash('Missing form data', 'error')
            return redirect(url_for('create_poll'))

        new_poll = Poll(question=question, option1=option1, option2=option2)
        db.session.add(new_poll)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_poll.html')

@app.route('/vote/<int:poll_id>', methods=['POST'])
def vote(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    option = request.form.get('option')
    if option == 'option1':
        poll.votes1 += 1
    elif option == 'option2':
        poll.votes2 += 1
    db.session.commit()
    return redirect(url_for('results', poll_id=poll_id))

@app.route('/results/<int:poll_id>')
def results(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    winner = None
    if poll.votes1 > poll.votes2:
        winner = 'Option 1'
    elif poll.votes2 > poll.votes1:
        winner = 'Option 2'
    else:
        winner = 'Tie'
    return render_template('results.html', poll=poll, winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
