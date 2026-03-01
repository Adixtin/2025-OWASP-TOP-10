from flask import Flask, request
import sqlite3

app = Flask(__name__)

DB = "Injection/sql_injection/database.db"


def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "password123"))
    conn.commit()
    conn.close()


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful!"
    else:
        return "Invalid credentials"


init_db()
app.run(debug=True, port=5002)
