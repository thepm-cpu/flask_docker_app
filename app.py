from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'guestbook.db'

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # allows us to access columns by name
    return conn

# Create the database table if it doesn't exist
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# Home route: show all messages and the form
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        conn.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        return redirect("/")
    
    # Fetch messages from database
    messages = conn.execute("SELECT * FROM messages ORDER BY id DESC").fetchall()
    conn.close()
    
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
