from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

# Route: Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        # Save to database
        new_message = Message(name=name, message=message)
        db.session.add(new_message)
        db.session.commit()

        return redirect(url_for('index'))

    # Show all messages
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

# Create DB on first run


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
