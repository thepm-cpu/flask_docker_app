from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session handling

# Database setup (compatible with Render)
db_path = os.path.join('/tmp', 'guestbook.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        content = request.form["message"]
        new_message = Message(name=name, content=content)
        db.session.add(new_message)
        db.session.commit()
        return redirect("/")

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    is_admin = session.get("logged_in", False)
    return render_template("index.html", messages=messages, is_admin=is_admin)

@app.route("/delete/<int:id>")
def delete(id):
    if not session.get("logged_in"):
        return redirect("/login")
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "password123":  # You can change this
            session["logged_in"] = True
            return redirect("/")
        else:
            return "Invalid credentials. Try again."
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
