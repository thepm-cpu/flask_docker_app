from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Use /tmp directory for Render compatibility
db_path = os.path.join('/tmp', 'guestbook.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)

# This ensures database + table is created before first request
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        content = request.form["message"]
        new_message = Message(name=name, content=content)
        db.session.add(new_message)
        db.session.commit()
        return redirect("/")
    
    messages = Message.query.all()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
